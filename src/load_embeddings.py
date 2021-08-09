import configuration

from sklearn.pipeline import Pipeline, FeatureUnion
from transformers import BertTokenizer, BertModel
from nltk.tokenize import TweetTokenizer
from src import features, tokenizer
from tqdm.auto import tqdm
import pandas as pd
import numpy as np
import torch
tqdm.pandas()

root = '../data/pretrained_models/word_embeddings/'


def glove_features(data):
    """
    Return glove Features of 100 dimensions extracted from the translated text. 
    """  
    print('Loading GloVe...')
    en_embeddings = features.EmbeddingsBulkToDict(root+'glove.twitter.27B.100d.txt', sep=' ', pos=(1, None))
    all_embeddings = {**en_embeddings.embedding}
    
    
    embeddings_pipe = Pipeline([
        ('tokenize', tokenizer.Tokenizer(tokenizer.GloveTokenizer(), 'translated')),
        ('w2v', features.EmbeddingsFromDict(all_embeddings, np.zeros(100), np.mean))])
    
    data_embedding = embeddings_pipe.transform(data)
    embedding_data_frame = pd.DataFrame(data_embedding)
    return embedding_data_frame



def muse_features(data):
    """
    Return MUSE Features of 300 dimensions extracted from the cleaned text. 
    """
    print('Loading MUSE...')
    it_embeddings = features.EmbeddingsBulkToDict(root+'wiki.multi.it.vec', sep=' ', pos=(1, None))
    es_embeddings = features.EmbeddingsBulkToDict(root+'wiki.multi.es.vec', sep=' ', pos=(1, None))
    en_embeddings = features.EmbeddingsBulkToDict(root+'wiki.multi.en.vec', sep=' ', pos=(1, None))

    all_embeddings = {'it': it_embeddings.embedding, 'es': es_embeddings.embedding, 'en':en_embeddings.embedding}
    
    embeddings_pipe = Pipeline([
        ('tokenize', tokenizer.TokenizerLan(TweetTokenizer(preserve_case=False), 'fixed_clean_total')),
        ('w2v', features.EmbeddingsFromDictLang(all_embeddings, np.zeros(300), np.mean))])

    data_embedding = embeddings_pipe.transform(data)
    embedding_data_frame = pd.DataFrame(data_embedding)
    return embedding_data_frame



#### Bert loaders #####

def features_from_bert(corpus, tokenizer, bert):    
    embedding = list()
    inputs = tokenizer(corpus, return_tensors="pt", padding=True)
    with torch.no_grad():
        outputs = bert(**inputs)
        for x, y in zip(outputs.last_hidden_state, inputs['attention_mask']):
            embedding.append(x[y.type(torch.BoolTensor)].mean(0))
        return torch.stack(embedding, 0).numpy()
    
    
def batch_features(data, tokenizer, bert, batch=100):
    features_lst = []
    for i in tqdm(range(0, len(data), batch)):
        features = features_from_bert(list(data.values[i:i+batch]), tokenizer, bert)
        features_lst.append(features)
    return np.vstack(features_lst)
    
    
def bert_features(data):
    """
    Return BERT Features of 768 dimensions extracted from the cleaned text.
    """
    print('Loading Bert...')
    ml = 'bert-base-multilingual-cased'
    tokenizer = BertTokenizer.from_pretrained(ml)
    bert = BertModel.from_pretrained(ml, return_dict=True)
    data_embedding = batch_features(data['fixed_clean_total'], tokenizer, bert)
    embedding_data_frame = pd.DataFrame(data_embedding)
    return embedding_data_frame

