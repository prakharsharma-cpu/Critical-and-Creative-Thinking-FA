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
.main {
    background-color: #f8fafc;
}

/* CARD */
.eco-card {
    background: white;
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.06);
    margin-bottom: 20px;
    border: 1px solid #e5e7eb;
}

/* TEXT */
.title {
    color: #064e3b;
    font-weight: 800;
    font-size: 2rem;
}

.subtitle {
    color: #334155;
    font-size: 1rem;
}

.section-title {
    color: #065f46;
    font-weight: 700;
}

.primary-text {
    color: #0f172a;
    font-weight: 600;
}

.secondary-text {
    color: #64748b;
    font-size: 0.85rem;
}

.good { color: #16a34a; font-weight: 600; }
.warn { color: #ca8a04; font-weight: 600; }
.bad { color: #dc2626; font-weight: 600; }

/* BUTTON */
.stButton > button {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: white;
    border-radius: 14px;
    padding: 14px;
    font-weight: 700;
    border: none;
}

.stButton > button:hover {
    transform: scale(1.02);
}

/* PRODUCT */
.product-img {
    width: 100%;
    height: 120px;
    object-fit: cover;
    border-radius: 14px;
}

/* SCORE BADGE */
.score {
    background: #ecfdf5;
    padding: 6px 12px;
    border-radius: 99px;
    font-size: 0.75rem;
    font-weight: 700;
}

/* CLEAN UI */
#MainMenu, footer, header {
    visibility: hidden;
}
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

# ---------------- HELPERS ----------------
def score_class(score):
    if score >= 80:
        return "good"
    elif score >= 60:
        return "warn"
    else:
        return "bad"

# ================= HOME =================
if st.session_state.page == "home":

    # HERO
    st.markdown("""
    <div class="eco-card" style="background:#f0fdf4">
        <div class="title">SustainStyle 🌿</div>
        <p class="subtitle">
            Scan clothes • Understand impact • Make better choices
        </p>
    </div>
    """, unsafe_allow_html=True)

    # PRIMARY ACTION
    if st.button("🔍 Scan Your Clothing", use_container_width=True):
        st.session_state.page = "scan"

    st.markdown("<br>", unsafe_allow_html=True)

    # GREEN POINTS (SECONDARY)
    st.markdown("""
    <div class="eco-card">
        <p class="secondary-text">Your GreenPoints</p>
        <h2 class="good">2,450</h2>
        <progress value="75" max="100" style="width:100%"></progress>
        <p class="secondary-text">550 points to next level</p>
    </div>
    """, unsafe_allow_html=True)

    # RECENT SCANS
    st.markdown('<h3 class="section-title">Recent Scans</h3>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    for i, product in enumerate(recent_scans):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class="eco-card">
                <img src="{product['image']}" class="product-img">
                <p class="primary-text">{product['name']}</p>
                <p class="secondary-text">{product['brand']}</p>
                <span class="score {score_class(product['score'])}">
                    Score {product['score']}
                </span>
            </div>
            """, unsafe_allow_html=True)

            if st.button("View Details", key=f"view_{product['id']}"):
                st.session_state.selected_product = product
                st.session_state.page = "details"

# ================= SCAN =================
elif st.session_state.page == "scan":

    score = random.randint(55, 95)

    st.markdown('<h2 class="section-title">Scan Result 📸</h2>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="eco-card">
        <h1 class="{score_class(score)}">{score}</h1>
        <p class="secondary-text">Sustainability Score</p>
        <progress value="{score}" max="100" style="width:100%"></progress>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="eco-card">
        <h4 class="section-title">Impact Breakdown</h4>
        <p class="good">🌱 Materials: Eco-friendly</p>
        <p class="warn">💧 Water Usage: Moderate</p>
        <p class="good">🏭 Carbon Footprint: Low</p>
    </div>
    """, unsafe_allow_html=True)

    st.success("✔ 50 GreenPoints earned")

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"

# ================= DETAILS =================
elif st.session_state.page == "details":

    p = st.session_state.selected_product

    st.markdown(f'<h2 class="section-title">{p["name"]}</h2>', unsafe_allow_html=True)
    st.image(p["image"], use_container_width=True)

    st.markdown(f"""
    <div class="eco-card">
        <p class="primary-text">Brand: {p['brand']}</p>
        <p class="{score_class(p['score'])}">
            Sustainability Score: {p['score']}
        </p>
        <p class="good">✅ Sustainable materials used</p>
        <p class="bad">❌ Dye process needs improvement</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="eco-card">
        <h4 class="section-title">Better Alternatives</h4>
        <p class="good">🌿 Hemp Cotton Tee</p>
        <p class="good">🌿 Bamboo Fabric Shirt</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅ Back"):
        st.session_state.page = "home"
