import os
import streamlit as st
import google.generativeai as genai

# ⚙️ CONFIGURACIÓN BÁSICA
# Puedes pasarlas a variables de entorno si quieres más seguridad.
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyAIzrEQaUE-00uwSceSI8EVpMKPBVVhZOQ")
FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN", "EAAWSW3IewfsBQOrFMVEXPKNLnrGq8fDXfR5y36LzR2DLZCpddWa2aV0irgTQD7zot9XCKAYmY0VoqASsagHbl4G25qxZBLBQMCapDjR7LRlpZBDhh0ty7ieNNJKoR4uZCDj7lOIK1HD1xgAKkBG6reQZAzBI9jVbhnhZAp3nxSSbvZB3nBZCpFxKd8pQkgDp2K47aZAcTB3j0Sg9KG2c8ZC0icZCpummUBPvlJZALxvtNcgx4SZCb6pg17zLb3RbMyZCAZD")
FB_POST_ID = os.getenv("FB_POST_ID", "877360362131874_122098324683140684")

# Config de página Streamlit
st.set_page_config(page_title="Yape Feedback Loop", page_icon="🟣", layout="wide")

# Config de Gemini
if GEMINI_API_KEY and len(GEMINI_API_KEY) > 10:
    genai.configure(api_key=GEMINI_API_KEY)
    IA_ACTIVA = True
else:
    st.warning("⚠️ GEMINI_API_KEY no configurada. Modo DEMO activo.")
    IA_ACTIVA = False
