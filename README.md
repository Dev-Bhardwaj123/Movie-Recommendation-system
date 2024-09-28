# Movie-Recommendation-system
This program uses a dataset of a lot of movies and takes a user input of movie name. Then based on certain parameters like genre, cast, director and tagline it gives a list of top 10 most eligible movies for the taste of the user based on input provided. 

Libraries:
I have used Python and it's libraries primarily pandas,sklearn and difflib to optimize the results and fine the searches for the closest match

Approach:
Transform each of the movies and it's features into a vector that can be represented on a graph.
Based on a similarity feature and using the difflib library it assigns each movie a numerical value
An algorithm named cosine similarity algorithm is used to identify the relationship between the user given movie name input and the names of movies lying closest to it. It compares the vector and sorts the ones closest to the input value.

Result:
At last we take input from user and top 10 most similar movies get displayed on the screen which are the most closest or have lot of common features in between the two movies.

