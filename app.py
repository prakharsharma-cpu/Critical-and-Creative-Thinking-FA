import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
from streamlit_lottie import st_lottie
import time
import random
from datetime import date

# ---------------- CONFIGURATION ----------------
st.set_page_config(
    page_title="SustainStyle Pro",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- ASSETS & STYLING ----------------
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200: return None
        return r.json()
    except: return None

# Load Animations
lottie_earth = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_sO4cnC.json")
lottie_scan = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_w51pcehl.json")

# Custom CSS: "Glassmorphism & Nature" Theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif; 
        background-color: #f1f8f5; /* Soft Mint Background */
    }
    
    /* The Glass Card Effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 24px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
        margin-bottom: 20px;
        transition: transform 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        border-left: 5px solid #10b981; /* Green accent on hover */
    }

    /* Metric Styling */
    .big-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #064e3b;
    }
    .label {
        color: #64748b;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Sidebar Clean Up */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "user_xp" not in st.session_state: st.session_state.user_xp = 1250
if "user_level" not in st.session_state: st.session_state.user_level = 3
if "history" not in st.session_state: 
    # Dummy history
    st.session_state.history = [
        {"Name": "Vintage Levi's", "Brand": "Levi's", "Score": 88, "Type": "Denim"},
        {"Name": "Fast Fashion Tee", "Brand": "H&M", "Score": 45, "Type": "Cotton"},
        {"Name": "Patagonia Fleece", "Brand": "Patagonia", "Score": 92, "Type": "Synthetic"}
    ]

# Gamification Logic
def add_xp(amount):
    st.session_state.user_xp += amount
    # Level up logic: Level up every 500 XP
    new_level = 1 + (st.session_state.user_xp // 500)
    if new_level > st.session_state.user_level:
        st.session_state.user_level = new_level
        st.balloons()
        st.toast(f"🎉 Level Up! Welcome to Level {new_level}!", icon="🌿")

# ---------------- SIDEBAR PROFILE ----------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4333/4333609.png", width=60)
    st.write(f"### Sustainability Profile")
    st.write(f"**Level {st.session_state.user_level} Eco-Guardian**")
    
    # Custom Progress Bar
    current_xp_in_level = st.session_state.user_xp % 500
    st.progress(current_xp_in_level / 500)
    st.caption(f"{current_xp_in_level} / 500 XP to next level")
    
    st.markdown("---")
    menu = st.radio("Navigation", ["🏠 Dashboard", "🔍 Smart Scan", "📚 Eco-Library"])
    
    st.markdown("---")
    st.info("💡 **Daily Tip:** Washing clothes in cold water reduces energy use by 90%.")

# ================= PAGE 1: DASHBOARD =================
if menu == "🏠 Dashboard":
    st.title(f"Hello, Green Hero 👋")
    st.markdown("Here is your impact summary.")

    # Top Metrics Row
    c1, c2, c3, c4 = st.columns(4)
    
    avg_score = sum(x['Score'] for x in st.session_state.history) / len(st.session_state.history)
    
    with c1:
        st.markdown(f"""<div class='glass-card'><div class='big-number'>{len(st.session_state.history)}</div><div class='label'>Items Saved</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class='glass-card'><div class='big-number'>{int(avg_score)}</div><div class='label'>Avg Eco Score</div></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class='glass-card'><div class='big-number'>{st.session_state.user_xp}</div><div class='label'>Total XP</div></div>""", unsafe_allow_html=True)
    with c4:
        st.markdown(f"""<div class='glass-card'><div class='big-number'>12kg</div><div class='label'>CO2 Avoided</div></div>""", unsafe_allow_html=True)

    # Main Visuals
    col_chart, col_recent = st.columns([2, 1])

    with col_chart:
        st.markdown("### 📊 Wardrobe Analysis")
        # Donut Chart for Material Types
        df = pd.DataFrame(st.session_state.history)
        fig = px.pie(df, names='Type', values='Score', hole=0.6, color_discrete_sequence=px.colors.qualitative.Pastel2)
        fig.update_layout(showlegend=True, height=300, margin=dict(l=0,r=0,t=0,b=0), paper_bgcolor='rgba(0,0,0,0)')
        
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_recent:
        st.markdown("### 🕒 Recent Activity")
        for item in st.session_state.history[-3:]:
            color = "#10b981" if item['Score'] > 70 else "#f59e0b"
            st.markdown(f"""
            <div class='glass-card' style='padding: 15px; margin-bottom: 10px;'>
                <div style='display:flex; justify-content:space-between;'>
                    <b>{item['Name']}</b>
                    <span style='color:{color}; font-weight:bold;'>{item['Score']}</span>
                </div>
                <div style='font-size:0.8rem; color:#888;'>{item['Brand']}</div>
            </div>
            """, unsafe_allow_html=True)

# ================= PAGE 2: SMART SCANNER =================
elif menu == "🔍 Smart Scan":
    st.title("AI Fabric Scanner")
    st.write("Point your camera at a garment tag to analyze its environmental footprint.")

    col_cam, col_results = st.columns([1, 1.5])

    with col_cam:
        # UX: Use a container to frame the camera nicely
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        picture = st.camera_input("Activate Scanner", label_visibility="collapsed")
        st.caption("Auto-detects: Material, Origin, Brand")
        st.markdown("</div>", unsafe_allow_html=True)

    if picture:
        with col_results:
            # Simulation of "Processing" (Great for UX)
            with st.status("🤖 AI Analysis in progress...", expanded=True) as status:
                st.write("🔍 Identifying fabric texture...")
                time.sleep(1)
                st.write("🌍 Tracing supply chain...")
                time.sleep(1)
                st.write("📊 Calculating carbon footprint...")
                time.sleep(0.5)
                status.update(label="Analysis Complete!", state="complete", expanded=False)

            # Generate Mock Data
            score_water = random.randint(30, 90)
            score_carbon = random.randint(30, 90)
            score_labor = random.randint(50, 95)
            total_score = int((score_water + score_carbon + score_labor) / 3)
            
            # THE RADAR CHART (The "Pro" Visual)
            categories = ['Water Usage', 'Carbon Footprint', 'Labor Ethics', 'Recyclability', 'Durability']
            r_values = [score_water, score_carbon, score_labor, random.randint(40,80), random.randint(50,90)]
            
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(
                r=r_values,
                theta=categories,
                fill='toself',
                name='Product Score',
                line_color='#10b981'
            ))
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                showlegend=False,
                height=300,
                margin=dict(l=40, r=40, t=20, b=20),
                paper_bgcolor='rgba(0,0,0,0)'
            )

            # Display Results Card
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            c1, c2 = st.columns([2, 1])
            with c1:
                st.subheader("Cotton Blend Hoodie")
                st.caption("Brand: UrbanWear • Origin: Vietnam")
            with c2:
                # Color code the score
                color = "green" if total_score > 75 else "orange" if total_score > 50 else "red"
                st.markdown(f"<h1 style='color:{color}; text-align:right;'>{total_score}/100</h1>", unsafe_allow_html=True)
            
            st.plotly_chart(fig, use_container_width=True)
            
            if st.button("✅ Add to Wardrobe (+50 XP)", type="primary"):
                st.session_state.history.append({
                    "Name": "Cotton Blend Hoodie", "Brand": "UrbanWear", "Score": total_score, "Type": "Cotton"
                })
                add_xp(50)
            
            st.markdown("</div>", unsafe_allow_html=True)

    else:
        with col_results:
            # Empty state animation
            if lottie_scan:
                st_lottie(lottie_scan, height=300)
            st.info("👈 Waiting for image capture...")

# ================= PAGE 3: LIBRARY =================
elif menu == "📚 Eco-Library":
    st.title("Sustainable Alternatives")
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("Based on your scans, try these:")
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.image("https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=300&q=80", use_container_width=True)
        st.write("**Hemp Fabric**")
        st.caption("Uses 50% less water than cotton.")
        
    with col_b:
        st.image("https://images.unsplash.com/photo-1523381210434-271e8be1f52b?auto=format&fit=crop&w=300&q=80", use_container_width=True)
        st.write("**Organic Linen**")
        st.caption("Biodegradable and durable.")
        
    with col_c:
        st.image("https://images.unsplash.com/photo-1542272617-08f086302542?auto=format&fit=crop&w=300&q=80", use_container_width=True)
        st.write("**Tencel / Lyocell**")
        st.caption("Made from sustainably sourced wood.")
    st.markdown("</div>", unsafe_allow_html=True)
