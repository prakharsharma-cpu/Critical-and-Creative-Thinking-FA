import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
from streamlit_lottie import st_lottie
import time
import random

# ---------------- CONFIGURATION ----------------
st.set_page_config(
    page_title="SustainStyle • Eco-Scanner",
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

# Load Eco Animations
lottie_plant = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_calmz.json") # Reusing a calm animation
lottie_scan = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_m6cu968e.json") # Scanning animation

# Custom CSS (Green/Eco Theme)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif; 
        background-color: #f0fdf4; /* Very light green bg */
    }
    
    /* Eco Card Styling */
    .eco-card {
        background: white;
        border: 1px solid #dcfce7;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 100, 0, 0.05);
        transition: transform 0.2s;
        margin-bottom: 1rem;
    }
    .eco-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 100, 0, 0.1);
        border-color: #22c55e;
    }
    
    /* Custom headings */
    h1, h2, h3 { color: #166534; }
    
    /* Highlight text */
    .highlight { color: #15803d; font-weight: bold; }
    
    /* Camera Input Styling Fix */
    div[data-testid="stCameraInput"] {
        border: 2px dashed #22c55e;
        border-radius: 15px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE & GAMIFICATION ----------------
if "green_points" not in st.session_state: st.session_state.green_points = 2450
if "eco_level" not in st.session_state: st.session_state.eco_level = 5
if "history" not in st.session_state: 
    st.session_state.history = [
        {"Name": "Organic Cotton Tee", "Brand": "EcoWear", "Score": 85, "Date": "Today"},
        {"Name": "Recycled Denim", "Brand": "GreenThreads", "Score": 72, "Date": "Yesterday"}
    ]

# Leveling Logic
def check_level_up():
    new_level = 1 + (st.session_state.green_points // 500)
    if new_level > st.session_state.eco_level:
        st.balloons()
        st.toast(f"🌱 Leveled Up! You are now an Eco-Guardian Lvl {new_level}!")
    st.session_state.eco_level = new_level

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("SustainStyle 🌿")
    st.write(f"### 👤 Eco-Warrior Lvl {st.session_state.eco_level}")
    
    # Progress Bar
    points_to_next = 500 - (st.session_state.green_points % 500)
    prog = (st.session_state.green_points % 500) / 500
    st.progress(prog)
    st.caption(f"{st.session_state.green_points} GP • {points_to_next} to next level")
    
    st.markdown("---")
    menu = st.radio("Menu", ["🏠 Dashboard", "📷 Scan Barcode", "🏆 Leaderboard"])
    
    st.markdown("---")
    st.info("💡 **Tip:** Look for the 'Fair Trade' logo on tags!")

# ---------------- PAGE 1: DASHBOARD ----------------
if menu == "🏠 Dashboard":
    st.title("Your Impact Dashboard")
    
    # Top Stats
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"<div class='eco-card'><h3>{len(st.session_state.history)}</h3><p>Items Scanned</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='eco-card'><h3>{st.session_state.green_points}</h3><p>Green Points</p></div>", unsafe_allow_html=True)
    with c3:
        avg_score = sum(i['Score'] for i in st.session_state.history) / len(st.session_state.history)
        st.markdown(f"<div class='eco-card'><h3>{avg_score:.0f}/100</h3><p>Avg Wardrobe Score</p></div>", unsafe_allow_html=True)

    col_main, col_hist = st.columns([2, 1])
    
    with col_main:
        st.markdown("### 📉 Sustainability Trends")
        # Dummy Data for Trend
        chart_data = pd.DataFrame({
            "Date": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "EcoScore": [60, 65, 70, 68, 85, 90, 88]
        })
        fig = px.area(chart_data, x="Date", y="EcoScore", color_discrete_sequence=["#22c55e"])
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=250)
        st.plotly_chart(fig, use_container_width=True)

    with col_hist:
        st.markdown("### 🕒 Recent Scans")
        for item in st.session_state.history[-3:]:
            st.markdown(f"""
            <div class='eco-card' style='padding:10px;'>
                <b>{item['Name']}</b><br>
                <span style='color:grey; font-size:0.8em'>{item['Brand']}</span>
                <span style='float:right; color:{'green' if item['Score']>80 else 'orange'}; font-weight:bold'>{item['Score']}</span>
            </div>
            """, unsafe_allow_html=True)

# ---------------- PAGE 2: BARCODE SCANNER ----------------
elif menu == "📷 Scan Barcode":
    st.title("Scan & Analyze")
    st.write("Point your camera at the clothing tag/barcode.")

    col_cam, col_result = st.columns([1, 1])

    with col_cam:
        # CAMERA INPUT
        img_buffer = st.camera_input("Scanner Active", label_visibility="collapsed")
        
        if not img_buffer:
            if lottie_scan:
                st_lottie(lottie_scan, height=200, key="scan_anim")
            st.info("Waiting for barcode...")

    # LOGIC: Simulating a scan result when an image is taken
    if img_buffer is not None:
        with col_result:
            with st.spinner("Decoding Barcode & Analyzing Supply Chain..."):
                time.sleep(2) # Cosmetic delay for realism
                
                # Randomized Mock Data for Demo
                score = random.randint(40, 95)
                water_usage = random.randint(30, 90)
                carbon = random.randint(20, 80)
                ethics = random.randint(50, 100)
                
                detected_item = random.choice(["Denim Jeans", "Polyester Jacket", "Hemp Shirt", "Wool Sweater"])
                brand_name = random.choice(["FastFashionCo", "GreenThread", "EarthWear", "UrbanBasic"])

            # RESULT CARD
            st.markdown(f"<div class='eco-card'>", unsafe_allow_html=True)
            st.subheader(f"{detected_item}")
            st.caption(f"Brand: {brand_name} • ID: 89340012")
            
            # Gauge Chart for Overall Score
            fig_gauge = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = score,
                title = {'text': "Eco Score"},
                gauge = {
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#15803d"},
                    'steps': [
                        {'range': [0, 50], 'color': "#fca5a5"},
                        {'range': [50, 80], 'color': "#fde047"},
                        {'range': [80, 100], 'color': "#86efac"}
                    ]
                }
            ))
            fig_gauge.update_layout(height=200, margin=dict(l=20,r=20,t=0,b=0))
            st.plotly_chart(fig_gauge, use_container_width=True)
            
            # Detailed Metrics
            c_a, c_b, c_c = st.columns(3)
            c_a.metric("Water", f"{water_usage}/100", help="Water consumption during manufacturing")
            c_b.metric("Carbon", f"{carbon}/100", help="CO2 emitted during transport")
            c_c.metric("Labor", f"{ethics}/100", help="Ethical labor practices score")
            
            # Action Button
            if st.button("✅ Add to Wardrobe (+50 XP)"):
                new_entry = {"Name": detected_item, "Brand": brand_name, "Score": score, "Date": "Just now"}
                st.session_state.history.append(new_entry)
                st.session_state.green_points += 50
                check_level_up()
                st.toast("Added successfully!")
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Suggestion Logic
            if score < 60:
                st.warning(f"⚠️ **Alternative:** This item has a high carbon footprint. Try looking for {detected_item} made from Recycled Polyester instead.")

# ---------------- PAGE 3: LEADERBOARD ----------------
elif menu == "🏆 Leaderboard":
    st.title("Community Leaderboard")
    
    st.markdown("<div class='eco-card'>", unsafe_allow_html=True)
    st.write("See how you stack up against other Eco-Warriors in your area.")
    
    leader_data = pd.DataFrame({
        "Rank": [1, 2, 3, 4, 5],
        "User": ["Sarah_Green", "EcoMike", "You (Admin)", "CleanLife", "SustainableSam"],
        "Level": [12, 10, st.session_state.eco_level, 4, 3],
        "Points": [6500, 5200, st.session_state.green_points, 1800, 1200]
    })
    
    # Simple formatting
    st.dataframe(
        leader_data, 
        hide_index=True, 
        use_container_width=True,
        column_config={
            "Rank": st.column_config.NumberColumn(format="🏆 %d"),
            "Points": st.column_config.ProgressColumn(
                "Green Points", format="%d", min_value=0, max_value=7000
            )
        }
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("<center style='color: #166534'>SustainStyle • Scan Good, Look Good, Do Good.</center>", unsafe_allow_html=True)
