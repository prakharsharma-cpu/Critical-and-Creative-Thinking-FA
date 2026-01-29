import streamlit as st
import random

# Page Configuration for a Mobile-like feel
st.set_page_config(page_title="SustainStyle", layout="centered")

# ---------------- SESSION STATE ----------------
if "points" not in st.session_state:
    st.session_state.points = 2450

if "recent_scans" not in st.session_state:
    st.session_state.recent_scans = [
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

# ---------------- STYLING (UNCHANGED) ----------------
st.markdown("""
<style>
.main { background-color: #f8fafc; }
.stButton>button {
    width: 100%;
    border-radius: 15px;
    height: 3em;
    background: linear-gradient(135deg, #4ade80 0%, #22c55e 100%);
    color: white;
    border: none;
    font-weight: bold;
}
.eco-card {
    background-color: white;
    padding: 20px;
    border-radius: 24px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}
.metric-text { color: #64748b; font-size: 0.8rem; }
.brand-title { color: #1e293b; font-size: 1.5rem; font-weight: 800; margin-bottom: 20px; }
.score-badge {
    background: #f0fdf4;
    color: #166534;
    padding: 2px 8px;
    border-radius: 8px;
    font-weight: bold;
    font-size: 0.8rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown('<p class="metric-text">Welcome back</p>', unsafe_allow_html=True)
    st.markdown('<h1 style="margin-top: -20px;">SustainStyle ✨</h1>', unsafe_allow_html=True)

# ---------------- GREEN POINTS CARD ----------------
progress = min(st.session_state.points / 3000 * 100, 100)

st.markdown(f"""
<div class="eco-card" style="background: #1e293b; color: white;">
    <p style="margin: 0; opacity: 0.8; font-size: 0.8rem;">GreenPoints Balance</p>
    <h2 style="margin: 0; color: #4ade80;">{st.session_state.points} pts</h2>
    <div style="background: #334155; height: 8px; border-radius: 4px; margin-top: 10px;">
        <div style="background: #4ade80; width: {progress}%; height: 100%; border-radius: 4px;"></div>
    </div>
    <p style="font-size: 0.7rem; margin-top: 5px; opacity: 0.7;">
        Level 5 • {3000 - st.session_state.points} pts to Level 6
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- SCAN CTA ----------------
st.markdown("""
<div class="eco-card">
    <h3 style="margin:0;">Scan Your Clothing</h3>
    <p class="metric-text">Discover the environmental impact of your fashion choices</p>
</div>
""", unsafe_allow_html=True)

if st.button("🔍 Scan Now"):
    score = random.randint(60, 95)
    st.session_state.points += score

    new_product = {
        "id": random.randint(100, 999),
        "name": random.choice([
            "Bamboo Fabric Hoodie",
            "Organic Linen Shirt",
            "Recycled Polyester Tee"
        ]),
        "brand": random.choice(["EcoWear", "GreenThreads", "EarthKind"]),
        "image": "https://images.unsplash.com/photo-1520975916090-3105956dac38?w=400",
        "score": score,
    }

    st.session_state.recent_scans.insert(0, new_product)
    st.toast(f"Scan complete! +{score} pts 🌱")

# ---------------- QUICK ACTIONS (UNCHANGED UX) ----------------
q1, q2 = st.columns(2)
with q1:
    if st.button("🍃 Eco Alternatives"):
        st.toast("Showing eco-friendly alternatives 🌿")
with q2:
    if st.button("📈 Track Progress"):
        st.toast("Tracking your sustainability journey 📊")

# ---------------- RECENT SCANS ----------------
st.markdown("### Recent Scans")
r1, r2 = st.columns(2)

for i, product in enumerate(st.session_state.recent_scans[:2]):
    target_col = r1 if i % 2 == 0 else r2
    with target_col:
        st.image(product["image"], use_container_width=True)
        st.markdown(f"**{product['name']}**")
        st.markdown(
            f"<span class='metric-text'>{product['brand']}</span>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<span class='score-badge'>Score: {product['score']}</span>",
            unsafe_allow_html=True
        )
