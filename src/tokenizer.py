from sklearn.base import BaseEstimator, TransformerMixin
from src.glove_tokenize_modified import tokenize
from src.utils import BaseFit
from pandas import DataFrame


class Tokenizer(BaseFit, BaseEstimator, TransformerMixin):
    """ It tokenizes the English text based on GloVe tokenizer
    (used with MT+GloVe model).    
    """

    def __init__(self, tokenizer, column):
        self.tokenizer = tokenizer
        self.column = column

    def tokens(self, text):
        return self.tokenizer.tokenize(text)

    def transform(self, data, y=None):
        return data[self.column].map(self.tokens)

    
class TokenizerLan(BaseFit, BaseEstimator, TransformerMixin):
    """ It tokenizes the text according to its language 
    (used with LF, MUSE and MUSE+LF models).  
    """

    def __init__(self, tokenizer, column):
        self.tokenizer = tokenizer
        self.column = column

    def tokens(self, text):
        return self.tokenizer.tokenize(text)

    def transform(self, data, y=None):
        data['tokens'] = data[self.column].map(self.tokens)
        return data[['tokens', 'lan_final']]
    
    
class GloveTokenizer(object):
    """ It applies the modified GloVe tokenizer.  
    """
    def __init__(self):
        self.functor = tokenize
        
    def tokenize(self, text):
        return self.functor(text)