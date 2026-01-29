import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="SustainStyle", page_icon="🌿", layout="centered")

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected_product" not in st.session_state:
    st.session_state.selected_product = None

# ---------------- CSS ----------------
st.markdown("""
<style>
.main { background-color: #f8fafc; }

.eco-card {
    background: white;
    padding: 24px;
    border-radius: 24px;
    box-shadow: 0 6px 24px rgba(0,0,0,0.06);
    margin-bottom: 20px;
    border: 1px solid #f1f5f9;
}

.gradient-nature {
    background: linear-gradient(135deg, #2ecc71, #27ae60);
    color: white;
    padding: 16px;
    border-radius: 16px;
    text-align: center;
    font-weight: 700;
    cursor: pointer;
    transition: 0.2s;
    text-decoration: none;
    display: block;
}

.gradient-nature:hover {
    transform: scale(1.03);
}

.score-badge {
    background: #ecfdf5;
    color: #059669;
    padding: 6px 14px;
    border-radius: 99px;
    font-size: 0.75rem;
    font-weight: 700;
}

.product-img {
    width: 100%;
    border-radius: 16px;
    height: 120px;
    object-fit: cover;
}

.click-card:hover {
    transform: translateY(-4px);
    transition: 0.2s;
    cursor: pointer;
}

#MainMenu, footer, header {visibility: hidden;}
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

# ---------------- HOME PAGE ----------------
if st.session_state.page == "home":

    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown("**Welcome back 👋**")
        st.markdown("## SustainStyle")
    with col2:
        st.markdown("✨")

    # Green Points
    st.markdown("""
    <div class="eco-card" style="background:#1e293b;color:white">
        <small>Total GreenPoints</small>
        <h2>2,450</h2>
        <div style="background:#334155;height:6px;border-radius:3px">
            <div style="background:#2ecc71;width:75%;height:100%;border-radius:3px"></div>
        </div>
        <small>550 points to Level 6</small>
    </div>
    """, unsafe_allow_html=True)

    # Scan CTA
    if st.button("🔍 Scan Your Clothing", use_container_width=True):
        st.session_state.page = "scan"

    st.markdown("### Recent Scans")

    colA, colB = st.columns(2)
    for i, product in enumerate(recent_scans):
        with (colA if i % 2 == 0 else colB):
            st.markdown(f"""
            <div class="eco-card click-card">
                <img src="{product['image']}" class="product-img">
                <b>{product['name']}</b><br>
                <small>{product['brand']}</small><br><br>
                <span class="score-badge">Score {product['score']}</span>
            </div>
            """, unsafe_allow_html=True)

            if st.button("View Details", key=f"view_{product['id']}"):
                st.session_state.selected_product = product
                st.session_state.page = "details"

# ---------------- SCAN PAGE ----------------
elif st.session_state.page == "scan":

    st.markdown("## 📸 Scan Result")

    score = random.randint(60, 95)

    st.markdown(f"""
    <div class="eco-card">
        <h3>Sustainability Score</h3>
        <h1 style="color:#2ecc71">{score}</h1>
        <progress value="{score}" max="100" style="width:100%"></progress>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="eco-card">
        <h4>Impact Breakdown</h4>
        🌱 Materials: Good  
        💧 Water Usage: Moderate  
        🏭 Carbon Footprint: Low  
    </div>
    """, unsafe_allow_html=True)

    st.success("✔ Eco-friendly choice! You earned 50 GreenPoints")

    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"

# ---------------- DETAILS PAGE ----------------
elif st.session_state.page == "details":

    product = st.session_state.selected_product

    st.markdown(f"## {product['name']}")
    st.image(product["image"], use_container_width=True)

    st.markdown(f"""
    <div class="eco-card">
        <b>Brand:</b> {product['brand']} <br><br>
        <b>Sustainability Score:</b> {product['score']} <br><br>
        ✅ Uses eco-friendly materials  
        ❌ Dye process needs improvement  
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="eco-card">
        <h4>Better Alternatives</h4>
        🌿 Hemp Cotton Tee  
        🌿 Bamboo Fabric Shirt  
    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅ Back"):
        st.session_state.page = "home"
