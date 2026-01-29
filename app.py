import streamlit as st
import time

# --- 1. THE UX ENGINE (80% UX: Layout & Visuals) ---
st.set_page_config(page_title="SustainStyle App", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
    /* Mobile App Frame */
    .stApp {
        background: #F8FAF9;
        max-width: 400px;
        margin: 0 auto;
        border: 10px solid #222;
        border-radius: 45px;
        height: 850px;
        overflow-y: auto;
    }

    /* Floating Navigation Bar (UX Component) */
    .nav-bar {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 320px;
        background: white;
        padding: 15px;
        border-radius: 30px;
        display: flex;
        justify-content: space-around;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        z-index: 100;
    }

    /* Eco-Score Traffic Light Graphics */
    .score-badge {
        width: 90px; height: 90px;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 36px; font-weight: 900; color: white;
        margin: 0 auto;
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
    }
    .grade-a { background: linear-gradient(135deg, #2E7D32, #4CAF50); }
    
    /* Product Card Styling */
    .alt-card {
        background: white;
        padding: 15px;
        border-radius: 15px;
        border-left: 5px solid #81C784;
        margin-bottom: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BACKEND FEATURES (20% UI Logic) ---
if 'page' not in st.session_state:
    st.session_state.page = "Home"
if 'points' not in st.session_state:
    st.session_state.points = 1250

def nav_to(page_name):
    st.session_state.page = page_name

# --- 3. THE 5 SCREENS ---

# SCREEN 1: HOME & SCAN INITIATOR
if st.session_state.page == "Home":
    st.markdown("<h2 style='text-align:center;'>🌿 SustainStyle</h2>", unsafe_allow_html=True)
    st.markdown(f"""<div style='text-align:center;'><span style='background:#E8F5E9; padding:5px 15px; border-radius:20px; color:#2E7D32;'><b>{st.session_state.points} GreenPoints</b></span></div>""", unsafe_allow_html=True)
    
    st.write("")
    st.markdown("### Scan to Analyze")
    st.write("Ready to check your clothing's impact?")
    
    # Scanner UX Graphic
    st.markdown("""
        <div style='border: 3px dashed #2E7D32; border-radius:20px; padding:40px; text-align:center; background:#fff;'>
            <span style='font-size:50px;'>📷</span><br>
            <small style='color:gray;'>Point at clothing barcode</small>
        </div>
    """, unsafe_allow_html=True)
    
    cam = st.camera_input("Scanner Viewfinder", label_visibility="collapsed")
    if cam:
        with st.spinner("AI analyzing fibers..."):
            time.sleep(2)
            st.session_state.points += 50
            nav_to("Eco-Score")
            st.rerun()

# SCREEN 2: ECO-SCORE RESULT (Color Coded)
elif st.session_state.page == "Eco-Score":
    st.markdown("<h3 style='text-align:center;'>Eco-Analysis</h3>", unsafe_allow_html=True)
    st.markdown('<div class="score-badge grade-a">A</div>', unsafe_allow_html=True)
    
    
    
    st.markdown("<h2 style='text-align:center; color:#2E7D32;'>Grade A: Excellent</h2>", unsafe_allow_html=True)
    st.info("This product uses **100% Organic Hemp**. Low water usage and ethical labor verified.")
    
    if st.button("See Greener Alternatives"):
        nav_to("Alternatives")
        st.rerun()

# SCREEN 3: ALTERNATIVES RECOMMENDATION
elif st.session_state.page == "Alternatives":
    st.markdown("### Better Alternatives")
    st.write("Looking for something even greener?")
    
    st.markdown("""
        <div class='alt-card'>
            <b>Patagonia R1 Fleece</b><br>
            <small>Score: A+ (Recycled Polyester)</small>
        </div>
        <div class='alt-card'>
            <b>Allbirds Tree Runners</b><br>
            <small>Score: A (Eucalyptus Fiber)</small>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Return to Dashboard"):
        nav_to("Dashboard")
        st.rerun()

# SCREEN 4: GREENPOINTS DASHBOARD (Gamified)
elif st.session_state.page == "Dashboard":
    st.markdown("### My Green Dashboard")
    st.metric("Total GreenPoints", f"{st.session_state.points} pts", "+50 today")
    
    st.progress(0.7)
    st.caption("70% to your next reward: **$10 Eco-Voucher**")
    
    st.markdown("#### Recent Impact")
    st.success("☁️ 14kg CO2 Offset this month")
    st.success("💧 200L Water Saved")

    if st.button("View My Profile"):
        nav_to("Profile")
        st.rerun()

# SCREEN 5: USER PROFILE & STYLE-SWAP
elif st.session_state.page == "Profile":
    st.markdown("### User Profile")
    st.markdown("""
        <div style='text-align:center;'>
            <div style='width:80px; height:80px; background:#ddd; border-radius:50%; margin: 0 auto;'></div>
            <h4>Eco-Warrior Alex</h4>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 🔄 Style-Swap")
    st.write("Exchange your Grade A clothes with others to extend the lifecycle.")
    st.button("Browse Local Swaps")
    
    if st.button("Back to Home"):
        nav_to("Home")
        st.rerun()

# --- 4. PERSISTENT NAV UX ---
if st.session_state.page != "Home":
    if st.button("🏠 Home"):
        nav_to("Home")
        st.rerun()
