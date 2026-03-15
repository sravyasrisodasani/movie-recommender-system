import pickle
import pandas as pd
import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

# ---------- CUSTOM STYLE ----------
st.markdown("""
<style>

/* Background */
body {
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

/* TITLE */
.title {
text-align:center;
font-size:90px;
font-weight:800;
color:#ff4b4b;
margin-bottom:10px;
}

/* SUBTITLE */
.subtitle {
text-align:center;
font-size:26px;
color:#f1f1f1;
margin-bottom:50px;
}

/* SELECT BOX LABEL */
.stSelectbox label {
font-size:26px !important;
color:white !important;
font-weight:600;
}

/* SELECT BOX */
div[data-baseweb="select"] {
background-color:#1f2937;
border-radius:12px;
}

/* BUTTON */
.stButton>button {
background: linear-gradient(90deg,#ff4b4b,#ff8c00);
color:white;
font-size:24px;
border-radius:14px;
padding:14px 40px;
border:none;
font-weight:600;
}

/* MOVIE CARDS */
.movie-card {
background:#ffffff;
padding:25px;
border-radius:20px;
box-shadow:0px 8px 25px rgba(0,0,0,0.4);
text-align:center;
font-size:22px;
font-weight:600;
color:#222;
}

</style>
""", unsafe_allow_html=True)

# ---------- LOAD DATA ----------
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies = pd.DataFrame(movies_dict)

# ---------- RECOMMEND FUNCTION ----------
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# ---------- UI ----------
st.markdown('<p class="title">🎬 MOVIE RECOMMENDER</p>', unsafe_allow_html=True)

st.markdown(
'<p class="subtitle">Discover movies similar to your favorites 🍿</p>',
unsafe_allow_html=True
)

selected_movie_name = st.selectbox(
    "🎥 Choose a movie you like",
    movies['title'].values
)

# ---------- BUTTON ----------
if st.button("Recommend Movies 🍿"):

    recommendations = recommend(selected_movie_name)

    st.markdown("## 🍿 Recommended Movies")

    col1, col2, col3, col4, col5 = st.columns(5)

    cols = [col1, col2, col3, col4, col5]

    for i in range(5):
        with cols[i]:
            st.markdown(
                f'<div class="movie-card">🎬 {recommendations[i]}</div>',
                unsafe_allow_html=True
            )