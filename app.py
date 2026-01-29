import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="SustainStyle", layout="centered")

# ---------------- SESSION STATE ----------------
if "points" not in st.session_state:
    st.session_state.points = 2450

if "recent_scans" not in st.session_state:
    st.session_state.recent_scans = []

DEFAULT_IMAGE = "https://images.unsplash.com/photo-1512436991641-6745cdb1723f?w=400"

# ---------------- PRODUCT DATABASE ----------------
PRODUCT_DB = {
    "ECO_COTTON_TEE": {
        "name": "Organic Cotton T-Shirt",
        "brand": "EcoWear",
        "material": "cotton",
        "weight": 0.25
    },
    "REC_POLY_JACKET": {
        "name": "Recycled Polyester Jacket",
        "brand": "GreenThreads",
        "material": "recycled_polyester",
        "weight": 0.8
    },
    "BAMBOO_HOODIE": {
        "name": "Bamboo Fabric Hoodie",
        "brand": "EarthKind",
        "material": "bamboo",
        "weight": 0.6
    }
}

# ---------------- EMISSION FACTORS ----------------
EMISSION_FACTORS = {
    "cotton": 5.9,
    "polyester": 9.5,
    "recycled_polyester": 3.0,
    "bamboo": 2.5,
    "linen": 2.1
}

# ---------------- STYLING (UNCHANGED UX) ----------------
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
st.markdown('<p class="metric-text">Welcome back</p>', unsafe_allow_html=True)
st.markdown('<h1 style="margin-top:-20px;">SustainStyle ✨</h1>', unsafe_allow_html=True)

# ---------------- GREEN POINTS ----------------
progress = min(st.session_state.points / 3000 * 100, 100)

st.markdown(f"""
<div class="eco-card" style="background:#1e293b;color:white;">
<p style="opacity:0.8;font-size:0.8rem;">GreenPoints Balance</p>
<h2 style="color:#4ade80;">{st.session_state.points} pts</h2>
<div style="background:#334155;height:8px;border-radius:4px;">
<div style="background:#4ade80;width:{progress}%;height:100%;border-radius:4px;"></div>
</div>
<p style="font-size:0.7rem;opacity:0.7;">Level 5</p>
</div>
""", unsafe_allow_html=True)

# ---------------- SCAN CTA ----------------
st.markdown("""
<div class="eco-card">
<h3 style="margin:0;">Scan Your Clothing</h3>
<p class="metric-text">Upload QR image or enter QR code manually</p>
</div>
""", unsafe_allow_html=True)

uploaded = st.file_uploader("Upload QR image (optional)", type=["png", "jpg", "jpeg"])
qr_code = st.text_input("Enter QR code value", placeholder="ECO_COTTON_TEE")

if st.button("🔍 Scan Now"):
    code = qr_code.strip()

    if code in PRODUCT_DB:
        product_data = PRODUCT_DB[code]
        factor = EMISSION_FACTORS[product_data["material"]]
        carbon = round(product_data["weight"] * factor, 2)
        eco_score = max(40, int(100 - carbon * 8))

        st.session_state.points += eco_score

        st.session_state.recent_scans.insert(0, {
            "id": code,
            "name": product_data["name"],
            "brand": product_data["brand"],
            "material": product_data["material"],
            "carbon": carbon,
            "score": eco_score,
            "image": DEFAULT_IMAGE
        })

        st.toast(f"Scan complete • {carbon} kg CO₂e • +{eco_score} pts 🌱")

    else:
        st.warning("QR code not recognised.")

# ---------------- RECENT SCANS ----------------
st.markdown("### Recent Scans")
c1, c2 = st.columns(2)

for i, p in enumerate(st.session_state.recent_scans[:2]):
    col = c1 if i % 2 == 0 else c2
    with col:
        st.image(p["image"], use_container_width=True)
        st.markdown(f"**{p['name']}**")
        st.markdown(f"<span class='metric-text'>{p['brand']}</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='score-badge'>Eco Score: {p['score']}</span>", unsafe_allow_html=True)
        st.caption(f"Carbon Footprint: {p['carbon']} kg CO₂e")

# ---------------- EVALUATION METRICS ----------------
st.markdown("### 📊 Sustainability Evaluation")

if st.session_state.recent_scans:
    avg_score = sum(p["score"] for p in st.session_state.recent_scans) / len(st.session_state.recent_scans)
    avg_carbon = sum(p["carbon"] for p in st.session_state.recent_scans) / len(st.session_state.recent_scans)

    baseline = 6.5
    improvement = ((baseline - avg_carbon) / baseline) * 100

    st.markdown(f"""
    <div class="eco-card">
    <p>Average Eco Score: <b>{avg_score:.1f}</b></p>
    <p>Average Carbon Footprint: <b>{avg_carbon:.2f} kg CO₂e</b></p>
    <p>Reduction vs Fast Fashion: <b>{improvement:.1f}%</b></p>
    </div>
    """, unsafe_allow_html=True)
