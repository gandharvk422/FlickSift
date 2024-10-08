import streamlit as st
import pickle as pkl

st.set_page_config(page_title="FlickSift - Discover Your Perfect Movie Instantly", page_icon=":movie:")

movies = pkl.load(open("movies_list.pkl", "rb"))
similarity = pkl.load(open("similarity.pkl", "rb"))
movies_list = movies["title"].values

st.title("FlickSift")
st.header("Discover Your Perfect Movie Instantly")

selectvalue = st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key = lambda vector:vector[1])
    
    recommend_movie = []

    for i in distance[1:6]:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie

if st.button("Show Recommendations"):
    movie_name = recommend(selectvalue)
    col1, col2, col3, col4, col5 = st.columns(5)
    st.text(movie_name[0])
    st.text(movie_name[1])
    st.text(movie_name[2])
    st.text(movie_name[3])
    st.text(movie_name[4])