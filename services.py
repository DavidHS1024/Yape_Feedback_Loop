import time
import requests
import streamlit as st
from config import FB_POST_ID, FB_PAGE_ACCESS_TOKEN

def obtener_comentarios():
    """Lectura desde el post de Facebook (Socialización)."""
    try:
        url = f"https://graph.facebook.com/v18.0/{FB_POST_ID}/comments"
        params = {
            "access_token": FB_PAGE_ACCESS_TOKEN,
            "summary": "true",
            "filter": "stream"
        }
        res = requests.get(url, params=params, timeout=10)
        res.raise_for_status()
        data = res.json()
        comentarios = [c['message'] for c in data.get('data', []) if 'message' in c]
        return comentarios
    except Exception as e:
        st.error(f"🚨 ERROR al leer comentarios: {e}")
        return []

def mock_data():
    """Datos de ejemplo cuando IA no esté disponible."""
    time.sleep(1)
    return [{
        "titulo": "Modo Offline",
        "tipo": "Demo",
        "problema": "Permitir usar la app con conectividad limitada",
        "solucion": "Ejemplo de solución...",
        "viabilidad": "N/A",
        "esfuerzo": "Bajo",
        "prioridad": "Baja"
    }]
