import streamlit as st
import time

# --- 1. THE GRAPHICS ENGINE (80% UX) ---
st.set_page_config(page_title="SustainStyle Pro", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
    /* Mobile App Frame */
    .stApp {
        background: linear-gradient(180deg, #FFFFFF 0%, #F1F8F1 100%);
        max-width: 410px;
        margin: 0 auto;
        border: 10px solid #222;
        border-radius: 45px;
        height: 820px;
        box-shadow: 0 40px 100px rgba(0,0,0,0.2);
    }

    /* Intuitive Scan Graphic */
    .barcode-scanner-ui {
        width: 240px;
        height: 240px;
        border: 4px solid #2E7D32;
        border-radius: 30px;
        position: relative;
        margin: 20px auto;
        display: flex;
        justify-content: center;
        align-items: center;
        background: rgba(0,0,0,0.05);
    }
    
    .scan-line {
        width: 100%;
        height: 4px;
        background: #4CAF50;
        position: absolute;
        box-shadow: 0 0 20px #4CAF50;
        animation: scanAnim 2s infinite ease-in-out;
    }
    
    @keyframes scanAnim {
        0% { top: 0%; }
        50% { top: 100%; }
        100% { top: 0%; }
    }

    /* Grade Badge Graphic */
    .eco-grade-badge {
        background: linear-gradient(135deg, #2E7D32, #4CAF50);
        color: white;
        width: 100px;
        height: 100px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 48px;
        font-weight: 900;
        margin: 0 auto;
        box-shadow: 0 10px 20px rgba(46, 125, 50, 0.3);
    }

    /* Point Pill Graphic */
    .points-pill {
        background: #E8F5E9;
        color: #2E7D32;
        padding: 8px 20px;
        border-radius: 30px;
        font-weight: bold;
        display: inline-block;
        border: 1px solid #C8E6C9;
    }

    /* Buttons UX */
    .stButton>button {
        border-radius: 20px;
        height: 55px;
        background: #2E7D32 !important;
        color: white !important;
        border: none;
        transition: 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. APP LOGIC (20% UI Features) ---
if 'page' not in st.session_state:
    st.session_state.page = "welcome"
if 'points' not in st.session_state:
    st.session_state.points = 1250

def go_to(page):
    st.session_state.page = page

# --- 3. SCREENS ---

# SCREEN 1: WELCOME
if st.session_state.page == "welcome":
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center; color:#2E7D32;'>🌿 SustainStyle</h1>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3063/3063822.png", width=150) # Graphics for branding
    st.markdown("<p style='text-align:center;'>Scan clothes. Save the Earth.<br>Earn rewards.</p>", unsafe_allow_html=True)
    st.button("Begin Journey", on_click=go_to, args=("home",))

# SCREEN 2: HOME DASHBOARD
elif st.session_state.page == "home":
    st.markdown("<div style='text-align:right;'><div class='points-pill'>🌱 " + str(st.session_state.points) + " pts</div></div>", unsafe_allow_html=True)
    st.markdown("## My Closet")
    
    # Visual Progress Card
    st.markdown("""
        <div style='background:white; padding:20px; border-radius:25px; border-left:8px solid #2E7D32; box-shadow:0 4px 10px rgba(0,0,0,0.05);'>
            <small>WEEKLY IMPACT</small>
            <h3 style='margin:0;'>12kg CO2 Saved</h3>
            <p style='font-size:12px; color:gray;'>You're in the top 5% of your city!</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.button("📸 SCAN BARCODE", on_click=go_to, args=("scanner",))

# SCREEN 3: SCANNER (WITH GRAPHICS)
elif st.session_state.page == "scanner":
    st.markdown("### Point at Barcode")
    
    # This creates the "Intuitive" scanning UI
    st.markdown("""
        <div class="barcode-scanner-ui">
            <div class="scan-line"></div>
            <img src="https://cdn-icons-png.flaticon.com/512/241/241503.png" width="80" style="opacity:0.3;">
        </div>
    """, unsafe_allow_html=True)
    
    # The actual functional camera
    photo = st.camera_input("Scanner Viewfinder", label_visibility="collapsed")
    
    if photo:
        with st.spinner("AI Analysis..."):
            time.sleep(1.5)
            st.session_state.points += 100
            go_to("result")
            st.rerun()
    
    st.button("Back", on_click=go_to, args=("home",))

# SCREEN 4: ECO-SCORE RESULT
elif st.session_state.page == "result":
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='eco-grade-badge'>A</div>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#2E7D32;'>Great Choice!</h2>", unsafe_allow_html=True)
    
    

    st.markdown("""
        <div style='background:#E8F5E9; padding:15px; border-radius:15px; text-align:center;'>
            <b>Organic Hemp Jacket</b><br>
            <span style='color:green;'>Low Carbon Footprint • Fair Trade</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.balloons()
    st.button("Claim +100 Points", on_click=go_to, args=("home",))
