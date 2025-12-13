import streamlit as st
import joblib
import requests
from PIL import Image
from io import BytesIO

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Movie Recommendation System",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================
@st.cache_resource
def load_models():
    df = joblib.load('df.pkl')
    vectors = joblib.load('vectors.pkl')
    model = joblib.load('model.pkl')
    return df, vectors, model

df, vectors, model = load_models()

# =========================
# SIDEBAR (ONLY CONTROLS)
# =========================
with st.sidebar:
    st.markdown("## ⚙ Recommendation Settings")

    top_k = st.slider(
        "Number of recommendations",
        min_value=3,
        max_value=10,
        value=5
    )

    show_scores = st.checkbox(
        "Show similarity score",
        value=False
    )

    st.markdown("---")
    st.markdown("### ℹ About")
    st.write(
        "This app recommends movies using **content-based filtering** "
        "and fetches posters via the **OMDb API**."
    )

# =========================
# HEADER (HERO SECTION)
# =========================
st.markdown(
    """
    <div style="text-align:center; padding:20px 0;">
        <h1 style="font-size:48px;">🎬 Movie Recommendation System</h1>
        <p style="font-size:18px; color:gray;">
            Discover movies similar to the one you love
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<hr>", unsafe_allow_html=True)

# =========================
# MOVIE SELECTION (MAIN PAGE)
# =========================
st.markdown("### 🎥 Choose a Movie")

item = st.selectbox(
    "Start typing to search",
    df.name,
    index=0
)

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# POSTER FETCH
# =========================
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    url = f"http://www.omdbapi.com/?i={movie_id}&apikey=1a13201a"
    try:
        resp = requests.get(url, timeout=5)
        data = resp.json()
        poster = data.get("Poster")
        if poster and poster != "N/A":
            headers = {"User-Agent": "Mozilla/5.0"}
            img_resp = requests.get(poster, headers=headers, timeout=5)
            return Image.open(BytesIO(img_resp.content))
    except:
        return None
    return None

# =========================
# RECOMMEND BUTTON
# =========================
if st.button("Recommend Similar Movies", use_container_width=True):
    with st.spinner("Finding movies you may like..."):
        index = df[df.name == item].index[0]
        test_vector = vectors[index]

        scores, indexes = model.kneighbors(
            [test_vector],
            n_neighbors=top_k + 1
        )

        rows = df.iloc[indexes[0][1:]]
        sim_scores = scores[0][1:]

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("🍿 Top Recommendations for You")

    cols = st.columns(top_k)

    for col, (name, mid, score) in zip(
        cols,
        zip(rows.name, rows.movie_id, sim_scores)
    ):
        with col:
            poster_img = fetch_poster(mid)

            if poster_img:
                st.image(poster_img, use_container_width=True)
            else:
                st.image("default_poster.jpg", use_container_width=True)

            st.markdown(
                f"<p style='text-align:center; font-weight:600;'>{name}</p>",
                unsafe_allow_html=True
            )

            if show_scores:
                st.caption(f"Similarity score: {score:.2f}")

# =========================
# FOOTER
# =========================
st.markdown("<hr>", unsafe_allow_html=True)
# st.caption("Built with Streamlit • Content-Based Movie Recommendation")
