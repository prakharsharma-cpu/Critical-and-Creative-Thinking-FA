import streamlit as st

# 1. SETUP & THEMING
st.set_page_config(page_title="SustainStyle", page_icon="🌿", layout="centered")

def inject_custom_css():
    st.markdown("""
        <style>
            /* Mobile-first Container */
            .main { background-color: #f9fafb; }
            
            /* Component: Card */
            .st-card {
                background: white;
                padding: 1.5rem;
                border-radius: 20px;
                border: 1px solid #f3f4f6;
                box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
                margin-bottom: 1rem;
            }
            
            /* GreenPoints Gradient */
            .points-card {
                background: linear-gradient(135deg, #064e3b 0%, #065f46 100%);
                color: white;
                border-radius: 24px;
                padding: 1.5rem;
            }

            /* Product Image */
            .prod-img {
                width: 100%;
                border-radius: 12px;
                aspect-ratio: 1/1;
                object-fit: cover;
            }
        </style>
    """, unsafe_allow_html=True)

# 2. "COMPONENTS" (Python Functions)
def render_header():
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.caption("Welcome back")
        st.subheader("SustainStyle")
    with col2:
        st.markdown("### ✨")

def render_points_summary(points=2450):
    st.markdown(f"""
        <div class="points-card">
            <small style='opacity: 0.8'>GreenPoints Balance</small>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <h2 style='color: white; margin: 0;'>{points:,}</h2>
                <span style='background: rgba(255,255,255,0.2); padding: 4px 12px; border-radius: 20px; font-size: 12px;'>Level 5</span>
            </div>
        </div>
        <br>
    """, unsafe_allow_html=True)

def render_scan_cta():
    with st.container():
        st.markdown('<div class="st-card">', unsafe_allow_html=True)
        st.markdown("#### Scan Your Clothing")
        st.write("Discover the environmental impact of your fashion.")
        if st.button("🔍 Scan Now", use_container_width=True, type="primary"):
            st.session_state.page = "scan"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

def render_recent_scans():
    st.markdown("#### Recent Scans")
    scans = [
        {"name": "Organic T-Shirt", "score": 85, "img": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=200"},
        {"name": "Recycled Denim", "score": 72, "img": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=200"}
    ]
    cols = st.columns(2)
    for i, item in enumerate(scans):
        with cols[i]:
            st.markdown(f'''
                <div class="st-card" style="padding: 10px;">
                    <img src="{item['img']}" class="prod-img">
                    <p style="margin: 8px 0 2px 0; font-weight: bold; font-size: 14px;">{item['name']}</p>
                    <span style="color: #059669; font-size: 12px; font-weight: 600;">Score: {item['score']}</span>
                </div>
            ''', unsafe_allow_html=True)
            if st.button("Details", key=f"btn_{i}", use_container_width=True):
                st.toast(f"Loading {item['name']}...")

# 3. MAIN APP LOGIC (State-based Navigation)
def main():
    inject_custom_css()
    
    # Initialize session state for navigation
    if "page" not in st.session_state:
        st.session_state.page = "home"

    # Navigation logic
    if st.session_state.page == "home":
        render_header()
        render_points_summary()
        render_scan_cta()
        
        # Quick Actions
        c1, c2 = st.columns(2)
        with c1:
            if st.button("🌿 Alternatives", use_container_width=True):
                st.info("Find eco-friendly swaps.")
        with c2:
            if st.button("📈 Progress", use_container_width=True):
                st.info("View your trends.")
        
        st.divider()
        render_recent_scans()

    elif st.session_state.page == "scan":
        if st.button("← Back"):
            st.session_state.page = "home"
            st.rerun()
        st.title("Scanner")
        st.camera_input("Capture garment label")

if __name__ == "__main__":
    main()
