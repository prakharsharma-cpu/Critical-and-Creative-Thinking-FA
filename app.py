import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# --- 1. CONFIGURATION & STATE MANAGEMENT ---
st.set_page_config(
    page_title="Sustainability Fashion App",
    page_icon="🌿",
    layout="centered", # Centered mimics a mobile app view
    initial_sidebar_state="collapsed"
)

# Initialize Session State for "Routing" (Navigation)
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def navigate_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- 2. CUSTOM STYLING (CSS) ---
# We inject CSS to mimic the Tailwind Design System from your HTML
st.markdown("""
    <style>
        /* Import Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;700;800&family=Noto+Sans:wght@400;500&display=swap');
        
        /* General App Styling */
        .stApp {
            background-color: #f9f9f6; /* background-light */
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: #131614;
        }
        
        /* Hide Standard Streamlit Elements for App-like feel */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Custom Colors based on your HTML */
        :root {
            --primary: #496e57;
            --secondary: #7FBABF;
            --accent: #D58C6A;
            --card-bg: #F3F5F1;
        }

        /* Card Styling */
        div[data-testid="stMetric"], div.stButton > button {
            background-color: white;
            border-radius: 1rem;
            box-shadow: 0 4px 20px -2px rgba(73, 110, 87, 0.05);
            border: 1px solid #e5e7eb;
        }

        /* Primary Button Styling */
        div.stButton > button {
            width: 100%;
            border: none;
            color: var(--primary);
            font-weight: 700;
        }
        div.stButton > button:hover {
            color: #3a5745;
            background-color: #f0fdf4;
        }

        /* Navigation Bar Styling */
        .nav-container {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: white;
            padding: 10px;
            border-top: 1px solid #ddd;
            z-index: 999;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# --- 3. HELPER COMPONENTS ---

def display_gauge(score):
    """Creates the Eco-Score gauge using Plotly"""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Eco-Score", 'font': {'size': 14, 'color': "#6a7c71"}},
        number = {'font': {'size': 50, 'color': "#131614", 'family': "Plus Jakarta Sans"}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "white"},
            'bar': {'color': "#496e57"}, # Primary Green
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#f9f9f6",
            'steps': [
                {'range': [0, 100], 'color': '#e2e8f0'}
            ],
        }
    ))
    fig.update_layout(
        paper_bgcolor = "rgba(0,0,0,0)",
        plot_bgcolor = "rgba(0,0,0,0)",
        font = {'family': "Plus Jakarta Sans"},
        margin=dict(l=20, r=20, t=30, b=20),
        height=200
    )
    return fig

# --- 4. PAGE VIEWS ---

def home_page():
    # -- Header --
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("https://ui-avatars.com/api/?name=Jessica&background=496e57&color=fff&rounded=true", width=50)
    with col2:
        st.markdown("### Good Morning, \n# **Jessica**", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # -- Search --
    st.text_input("🔍 Search brands or materials...", placeholder="Try 'Organic Cotton'...")
    
    st.write("") # Spacer

    # -- Hero Section (Scan Trigger) --
    with st.container():
        st.markdown(
            """
            <div style="background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1576995853123-5a2946b92885?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=80'); 
            background-size: cover; padding: 2rem; border-radius: 1.5rem; color: white; margin-bottom: 20px;">
                <h2>📷 Scan a tag</h2>
                <p>Instantly analyze fabric composition and eco-impact.</p>
            </div>
            """, unsafe_allow_html=True
        )
        # We use a Streamlit button to handle the click event logic
        if st.button("Scan Item Now ➔", type="primary"):
            navigate_to('score')

    st.write("") # Spacer

    # -- Carousel / Tips --
    st.subheader("Daily Green Tips")
    col_tip1, col_tip2 = st.columns(2)
    
    with col_tip1:
        st.image("https://images.unsplash.com/photo-1542272617-0858607c2242", use_container_width=True)
        st.caption("**Wash Less**\n\nAir denim out to save water.")
        

    with col_tip2:
        st.image("https://images.unsplash.com/photo-1509631179647-0177331693ae", use_container_width=True)
        st.caption("**Polyester?**\n\nTakes 200 years to decompose.")

    # -- Recent Activity --
    st.subheader("Recent Scans")
    with st.container():
        col_rec1, col_rec2 = st.columns([1, 3])
        with col_rec1:
            st.image("https://images.unsplash.com/photo-1521572163474-6864f9cf17ab", width=60)
        with col_rec2:
            st.markdown("**Organic Cotton Tee**")
            st.caption("Scanned 2 hours ago • Grade A+")

def score_page():
    # -- Top Bar --
    col_back, col_title = st.columns([1, 5])
    with col_back:
        if st.button("⬅"):
            navigate_to('home')
    with col_title:
        st.subheader("Impact Analysis")

    # -- Item Mini Card --
    with st.container():
        col_img, col_desc = st.columns([1, 3])
        with col_img:
            st.image("https://images.unsplash.com/photo-1542272454315-4c01d7abdf4a", width=60)
        with col_desc:
            st.markdown("**Levi's 501 Original Fit**")
            st.caption("Denim • 100% Cotton • ✅ Verified")

    # -- Main Score Gauge --
    st.plotly_chart(display_gauge(78), use_container_width=True)
    
    st.info("This item scores better than **82%** of similar denim products scanned this month.")
    

    # -- Grid Breakdown --
    st.markdown("### Impact Breakdown")
    
    row1_1, row1_2 = st.columns(2)
    with row1_1:
        st.metric(label="Material", value="A", delta="Low Impact")
        st.caption("Organic Cotton")
    with row1_2:
        st.metric(label="Water Usage", value="C-", delta="-High Use", delta_color="inverse")
        st.caption("Needs Improvement")
        
    row2_1, row2_2 = st.columns(2)
    with row2_1:
        st.metric(label="Labor Ethics", value="A+", delta="Certified")
        st.caption("Fair Trade")
    with row2_2:
        st.metric(label="Transport", value="B", delta="Average", delta_color="off")
        st.caption("Regional Hub")

    st.write("")
    
    # -- Trend Chart --
    st.markdown("### Brand Trend (5 Years)")
    chart_data = pd.DataFrame({
        'Year': ['2020', '2021', '2022', '2023', '2024'],
        'Score': [65, 68, 72, 75, 78]
    })
    st.line_chart(chart_data, x='Year', y='Score', color="#496e57")

# --- 5. MAIN APP LOGIC ---

if st.session_state.page == 'home':
    home_page()
elif st.session_state.page == 'score':
    score_page()
elif st.session_state.page == 'points':
    st.title("Points Page")
    st.write("Placeholder for points logic.")
    if st.button("Back Home"): navigate_to('home')
elif st.session_state.page == 'profile':
    st.title("Profile Page")
    st.write("Placeholder for profile settings.")
    if st.button("Back Home"): navigate_to('home')

# --- 6. SIMULATED BOTTOM NAVIGATION ---
# Since Streamlit doesn't support fixed bottom navbars natively, 
# we inject buttons at the bottom of the script.
st.markdown("---")
nav_cols = st.columns(4)

if nav_cols[0].button("🏠\nHome"):
    navigate_to('home')
if nav_cols[1].button("📷\nScan"):
    navigate_to('score')
if nav_cols[2].button("💎\nPoints"):
    navigate_to('points')
if nav_cols[3].button("👤\nProfile"):
    navigate_to('profile')
