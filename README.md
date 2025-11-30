# 🟣 Yape Feedback Loop: SECI + GenAI

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Gemini AI](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![Meta for Developers](https://img.shields.io/badge/Meta%20Graph%20API-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://developers.facebook.com)

> **Sistema de Gestión del Conocimiento** que transforma automáticamente el feedback de usuarios en tickets técnicos y comunicación estratégica, aplicando el modelo **SECI** (Nonaka & Takeuchi).

---

## 🚀 Demo en Vivo
¡Prueba la aplicación desplegada en la nube!
### [👉 Ver Yape Feedback Loop App](https://yapefeedbackloopv2.streamlit.app)

---

## 📖 Descripción del Proyecto

Este proyecto es una implementación tecnológica del ciclo de gestión del conocimiento aplicada al contexto de **Yape** (Billetera Digital del BCP). Su objetivo es reducir la brecha entre la "Voz del Cliente" (informal/tácita) y la "Ejecución Técnica" (formal/explícita).

El sistema automatiza las 4 fases del modelo SECI utilizando **Inteligencia Artificial Generativa**:

1.  **Socialización:** Escucha activa de comentarios reales en Facebook.
2.  **Exteriorización:** La IA (Gemini) actúa como Arquitecto de Software, convirtiendo quejas en tickets técnicos (JSON).
3.  **Combinación:** Interfaz para que un experto humano valide y priorice las soluciones.
4.  **Internalización:** Generación automática de posts y arte visual para comunicar la mejora a la comunidad.

---

## 💻 Stack Tecnológico

El proyecto utiliza tecnologías modernas de IA y desarrollo web:

* **Frontend & UI:** [Streamlit](https://streamlit.io/) (Framework de Python para Data Apps).
* **Inteligencia Artificial:** [Google Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/) (Motor de razonamiento y generación).
* **Datos en Tiempo Real:** [Facebook Graph API v18.0](https://developers.facebook.com/docs/graph-api/) (Integración social).
* **Arte Generativo:** [Pollinations AI](https://pollinations.ai/) (Generación de ilustraciones vectoriales).
* **Lenguaje:** Python 3.11.

---

## ⚙️ Instalación Local

Si deseas correr este proyecto en tu máquina local:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/DavidHS1024/Yape_Feedback_Loop.git](https://github.com/DavidHS1024/Yape_Feedback_Loop.git)
    cd Yape_Feedback_Loop
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configurar Variables de Entorno:**
    Crea un archivo `.env` en la raíz del proyecto con las siguientes claves:
    ```env
    GEMINI_API_KEY="Tu_API_Key_de_Google_AI"
    FB_PAGE_ACCESS_TOKEN="Tu_Token_Larga_Duracion_Facebook"
    FB_POST_ID="ID_del_Post_a_Analizar"
    ```

4.  **Ejecutar la aplicación:**
    ```bash
    streamlit run app.py
    ```

---

## 🧠 El "Cerebro" del Sistema (`conocimiento_base.py`)

A diferencia de un chatbot genérico, este sistema inyecta un **Contexto Experto** en cada interacción con la IA. El archivo `conocimiento_base.py` contiene:
* Reglas de negocio de Yape.
* Normativa de la **SBS y BCRP** (Perú).
* Principios de **Seguridad y Privacidad** de datos.
* Restricciones de arquitectura de microservicios.

Esto asegura que las propuestas generadas sean **viables, legales y seguras**.

---

## 🔮 Roadmap y Mejoras Futuras

* [ ] **Persistencia:** Guardar tickets aprobados en una base de datos (SQLite/PostgreSQL).
* [ ] **Métricas:** Dashboard de análisis de sentimientos y frecuencia de problemas.
* [ ] **Multicanalidad:** Integrar WhatsApp y Play Store Reviews como fuentes de socialización.
* [ ] **Autenticación:** Login para distinguir roles (Usuario vs. Admin).

---

## 📄 Licencia y Descargo

Este es un proyecto **académico** desarrollado para el curso de Gestión del Conocimiento.
* **No oficial:** No tiene afiliación directa con Yape ni el BCP.
* **Propósito:** Demostración educativa de la aplicación del modelo SECI con tecnologías modernas.

---





