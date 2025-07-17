# The Movie Recommender System Website

This project is a content-based movie recommender system that suggests similar movies based on a selected title.  
It uses **natural language processing**, **vector similarity techniques**, and a user-friendly **Streamlit web interface** for seamless interaction.

---

## About the Project

The aim of this project is to recommend similar movies using their metadata such as title, genre, overview, keywords, etc.  
I deployed the app using **Streamlit** and utilizes **The Movie Database (TMDB) API** for fetching posters and movie details.  

Key techniques used include:
- **CountVectorizer** for transforming text to vectors
- **Cosine Similarity** to find similar movies
- **Porter Stemmer** for text cleaning
- **TMDB API** to fetch real-time movie posters and metadata
- **Kaggle dataset** for historical movie data

---

## Topics Covered

- Text vectorization with CountVectorizer
- Cosine similarity for recommendation
- Text cleaning with NLTK's PorterStemmer
- REST API integration (TMDB)
- Streamlit Web App Development
- Data Cleaning and Feature Engineering
- Python libraries: Pandas, scikit-learn, NLTK, requests

---

## Dataset Source:

Kaggle movie metadata dataset  (TMDB)

---

## Technologies Used in Project:

Python, Data Proprocessing
Pandas, NumPy
scikit-learn
NLTK (PorterStemmer)
Streamlit
TMDB API
CountVectorizer & Cosine Similarity

---

## Features:

1. Suggests top 5 similar movies based on selected title.
2. Fetches posters and movie data in real-time from TMDB.
3. Simple and fast web interface.
4. Easy to scale and deploy.
