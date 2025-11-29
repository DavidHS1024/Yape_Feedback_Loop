import os
import streamlit as st
import google.generativeai as genai

# ⚙️ CONFIGURACIÓN BÁSICA
# Puedes pasarlas a variables de entorno si quieres más seguridad.
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyAIzrEQaUE-00uwSceSI8EVpMKPBVVhZOQ")
FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN", "EAAWSW3IewfsBQDKm5l2xCG2jchw22uOlCRR7kpL0ul3rU5sPO8cZBWJtSsZBJ0JJrEkAOVCxJaNsRrKb1z2tgZBSJKijZAngEDSzPFJGPooVmtHEA8n2vZCrEVLeS2InSUH3SZAhBFc00cZCiZC9MSZAsubcDjZAmjLZAQ73RzFurvtjog42vAKQCZASyy7Uk3RcEXa9HZBQphmRCvLV9BTLwZBV3OZBcKLAJ0veXjzZBp6f7VHqE0qgGVZAMn5NWouFFkr0ZD")
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
