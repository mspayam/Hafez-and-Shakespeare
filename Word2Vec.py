import re
import nltk


article = open("filename.txt").read().lower().strip()

# Cleaing the text
processed_article = article.lower()
processed_article = re.sub('[^a-zA-Z]', ' ', processed_article )
processed_article = re.sub(r'\s+', ' ', processed_article)

# Preparing the dataset
all_sentences = nltk.sent_tokenize(processed_article)

all_words = [nltk.word_tokenize(sent) for sent in all_sentences]

# Removing Stop Words
from nltk.corpus import stopwords
for i in range(len(all_words)):
    all_words[i] = [w for w in all_words[i] if w not in stopwords.words('English')]

from gensim.models import Word2Vec

for i in range (1, 1000):
    word2vec = Word2Vec(all_words, min_count=5)
    vocabulary = word2vec.wv.vocab
    sim_words = word2vec.wv.most_similar_cosmul('love', topn=10)
print (sim_words)