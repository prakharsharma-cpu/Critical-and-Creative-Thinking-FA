import streamlit as st
import time

# --- 1. THE UX ENGINE (Modern Mobile Interface) ---
st.set_page_config(page_title="SustainStyle Pro", page_icon="🌿", layout="centered")

st.markdown("""
    <style>
    /* Mobile Shell */
    .stApp {
        background: #F4F7F5;
        max-width: 400px;
        margin: 0 auto;
        border-radius: 40px;
        border: 10px solid #222;
        height: 800px;
        overflow: hidden;
    }

    /* Scanner UI */
    .scanner-container {
        position: relative;
        width: 100%;
        height: 300px;
        background: #000;
        border-radius: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    }
    
    .barcode-target {
        width: 200px;
        height: 150px;
        border: 2px solid #00ff00;
        border-radius: 10px;
        position: relative;
        z-index: 5;
    }

    .scan-laser {
        width: 100%;
        height: 3px;
        background: #00ff00;
        position: absolute;
        box-shadow: 0 0 15px #00ff00;
        animation: laserMove 2s infinite linear;
    }

    @keyframes laserMove {
        0% { top: 0; }
        50% { top: 100%; }
        100% { top: 0; }
    }

    /* Eco-Badge */
    .eco-badge-large {
        width: 100px; height: 100px;
        background: #2E7D32;
        color: white;
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        font-size: 40px; font-weight: bold;
        margin: 0 auto 15px;
        box-shadow: 0 8px 20px rgba(46,125,50,0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE UI FEATURES (Python Logic & State) ---
if 'page' not in st.session_state:
    st.session_state.page = "onboarding"
if 'points' not in st.session_state:
    st.session_state.points = 1250

def navigate(target):
    st.session_state.page = target

# --- 3. APP SCREENS ---

# SCREEN 1: ONBOARDING
if st.session_state.page == "onboarding":
    st.markdown("<h1 style='text-align: center; color: #2E7D32;'>🌿 SustainStyle</h1>", unsafe_allow_html=True)
    st.write("Welcome to the next generation of sustainable shopping. Scan any barcode to reveal its true environmental cost.")
    
    
    
    if st.button("Start Scanning"):
        navigate("scanner")
        st.rerun()

# SCREEN 2: BARCODE SCANNER
elif st.session_state.page == "scanner":
    st.markdown("### AI Barcode Scanner")
    st.write("Align the product barcode within the green frame.")

    # Functional Scanner Logic
    # Streamlit camera_input acts as the "Live" viewfinder
    img_file = st.camera_input("Scanner Viewfinder", label_visibility="collapsed")
    
    # Custom HTML Overlay for the "Scanner UX"
    st.markdown("""
        <div class="scanner-container">
            <div class="barcode-target">
                <div class="scan-laser"></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    if img_file:
        with st.spinner("Decoding Barcode..."):
            time.sleep(1.5)
            # Simulate fetching data from a database based on the barcode
            st.session_state.points += 50 
            navigate("eco_score")
            st.rerun()
    
    if st.button("Cancel"):
        navigate("onboarding")

# SCREEN 3: ECO-SCORE RESULT
elif st.session_state.page == "eco_score":
    st.markdown("<h3 style='text-align: center;'>Analysis Complete</h3>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style="background: white; padding: 20px; border-radius: 20px; text-align: center;">
            <div class="eco-badge-large">A</div>
            <h2 style='margin:0; color: #2E7D32;'>Grade A Sustainable</h2>
            <p style='color: #666;'>100% Recycled Content</p>
        </div>
    """, unsafe_allow_html=True)

    

    st.markdown("#### Impact Breakdown")
    col1, col2 = st.columns(2)
    col1.metric("CO2 Saved", "12.4kg")
    col2.metric("Water Saved", "45L")
    
    st.success("You earned **+50 GreenPoints**!")
    
    if st.button("Go to Rewards Dashboard"):
        navigate("rewards")
        st.rerun()

# SCREEN 4: REWARDS DASHBOARD
elif st.session_state.page == "rewards":
    st.markdown(f"""
        <div style='background: #2E7D32; color: white; padding: 25px; border-radius: 25px;'>
            <p style='margin:0; opacity: 0.8;'>Total GreenPoints</p>
            <h1 style='margin:0;'>🌱 {st.session_state.points}</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.markdown("### Available Rewards")
    st.markdown("🎁 **15% Off Organic Basics** (800 pts)")
    st.markdown("🌳 **Donate 1 Tree** (500 pts)")
    
    if st.button("Scan Another Item"):
        navigate("scanner")
        st.rerun()
