import re

"""
List of the most common patterns in tweets
"""

EYES, NOSE = r'[8:=;]', r"['`\-]?"
URL = r'https?:\/\/\S+\b|www\.(\w+\.)+\S*'
SLASH = r'/'
USER = r'@\w+'
SMILEFACE = r'{}{}[)dD]+|[)dD]+{}{}'.format(EYES, NOSE, NOSE, EYES)
LOL = r'{}{}p+'.format(EYES, NOSE)
SADFACE = r'{}{}\(+|\)+{}{}'.format(EYES, NOSE, NOSE, EYES)
NEUTRALFACE = r'{}{}[\/|l*]'.format(EYES, NOSE)
HEART = r'<3'
NUMBER = r'[-+]?[.\d]*[\d]+[:,.\d]*'
HASHTAG = r'#\S+'
REPETITIONS = r'([!?.]){2,}'
ELONG = r'\b(\S*?)(.)\2{2,}\b'
ALLCAPS = r'([A-Z]){2,}'

SOS = u'\U0001F198'
CRY = u'\U0001F622'
BLESS = u'\U0001F64F'
FEAR = u'\U0001F631'


COMMONS_SENTENCE_FEATURES = (
    ('_url', lambda a: len(re.findall(URL, a))),
    ('_user', lambda b: len(re.findall(USER, b))),
    ('_hashtag', lambda c: len(re.findall(HASHTAG, c))),
    ('_cry', lambda g: len(re.findall(CRY, g))),
    ('_bless', lambda h: len(re.findall(BLESS, h))),
    ('_fear', lambda i: len(re.findall(FEAR, i))),
    ('_sad', lambda j: len(re.findall(SADFACE, j))),
    ('_lol', lambda l: len(re.findall(LOL, l))),    
)


ALL_P2P = ['ADJ', 'ADP', 'ADV', 'AUX', 'CONJ', 'DET', 'INTJ', 'NOUN', 'NUM', 'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X',
          'I-LOC', 'I-ORG', 'I-PER']


PATTERNS_UPDATE_NORMALIZE = (
    (URL, '<url>'),
    (USER, '<user>'),
    (SADFACE, '<emoticon>'),
    (SMILEFACE, '<emoticon>'),
    (NEUTRALFACE, '<emoticon>'),
    (HEART, '<emoticon>'),
    (NUMBER, '<number>'),
    (HASHTAG, '<hashtag>')
)
