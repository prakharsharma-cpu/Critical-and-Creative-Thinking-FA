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

# ---------------- CSS (HIGH CONTRAST ONLY) ----------------
st.markdown("""
<style>
.main {
    background-color: #f9fafb;
}

/* CARDS */
.eco-card {
    background-color: #ffffff;
    padding: 22px;
    border-radius: 14px;
    border: 1px solid #d1d5db;
    margin-bottom: 18px;
}

/* TEXT – ALWAYS VISIBLE */
.title {
    color: #065f46;
    font-size: 2rem;
    font-weight: 800;
}

.subtitle {
    color: #1f2933;
    font-size: 1rem;
}

.section-title {
    color: #064e3b;
    font-weight: 700;
    font-size: 1.2rem;
}

.primary-text {
    color: #111827;
    font-weight: 600;
}

.secondary-text {
    color: #374151;
    font-size: 0.9rem;
}

/* STATUS COLORS (READABLE) */
.good {
    color: #166534;
    font-weight: 600;
}

.warn {
    color: #92400e;
    font-weight: 600;
}

.bad {
    color: #991b1b;
    font-weight: 600;
}

/* BUTTON – CLEAR */
.stButton > button {
    background-color: #22c55e;
    color: #052e16;
    border-radius: 10px;
    font-weight: 700;
    border: 1px solid #16a34a;
    padding: 12px;
}

.stButton > button:hover {
    background-color: #16a34a;
}

/* PRODUCT IMAGE */
.product-img {
    width: 100%;
    height: 120px;
    object-fit: cover;
    border-radius: 10px;
}

/* SCORE BADGE */
.score {
    background-color: #ecfdf5;
    border: 1px solid #16a34a;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
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

    st.markdown("""
    <div class="eco-card">
        <div class="title">SustainStyle 🌿</div>
        <p class="subtitle">
            Scan clothes, understand environmental impact, and make better fashion choices.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔍 Scan Your Clothing", use_container_width=True):
        st.session_state.page = "scan"

    st.markdown("""
    <div class="eco-card">
        <p class="section-title">Your GreenPoints</p>
        <h2 class="good">2,450</h2>
        <progress value="75" max="100" style="width:100%"></progress>
        <p class="secondary-text">550 points needed for next level</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<p class="section-title">Recent Scans</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    for i, product in enumerate(recent_scans):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class="eco-card">
                <img src="{product['image']}" class="product-img">
                <p class="primary-text">{product['name']}</p>
                <p class="secondary-text">{product['brand']}</p>
                <span class="score {score_class(product['score'])}">
                    Score: {product['score']}
                </span>
            </div>
            """, unsafe_allow_html=True)

            if st.button("View Details", key=f"view_{product['id']}"):
                st.session_state.selected_product = product
                st.session_state.page = "details"

# ================= SCAN =================
elif st.session_state.page == "scan":

    score = random.randint(55, 95)

    st.markdown('<p class="section-title">Scan Result</p>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="eco-card">
        <h1 class="{score_class(score)}">{score}</h1>
        <p class="secondary-text">Sustainability Score</p>
        <progress value="{score}" max="100" style="width:100%"></progress>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="eco-card">
        <p class="section-title">Impact Breakdown</p>
        <p class="good">🌱 Materials: Eco-friendly</p>
        <p class="warn">💧 Water usage: Moderate</p>
        <p class="good">🏭 Carbon footprint: Low</p>
    </div>
    """, unsafe_allow_html=True)

    st.success("You earned 50 GreenPoints")

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"

# ================= DETAILS =================
elif st.session_state.page == "details":

    p = st.session_state.selected_product

    st.markdown(f'<p class="section-title">{p["name"]}</p>', unsafe_allow_html=True)
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
        <p class="section-title">Better Alternatives</p>
        <p class="good">🌿 Hemp Cotton Tee</p>
        <p class="good">🌿 Bamboo Fabric Shirt</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅ Back"):
        st.session_state.page = "home"
