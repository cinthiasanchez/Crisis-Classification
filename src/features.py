from src.patterns import COMMONS_SENTENCE_FEATURES, ALL_P2P, PATTERNS_UPDATE_NORMALIZE
from sklearn.base import BaseEstimator, TransformerMixin
from src.utils import FunctionComposer, BaseFit
from collections import Counter
from polyglot.text import Text
from pandas import DataFrame
from tqdm.auto import tqdm
import numpy as np
import re


class StatsInterface(BaseEstimator, TransformerMixin):

    def __init__(self, column):
        self.descriptors = self.build_descriptors()
        self.column = column

    def build_descriptors(self):
        raise NotImplementedError

    def transform(self, x, y=None):
        """ Map a set of functions and crate a pandas DataFrame
        to storage the descriptors
        :param x: A set of values with text or tokens
        :param y: actual labels
        :return:
        """
        container = DataFrame()
        for column, func in self.descriptors.items():
            container.__setitem__(column,
                                  x[self.column].map(func))
        return container

    @staticmethod
    def uniques(text):
        return FunctionComposer(len, set)(text)

    def name_features(self):
        return list(self.descriptors.keys())


class SentenceLevelStats(BaseFit, StatsInterface):
    """ Compute Basic Stats from the plain text or tweet
    and 1 as value for the entire set e.g dict(the=1, i=1)
    """

    def __init__(self, column='tweet_text'):
        super().__init__(column)

    def build_descriptors(self):
        """
        Is a collection of basis stats, taken of the corpus
        :return: dict with features name and its analogous
        function
        """

        descriptors = dict(uniqueness=self.uniques)
        for name, pattern in COMMONS_SENTENCE_FEATURES:
            descriptors[name] = pattern
        descriptors['_exclamation'] = lambda x: x.count('!')
        descriptors['_interrogate'] = lambda x: x.count('?')
        #descriptors['_cashtag'] = lambda x: x.count('$')
        descriptors['nchars'] = len

        return descriptors


class FeaturesExistence(BaseFit, BaseEstimator, TransformerMixin):
    """ Compute Sentence Level Stats
    """

    def __init__(self, initial_mark='_'):
        self.columns = []
        self.mark = initial_mark

    def transform(self, x, y=None):
        """ Map a set of functions and crate a pandas DataFrame
        to storage the descriptors
        :param x: A set of values with text or tokens
        :param y: actual labels
        :return:
        """
        selected = x.columns.str.startswith(self.mark)
        for selection in x.columns[selected]:
            x['has{}'.format(selection)] = x[selection] > 0
        return x


class WordLevelStats(BaseFit, StatsInterface):
    """ This class takes a token and extract the functions
    pattern that was written in features_construction method
    """

    def __init__(self, column):
        super().__init__(column)

    def build_descriptors(self):
        """
        Is a collection of basis stats, taken of the corpus
        :return: dict with features name and its analogous
        function
        """
        descriptors = dict(uniqueness=self.uniques)
        descriptors['ntokens'] = len
        return descriptors


    
class PartOfSpeech(BaseFit, BaseEstimator, TransformerMixin):

    def __init__(self, column, lang, is_translated, p2p=None):
        self.column, self.lan, self.is_translated = column, lang, is_translated
        self.columns = self.cast(p2p)

    @staticmethod
    def cast(p2p):
        part_of_speech = ALL_P2P if p2p is None else p2p
        iterator = enumerate(part_of_speech)
        return dict((k, i) for i, k in iterator)
          

    def compute(self, row):
        if self.is_translated:
            text = Text(row[self.column], 'en')
        else:
            text = Text(row[self.column], row[self.lan]) 
        entities = Counter((v.tag for v in text.entities))
        pos = Counter((v for k, v in text.pos_tags))
        return {**dict(entities), **dict(pos)}
    

    def transform(self, x, y=None):
        kw = dict(columns=self.columns)
        series = x.progress_apply(self.compute, axis=1)
        data = DataFrame(list(series), **kw)
        return data.fillna(0.0)

