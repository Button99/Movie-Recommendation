import pickle
import pandas as pd

def ReadFile():
    df_movies= pd.read_csv("Movies.csv")
    cosine_sim= pickle.load(open("cos.pkl", "rb"))
    f= open("SimMovie.txt", "r")
    movie_title= f.read()
    f.close()
    df_movies = df_movies.reset_index()
    indices = pd.Series(df_movies.index, index=df_movies["title"])
    movies= get_recom(movie_title, cosine_sim, indices, df_movies)
    f=open("Rec_Movies.csv", "w")
    f.write(str(movies))
    f.close()

def get_recom(title, cosine_sim, indices, df_movies):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:10]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    return df_movies["title"].iloc[movie_indices]




