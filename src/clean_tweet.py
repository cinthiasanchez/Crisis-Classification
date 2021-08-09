import re
import demoji
demoji.download_codes()

#Motivated on Translation of Ruby script to create features for GloVe vectors for Twitter data (Stanford).
#https://gist.github.com/ppope/0ff9fa359fb850ecf74d061f3072633a

def clean_tweet_lan(text, lower=False):
    """
    This function clean tweets for detecting language. It removes:
        retweet symbols, urls, users, emoticons,
        emojis, hashtags, cashtags, ellipses (...). 
    Maintain capital letters (lower=False), numbers and 
    specific punctuation marks in order to preserve the 
    semantics to detect language more precisely
    
    """       
    text = re.sub(r'\b(RT|rt)\b', " ", text) #retweet symbol  
    text = re.sub(r"https?:\/\/\S+\b|www\.(\w+\.)+\S*", " ", text) #urls 
    text = re.sub(r"@\w+", " ", text) #users (mentions)
    text = demoji.replace(text, repl=" ") #emojis   
    text = re.sub(r"#\S+", " ", text) #hashtags    
    text = re.sub('\$([a-zA-Z]+)', " ", text) #cashtag    
    text = re.sub(r"[.]{2,}", " ", text) #delete ellipses (...)
    text = re.sub(r"http", " ", text) #delete ‘http’ text
    text = re.sub(r"[^\w.,¡!¿?]", " ", text) #characters keep
    text = " ".join(text.split()) 
    text = text.lower() if lower else text
    return text

def clean_tweet_totally(text, lower=True):
    """
    This function clean (normalize) tweets for extracting features with word embeddings. 
    It only maintains letters, removing:
        retweet symbols, urls, users, emoticons, emojis, 
        hashtags, cashtags, numbers, ellipses (...), symbols    
    """    
    
    text = re.sub(r'\b(RT|rt)\b', " ", text) #retweet symbol
    text = re.sub(r"https?:\/\/\S+\b|www\.(\w+\.)+\S*", " ", text) #urls
    text = re.sub(r"@\w+", " ", text) #users (mentions)
    text = demoji.replace(text, repl=" ") #emojis   
    text = re.sub(r"#\S+", " ", text) #hashtags    
    text = re.sub('\$([a-zA-Z]+)', " ", text) #cashtag    
    text = re.sub(r"[-+]?[.\d]*[\d]+[:,.\d]*", " ", text) #numbers
    text = re.sub(r"[.]{2,}", " ", text) #delete ellipses (...)
    text = re.sub(r"http", " ", text) #delete ‘http’ text
    text = re.sub(r"[^\w]", " ", text) #only text ^\w
    text = " ".join(text.split()) 
    text = text.lower() if lower else text
    return text