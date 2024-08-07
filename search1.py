import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import requests

# Cache data and model loading for better performance
@st.cache_data
def load_data():
    anime_data = pd.read_csv("anime.csv")
    return anime_data

@st.cache_resource
def load_model():
    svd_model = joblib.load('svd.pkl')
    return svd_model

@st.cache_data
def get_anime_embeddings(_svd_model):
    """Extracts anime embeddings from the SVD model."""
    anime_embeddings = _svd_model.pu
    return anime_embeddings

def recommend_similar_anime(anime_ids, anime_embeddings, anime_data, top_n=5):
    """Recommends similar anime based on cosine similarity of anime embeddings."""
    valid_anime_ids = [anime_id - 1 for anime_id in anime_ids if anime_id - 1 < len(anime_embeddings)]
    
    if not valid_anime_ids:
        st.error("Invalid anime_id(s): out of bounds")
        return []

    # Calculate similarity scores for selected anime
    selected_embeddings = anime_embeddings[valid_anime_ids]
    similarity_scores = cosine_similarity(selected_embeddings, anime_embeddings).mean(axis=0)

    # Get indices of similar anime, sorted by similarity score in descending order
    similar_anime_indices = similarity_scores.argsort()[::-1][1:]

    # Ensure indices are within bounds
    valid_indices = [idx for idx in similar_anime_indices if idx < len(anime_data)]

    # Select top N valid indices
    top_indices = valid_indices[:top_n]

    similar_anime = anime_data.iloc[top_indices]
    return similar_anime

def get_recommendations(anime_ids, svd_model, anime_data, top_n=5):
    """Recommends anime based on anime IDs using content-based filtering."""

    # Extract anime embeddings
    anime_embeddings = get_anime_embeddings(svd_model)

    # Recommend similar anime based on content
    similar_anime = recommend_similar_anime(anime_ids, anime_embeddings, anime_data, top_n)

    return similar_anime

def search_page_content():
    st.title("Anime Recommender")

    # Load data and model
    anime_data = load_data()
    svd_model = load_model()

    # Create a display name with rating for each anime
    anime_data['display_name'] = anime_data['name'] + ' (Rating: ' + anime_data['rating'].astype(str) + ')'

    # User input for selecting multiple anime
    anime_titles = st.multiselect("Select anime", anime_data['display_name'])
    anime_ids = anime_data[anime_data['display_name'].isin(anime_titles)]['anime_id'].values

    if st.button("Recommend"):
        recommendations = get_recommendations(anime_ids, svd_model, anime_data)
        if not recommendations.empty:
            st.write("Recommended Anime:")
            for index, row in recommendations.iterrows():
                st.write(f"**Title:** {row['name']}")
                st.write(f"**Genres:** {row['genre']}")
                st.write(f"**Rating:** {row['rating']}")
                st.write("---")
        else:
            st.write("No recommendations found")

if __name__ == "__main__":
    search_page_content()

