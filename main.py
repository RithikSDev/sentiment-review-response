import streamlit as st
from utils import respond_to_review

# ─── Set Page Configuration ─────────────────────────────
st.set_page_config(page_title="Sentiment Review Response", page_icon="💬", layout="wide")

# ─── Custom Navy Gradient Background ─────────────────────────────
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: #ffffff;
    }
    header[data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }
    .st-emotion-cache-6qob1r, .st-emotion-cache-1v0mbdj, .st-emotion-cache-ffhzg2, .st-emotion-cache-1d391kg, .st-emotion-cache-1offfwp {
        color: #ffffff !important;
    }
    .st-emotion-cache-1v0mbdj textarea {
        background-color: #1a2a38;
        color: #ffffff;
        border: 1px solid #4c5c68;
        border-radius: 0.5rem;
    }
    .st-emotion-cache-1v0mbdj button {
        background-color: #4c5c68;
        color: #ffffff;
    }
    .st-emotion-cache-6qob1r {
        background-color: #12232e;
        color: #ffffff;
    }
    .st-emotion-cache-6qob1r .css-1v0mbdj {
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ─── Sidebar ─────────────────────────────
with st.sidebar:
    st.markdown("""<style>section[data-testid="stSidebar"] { background-color: #0b1e2d; } .sidebar-content { color: #ffffff; }</style>""", unsafe_allow_html=True)
    st.title("📌 About")
    st.markdown("""
    This app uses **Natural Language Processing (NLP)**  
    to:
    - Analyze customer review **sentiment**
    - Generate a **smart reply** in seconds!
    """)
    st.markdown("👨‍💻 Created by [Rithik S.](https://github.com/RithikSDev)")

# ─── Main Title Section ─────────────────────────────
st.title("🧠 Sentiment Review Response Generator")
st.markdown("Give us a review, we’ll give you the perfect reply!")

# ─── Two-column Layout ─────────────────────────────
col1, col2 = st.columns([1.3, 1])

with col1:
    review = st.text_area("✍️ Paste a customer review here:", height=180, placeholder="e.g. The delivery was late, and the package was damaged...")

with col2:
    st.markdown("#### 🚀 How it works:")
    st.markdown("""
    - 🧠 Detects **Sentiment**: Positive, Negative, or Neutral  
    - ✍️ Generates a **Contextual Response**  
    - 🕒 Saves your time in customer support
    """)
    
    # Dynamically change the text based on whether a review is entered
    if review.strip() == "":
        st.markdown("<span style='color: #ff6347;'>Please enter a review first!</span>", unsafe_allow_html=True)
    else:
        st.markdown("<span style='color: #32cd32;'>Click below to analyze your review!</span>", unsafe_allow_html=True)

# ─── Colorful Analyze Button ─────────────────────────────
button_style = """
    <style>
    .stButton button {
        background-color: #4CAF50; /* Green */
        color: white;
        font-size: 16px;
        border-radius: 10px;
        padding: 12px 24px;
        transition: all 0.3s;
    }
    .stButton button:hover {
        background-color: #45a049; /* Darker Green */
        box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.2);
        transform: scale(1.05);
    }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# ─── Analyze Button ─────────────────────────────
if st.button("✨ Analyze Review"):
    if review.strip() == "":
        st.warning("⚠️ Please enter a review first.")
    else:
        with st.spinner("🔎 Analyzing..."):
            response, sentiment = respond_to_review(review)

        # ─── Display Result ─────────────────────────────
        st.success(f"✅ Sentiment Detected: **{sentiment}**")

        st.markdown("### 💬 Auto-generated Response:")
        st.markdown(f"""
        <div style="background-color:#1a2a38; padding:20px; border-radius:10px; border-left:5px solid #4CAF50;">
            <p style="font-size:16px; color:#ffffff;">{response}</p>
        </div>
        """, unsafe_allow_html=True)

        st.balloons()

# ─── Footer ─────────────────────────────
st.markdown("---")
st.markdown("<div style='text-align:center; color: #ccc;'>Built with ❤️ using Streamlit | NLP Powered | Feedback welcomed!</div>", unsafe_allow_html=True)
