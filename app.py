import pandas as pd
import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=eb54716b696e9ee5e96f52c188ec2395'.format(movie_id))
    data = response.json()
    print(data)

    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    recommended_movie_poster =[]
    for i in movies_list:
        movie_id = i[0]
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movie, recommended_movie_poster


movies_df = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_df)

similarity = pickle.load(open('similarity.pkl','rb'))

movies_list = movies_df['title'].values

st.title('Movie Recommender System')
selected_movies_name = st.selectbox('Type movie name here : ',movies['title'].values)

if st.button('More like this'):
    name,poster = recommend(selected_movies_name)

    col1, col2, col3, col4, col5= st.beta_columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])

    with col4:
        st.text(name[3])
        st.image(poster[3])

    with col5:
        st.text(name[4])
        st.image(poster[4])