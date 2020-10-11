import pandas as pd
from nltk.corpus import stopwords
from nltk import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pickle


class TfidfModel:
    def __init__(self):
        i_data = pd.read_csv('./dataset/movie_overviews.csv')
        self._data = i_data.head()

    def process_overview(self,string):
        if type(string) == str:
            bow = word_tokenize(string)
            bow_lowercase = [t.lower() for t in bow if t.isalpha() and  t not in stopwords.words('english')]
            return ' '.join(bow_lowercase)

    def vectorization(self):
        self._data['overview'] = self._data['overview'].apply(self.process_overview)
        tfidf = TfidfVectorizer()
        tfidf_matrix = tfidf.fit_transform(self._data['overview'])
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        with open('./rf.pkl','wb') as model_pkl:
            pickle.dump(cosine_sim, model_pkl)

    def recommender(self,cosine_sim,title):
        indices = pd.Series(self._data.index, index=self._data['title']).drop_duplicates()
        idx = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]
        return self._data['title'].iloc[movie_indices]