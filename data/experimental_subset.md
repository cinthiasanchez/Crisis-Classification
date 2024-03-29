## Additional preprocessing for experiments

For our experimentation we selected English (EN), Spanish (ES) and Italian (IT) languages of three hazard types, which are earthquake (all languages), 
flood (EN and IT) and explosion (EN and ES), totaling 82,607 tweets.

We then consider three steps to prepare the data for further classification, which are detailed below.

**1. Text Cleaning**

We expanded English contractions (e.g., *let's* is converted to *let us* and *isn't'* to *is not*) using a python library called **pycontractions**, 
taking the *precise* version and the semantic model *glove-twitter-100*. 
In the case of the *ChileEarthquakeT1* dataset, we excluded truncated text messages and consider only those that we downloaded by tweet ID. 
For *Ecuador-Earthquake* dataset, we removed tweets starting with a user mention (i.e., replies) because it is focused on conversations and our work consider single messages like the other datasets.

Text preprocessing and tokenization according to data representations: With MUSE embeddings (trained on general corpus), we used the clean text, which consisted of removing urls, user mentions, hashtags, retweet symbols, emojis, emoticons, numbers and symbols, and converted it to lowercase. 
In the case of MT+GloVe model, we replaced these strings on the translated text by special tokens (e.g., &lt;hashtag>) 
according to the [GloVe](https://nlp.stanford.edu/projects/glove/) script for preprocessing Twitter data.
As for the contextual data models ([mBERT](https://huggingface.co/bert-base-multilingual-cased), [BERT](https://huggingface.co/bert-base-uncased), [XLM-R](https://huggingface.co/xlm-roberta-base), [XLM-T](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base)), we used the original text after expanding the English contractions. For these models, we use their respective tokenizer, that is, AutoTokenizer('model').

**2. Duplicate and Near-Duplicate Removal**

We removed 9,926 messages with duplicated clean text (mainly retweets).
To avoid having similar messages multiple times that could overestimating our result, we further removed near-duplicated messages. 
Thus, we computed the cosine similarity over the original text and removed those with a score greater than 0.75, maintaining only one message as unique.
The following table presents examples of detected near duplicates by language.
Considering this step, we found 1,135 near duplicates in English (2.1% of this language),
118 in Spanish (1.5% of Spanish messages) and 313 messages in Italian (5.0% of Italian messages).

| Tweet                                                                                                                                       | Near duplicate                                                                                                                     | Lang. |
|---------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|:-----:|
| Clean up operation is under the in north east australia as flood water begin to recede.                                                     | CLEAN-UP OPERATION IS UNDERWAY IN NORTH EAST AUSTRALIA AS FLOOD WATERS BEGIN TO RECEDE                                             |   EN  |
| RT @24HorasTVN: AHORA: SHOA publica en este momento, que hay alerta de tsunami para #Chile por terremoto en #CostaRica http://t.co/N3brPnyY | RT @24HorasTVN:SHOA publica en este momento, q' hay alerta d tsunami para #Chile por terremoto en #CostaRica http://t.co/1A8FwqwV” |   ES  |
| altra scossa forte. #terremoto                                                                                                              | #terremoto altra forte scossa.                                                                                                     |   IT  |

**3. Tweet Relabeling**

We relabeled 328 messages from CrisisMMD and CrisisLexT26 datasets, updating the label mapped initially as negative class to **related**.
In detail, we relabeled 313 *not informative* messages from CrisisMMD dataset that could be considered as crisis related
because this label is more specific compared to other datasets such as CrisisLexT26 (e.g., *Related - but not informative* label). 
For example, *Volunteers filling semi trailer for Mexico earthquake relief https://t.co/rHt9ZzLeyH https://t.co/xmLr1CYie8*. 
Furthermore, we relabeled 15 *Not applicable* tweets (too short; not readable; or other issues) from the CrisisLexT26 dataset,
when the detected language was different from English. 
For example, *Una explosión en Texas provocó al menos 5 muertos y más de 130 heridos La Policía de Waco dio la primera cifra... http://t.co/4TRPu0fO04*
(***Translation:*** *An explosion in Texas caused at least 5 deaths and more than 130 injured Waco Police gave the first figure ... http://t.co/4TRPu0fO04)*. 


## Summary of the experimental subset of data

After these preprocessing steps, we selected the crisis events with at least 100 instances per language and domain. 
The following table shows a summary of the resulting subset of data used in our experiments.
This compilation of 67,001 instances covers crisis events from various continents, 
different hazard categories and subcategories, temporal development and geographic spread. 
Additionally, 80.0% of these messages were published in English, 11.3% in Spanish and the 8.7% in Italian. 
With regard to the domain, 46.9% correspond to earthquakes, 38.4% to floods and 14.7% to explosions. 
About 36.0% of messages are labeled as not related to crisis while 64.0% as related.


|  Lang.  |   Domain   | Events |                                                   Crises                                                   | Related | Not  related |  Total |
|:-------:|:----------:|:------:|:----------------------------------------------------------------------------------------------------------:|:-------:|:------------:|:------:|
| English | Earthquake | 11     | Nepal, Chile 2014, California, Pakistan, Ecuador, Mexico, Bohol, Costa Rica, Iraq_Iran, Emilia, Guatemala |  13,870 |        6,832 | 20,702 |
|         | Explosion  | 1      | West Texas                                                                                                 |   4,415 |        4,641 |  9,056 |
|         | Flood      | 9      | Alberta, Queensland, Pakistan, India, Colorado, Philippines, Sri Lanka, Manila, Sardinia                 |  13,445 |       10,389 | 23,834 |
| Spanish | Earthquake | 5      | Chile 2014, Chile 2010, Ecuador, Guatemala, Costa Rica                                                     |   5,356 |        1,394 |  6,750 |
|         | Explosion  | 1      | Venezuela                                                                                                  |     747 |           50 |    797 |
| Italian | Earthquake | 2      | Emilia, L’Aquila                                                                                           |   3,260 |          705 |  3,965 |
|         | Flood      | 2      | Sardinia, Genova                                                                                           |   1,759 |          138 |  1,897 |



### Detailed training/testing partitions


**Testing:** For each target (language and domain), we used the same testing crises across the classification scenarios.

| **Lang.** | **Domain** |                                             **Crises**                                             |
|:---------:|:----------:|:--------------------------------------------------------------------------------------------------:|
| English   | Earthquake | Chile 2014, California, Pakistan, Ecuador, Mexico, Bohol, Costa Rica, Iraq_Iran, Emilia, Guatemala |
|           | Explosion  | West Texas                                                                                         |
|           | Flood      | Queensland, Pakistan, India, Colorado, Philippines, Sri Lanka, Manila, Sardinia                    |
| Spanish   | Earthquake | Ecuador, Guatemala, Costa Rica                                                                     |
|           | Explosion  | Venezuela                                                                                          |
| Italian   | Earthquake | L’Aquila                                                                                           |
|           | Flood      | Sardinia, Genova                                                                                   |


**Training:** For each target, we show the training events used in each scenario. 
For better readability we show these events in two tables. The first one shows the training events used in the *monolingual* scenarios, while the second one shows those of the *Cross-lingual and Multilingual* scenarios.
The symbol “-” means that no experiments were performed.

*Monolingual scenarios*

| **Lang.** | **Domain** |     **Monolingual & Mono-Domain**     |                                                                                                  **Monolingual & Cross-Domain**                                                                                                 |                                                                       **Monolingual & Multi-Domain**                                                                      |
|:---------:|:----------:|:---------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| English   | Earthquake | **Earthquakes:** Nepal                  | **Explosions:** West Texas, **Floods:** Alberta, Colorado, India, Manila, Pakistan, Philippines, Queensland, Sardinia, Sri Lanka                                                                                                  | **Earthquakes:** Nepal, **Explosions:** West Texas, **Floods:** Alberta, Colorado, India, Manila, Pakistan, Philippines, Queensland, Sardinia, Sri Lanka                    |
|           | Explosion  |                    -                    | **Earthquakes:** Bohol, California, Chile 2014, Costa Rica, Ecuador, Guatemala, Iraq_Iran, Emilia, Mexico, Nepal, Pakistan,  **Floods:** Alberta, Colorado, India, Manila, Pakistan, Philippines, Queensland, Sardinia, Sri Lanka |                                                                                      -                                                                                      |
|           | Flood      | **Floods:** Alberta                     | **Earthquakes:** Bohol, California, Chile 2014, Costa Rica, Ecuador, Guatemala, Iraq_Iran, Emilia, Mexico, Nepal, Pakistan,  **Explosions:** West Texas                                                                           | **Earthquakes:** Bohol, California, Chile 2014, Costa Rica, Ecuador, Guatemala, Iraq_Iran, Emilia, Mexico, Nepal, Pakistan, **Explosions:** West Texas, **Floods:** Alberta |
| Spanish   | Earthquake | **Earthquakes:** Chile 2014, Chile 2010 | **Explosions:** Venezuela                                                                                                                                                                                                         |                                                                                      -                                                                                      |
|           | Explosion  |                    -                    | **Earthquakes:** Chile 2010, Chile 2014, Costa Rica, Ecuador, Guatemala                                                                                                                                                           |                                                                                      -                                                                                      |
| Italian   | Earthquake | **Earthquakes:** Emilia                 | **Floods:** Genova, Sardinia                                                                                                                                                                                                      |                                                                                      -                                                                                      |
|           | Flood      |                    -                    | Earthquakes: Emilia, L’Aquila                                                                                                                                                                                                     |                                                                                      -                                                                                      |


*Cross-lingual and Multilingual scenarios*

| **Lang.** | **Domain** |                                          **Cross-lingual and Mono-Domain**                                         |                                                                                                 **Cross-lingual and Cross-Domain**                                                                                                |                                                                                                              **Cross-lingual and Multi-Domain**                                                                                                              |                                                                                                                    **Multi-lingual and Multi-Domain**                                                                                                                    |
|:---------:|:----------:|:------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Spanish   | Earthquake | **Earthquakes:** Bohol, California, Iraq_Iran, Emilia, Mexico, Nepal, Pakistan                                     | **Explosions:** West Texas, **Floods:** Alberta, Colorado, India, Manila, Pakistan, Philippines, Queensland, Sardinia, Sri Lanka                                                                                                  | **Earthquakes:** Bohol, California, Iraq_Iran, Emilia, Mexico, Nepal, Pakistan,  **Explosions:** West Texas, **Floods:** Alberta, Colorado, India, Manila, Pakistan, Philippines, Queensland, Sardinia, Sri Lanka                                            | **Earthquakes:** Bohol, California, Chile 2010, Chile 2014, Iraq_Iran, Emilia, Mexico, Nepal, Pakistan, **Explosions:** Venezuela, West Texas, **Floods:** Alberta, Colorado, India, Manila, Pakistan, Philippines, Queensland, Sardinia, Sri Lanka                      |
|           | Explosion  | **Explosions:** West Texas                                                                                         | **Earthquakes:** Bohol, California, Chile 2014, Costa Rica, Ecuador, Guatemala, Iraq_Iran, Emilia, Mexico, Nepal, Pakistan,  **Floods:** Alberta, Colorado, India, Manila, Pakistan, Philippines, Queensland, Sardinia, Sri Lanka | **Earthquakes:** Bohol, California, Chile 2014, Costa Rica, Ecuador, Guatemala, Iraq_Iran, Emilia, Mexico, Nepal, Pakistan, **Explosions:** West Texas, **Floods:** Alberta, Colorado, India, Manila, Pakistan, Philippines, Queensland, Sardinia, Sri Lanka | **Earthquakes:** Bohol, California, Chile 2010, Chile 2014, Costa Rica, Ecuador, Guatemala, Iraq_Iran, Emilia, Mexico, Nepal, Pakistan, **Explosions:** West Texas, **Floods:** Alberta, Colorado, India, Manila, Pakistan, Philippines, Queensland, Sardinia, Sri Lanka |
| Italian   | Earthquake | **Earthquakes:** Bohol, California, Chile 2014, Costa Rica, Ecuador, Guatemala, Iraq_Iran, Mexico, Nepal, Pakistan | **Explosions:** West Texas, **Floods:** Alberta, Colorado, India, Manila, Pakistan, Philippines, Queensland, Sardinia, Sri Lanka                                                                                                  | **Earthquakes:** Bohol, California, Chile 2014, Costa Rica, Ecuador, Guatemala, Iraq_Iran, Mexico, Nepal, Pakistan,  **Explosions:** West Texas,  **Floods:** Alberta, Colorado, India, Manila, Pakistan, Philippines, Queensland, Sardinia, Sri Lanka       | **Earthquakes:** Bohol, California, Chile 2014, Costa Rica, Ecuador, Guatemala, Iraq_Iran, Emilia, Mexico, Nepal, Pakistan, **Explosions:** West Texas, **Floods:** Alberta, Colorado, Genova, India, Manila, Pakistan, Philippines, Queensland, Sardinia, Sri Lanka     |
|           | Flood      | **Floods:** Alberta, Colorado, India, Manila, Pakistan, Philippines, Queensland, Sri Lanka                         | **Earthquakes:** Bohol, California, Chile 2014, Costa Rica, Ecuador, Guatemala, Iraq_Iran, Emilia, Mexico, Nepal, Pakistan,  **Explosions:** West Texas                                                                           | **Earthquakes:** Bohol, California, Chile 2014, Costa Rica, Ecuador, Guatemala, Iraq_Iran, Emilia, Mexico, Nepal, Pakistan, **Explosions:** West Texas, **Floods:** Alberta, Colorado, India, Manila, Pakistan, Philippines, Queensland, Sri Lanka           | **Earthquakes:** Bohol, California, Chile 2014, Costa Rica, Ecuador, Guatemala, Iraq_Iran, Emilia, L’Aquila, Mexico, Nepal, Pakistan, **Explosions:** West Texas, **Floods:** Alberta, Colorado, India, Manila, Pakistan, Philippines, Queensland, Sri Lanka             |



