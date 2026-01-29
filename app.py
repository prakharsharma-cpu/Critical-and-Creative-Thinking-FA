import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="SustainStyle", layout="centered")

# ---------------- SESSION STATE ----------------
if "points" not in st.session_state:
    st.session_state.points = 2450

if "recent_scans" not in st.session_state:
    st.session_state.recent_scans = []

if "view" not in st.session_state:
    st.session_state.view = "home"

# ---------------- STYLING ----------------
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
    padding: 4px 10px;
    border-radius: 8px;
    font-weight: bold;
    font-size: 0.8rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<p class="metric-text">Welcome back</p>', unsafe_allow_html=True)
st.markdown('<h1 style="margin-top:-10px;">SustainStyle ✨</h1>', unsafe_allow_html=True)

# ---------------- GREEN POINTS ----------------
level = st.session_state.points // 500
progress = (st.session_state.points % 500) / 500 * 100

st.markdown(f"""
<div class="eco-card" style="background:#1e293b;color:white;">
<p style="opacity:0.8;font-size:0.8rem;">GreenPoints Balance</p>
<h2 style="color:#4ade80;">{st.session_state.points} pts</h2>
<div style="background:#334155;height:8px;border-radius:4px;">
<div style="background:#4ade80;width:{progress}%;height:100%;border-radius:4px;"></div>
</div>
<p style="font-size:0.7rem;opacity:0.7;">Level {level}</p>
</div>
""", unsafe_allow_html=True)

# ---------------- NAVIGATION ----------------
q1, q2 = st.columns(2)
with q1:
    if st.button("🍃 Eco Alternatives"):
        st.session_state.view = "alternatives"
with q2:
    if st.button("📈 Track Progress"):
        st.session_state.view = "progress"

# ================= HOME VIEW =================
if st.session_state.view == "home":

    st.markdown("""
    <div class="eco-card">
        <h3>Scan Your Clothing</h3>
        <p class="metric-text">Discover environmental impact instantly</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔍 Scan Now"):
        score = random.randint(60, 95)
        points_earned = score // 2
        st.session_state.points += points_earned

        product = {
            "name": random.choice([
                "Organic Cotton T-Shirt",
                "Recycled Denim Jacket",
                "Bamboo Fabric Hoodie"
            ]),
            "brand": random.choice(["EcoWear", "GreenThreads", "EarthKind"]),
            "score": score,
            "points": points_earned
        }

        st.session_state.recent_scans.insert(0, product)
        st.toast(f"Scan complete! +{points_earned} pts 🌱")

    st.markdown("### Recent Scans")

    if not st.session_state.recent_scans:
        st.caption("No scans yet. Try scanning something 👕")
    else:
        for item in st.session_state.recent_scans[:3]:
            st.markdown(f"""
            <div class="eco-card">
            <b>{item['name']}</b><br>
            <span class="metric-text">{item['brand']}</span><br><br>
            <span class="score-badge">Eco Score: {item['score']}</span>
            <span class="metric-text"> +{item['points']} pts</span>
            </div>
            """, unsafe_allow_html=True)

# ================= ALTERNATIVES VIEW =================
elif st.session_state.view == "alternatives":
    st.markdown("### 🌿 Better Eco Alternatives")

    alternatives = [
        ("Hemp Cotton Shirt", "90 Eco Score"),
        ("Upcycled Denim", "88 Eco Score"),
        ("Bamboo Activewear", "92 Eco Score")
    ]

    for name, score in alternatives:
        st.markdown(f"""
        <div class="eco-card">
        <b>{name}</b><br>
        <span class="score-badge">{score}</span>
        </div>
        """, unsafe_allow_html=True)

    if st.button("⬅ Back"):
        st.session_state.view = "home"

# ================= PROGRESS VIEW =================
elif st.session_state.view == "progress":
    st.markdown("### 📊 Your Impact")

    total_scans = len(st.session_state.recent_scans)
    avg_score = (
        sum(p["score"] for p in st.session_state.recent_scans) / total_scans
        if total_scans else 0
    )

    st.markdown(f"""
    <div class="eco-card">
    <p>Total Scans: <b>{total_scans}</b></p>
    <p>Average Eco Score: <b>{avg_score:.1f}</b></p>
    <p>Carbon Conscious Choices 🌍</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("⬅ Back"):
        st.session_state.view = "home"
