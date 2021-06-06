## Linguistic Features (LF) extracted tweets

The following table shows the description of the 48 statistical features extracted from the tweet text. The first and second columns describe the general features, while the third and fourth columns describe the features extracted according to message language. 

| Feature (general)     | Description                          | Feature (by language) | Description                                                                                                      |
|-----------------------|--------------------------------------|-----------------------|------------------------------------------------------------------------------------------------------------------|
| *# Total characters*    | Length of message.                   | *Polarity*              | Sentiment score (from -1 for negatives words to +1 for positive words).                                          |
| *# Unique characters*   | No. of unique characters.            | *# Adjectives*          | No. of ADJ POS (e.g., scared, high).                                                                             |
| *# Total words*         | No. of total words.                  | *# Adpositions*         | No. of ADP POS (e.g., on, in, of, by)                                                                            |
| *# Unique words*        | No. of unique words.                 | *# Adverbs*             | No. of ADV POS (e.g., ago, very)                                                                                 |
| *# Links*               | No. of urls.                         | *# Aux. verb*           | No. of AUX POS (e.g., was, should)                                                                               |
| *# Mentions*            | No. of user mentions.                | *# Coord. conjunctions* | No. of CONJ POS (e.g., for, and, but, or)                                                                        |
| *# Hashtags*            | No. of hashtags.                     | *# Determiners*         | No. of DET POS (e.g., which, a, some)                                                                            |
| *# Cry emoji*           | No. of cry emojis.                   | *# Interjections*       | No. of INTJ POS (e.g., Wow!, hey, please)                                                                        |
| *# Bless emoji*         | No. of bless emojis.                 | *# Nouns*               | No. of NOUN POS (e.g., days)                                                                                     |
| *# Fear emoji*          | No. of fear emojis.                  | *# Numerals*            | No. of NUM POS (e.g., 2020, five, #)                                                                             |
| *# Sad face emoticon*   | No. of sad face emoticons.           | *# Particles*           | No. of PART POS (e.g., to, not)                                                                                  |
| *# Lol emoticon*        | No. of Lol emoticons.                | *# Pronouns*            | No. of PRON POS (e.g., I, their)                                                                                 |
| *# Exclamation marks*   | No. of exclamation marks.            | *# Proper nouns*        | No. of PROPN POS (e.g., Chile)                                                                                   |
| *# Question marks*      | No. of question marks.               | *# Punctuations*        | No. of PUNCT POS (e.g., , . -)                                                                                   |
| *Has link*              | Binary, contains links?              | *# Sub. conjunctions*   | No. of SCONJ POS (e.g., if, that, as)                                                                            |
| *Has mention*           | Binary, contains user mentions?      | *# Symbols*             | No. of SYM POS (e.g., @, +, $, /)                                                                                |
| *Has hashtag*           | Binary, contains hashtags?           | *# Verbs*               | No. of VERB POS (e.g., am, scared)                                                                               |
| *Has cry emoji*         | Binary, contains cry emojis?         | *# Other POS*           | No. of X POS (e.g., l, m, x)                                                                                     |
| *Has bless emoji*       | Binary, contains bless emojis?       | *# Locations*           | No. of location entities (e.g., cities, countries, regions, continents, neighborhoods, administrative divisions) |
| *Has fear emoji*        | Binary, contains fear emojis?        | *# Organizations*       | No. of organization entities (e.g., sports teams, newspapers, banks, universities, schools, companies)           |
| *Has sad face emoticon* | Binary, contains sad face emoticons? | *# Persons*             | No. of person entities (e.g., politicians, scientists, artists, atheletes)                                       |
| *Has lol emoticon*      | Binary, contains Lol emoticons?      | *Has location*          | Binary, contains location entities?                                                                              |
| *Has exclamation mark*  | Binary, contains exclamation marks?  | *Has organization*      | Binary, contains organization entities?                                                                          |
| *Has question mark*     | Binary, contains question marks?     | *Has person*            | Binary, contains person entities?                                                                                |
