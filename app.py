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
    st.session_state.eco_points = 120

if "last_scan" not in st.session_state:
    st.session_state.last_scan = False

# -------------------------------------------------
# GLOBAL CSS (APP-LIKE UI)
# -------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.card {
    background: #F9FBF9;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.06);
    margin-bottom: 18px;
}

.scan-box {
    border: 2px dashed #496e57;
    border-radius: 18px;
    padding: 26px;
    text-align: center;
    background: #ffffff;
}

.grade-a {
    background: #dcfce7;
    color: #166534;
    padding: 10px 14px;
    border-radius: 999px;
    font-weight: 700;
    display: inline-block;
}

.muted {
    color: #6b7280;
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
# SCREEN 1 — ONBOARDING (STRONG FIRST IMPRESSION)
# -------------------------------------------------
if not st.session_state.onboarded:
    st.title("GreenStyle 🌿")
    st.subheader("Make fashion choices that matter")

    st.markdown("""
    <div class="card">
    <b>How it works</b><br><br>
    ① Scan product QR<br>
    ② Get Eco-Score instantly<br>
    ③ Earn rewards for sustainable choices
    </div>
    """, unsafe_allow_html=True)

    if st.button("Start Scanning →", use_container_width=True):
        st.session_state.onboarded = True
        st.rerun()

    st.stop()

# -------------------------------------------------
# NAVIGATION (SIMPLE & CLEAR)
# -------------------------------------------------
page = st.radio(
    "",
    ["🏠 Home", "📦 Scan", "🌿 Impact", "🎁 Rewards"],
    horizontal=True
)

# -------------------------------------------------
# HOME — GUIDED DASHBOARD
# -------------------------------------------------
if page == "🏠 Home":
    st.title("Your Sustainability Dashboard")

    c1, c2, c3 = st.columns(3)
    c1.metric("Items Scanned", "42")
    c2.metric("Water Saved", "1.2k L")
    c3.metric("Eco Points", st.session_state.eco_points)

    st.markdown("""
    <div class="card">
    💡 <b>Next best action:</b><br>
    Scan your next clothing item to earn more Eco Points.
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# SCAN — INTUITIVE QR EXPERIENCE
# -------------------------------------------------
elif page == "📦 Scan":
    st.title("Scan Product QR")

    st.markdown("""
    <div class="scan-box">
    📷 Scan the QR code on the clothing tag<br>
    <span class="muted">Paste the product link or ID below</span>
    </div>
    """, unsafe_allow_html=True)

    qr_value = st.text_input(
        "",
        placeholder="e.g. https://brand.com/product/501"
    )

    if qr_value:
        st.toast("Scanning product…", icon="🔍")
        time.sleep(1)

        st.session_state.last_scan = True
        st.session_state.eco_points += 10

        st.markdown("### Levi’s 501 – Organic Cotton")
        st.markdown("<span class='grade-a'>Grade A · Sustainable</span>", unsafe_allow_html=True)

        st.plotly_chart(eco_gauge(88), use_container_width=True)

        st.success("You earned +10 Eco Points 🌱")
        st.balloons()

# -------------------------------------------------
# IMPACT — FEELS MEANINGFUL
# -------------------------------------------------
elif page == "🌿 Impact":
    st.title("Your Environmental Impact")

    st.plotly_chart(eco_gauge(92), use_container_width=True)

    st.progress(95, text="Material Health – A+")
    st.progress(88, text="Water Efficiency – A")
    st.progress(90, text="Ethical Labour – A+")

    st.info("Certified by global sustainability standards")

# -------------------------------------------------
# REWARDS — MOTIVATING, NOT BORING
# -------------------------------------------------
elif page == "🎁 Rewards":
    st.title("Rewards Store")
    st.write(f"🌱 Eco Points: **{st.session_state.eco_points}**")

    st.markdown("""
    <div class="card">
    🎯 <b>Next reward at 150 points</b><br>
    Keep scanning sustainable products to unlock it.
    </div>
    """, unsafe_allow_html=True)

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
