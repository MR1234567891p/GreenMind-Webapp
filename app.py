import streamlit as st
import pandas as pd
import time
import random
import folium
from streamlit_folium import st_folium

# PAGE CONFIGURATION

st.set_page_config(
    page_title="GreenMind",
    page_icon="🌱",
    layout="wide"
)

# Logo Display
def show_logo():
    try:
        st.image("logo.png", width=120)  
    except:
        st.markdown("### 🌱 GreenMind")  


# BACKGROUND AND STYLING

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e) !important;
    background-size: 400% 400%;
    animation: gradientMove 15s ease infinite;
}
@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
h1, h2, h3, h4, h5, h6, p, label, span {
    color: #e3f2fd !important;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Load Dataset

@st.cache_data
def load_data():
    return pd.read_csv("plastic_alternative_dataset.csv")

data = load_data()


# Sidebar 

st.sidebar.markdown("""
<style>
[data-testid="stSidebar"] {
    background: rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(8px);
}
</style>
""", unsafe_allow_html=True)
show_logo()
st.sidebar.markdown("## GreenMind Navigation")
page = st.sidebar.radio(
    "Choose Page",
    ["Home", "Find Alternatives", "Dashboard", "Chatbot", "Vendor Map", "About" , "Contact"]
)

st.sidebar.markdown("---")
st.sidebar.write("### Special Filters")
filter_price = st.sidebar.checkbox("Show Cheapest Only")
filter_bio = st.sidebar.checkbox("Biodegradable Only")
filter_material = st.sidebar.selectbox(
    "Filter by Material Type",
    ["All"] + list(data["Material Type"].unique())
)

st.sidebar.markdown("---")
st.sidebar.caption("🌱 GreenMind © 2025")


#  HOME PAGE -----------------------------------------------------------------

if page == "Home":
    
    st.markdown("""
    <style>
    .hero-title {
        font-size: 70px;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #00FF99, #00BFFF, #A5FFD6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientMove 6s ease-in-out infinite;
        letter-spacing: 2px;
    }
    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>

    <div style="text-align:center; padding: 40px 0;">
        <h1 class="hero-title">🌱 GreenMind </h1>
        <h3 style='color:#00FF99; font-weight:400;'>
            <b>Beyond Plastic. Beyond Ordinary</b>.
        </h3>
        <p style='max-width:800px; margin:auto; color:#C8E6F9; font-size:19px;'>
            Every day, over <b>1,700 tonnes</b> of plastic waste are generated in Bangladesh - 
            with less than 40% recycled. GreenMind helps brands turn this challenge into a 
            business advantage by identifying affordable, credible, and high-impact 
            alternatives to plastic.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 💡 What We Do
        We empower companies to:
        - Audit and reduce their plastic use  
        - Replace harmful packaging with sustainable materials  
        - Align operations with **EPR** and **ESG** requirements  
        - Build stronger, eco-conscious brands that customers trust  
        """)

    with col2:
        st.markdown("""
        ### 🌍 Why It Matters
        Sustainability isn’t a luxury - it’s a competitive edge.  
        Smarter plastic use saves money, cuts emissions, and enhances reputation.  
        GreenMind AI makes this transition measurable, achievable, and profitable.
        """)

    st.markdown("---")

    st.markdown("""
    <div style="text-align:center; padding: 20px;">
        <h3>🚀 Ready to Go Plastic-Smart?</h3>
        <p>Discover eco-friendly material alternatives tailored to your products.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        "<div style='text-align:center;'>"
        "<a href='#' style='background:#00FF99; color:#000; padding:12px 24px; border-radius:8px; text-decoration:none; font-weight:bold;'>Find Alternatives</a>"
        "</div>",
        unsafe_allow_html=True
    )


# FIND ALTERNATIVES ---------------------------------------------------------------

elif page == "Find Alternatives":

    st.title("🔎 AI Sustainable Alternative Finder")

    user_input = st.text_input("Enter a plastic product:")

    if st.button("Search"):
        results = data.copy()

        results = results[results["Product Name"].str.contains(user_input, case=False, na=False)]

        if filter_price:
            results = results[results["Price Range"].str.contains("cheap", case=False)]

        if filter_bio:
            bio_keywords = ["bio", "compost", "plant", "natural"]
            results = results[results["Benefit"].str.contains("|".join(bio_keywords), case=False)]

        if filter_material != "All":
            results = results[results["Material Type"] == filter_material]

        if len(results) > 0:
                row = results.iloc[0]

                st.success("✅ Sustainable Alternative Found")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown(f"### 🌿 Alternative Material")
                    st.markdown(f"**{row['Sustainable Alternative']}**")

                    st.markdown(f"### 🧪 Material Type")
                    st.markdown(f"{row['Material Type']}")

                    st.markdown(f"### 💰 Price Range")
                    st.markdown(f"{row['Price Range']}")

                with col2:
                    st.markdown(f"### 🏭 Vendor Suggestion")
                    st.markdown(f"{row['Vendor']}")

                    st.markdown(f"### 🌎 Environmental Benefit")
                    st.markdown(f"{row['Benefit']}")

                    st.markdown(f"### 🎯 SDG Alignment")
                    if row['SDG Alignment']:
                        st.markdown(f"{row['SDG Alignment']}")
                    else:
                        st.markdown("N/A")

        else:
                st.error("No matching alternative found in database.")
                st.info("Try terms like: bottle, straw, bag, film, cutlery, toothbrush, etc.")


# DASHBOARD ---------------------------------------------------------------

elif page == "Dashboard":

    st.title("📊 GreenMind Impact Dashboard")

    companies = random.randint(20, 50)
    plastic_saved = random.randint(1000, 3000)
    co2_reduced = plastic_saved * 0.04

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🏢 Companies Joined", companies)

    with col2:
        st.metric("🌱 Plastic Reduced (kg)", plastic_saved)

    with col3:
        st.metric("☁️ CO₂ Saved (tons)", round(co2_reduced, 2))

    st.markdown("---")
    st.write("This dashboard simulates real-time impact of using GreenMind.")

# CHATBOT --------------------------------------------------------------- 


elif page == "Chatbot":

    st.title("🤖 GreenMind AI Chatbot")

    @st.cache_data
    def load_chatbot_data():
        return pd.read_csv("chatbot_data.csv")

    chatbot_data = load_chatbot_data()

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Ask me about sustainability or alternatives:")

    if st.button("Ask AI"):
        if user_input.strip() == "":
            st.warning("Please type your question!")
        else:
            answer_found = False
            for idx, row in chatbot_data.iterrows():
                if any(keyword.lower() in user_input.lower() for keyword in row["Question Keywords"].split(",")):
                    answer = row["Answer"]
                    answer_found = True
                    break
            if not answer_found:
                answer = "Sorry, I don't have an answer yet. Try asking about bottles, straws, packaging, bags, or cutlery."

            st.session_state.chat_history.append({"user": user_input, "bot": answer})

    for chat in st.session_state.chat_history:
        st.markdown(f"<div style='background:#0d1117; color:#00ff99; padding:10px; border-radius:8px; margin-bottom:5px;'>🤖 {chat['bot']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='background:#1b1b1b; color:#ffffff; padding:10px; border-radius:8px; margin-bottom:5px;'>👤 {chat['user']}</div>", unsafe_allow_html=True)

#  VENDOR MAP ---------------------------------------------------------------

elif page == "Vendor Map":

    st.title("🗺️ Sustainable Vendor Map")

    m = folium.Map(location=[23.8103, 90.4125], zoom_start=10)

    folium.Marker([23.8103, 90.4125], popup="GreenEarth Ltd").add_to(m)
    folium.Marker([23.7806, 90.4070], popup="EcoCraft").add_to(m)
    folium.Marker([23.7300, 90.4200], popup="BD JuteWorks").add_to(m)

    st_folium(m, width=700, height=450)


#  ABOUT PAGE ---------------------------------------------------------------

elif page == "About":
    st.title("🌿 About GreenMind")

    st.markdown("""
    <div style="text-align:center; padding: 40px 0;">
        <p style='max-width:800px; margin:auto; color:#C8E6F9; font-size:18px;'>
            GreenMind is a sustainability transformation agency that helps brands rethink every touchpoint of their identity - from packaging and product design to in-office materials and customer experiences, without compromising profits.<br>
            <b>We go beyond audits and compliance - guiding brands to design out waste, embed sustainability in their DNA, and build meaningful, future-ready experiences.</b>
        </p>    
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 🎯 Our Mission
        To empower Bangladeshi companies to reduce plastic waste
        without reducing profitability.
        
        Every product, every package, every brand transformation
        brings us closer to a cleaner, smarter future.
        """)

        st.markdown("""
        ### 🧭 Our Approach
        We act as the bridge between intention and action in sustainability:
        - **Audit & Analyze:** Identify plastic footprints across SKUs  
        - **Optimize & Replace:** Recommend cost-effective local materials  
        - **Certify & Report:** Provide verified ESG & EPR compliance reports  
        - **Empower & Inspire:** Train teams to adopt sustainable design thinking  
        """)

    with col2:
        st.markdown("""
        ### 🌍 Why It Matters
        The sustainability shift is no longer optional.
        - New **EPR laws** are reshaping supply chains  
        - Global buyers demand cleaner, compliant packaging  
        - Consumers are rewarding transparent, eco-smart brands  

        GreenMind AI helps companies stay ahead - turning sustainability into a competitive advantage.
        """)

        st.markdown("""
        ### 💚 Our Impact Vision
        - Reduce plastic dependency across industries  
        - Support circular material innovation in South Asia  
        - Build data-backed, scalable sustainability roadmaps for every brand  
        """)

    st.markdown("---")

    st.markdown("""
    <div style="text-align:center; padding: 30px;">
        <h3 style='color:#A5FFD6;'>Together, We Can Rethink Waste.</h3>
        <p style='color:#C8E6F9;'>Join us in transforming the way Bangladesh designs, packages, and consumes.</p>
    </div>
    """, unsafe_allow_html=True)


#  CONTACT PAGE ---------------------------------------------------------------

elif page == "Contact":
    st.title("📩 Contact GreenMind Team")

    st.write("For collaborations, mentorship, or partnerships:")

    st.markdown("""
    **📧 Email:** greenmind.team@gmail.com <br>
    **📞 Mobile:** 01234673983 <br>
    **📍 Location:** Dhaka, Bangladesh
    """, unsafe_allow_html=True)
 

    st.success("We reply within 24 hours 💚")



#  FOOTER 

st.markdown("<br><hr><center>Made with 💚 by GreenMind Team — 2025</center>", unsafe_allow_html=True)
