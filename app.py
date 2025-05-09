import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv('cleaned_netflix_titles.csv')

# Fill missing values in description
df['description'] = df['description'].fillna('')
df['title'] = df['title'].fillna('Unknown Title')
df['listed_in'] = df['listed_in'].fillna('Unknown Genre')
df['release_year'] = df['release_year'].fillna('Unknown Year')

# Vectorize the descriptions
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

# Compute similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Reset index for easier lookups
df = df.reset_index()

# Recommend function
def recommend(movie_title):
    indices = pd.Series(df.index, index=df['title'].str.lower())
    idx = indices.get(movie_title.lower())

    if idx is None:
        return []

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]

    recommended = []
    for i in movie_indices:
        movie = df.iloc[i]
        recommended.append({
            "title": movie['title'],
            "description": movie['description'],
            "genre": movie['listed_in'],
            "year": movie['release_year']
        })
    return recommended

# Streamlit UI
st.title("🎬 Netflix Movie Recommender System")

selected_movie = st.selectbox("📽️ Select a movie from the list", sorted(df['title'].unique()))

if st.button("🎯 Recommend"):
    results = recommend(selected_movie)

    if results:
        st.subheader("Top 5 Similar Movies")
        for movie in results:
            with st.container():
                st.markdown(f"**🎬 Title:** {movie['title']}")
                st.markdown(f"📅 **Year:** {movie['year']}")
                st.markdown(f"📚 **Genre:** {movie['genre']}")
                st.markdown(f"📝 **Description:** {movie['description']}")
                st.markdown("---")
    else:
        st.warning("Movie not found in database. Try another.")
