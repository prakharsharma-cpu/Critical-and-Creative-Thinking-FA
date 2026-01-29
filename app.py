import streamlit as st
import time

# --- 1. SETTING THE UX STAGE (80% UX Structure) ---
st.set_page_config(page_title="SustainStyle Prototype", page_icon="🌿", layout="centered")

# Custom CSS to force a mobile-app feel and professional Earth-tone branding
st.markdown("""
    <style>
    /* Main App Container */
    .stApp {
        background-color: #F8FAF8;
        max-width: 400px;
        margin: 0 auto;
        border: 8px solid #333;
        border-radius: 40px;
        height: 800px;
        overflow-y: auto;
    }
    /* Buttons UX */
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        height: 3em;
        background-color: #2E7D32 !important;
        color: white !important;
        font-weight: bold;
        border: none;
    }
    /* Eco-Score Traffic Light Card */
    .eco-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #E8F5E9;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .grade-a {
        font-size: 60px;
        font-weight: 800;
        color: #2E7D32;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. BACKEND LOGIC (20% UI Features) ---
if 'page' not in st.session_state:
    st.session_state.page = "onboarding"
if 'points' not in st.session_state:
    st.session_state.points = 1250

def change_page(page_name):
    st.session_state.page = page_name

# --- 3. SCREEN DEFINITIONS ---

# SCREEN 1: THE ONBOARDING
if st.session_state.page == "onboarding":
    st.markdown("<h1 style='text-align: center; color: #2E7D32;'>🌿 SustainStyle</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1523381210434-271e8be1f52b?w=400", use_container_width=True)
    st.markdown("<h3 style='text-align: center;'>Welcome to the Journey</h3>", unsafe_allow_html=True)
    st.write("Transform your wardrobe into a force for good. Scan tags, see the impact, and earn rewards.")
    st.button("Start Journey", on_click=change_page, args=("home",))

# SCREEN 2: REAL-TIME SCANNER (SIMULATION)
elif st.session_state.page == "scanner":
    st.markdown("### AI Powered Scanner")
    st.write("Align the clothing barcode or material tag within the frame.")
    
    # Using Streamlit's native camera input for the "Functional" aspect
    img_file = st.camera_input("Scanner Active")
    
    if img_file:
        with st.spinner("AI analyzing fiber composition..."):
            time.sleep(2) # Simulated AI latency
            st.session_state.points += 50 # Reward UI feature
            change_page("eco_score")
            st.rerun()
    
    if st.button("Cancel"):
        change_page("home")

# SCREEN 3: THE ECO-SCORE CARD
elif st.session_state.page == "eco_score":
    st.markdown("### Product Analysis")
    st.markdown("""
        <div class="eco-card">
            <div class="grade-a">A</div>
            <p style='color: #2E7D32; font-weight: bold;'>Sustainable Choice</p>
            <hr>
            <p><strong>Item:</strong> Organic Cotton Hoodie</p>
            <p><strong>Impact:</strong> 120L Water Saved</p>
            <p><strong>Reward:</strong> +50 GreenPoints</p>
        </div>
    """, unsafe_allow_html=True)
    
    

    st.write("")
    st.button("Claim Rewards & Go Home", on_click=change_page, args=("home",))

# SCREEN 4: REWARDS STORE (GAMIFICATION)
elif st.session_state.page == "home":
    st.markdown(f"""
        <div style='background: #2E7D32; color: white; padding: 20px; border-radius: 20px;'>
            <p style='margin:0;'>Total Balance</p>
            <h1 style='margin:0;'>🌱 {st.session_state.points} pts</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Rewards Store")
    col1, col2 = st.columns(2)
    with col1:
        st.info("🌳 **Plant a Tree**\n\nCost: 500 pts")
        st.button("Redeem Tree", key="b1")
    with col2:
        st.info("☕ **Bamboo Cup**\n\nCost: 300 pts")
        st.button("Redeem Cup", key="b2")

    st.write("---")
    st.button("📸 Scan New Product", on_click=change_page, args=("scanner",))
