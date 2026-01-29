import streamlit as st
import time

# --- 1. THE UX ENGINE (80% UX: Professional Mobile Aesthetic) ---
st.set_page_config(page_title="SustainStyle Pro", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
    /* Mobile App Shell with Smooth Shadow */
    .stApp {
        background: #F0F4F2;
        max-width: 420px;
        margin: 0 auto;
        border: 12px solid #1a1a1a;
        border-radius: 50px;
        height: 850px;
        overflow-y: auto;
        box-shadow: 0 50px 100px rgba(0,0,0,0.3);
    }

    /* Glassmorphism Point Header */
    .header-box {
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(10px);
        padding: 15px;
        border-radius: 25px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.3);
        margin-bottom: 20px;
    }

    /* Eco-Score Circle (Traffic Light System) */
    .score-circle {
        width: 110px; height: 110px;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 45px; font-weight: 900; color: white;
        margin: 0 auto;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        background: linear-gradient(135deg, #2E7D32, #4CAF50); /* Default Green */
    }

    /* Recommendation Cards */
    .rec-card {
        background: white;
        padding: 15px;
        border-radius: 20px;
        border-left: 6px solid #4CAF50;
        margin-bottom: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }

    /* Custom Streamlit Button Styling */
    div.stButton > button {
        border-radius: 20px !important;
        height: 3.5em !important;
        background-color: #2E7D32 !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        transition: 0.3s ease !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(46, 125, 50, 0.4) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BACKEND FEATURES (20% UI Logic) ---
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'points' not in st.session_state:
    st.session_state.points = 1250
if 'recent_scan' not in st.session_state:
    st.session_state.recent_scan = None

def nav(target):
    st.session_state.page = target

# --- 3. THE 5-PAGE INTERACTIVE JOURNEY ---

# --- PERSISTENT HEADER ---
if st.session_state.page != "Scanner":
    st.markdown(f"""<div class='header-box'>
        <small style='color:#666;'>GREENPOINTS BALANCE</small><br>
        <span style='font-size:24px; color:#2E7D32;'>🌿 <b>{st.session_state.points}</b></span>
    </div>""", unsafe_allow_html=True)

# PAGE 1: HOME & SCAN START
if st.session_state.page == "Home":
    st.markdown("## Hello, Eco-Warrior!")
    st.markdown("### Weekly Impact")
    st.info("☁️ You saved **12.4kg of CO2** this week. You are in the top 10% of users!")
    
    st.markdown("---")
    st.write("Ready to check a new item?")
    if st.button("📸 START AI SCAN"):
        nav("Scanner")
        st.rerun()

# PAGE 2: FUNCTIONAL SCANNER (With UX Graphic)
elif st.session_state.page == "Scanner":
    st.markdown("### AI Barcode Scanner")
    st.write("Align barcode within the frame below.")
    
    # Graphic Overlay Simulation
    st.markdown("""
        <div style='border: 4px solid #4CAF50; border-radius: 30px; padding: 20px; background: #000; text-align: center;'>
            <div style='width: 100%; height: 2px; background: #0f0; box-shadow: 0 0 10px #0f0;'></div>
            <p style='color: white; margin-top: 100px;'>Viewfinder Active</p>
        </div>
    """, unsafe_allow_html=True)
    
    cam_photo = st.camera_input("Scanner", label_visibility="collapsed")
    
    if cam_photo:
        with st.status("AI is processing barcode...", expanded=True) as status:
            time.sleep(1)
            st.write("Identifying material composition...")
            time.sleep(1)
            status.update(label="Analysis Complete!", state="complete", expanded=False)
        
        st.session_state.points += 50
        nav("Eco-Score")
        st.rerun()
    
    if st.button("← Back to Dashboard"):
        nav("Home")
        st.rerun()

# PAGE 3: ECO-SCORE RESULT (Traffic Light)
elif st.session_state.page == "Eco-Score":
    st.markdown("<h3 style='text-align:center;'>Product Analysis</h3>", unsafe_allow_html=True)
    
    # Traffic Light Color Logic
    st.markdown('<div class="score-circle">A</div>', unsafe_allow_html=True)
    
    
    
    st.markdown("<h2 style='text-align:center; color:#2E7D32;'>Eco-Grade: Excellent</h2>", unsafe_allow_html=True)
    
    with st.expander("Why this score?", expanded=True):
        st.write("✅ **100% Recycled Cotton**")
        st.write("✅ **Water-based non-toxic dyes**")
        st.write("✅ **Fair Trade Certified Factory**")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("See Alternatives"): nav("Alternatives"); st.rerun()
    with col2:
        if st.button("Claim +50 Pts"): nav("Dashboard"); st.rerun()

# PAGE 4: ALTERNATIVES RECOMMENDATIONS
elif st.session_state.page == "Alternatives":
    st.markdown("### Greener Picks for You")
    st.write("Based on your scan, here are even better choices:")
    
    st.markdown("""
        <div class='rec-card'>
            <b>Patagonia Better Sweater</b><br>
            <span style='color:green;'>Grade: A+</span> | Recycled Polyester
        </div>
        <div class='rec-card'>
            <b>Tentree Hemp Hoodie</b><br>
            <span style='color:green;'>Grade: A</span> | CO2 Neutral
        </div>
    """, unsafe_allow_html=True)
    
    

    if st.button("Go to Rewards"):
        nav("Dashboard")
        st.rerun()

# PAGE 5: GREENPOINTS DASHBOARD & SWAP
elif st.session_state.page == "Dashboard":
    st.markdown("### GreenPoints Dashboard")
    st.success("🎉 You just earned 50 points for your last scan!")
    
    st.metric("Total Balance", f"{st.session_state.points} Pts", delta="50 Today")
    
    st.markdown("#### Redeem Rewards")
    st.progress(0.85)
    st.caption("85% to your next reward: **Plant-a-Tree Donation**")
    
    st.markdown("---")
    st.markdown("#### 🔄 Style-Swap Community")
    st.write("Trade your Grade-A items with others.")
    if st.button("Open Swap Map"):
        st.toast("Feature coming soon: Style-Swap Beta")
    
    if st.button("Scan Another Item"):
        nav("Scanner")
        st.rerun()