class SentimentPolarity(BaseFit, BaseEstimator, TransformerMixin):

    def __init__(self, column, lang, is_translated):     
        self.column, self.lan = column, lang
        self.is_translated = is_translated   

    def compute(self, row):
        if self.is_translated:
            text = Text(row[self.column], 'en')
        else:
            text = Text(row[self.column], row[self.lan])     
                        
        return dict(polarity=text.polarity)

    def transform(self, x, y=None):
        series = x.progress_apply(self.compute, axis=1)
        data = DataFrame(list(series))
        return data.fillna(0.0)


class EmbeddingsBulkToDict(object):

    def __init__(self, file, sep='\t', pos=(None, -1)):
        self.filename, self.sep = file, sep
        self.embedding = dict()
        self.load(pos)

    def load(self, pos):
        with open(self.filename, encoding='utf8') as file:
            for line in tqdm(file):
                self.fill_data(line.split(self.sep), pos)

    def fill_data(self, line, pos):
        word_pos = min((pos[0] or 0), (pos[1] or 0))
        word = line[word_pos].strip()
        x = np.array(line[slice(*pos)])
        self.embedding[word] = x.astype(np.float32)


class EmbeddingsFromDict(BaseFit, TransformerMixin):

    def __init__(self, embeddings, unknown, redux):
        self.embedding = embeddings
        self.unknown = unknown
        self.redux = redux

    def recover(self, word):
        return self.embedding.get(word, self.unknown)

    def compute(self, tokens):
        iterator = map(self.recover, tokens)
        return self.redux(list(iterator), axis=0)

    def transform(self, corpus, y=None):
        return list(corpus.map(self.compute))
    

class EmbeddingsFromDictLang(BaseFit, TransformerMixin):

    def __init__(self, embeddings, unknown, redux):
        self.embedding = embeddings
        self.unknown = unknown
        self.redux = redux

    def compute(self, data):
        langs = self.embedding.get(data.lan_final)
        iterator = (langs.get(word, self.unknown)
                    for word in data.tokens)
        return self.redux(list(iterator), axis=0)

    def transform(self, dataframe, y=None):
        return list(dataframe.apply(self.compute, axis=1))

    
##### OOV we analysis    
class UnknownVocabularyLang(BaseFit, TransformerMixin):

    def __init__(self, embeddings):
        self.embedding = embeddings

    def recover(self, data):
        langs = self.embedding.get(data.lan_final)  
        iterator = [0 if langs.get(word) is None else 1
                    for word in data.tokens]
        return sum(iterator)
    

    def transform(self, dataframe, y=None):
        data = dataframe.apply(self.recover, axis=1)
        return DataFrame({'known': data,
                          'size': dataframe.tokens.map(len)})
    
    
class UnknownVocabulary(BaseFit, TransformerMixin):

    def __init__(self, embeddings):
        self.embedding = embeddings

    def recover(self, word):
        emb = self.embedding.get(word)
        return 0 if emb is None else 1

    def compute(self, tokens):
        return sum(map(self.recover, tokens))

    def transform(self, corpus, y=None):
        data = corpus.map(self.compute)
        return DataFrame({'known': data,
                          'size': corpus.map(len)})
    
    
    
class NormalizeSentence(BaseFit, BaseEstimator, TransformerMixin):
    """In order to reduce the number of vocabulary, this class try
    to change some word patterns to especifics ones. e.g
    @name -> <user>
    #brain -> <hashtag>
    ...
    """
    
    def __init__(self, column):
        self.patterns = PATTERNS_UPDATE_NORMALIZE
        self.flags = re.MULTILINE | re.DOTALL
        self.column = column
        
    def compute(self, text):
        """Update rules
        :param text: sentence to process
        :return: string with remplaced text
        """
        for pattern, value in self.patterns:
            text = re.sub(pattern, value,
                          text, flags=self.flags)
        return text

    def transform(self, data, y=None):
        """ Map a set of functions and crate a pandas DataFrame
        to storage the descriptors
        :param x: A set of values with text or tokens
        :param y: actual labels
        :return:
        """
        data['tokenized'] = data[self.column].apply(self.compute)
        return data[[self.column, 'tokenized', 'lan_final']]