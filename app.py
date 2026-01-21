import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import time

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Sustainability Fashion App",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- 2. CSS STYLING (Tweaked for Streamlit Native Feel) ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;700;800&display=swap');
        
        /* Apply font globally */
        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        
        /* Custom Primary Color Highlight */
        .stMetricValue {
            color: #496e57 !important;
        }
        
        /* Clean up the camera input look */
        div[data-testid="stCameraInput"] {
            border-radius: 1rem;
            overflow: hidden;
            border: 2px solid #496e57;
        }
    </style>
""", unsafe_allow_html=True)

# --- 3. HELPER FUNCTIONS ---

def display_gauge(score):
    """Interactive Plotly Gauge"""
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Eco-Score", 'font': {'size': 20, 'color': "#496e57"}},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "#496e57"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#f9f9f6",
            'steps': [
                {'range': [0, 50], 'color': '#fee2e2'}, # Red tint
                {'range': [50, 80], 'color': '#fef3c7'}, # Yellow tint
                {'range': [80, 100], 'color': '#dcfce7'} # Green tint
            ],
        }
    ))
    fig.update_layout(height=250, margin=dict(l=20, r=20, t=50, b=20))
    return fig

# --- 4. NAVIGATION (SIDEBAR) ---
# Streamlit works best when navigation is in the sidebar
with st.sidebar:
    st.image("https://ui-avatars.com/api/?name=Jessica&background=496e57&color=fff&rounded=true", width=80)
    st.title("GreenStyle")
    
    # Navigation Logic
    selected_page = st.radio(
        "Navigate", 
        ["Home", "Scan Item", "My Profile"], 
        index=0 if 'page' not in st.session_state else ["Home", "Scan Item", "My Profile"].index(st.session_state.get('last_page', 'Home'))
    )

# --- 5. PAGE LOGIC ---

if selected_page == "Home":
    st.session_state.last_page = "Home"
    
    # Hero Section
    st.title("Good Morning, Jessica 🌿")
    st.markdown("Your sustainability score is **Top 10%** this week!")
    
    # Search with visual feedback
    search_query = st.text_input("🔍 Find brands...", placeholder="Type 'Patagonia' or 'Denim'...")
    if search_query:
        st.success(f"Searching database for '{search_query}'...")

    st.divider()

    # Call to Action (The "Awesome" Transition)
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### Ready to check a new item?")
        st.write("Scan tags to instantly see water usage, carbon footprint, and labor ethics.")
    with col2:
        # A large primary button that directs users to the Scan page
        # Note: In Streamlit, buttons can't directly change the radio selection easily without rerun hacks,
        # so we rely on the Sidebar for main nav, but this button adds visual CTA.
        st.info("👈 Use the Sidebar to Scan!")

    # Native Streamlit 'Metric' Cards
    st.subheader("Your Impact Stats")
    m1, m2, m3 = st.columns(3)
    m1.metric("Items Scanned", "42", "+3")
    m2.metric("Water Saved", "1.2k L", "+150L")
    m3.metric("Trees Planted", "5", "Goal: 10")

    # Expandable Tips (Cleaner UI)
    with st.expander("💡 Daily Green Tip: Denim Care"):
        st.image("https://images.unsplash.com/photo-1542272617-0858607c2242", use_container_width=True)
        st.write("""
        **Wash Less, Air More.**
        Washing denim too frequently breaks down fibers and wastes water. 
        Try hanging them in a breezy spot or freezing them to kill bacteria!
        """)
        

elif selected_page == "Scan Item":
    st.session_state.last_page = "Scan Item"
    st.title("Scan Tag 📷")
    st.write("Align the clothing label within the frame below.")

    # AWESOME FEATURE 1: Real Camera Input
    img_file_buffer = st.camera_input("Take a picture")

    if img_file_buffer is not None:
        # AWESOME FEATURE 2: Toast Notification
        st.toast("Processing Image...", icon="🔄")
        time.sleep(1.5) # Simulate processing
        st.toast("Scan Complete!", icon="✅")
        
        st.divider()
        
        # Results Section
        st.subheader("Analysis Results")
        
        col_res1, col_res2 = st.columns([1, 1])
        
        with col_res1:
            st.image(img_file_buffer, caption="Captured Image", width=200)
            
        with col_res2:
            st.markdown("### Levi's 501 Original")
            st.caption("100% Organic Cotton")
            
            # AWESOME FEATURE 3: Balloons on high score
            score = 78
            st.plotly_chart(display_gauge(score), use_container_width=True)
            if score > 75:
                st.balloons()
                st.success("Excellent Choice! This item is eco-friendly.")

        # AWESOME FEATURE 4: Native Progress Bars for breakdown
        st.subheader("Detailed Breakdown")
        
        st.write("**Material Health** (A)")
        st.progress(90)
        
        st.write("**Water Usage** (C-)")
        st.progress(40)
        
        st.write("**Labor Standards** (A+)")
        st.progress(95)
        
        st.info("This brand is a member of the **Better Cotton Initiative**.")
        

elif selected_page == "My Profile":
    st.session_state.last_page = "My Profile"
    st.title("Jessica's Profile")
    
    # Interactive Tab Interface
    tab1, tab2, tab3 = st.tabs(["History", "Settings", "Badges"])
    
    with tab1:
        st.dataframe(pd.DataFrame({
            "Item": ["Denim Jacket", "Cotton Tee", "Sneakers"],
            "Date": ["2023-10-01", "2023-10-05", "2023-10-12"],
            "Score": [85, 92, 65]
        }), use_container_width=True)
        
    with tab2:
        st.toggle("Dark Mode Support", value=True)
        st.toggle("Notifications", value=False)
        st.slider("Daily Goal (Scans)", 1, 10, 3)

    with tab3:
        col_b1, col_b2, col_b3 = st.columns(3)
        col_b1.image("https://cdn-icons-png.flaticon.com/512/3209/3209265.png", width=80, caption="Earth Guardian")
        col_b2.image("https://cdn-icons-png.flaticon.com/512/3209/3209238.png", width=80, caption="Water Saver")
