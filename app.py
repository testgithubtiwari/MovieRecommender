import streamlit as st
import pickle
import pandas as pd
import requests
st.title('Movie Recommender System')

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)


selected_movie_name=st.selectbox(
    'List of the movies',
     movies['title'].values
)


def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?'
                          'api_key=2f203ad7a297788020cff0a7d2816d61&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        ## fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return  recommended_movies,recommended_movies_posters


if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Create columns for displaying recommended movies
    cols = st.columns(5)

    for i, col in enumerate(cols):
        with col:
            st.write(f"**{names[i]}**")
            st.image(posters[i], use_column_width=True)
