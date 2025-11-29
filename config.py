import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env (si existe localmente)
load_dotenv()

# ⚙️ CONFIGURACIÓN BÁSICA
# Leemos la KEY exclusivamente de las variables de entorno.
# NUNCA escribas la clave real como segundo parámetro (valor por defecto).
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN", "EAAWSW3IewfsBQDKm5l2xCG2jchw22uOlCRR7kpL0ul3rU5sPO8cZBWJtSsZBJ0JJrEkAOVCxJaNsRrKb1z2tgZBSJKijZAngEDSzPFJGPooVmtHEA8n2vZCrEVLeS2InSUH3SZAhBFc00cZCiZC9MSZAsubcDjZAmjLZAQ73RzFurvtjog42vAKQCZASyy7Uk3RcEXa9HZBQphmRCvLV9BTLwZBV3OZBcKLAJ0veXjzZBp6f7VHqE0qgGVZAMn5NWouFFkr0ZD")
FB_POST_ID = os.getenv("FB_POST_ID", "877360362131874_122098324683140684")

# Config de página Streamlit
st.set_page_config(page_title="Yape Feedback Loop", page_icon="🟣", layout="wide")

# Config de Gemini
# Verificamos que la clave exista y no sea None
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    IA_ACTIVA = True
else:
    # Si no hay clave, mostramos advertencia pero no rompemos la app
    IA_ACTIVA = False
    # Opcional: Mostrar advertencia solo en desarrollo
    # st.warning("⚠️ GEMINI_API_KEY no configurada. Revisa tu archivo .env")