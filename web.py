# import streamlit as st
# import pickle
# import pandas as pd
# import requests

# def  fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0ed97a86193fe95abb5f3d708326ae42&language=en-US'.format(movie_id))
#     data = response.json()
#     st.text(data)
#     st.text('https://api.themoviedb.org/3/movie/{}?api_key=0ed97a86193fe95abb5f3d708326ae42&language=en-US'.format(movie_id)) 
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# def recommend(movie):
#     movie_index = movies[movies['title']==movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(similarity[0])),reverse=True, key=lambda x:x[1])[1:6]


#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
        
#         recommended_movies.append(movies.iloc[i[0]].title)
#         # fetch poster from API 
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies,recommended_movies_posters


# movies_dict = pickle.load(open('movie_dict.pkl','rb'))
# movies = pd.DataFrame(movies_dict)

# similarity = pickle.load(open('similarity.pkl','rb'))

# st.title('Movie Recommender System') 

# selected_movie_name = st.selectbox(
# 'How would you like to be contacted?',
# movies['title'].values)

# if st.button('Recommend'):
#     names,posters = recommend(selected_movie_name)
    
#     col1, col2, col3, col4, col5 = st.beta_columns(5)
#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
#     with col4:
#         st.text(names[3])
#         st.image(posters[3])
#     with col5:
#         st.text(names[4])
#         st.image(posters[4])

import streamlit as st # type: ignore
import pickle
import pandas as pd
import requests

# Function to fetch movie poster from TMDB API
def fetch_poster(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=0ed97a86193fe95abb5f3d708326ae42&language=en-US'
        )
        data = response.json()
        
        # Extract poster path properly
        poster_path = data.get('poster_path', None)
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Image+Found"  # Default placeholder

    except Exception as e:
        st.error(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750?text=Error"

# Movie recommendation function
def recommend(movie):
    # Get the index of the selected movie
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    
    # Sort movies based on similarity scores
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Collect recommended movie names and posters
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    
    return recommended_movies, recommended_movies_posters

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI layout
st.title('🎬 Movie Recommender System 🍿')

# Dropdown to select a movie
selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

# Display recommendations on button click
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Arrange results in columns
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])
