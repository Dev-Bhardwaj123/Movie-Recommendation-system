import pandas as pd
import difflib   #gives us close match
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#loading data from csv to pandas df
movies_data=pd.read_csv('/content/movies.csv')

#printing first five rows of dataframe
movies_data.head()

#no. of rows and cols in df
movies_data.shape

#selecting the relevant features for recommendation
selected_features=['genres','title','keywords','tagline','cast','director']
print(selected_features)

#replacing null/missing values with null strings
for feature in selected_features:
  movies_data[feature]=movies_data[feature].fillna('')

#combining all 5 selected features
combined_features=movies_data['genres']+' '+movies_data['title']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']
print(combined_features)

#convert text data to feature vectors

vectorizer = TfidfVectorizer()
feature_vectors=vectorizer.fit_transform(combined_features)
print(feature_vectors)

#getting the similarity scores using cosine similarity
similarity=cosine_similarity(feature_vectors)
print(similarity)
print(similarity.shape)

#getting the movie name from user
movie_name=input(' Enter the movie name: ')

#creating list with all movie names given in the dataset
list_of_all_titles=movies_data['title'].tolist()
print(list_of_all_titles)

#finding the close match for the movie name given by user
find_close_match=difflib.get_close_matches(movie_name,list_of_all_titles)
print(find_close_match)
close_match=find_close_match[0]
print(close_match)

#find index of movie with title
index_of_movie=movies_data[movies_data.title==close_match]['index'].values[0]
print(index_of_movie)

#getting list of similar movies based on index
similarity_score=list(enumerate(similarity[index_of_movie]))
print(similarity_score)

#sorting the movies based on their similarity scores in descending order
sorted_similar_movies=sorted(similarity_score,key=lambda x:x[1],reverse=True)
print(sorted_similar_movies)


#print the name of the similar movies based on index
print('Movies suggested for you: \n')

i=1
for movie in sorted_similar_movies:
  index=movie[0]
  title_from_index=movies_data[movies_data.index==index]['title'].values[0]
  if(i<11):
      print(i,'.',title_from_index)
      i+=1