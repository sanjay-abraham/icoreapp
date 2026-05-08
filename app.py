
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="iCore - ElementFlow",
    layout="wide"
)

# ---------------------------------
# DARK THEME
# ---------------------------------

dark_css = """
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #161b22;
}

.stButton>button {
    background-color: orange;
    color: black;
    border-radius: 10px;
}
</style>
"""

st.markdown(dark_css, unsafe_allow_html=True)

# ---------------------------------
# SIDEBAR
# ---------------------------------

st.sidebar.title("iCore - ElementFlow")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Login",
        "Register",
        "Submit Single Core",
        "Bulk Upload",
        "Dashboard"
    ]
)

# ---------------------------------
# LOGIN
# ---------------------------------

if menu == "Login":

    st.title("Login")

    mobile = st.text_input("Mobile Number")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        st.success("Login Successful")

# ---------------------------------
# REGISTER
# ---------------------------------

elif menu == "Register":

    st.title("Register")

    name = st.text_input("Full Name")
    mobile = st.text_input("Mobile")
    email = st.text_input("Email (Optional)")
    address = st.text_area("Address")

    latitude = st.number_input("Latitude")
    longitude = st.number_input("Longitude")

    password = st.text_input("Password", type="password")

    if st.button("Register"):
        st.success("Registration Successful")

# ---------------------------------
# SINGLE CORE SUBMISSION
# ---------------------------------

elif menu == "Submit Single Core":

    st.title("Submit Core")

    user_name = st.text_input("Your Name")

    product_name = st.text_input("Product Name")

    brand = st.selectbox(
        "Brand",
        [
            "Bosch",
            "Valeo",
            "Denso",
            "Delphi",
            "Other"
        ]
    )

    year = st.number_input(
        "Year of Manufacture",
        min_value=1980,
        max_value=2035,
        step=1
    )

    working = st.radio(
        "Working Condition",
        [
            "Working",
            "Non Working"
        ]
    )

    visible_damage = st.radio(
        "Visible Damage",
        [
            "Yes",
            "No"
        ]
    )

    damage_type = st.multiselect(
        "Type of Damage",
        [
            "Broken Housing",
            "Burnt",
            "Corrosion",
            "Leakage",
            "Cracked",
            "Rust"
        ]
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=1
    )

    latitude = st.number_input("Latitude")
    longitude = st.number_input("Longitude")

    uploaded_image = st.file_uploader(
        "Upload Image",
        type=["jpg", "png", "jpeg"]
    )

    if uploaded_image:

        os.makedirs("uploads", exist_ok=True)

        image_path = f"uploads/{uploaded_image.name}"

        with open(image_path, "wb") as f:
            f.write(uploaded_image.getbuffer())

    if st.button("Submit Core"):

        st.success("The data submitted successfully")

# ---------------------------------
# BULK UPLOAD
# ---------------------------------

elif menu == "Bulk Upload":

    st.title("Bulk Upload")

    st.download_button(
        "Download CSV Template",
        data="""product_name,brand,year,working,damage_type,quantity""",
        file_name="core_template.csv"
    )

    uploaded_csv = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if uploaded_csv:

        df = pd.read_csv(uploaded_csv)

        st.dataframe(df)

        st.success("Bulk data uploaded successfully")

# ---------------------------------
# DASHBOARD
# ---------------------------------

elif menu == "Dashboard":

    st.title("Dashboard")

    st.metric("Total Demo Submissions", "125")
    st.metric("Working Components", "74")
    st.metric("Damaged Components", "51")

    st.subheader("Brand Distribution")

    demo_data = pd.DataFrame({
        "Brand": ["Bosch", "Valeo", "Denso", "Delphi"],
        "Count": [40, 30, 35, 20]
    })

    fig, ax = plt.subplots()

    ax.pie(
        demo_data["Count"],
        labels=demo_data["Brand"],
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

    st.success("Demo dashboard loaded successfully")
