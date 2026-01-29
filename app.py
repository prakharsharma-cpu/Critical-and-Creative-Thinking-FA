import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="SustainStyle", page_icon="🌿", layout="centered")

# --- CUSTOM CSS (Tailwind & Framer Motion Mimicry) ---
st.markdown("""
    <style>
    /* Main Container Styles */
    .main {
        background-color: #f8fafc;
    }
    
    /* Card Styles */
    .eco-card {
        background-color: white;
        padding: 24px;
        border-radius: 24px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        border: 1px solid #f1f5f9;
    }

    /* Green Nature Gradient for Scan Button */
    .gradient-nature {
        background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
        color: white;
        padding: 16px;
        border-radius: 16px;
        text-align: center;
        font-weight: 700;
        cursor: pointer;
        transition: transform 0.2s;
        text-decoration: none;
        display: block;
        margin-top: 10px;
    }
    .gradient-nature:hover {
        transform: scale(1.02);
        color: white;
    }

    /* Score Badge */
    .score-badge {
        background: #ecfdf5;
        color: #059669;
        padding: 4px 12px;
        border-radius: 99px;
        font-size: 0.8rem;
        font-weight: 600;
    }

    /* Product Image Styling */
    .product-img {
        width: 100%;
        border-radius: 16px;
        object-fit: cover;
        height: 120px;
        margin-bottom: 8px;
    }

    /* Quick Action Buttons */
    .quick-action {
        background: white;
        border-radius: 20px;
        padding: 16px;
        text-align: left;
        box-shadow: 0 2px 10px rgba(0,0,0,0.03);
        border: 1px solid #f1f5f9;
        display: flex;
        flex-direction: column;
        gap: 8px;
    }

    /* Hide Streamlit elements for cleaner UI */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
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

# --- UI LAYOUT ---

# 1. Header
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown('<p style="color: #64748b; margin-bottom: 0;">Welcome back</p>', unsafe_allow_html=True)
    st.markdown('<h1 style="margin-top: 0; font-weight: 800;">SustainStyle</h1>', unsafe_allow_html=True)
with col2:
    st.markdown('<div style="background: #f1f5f9; padding: 12px; border-radius: 50%; text-align: center;">✨</div>', unsafe_allow_html=True)

# 2. GreenPoints Summary (Mock Component)
st.markdown(f"""
    <div class="eco-card" style="background: #1e293b; color: white;">
        <p style="font-size: 0.8rem; opacity: 0.8; margin-bottom: 4px;">Total GreenPoints</p>
        <div style="display: flex; justify-content: space-between; align-items: baseline;">
            <h2 style="color: white; margin: 0;">2,450</h2>
            <span style="font-size: 0.9rem;">Level 5</span>
        </div>
        <div style="background: rgba(255,255,255,0.1); height: 6px; border-radius: 3px; margin-top: 12px;">
            <div style="background: #2ecc71; width: 75%; height: 100%; border-radius: 3px;"></div>
        </div>
        <p style="font-size: 0.7rem; margin-top: 8px; opacity: 0.7;">550 points until Level 6</p>
    </div>
""", unsafe_allow_html=True)

# 3. Scan CTA
st.markdown("""
    <div class="eco-card">
        <h3 style="margin-top: 0;">Scan Your Clothing</h3>
        <p style="color: #64748b; font-size: 0.9rem;">Discover the environmental impact of your fashion choices</p>
        <a href="/scan" class="gradient-nature">🔍 Scan Now</a>
    </div>
""", unsafe_allow_html=True)

# 4. Quick Actions
st.markdown('<h3 style="font-size: 1.1rem; margin-bottom: 12px;">Quick Actions</h3>', unsafe_allow_html=True)
qa_col1, qa_col2 = st.columns(2)
with qa_col1:
    st.markdown("""
        <div class="quick-action">
            <span style="background: #ecfdf5; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; border-radius: 8px;">🌿</span>
            <span style="font-size: 0.85rem; font-weight: 600;">Find Eco Alternatives</span>
        </div>
    """, unsafe_allow_html=True)
with qa_col2:
    st.markdown("""
        <div class="quick-action">
            <span style="background: #eff6ff; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; border-radius: 8px;">📈</span>
            <span style="font-size: 0.85rem; font-weight: 600;">Track Progress</span>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 5. Recent Scans
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <h3 style="margin: 0; font-size: 1.1rem;">Recent Scans</h3>
        <a href="#" style="color: #2ecc71; font-size: 0.85rem; text-decoration: none; font-weight: 600;">See All</a>
    </div>
""", unsafe_allow_html=True)

# Grid for products
prod_col1, prod_col2 = st.columns(2)
cols = [prod_col1, prod_col2]

for idx, product in enumerate(recent_scans):
    with cols[idx % 2]:
        st.markdown(f"""
            <div class="eco-card" style="padding: 12px;">
                <img src="{product['image']}" class="product-img">
                <p style="font-weight: 700; font-size: 0.85rem; margin-bottom: 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{product['name']}</p>
                <p style="color: #64748b; font-size: 0.75rem; margin-top: 0;">{product['brand']}</p>
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="score-badge">Score: {product['score']}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"View Details", key=f"prod_{product['id']}"):
            st.info(f"Navigating to details for {product['name']}...")
