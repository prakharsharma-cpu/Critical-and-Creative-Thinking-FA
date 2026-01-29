import streamlit as st
import cv2
import numpy as np
from PIL import Image
import time

# --- 1. SETTINGS & CUSTOM THEME ---
st.set_page_config(page_title="SustainStyle", page_icon="🌿", layout="centered")

def inject_styles():
    st.markdown("""
        <style>
            /* Main Background */
            .stApp { background-color: #F9FAFB; }
            
            /* Mobile-style Cards */
            .mobile-card {
                background: white;
                padding: 20px;
                border-radius: 24px;
                border: 1px solid #F1F5F9;
                box-shadow: 0 4px 15px rgba(0,0,0,0.04);
                margin-bottom: 20px;
            }

            /* GreenPoints Gradient Card */
            .points-gradient {
                background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
                color: white;
                padding: 24px;
                border-radius: 28px;
                margin-bottom: 20px;
            }

            /* Progress Bar Styling */
            .progress-bg {
                background: rgba(255,255,255,0.1);
                height: 8px;
                border-radius: 10px;
                margin: 15px 0;
            }
            .progress-fill {
                background: #2ECC71;
                height: 100%;
                border-radius: 10px;
                width: 75%;
            }

            /* Scan CTA Button */
            .stButton>button {
                border-radius: 16px;
                padding: 12px 24px;
                font-weight: 600;
                transition: all 0.3s;
            }

            /* Product Image Styling */
            .product-thumb {
                width: 100%;
                border-radius: 16px;
                aspect-ratio: 1/1;
                object-fit: cover;
            }
        </style>
    """, unsafe_allow_html=True)

# --- 2. BARCODE LOGIC ---
def process_barcode(image):
    """Detects and decodes barcode from image."""
    try:
        # Convert PIL to OpenCV format
        img_array = np.array(image.convert('RGB'))
        img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        
        # Initialize Detector
        detector = cv2.barcode.BarcodeDetector()
        ok, decoded_info, decoded_type, _ = detector.detectAndDecode(img_bgr)
        
        if ok and decoded_info[0]:
            return decoded_info[0], decoded_type[0]
    except Exception as e:
        st.error(f"Detection error: {e}")
    return None, None

# --- 3. PAGE COMPONENTS ---

def render_home():
    # Header
    h_col1, h_col2 = st.columns([0.8, 0.2])
    with h_col1:
        st.caption("Welcome back")
        st.title("SustainStyle")
    with h_col2:
        st.markdown("<h1 style='text-align:right;'>✨</h1>", unsafe_allow_html=True)

    # GreenPoints Card
    st.markdown(f"""
        <div class="points-gradient">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="opacity:0.8; font-size:14px;">GreenPoints Balance</span>
                <span style="background:rgba(255,255,255,0.2); padding:4px 12px; border-radius:20px; font-size:12px;">Level 5</span>
            </div>
            <h1 style="color:white; margin:10px 0;">2,450</h1>
            <div class="progress-bg"><div class="progress-fill"></div></div>
            <span style="opacity:0.7; font-size:12px;">550 points until Level 6</span>
        </div>
    """, unsafe_allow_html=True)

    # Scan CTA
    st.markdown('<div class="mobile-card">', unsafe_allow_html=True)
    st.subheader("Scan Your Clothing")
    st.write("Find the eco-impact of your fashion choices.")
    if st.button("🔍 Start Scanning", use_container_width=True, type="primary"):
        st.session_state.page = "scan"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # Recent Scans Grid
    st.subheader("Recent Scans")
    scans = [
        {"name": "Organic Cotton Tee", "score": 85, "img": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400"},
        {"name": "Recycled Denim", "score": 72, "img": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400"}
    ]
    cols = st.columns(2)
    for i, item in enumerate(scans):
        with cols[i]:
            st.markdown(f"""
                <div class="mobile-card" style="padding:10px;">
                    <img src="{item['img']}" class="product-thumb">
                    <p style="margin:8px 0 2px 0; font-weight:bold; font-size:14px;">{item['name']}</p>
                    <span style="color:#2ECC71; font-weight:600; font-size:12px;">Score: {item['score']}</span>
                </div>
            """, unsafe_allow_html=True)

def render_scan_page():
    if st.button("← Back to Home"):
        st.session_state.page = "home"
        st.rerun()

    st.title("Scanner")
    
    # Choice of Input
    mode = st.radio("Choose Scanner Source:", ["Upload Photo", "Use Camera"], horizontal=True)
    
    img_file = None
    if mode == "Upload Photo":
        img_file = st.file_uploader("Select garment tag image", type=['jpg', 'jpeg', 'png'])
    else:
        img_file = st.camera_input("Point at the barcode")

    if img_file:
        image = Image.open(img_file)
        
        with st.status("Analyzing garment barcode...", expanded=True) as status:
            time.sleep(1) # Visual polish
            barcode_val, barcode_type = process_barcode(image)
            
            if barcode_val:
                status.update(label="Scan Complete!", state="complete", expanded=False)
                st.balloons()
                
                # Success Display
                st.success(f"**Found {barcode_type}:** `{barcode_val}`")
                
                # Mock Result Card
                st.markdown(f"""
                    <div class="mobile-card" style="border-left: 5px solid #2ECC71;">
                        <h3>Eco-Analysis Result</h3>
                        <p><b>Brand:</b> SustainCo Premium</p>
                        <p><b>Material:</b> 100% Recycled Polyester</p>
                        <hr>
                        <h2 style="color:#2ECC71;">Score: 92/100</h2>
                        <p style="font-size:14px; color:#64748B;">This item saves approx. 12 liters of water compared to standard polyester.</p>
                    </div>
                """, unsafe_allow_html=True)
                
                if st.button("Claim +100 GreenPoints", use_container_width=True):
                    st.toast("Points added to your profile!")
            else:
                status.update(label="Scanning Failed", state="error")
                st.error("No clear barcode detected. Please ensure the tag is flat and well-lit.")
                st.info("💡 Tip: Try to get closer to the barcode and avoid shadows.")

# --- 4. APP CONTROLLER ---
def main():
    inject_styles()
    
    # Initialize Session State
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    # Route Rendering
    if st.session_state.page == "home":
        render_home()
    elif st.session_state.page == "scan":
        render_scan_page()

if __name__ == "__main__":
    main()
