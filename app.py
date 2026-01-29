import streamlit as st
import time

# --- 1. THE UX ENGINE (80% UX / High-End Design) ---
st.set_page_config(page_title="SustainStyle Pro", page_icon="🌱", layout="centered")

st.markdown("""
    <style>
    /* Glassmorphism Design */
    .stApp {
        background: linear-gradient(135deg, #f5f7f6 0%, #e1e8e2 100%);
        max-width: 420px;
        margin: 0 auto;
        border-radius: 50px;
        border: 12px solid #222;
        height: 850px;
        box-shadow: 0 50px 100px rgba(0,0,0,0.3);
    }

    /* Animated Progress Bar for Points */
    .points-container {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        padding: 15px;
        border-radius: 25px;
        border: 1px solid rgba(255,255,255,0.3);
        text-align: center;
        margin-bottom: 20px;
    }

    /* Custom Green Buttons with Haptic-style Hover */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #2E7D32, #43A047);
        color: white;
        border: none;
        padding: 20px;
        border-radius: 20px;
        font-size: 18px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(46, 125, 50, 0.3);
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(46, 125, 50, 0.5);
    }

    /* Score Badge Animation */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .eco-badge {
        width: 120px; height: 120px;
        background: #2E7D32;
        color: white;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 50px; font-weight: 900;
        margin: 0 auto;
        animation: pulse 2s infinite;
        box-shadow: 0 0 20px rgba(46,125,50,0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE UI FEATURES (20% Python Logic) ---
if 'page' not in st.session_state:
    st.session_state.page = "onboarding"
if 'points' not in st.session_state:
    st.session_state.points = 1250

def nav(target):
    st.session_state.page = target

# --- 3. THE INTERACTIVE SCREENS ---

# SCREEN 1: IMMERSIVE ONBOARDING
if st.session_state.page == "onboarding":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #1B5E20;'>SustainStyle</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Scanning the future of fashion.</p>", unsafe_allow_html=True)
    
    # Hero Visual
    st.image("https://images.unsplash.com/photo-1545291730-f48a30a4c7a3?w=500", use_container_width=True)
    
    st.write("")
    if st.button("Get Started →"):
        nav("home")
        st.rerun()

# SCREEN 2: DYNAMIC HOME & REWARDS
elif st.session_state.page == "home":
    st.markdown(f"""
        <div class='points-container'>
            <small style='color: #666;'>YOUR IMPACT</small>
            <h1 style='color: #2E7D32; margin:0;'>🌱 {st.session_state.points}</h1>
            <p style='font-size: 12px; color: #888;'>Rank: <b>Eco-Expert</b></p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### Daily Mission")
    st.success("Scan a garment made of 100% Hemp for 2x points!")
    
    st.markdown("### Eco-Rewards")
    # Horizontal scroll-style cards using columns
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div style='background:white; padding:15px; border-radius:15px; border-left: 5px solid #2E7D32;'><b>Tree Plan</b><br><small>500 pts</small></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='background:white; padding:15px; border-radius:15px; border-left: 5px solid #2E7D32;'><b>Eco-Tote</b><br><small>300 pts</small></div>", unsafe_allow_html=True)

    st.write("")
    st.write("")
    if st.button("📸 OPEN SCANNER"):
        nav("scanner")
        st.rerun()

# SCREEN 3: INTERACTIVE AI SCANNER
elif st.session_state.page == "scanner":
    st.markdown("### 📷 AI Fiber Analysis")
    st.write("Processing material composition in real-time...")
    
    # Functional UI Feature: Camera
    cam_input = st.camera_input("Scan clothing tag")
    
    if cam_input:
        progress_text = "Identifying materials..."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        
        st.session_state.points += 150 # Large reward for scanning
        nav("eco_score")
        st.rerun()
    
    if st.button("Cancel"):
        nav("home")
        st.rerun()

# SCREEN 4: THE ECO-SCORE CARD (Visual Peak)
elif st.session_state.page == "eco_score":
    st.markdown("<h3 style='text-align:center;'>Eco-Analysis Result</h3>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class="eco-badge">A</div>
        <div style='text-align: center; margin-top: 20px;'>
            <h2 style='color: #2E7D32; margin-bottom:0;'>Excellent!</h2>
            <p style='color: #666;'>Recycled Cotton Blend</p>
        </div>
    """, unsafe_allow_html=True)

    

    # Impact Stats
    col1, col2, col3 = st.columns(3)
    col1.metric("CO2", "Low", "-3kg")
    col2.metric("Water", "Saved", "50L")
    col3.metric("Ethics", "Fair", "✅")

    st.write("")
    st.balloons() # UX Delight factor
    if st.button("Add to My Closet (+150 pts)"):
        nav("home")
        st.rerun()
