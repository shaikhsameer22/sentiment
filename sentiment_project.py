
import streamlit as st
import joblib

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="💬",
    layout="centered"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("sentiment_model.pkl")


# ---------------- CSS ----------------
st.markdown("""
<style>

body {
    background-color: #f7f7fb;
}

.header {
    background: linear-gradient(90deg, #6c5ce7, #8e44ad);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 30px;
}

.header h1 {
    color: white;
    font-size: 38px;
    margin: 0;
    font-family: Arial;
}

.positive {
    background-color: #dff7e8;
    color: #198754;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    margin-top: 20px;
}

.negative {
    background-color: #ffe3e3;
    color: #dc3545;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    margin-top: 20px;
}

.stButton button {
    width: 100%;
    background-color: #6c5ce7;
    color: white;
    border: none;
    border-radius: 10px;
    height: 45px;
    font-size: 16px;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #5848c2;
}

[data-testid="stSidebar"] {
    background-color: #211a3c;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------
st.markdown("""
<div class="header">
    <h1>Sentiment Analysis</h1>
</div>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
st.sidebar.image(
    "sentiment analysis.jpg",
    use_container_width=True
)

st.sidebar.markdown("## 👥 About Us")

st.sidebar.write(
    "We are developing Machine Learning projects "
    "based on NLP."
)

st.sidebar.markdown("## 📖 About Project")

st.sidebar.write(
    "Sentiment Analysis is an NLP and Machine Learning "
    "project that analyzes text and classifies it as "
    "Positive or Negative."
)

st.sidebar.markdown("## 📞 Contact Us")

st.sidebar.write("📱 +91 8090428587")


# ---------------- SAMPLE REVIEW ----------------
st.markdown("### 🎯 Sample Review")

sample_review = st.selectbox(
    "Select a review",
    [
        "Good Food",
        "Quality was not Good",
        "Awesome taste",
        "Nice Behaviour and taste was also Good",
        "I did not like the taste at all.",
        "The service was very slow and disappointing."
    
    ]
)

if st.button("🔍 Predict", key="sample"):

    pred = model.predict([sample_review])

    if pred[0] == 0:

        st.markdown(
            """
            <div class="negative">
                😞 Negative
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="positive">
                😊 Positive
            </div>
            """,
            unsafe_allow_html=True
        )

        st.snow()


# ---------------- USER REVIEW ----------------
st.markdown("---")

st.markdown("### ✍️ Your Review")

user_review = st.text_area(
    "Write your review",
    placeholder="Write your review here...",
    height=120
)

if st.button("🚀 Predict", key="user"):

    if user_review.strip() == "":
        st.warning("⚠️ Please enter a review.")

    else:

        pred = model.predict([user_review])

        if pred[0] == 0:

            st.markdown(
                """
                <div class="negative">
                    😞 Negative
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                """
                <div class="positive">
                    😊 Positive
                </div>
                """,
                unsafe_allow_html=True
            )

            st.snow()


# ---------------- FOOTER ----------------
st.markdown("---")

st.caption("💜 Sentiment Analysis • Python & Streamlit")
