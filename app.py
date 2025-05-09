import pickle
import streamlit as st
import pandas as pd

# Load data
movies = pickle.load(open('Model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('Model/similarity.pkl', 'rb'))

# Title
st.title("🎬 Netflix Movie Recommender System")

# Select box
selected_movie = st.selectbox("📽️ Select a movie from the list", movies['title'].values)

# Recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_data = movies.iloc[i[0]]
        recommended_movies.append({
            "title": movie_data.title,
            "description": movie_data.description,
            "genre": movie_data.listed_in,
            "year": movie_data.release_year
        })
    return recommended_movies

# On button click
if st.button('🎯 Recommend'):
    recommendations = recommend(selected_movie)
    st.subheader("Top 5 Similar Movies")
    for movie in recommendations:
        with st.container():
            st.markdown(f"**🎬 Title:** {movie['title']}")
            st.markdown(f"📅 **Year:** {movie['year']}")
            st.markdown(f"📚 **Genre:** {movie['genre']}")
            st.markdown(f"📝 **Description:** {movie['description']}")
            st.markdown("---")
