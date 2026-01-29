import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SustainStyle",
    page_icon="🌿",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "selected_product" not in st.session_state:
    st.session_state.selected_product = None

# ---------------- DATA ----------------
recent_scans = [
    {
        "id": 1,
        "name": "Organic Cotton T-Shirt",
        "brand": "EcoWear",
        "score": 85,
    },
    {
        "id": 2,
        "name": "Recycled Denim Jacket",
        "brand": "GreenThreads",
        "score": 72,
    },
]

# ---------------- HELPERS ----------------
def score_label(score):
    if score >= 80:
        return "Good"
    elif score >= 60:
        return "Moderate"
    else:
        return "Poor"

# ================= HOME PAGE =================
if st.session_state.page == "home":

    st.title("SustainStyle 🌿")
    st.write(
        "Scan clothing items to understand their environmental impact "
        "and make more sustainable fashion choices."
    )

    st.divider()

    # PRIMARY ACTION
    if st.button("Scan Clothing Item"):
        st.session_state.page = "scan"

    st.divider()

    # GREEN POINTS (CLEAR + SIMPLE)
    st.subheader("Your GreenPoints")
    st.metric(label="Total Points", value="2,450", delta="+50 this week")
    st.progress(0.75)
    st.caption("550 points needed to reach the next level")

    st.divider()

    # RECENT SCANS
    st.subheader("Recent Scans")

    for product in recent_scans:
        with st.container(border=True):
            st.write(f"**Product:** {product['name']}")
            st.write(f"**Brand:** {product['brand']}")
            st.write(f"**Sustainability Score:** {product['score']} ({score_label(product['score'])})")

            if st.button("View Details", key=f"view_{product['id']}"):
                st.session_state.selected_product = product
                st.session_state.page = "details"

# ================= SCAN PAGE =================
elif st.session_state.page == "scan":

    st.header("Scan Result")

    score = random.randint(55, 95)

    st.subheader("Sustainability Score")
    st.metric("Score", score)
    st.progress(score / 100)

    st.divider()

    st.subheader("Impact Breakdown")
    st.write("- **Materials:** Eco-friendly")
    st.write("- **Water Usage:** Moderate")
    st.write("- **Carbon Footprint:** Low")

    st.success("You earned 50 GreenPoints")

    if st.button("Back to Home"):
        st.session_state.page = "home"

# ================= DETAILS PAGE =================
elif st.session_state.page == "details":

    product = st.session_state.selected_product

    st.header("Product Details")

    st.write(f"**Product Name:** {product['name']}")
    st.write(f"**Brand:** {product['brand']}")
    st.write(f"**Sustainability Score:** {product['score']} ({score_label(product['score'])})")

    st.divider()

    st.subheader("Assessment")
    st.write("✔ Uses sustainable materials")
    st.write("✖ Dyeing process has moderate environmental impact")

    st.divider()

    st.subheader("Better Alternatives")
    st.write("- Hemp cotton clothing")
    st.write("- Bamboo fabric apparel")

    if st.button("Back"):
        st.session_state.page = "home"
