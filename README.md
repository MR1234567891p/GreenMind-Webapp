# 🌱 GreenMind - "Beyond Plastic. Beyond Ordinary."

**GreenMind** is a sustainability focused Streamlit web application that helps users explore eco-friendly alternatives to plastic, visualize impact metrics, and connect with sustainable vendors.

⚠️ This is a **demo version** built using mock datasets for both the alternative finder and chatbot model. The AI recommendation system is in prototype stage.

---

## 🚀 Features

- **🌱 Plastic Alternative Finder:** Search for sustainable replacements by product type.  
- **📊 Impact Dashboard:** Simulates plastic and CO₂ reduction metrics.  
- **🤖 Sustainability Chatbot:** Answers basic sustainability and product questions using demo data.  
- **🗺️ Vendor Map:** Displays local eco-friendly vendor locations.  
- **📬 Contact & About Pages:** Professional interface for outreach and brand info.

---

## 🧩 Tech Stack

- **Python 3**
- **Streamlit** for web interface  
- **Pandas** for dataset handling  
- **Folium** for interactive maps  
- **HTML** for custom styling  

---

## 📂 Datasets

- `plastic_alternative_dataset.csv` — demo dataset containing product alternatives and metadata.  
- `chatbot_data.csv` — demo question–answer dataset for sustainability chatbot.

*(All datasets are mock data created for prototype demonstration purposes only.)*

---

## 💻 Run Locally

```bash
pip install streamlit pandas folium streamlit-folium
streamlit run app.py

