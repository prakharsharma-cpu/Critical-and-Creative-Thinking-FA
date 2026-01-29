import streamlit as st

# Page Configuration for a Mobile-like feel
st.set_page_config(page_title="SustainStyle", layout="centered")

# --- CUSTOM STYLING (The "Eco" Look) ---
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        height: 3em;
        background: linear_gradient(135deg, #4ade80 0%, #22c55e 100%);
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
    .product-card {
        background: white;
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid #e2e8f0;
    }
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

# --- DATA ---
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

# --- HEADER ---
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown('<p class="metric-text">Welcome back</p>', unsafe_allow_html=True)
    st.markdown('<h1 style="margin-top: -20px;">SustainStyle ✨</h1>', unsafe_allow_html=True)

# --- GREEN POINTS CARD ---
with st.container():
    st.markdown("""
    <div class="eco-card" style="background: #1e293b; color: white;">
        <p style="margin: 0; opacity: 0.8; font-size: 0.8rem;">GreenPoints Balance</p>
        <h2 style="margin: 0; color: #4ade80;">2,450 pts</h2>
        <div style="background: #334155; height: 8px; border-radius: 4px; margin-top: 10px;">
            <div style="background: #4ade80; width: 75%; height: 100%; border-radius: 4px;"></div>
        </div>
        <p style="font-size: 0.7rem; margin-top: 5px; opacity: 0.7;">Level 5 • 550 pts to Level 6</p>
    </div>
    """, unsafe_allow_html=True)

# --- SCAN CTA ---
st.markdown("""
<div class="eco-card">
    <h3 style="margin:0;">Scan Your Clothing</h3>
    <p class="metric-text">Discover the environmental impact of your fashion choices</p>
</div>
""", unsafe_allow_html=True)

if st.button("🔍 Scan Now"):
    st.toast("Camera initializing...")

# --- QUICK ACTIONS ---
q1, q2 = st.columns(2)
with q1:
    if st.button("🍃 Eco Alternatives"):
        st.switch_page("pages/alternatives.py") if False else st.write("Navigating...")
with q2:
    if st.button("📈 Track Progress"):
        st.write("Navigating...")

# --- RECENT SCANS ---
st.markdown("### Recent Scans")
r1, r2 = st.columns(2)

for i, product in enumerate(recent_scans):
    target_col = r1 if i == 0 else r2
    with target_col:
        st.image(product["image"], use_container_width=True)
        st.markdown(f"**{product['name']}**")
        st.markdown(f"<span class='metric-text'>{product['brand']}</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='score-badge'>Score: {product['score']}</span>", unsafe_allow_html=True)
