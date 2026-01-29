import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SustainStyle",
    page_icon="🌿",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected_product" not in st.session_state:
    st.session_state.selected_product = None

# ---------------- CSS ----------------
st.markdown("""
<style>
.main { background-color: #f8fafc; }

/* CARDS */
.eco-card {
    background: white;
    padding: 24px;
    border-radius: 24px;
    box-shadow: 0 6px 24px rgba(0,0,0,0.06);
    margin-bottom: 20px;
    border: 1px solid #f1f5f9;
}

/* TEXT COLORS */
.title-text { color: #14532d; font-weight: 800; }
.section-title { color: #064e3b; font-weight: 700; }
.primary-text { color: #0f172a; font-weight: 600; }
.secondary-text { color: #64748b; font-size: 0.85rem; }

.good-text { color: #16a34a; font-weight: 600; }
.warn-text { color: #ca8a04; font-weight: 600; }
.bad-text { color: #dc2626; font-weight: 600; }

/* BUTTON */
.gradient-nature {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: white;
    padding: 16px;
    border-radius: 16px;
    text-align: center;
    font-weight: 700;
    cursor: pointer;
    transition: 0.2s;
}

.gradient-nature:hover {
    transform: scale(1.03);
}

/* SCORE BADGE */
.score-badge {
    background: #ecfdf5;
    color: #16a34a;
    padding: 6px 14px;
    border-radius: 99px;
    font-size: 0.75rem;
    font-weight: 700;
}

/* PRODUCT */
.product-img {
    width: 100%;
    height: 120px;
    object-fit: cover;
    border-radius: 16px;
}

.click-card:hover {
    transform: translateY(-4px);
    transition: 0.2s;
    cursor: pointer;
}

/* CLEAN UI */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ---------------- DATA ----------------
recent_scans = [
    {
        "id": 1,
        "name": "Organic Cotton T-Shirt",
        "brand": "EcoWear",
        "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400",
        "score": 85,
    },
    {
        "id": 2,
        "name": "Recycled Denim Jacket",
        "brand": "GreenThreads",
        "image": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400",
        "score": 72,
    },
]

# ---------------- HELPER ----------------
def score_color(score):
    if score >= 80:
        return "good-text"
    elif score >= 60:
        return "warn-text"
    else:
        return "bad-text"

# ---------------- HOME PAGE ----------------
if st.session_state.page == "home":

    st.markdown('<h1 class="title-text">SustainStyle 🌿</h1>', unsafe_allow_html=True)
    st.markdown('<p class="secondary-text">Make fashion choices that actually matter</p>', unsafe_allow_html=True)

    # GREEN POINTS
    st.markdown("""
    <div class="eco-card" style="background:#022c22;color:white">
        <small style="opacity:0.8">Total GreenPoints</small>
        <h2>2,450</h2>
        <div style="background:#134e4a;height:6px;border-radius:3px">
            <div style="background:#22c55e;width:75%;height:100%;border-radius:3px"></div>
        </div>
        <small style="opacity:0.7">550 points to Level 6</small>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔍 Scan Your Clothing", use_container_width=True):
        st.session_state.page = "scan"

    st.markdown('<h3 class="section-title">Recent Scans</h3>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    for i, product in enumerate(recent_scans):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class="eco-card click-card">
                <img src="{product['image']}" class="product-img">
                <p class="primary-text">{product['name']}</p>
                <p class="secondary-text">{product['brand']}</p>
                <span class="score-badge {score_color(product['score'])}">
                    Score {product['score']}
                </span>
            </div>
            """, unsafe_allow_html=True)

            if st.button("View Details", key=f"view_{product['id']}"):
                st.session_state.selected_product = product
                st.session_state.page = "details"

# ---------------- SCAN PAGE ----------------
elif st.session_state.page == "scan":

    st.markdown('<h2 class="section-title">Scan Result 📸</h2>', unsafe_allow_html=True)

    score = random.randint(55, 95)
    color_class = score_color(score)

    st.markdown(f"""
    <div class="eco-card">
        <h3 class="{color_class}">Sustainability Score</h3>
        <h1 class="{color_class}">{score}</h1>
        <progress value="{score}" max="100" style="width:100%"></progress>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="eco-card">
        <h4 class="section-title">Impact Breakdown</h4>
        <p class="good-text">🌱 Materials: Eco-Friendly</p>
        <p class="warn-text">💧 Water Usage: Moderate</p>
        <p class="good-text">🏭 Carbon Footprint: Low</p>
    </div>
    """, unsafe_allow_html=True)

    st.success("✔ You earned 50 GreenPoints")

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"

# ---------------- DETAILS PAGE ----------------
elif st.session_state.page == "details":

    product = st.session_state.selected_product

    st.markdown(f'<h2 class="section-title">{product["name"]}</h2>', unsafe_allow_html=True)
    st.image(product["image"], use_container_width=True)

    st.markdown(f"""
    <div class="eco-card">
        <p class="primary-text">Brand: {product['brand']}</p>
        <p class="{score_color(product['score'])}">
            Sustainability Score: {product['score']}
        </p>
        <p class="good-text">✅ Eco-friendly materials used</p>
        <p class="bad-text">❌ Dye process needs improvement</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="eco-card">
        <h4 class="section-title">Better Alternatives</h4>
        <p class="good-text">🌿 Hemp Cotton Tee</p>
        <p class="good-text">🌿 Bamboo Fabric Shirt</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅ Back"):
        st.session_state.page = "home"
