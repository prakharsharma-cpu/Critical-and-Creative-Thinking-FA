import streamlit as st
import plotly.graph_objects as go
import time

# -------------------------------------------------
# CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="GreenStyle",
    page_icon="🌿",
    layout="centered"
)

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "onboarded" not in st.session_state:
    st.session_state.onboarded = False

if "eco_points" not in st.session_state:
    st.session_state.eco_points = 100

# -------------------------------------------------
# GLOBAL CSS (Figma-friendly)
# -------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.card {
    background: #F9FBF9;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0px 8px 24px rgba(0,0,0,0.05);
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# ECO GAUGE
# -------------------------------------------------
def eco_gauge(score):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Eco-Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#496e57"},
            "steps": [
                {"range": [0, 60], "color": "#fee2e2"},
                {"range": [60, 80], "color": "#fef3c7"},
                {"range": [80, 100], "color": "#dcfce7"},
            ],
        }
    ))
    fig.update_layout(height=260, margin=dict(t=40, b=20))
    return fig

# -------------------------------------------------
# SCREEN 1 — ONBOARDING
# -------------------------------------------------
if not st.session_state.onboarded:
    st.title("Welcome to GreenStyle 🌿")
    st.subheader("Scan fashion. Make sustainable choices.")

    st.markdown("""
    <div class="card">
    ✔ QR-based product identification<br>
    ✔ Instant Eco-Score & Grade<br>
    ✔ Earn rewards for sustainability
    </div>
    """, unsafe_allow_html=True)

    if st.button("Start My Journey →", use_container_width=True):
        st.session_state.onboarded = True
        st.rerun()

    st.stop()

# -------------------------------------------------
# NAVIGATION
# -------------------------------------------------
page = st.radio(
    "Navigation",
    ["🏠 Home", "📦 QR Scanner", "🌿 Eco-Score", "🎁 Rewards"],
    horizontal=True
)

# -------------------------------------------------
# HOME
# -------------------------------------------------
if page == "🏠 Home":
    st.title("Good Morning 🌱")

    c1, c2, c3 = st.columns(3)
    c1.metric("Items Scanned", "42")
    c2.metric("Water Saved", "1.2k L")
    c3.metric("Eco Points", st.session_state.eco_points)

# -------------------------------------------------
# QR SCANNER (CLOUD SAFE)
# -------------------------------------------------
elif page == "📦 QR Scanner":
    st.title("QR Product Scanner")

    st.write("Scan the QR code on the product tag and paste the code below.")

    qr_value = st.text_input(
        "Paste QR Code / Product URL / Product ID",
        placeholder="e.g. https://brand.com/product/501"
    )

    if qr_value:
        st.toast("Product Identified", icon="✅")
        time.sleep(0.5)

        st.markdown("### Levi’s 501 – Organic Cotton")

        score = 88
        st.plotly_chart(eco_gauge(score), use_container_width=True)

        st.success("🌿 Grade A Sustainable Product")
        st.session_state.eco_points += 10
        st.balloons()

# -------------------------------------------------
# ECO SCORE CARD
# -------------------------------------------------
elif page == "🌿 Eco-Score":
    st.title("Eco-Score Card")

    st.metric("Overall Grade", "A+")

    st.plotly_chart(eco_gauge(92), use_container_width=True)

    st.progress(95, text="Material Health – A+")
    st.progress(88, text="Water Usage – A")
    st.progress(90, text="Labor Ethics – A+")

# -------------------------------------------------
# REWARDS STORE
# -------------------------------------------------
elif page == "🎁 Rewards":
    st.title("Rewards Store")
    st.write(f"Eco Points: **{st.session_state.eco_points}**")

    r1, r2, r3 = st.columns(3)

    with r1:
        st.markdown("🌱 **Plant a Tree**")
        st.button("Redeem – 50 pts")

    with r2:
        st.markdown("🛍 **₹500 Eco Voucher**")
        st.button("Redeem – 100 pts")

    with r3:
        st.markdown("🏆 **Earth Guardian Badge**")
        st.button("Unlock – 150 pts")
