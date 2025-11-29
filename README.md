# Yape Feedback Loop – SECI + IA

Aplicación desarrollada con **Streamlit** que implementa un ciclo de **Gestión del Conocimiento** basado en el modelo **SECI** (Socialización, Exteriorización, Combinación, Internalización) aplicado al contexto de **Yape**.  

El objetivo es transformar comentarios de usuarios (feedback informal) en **tickets técnicos de mejora**, validados y comunicados como parte de un **roadmap de producto**, usando **IA generativa (Gemini)** como apoyo.

---

## 1. Arquitectura general del proyecto

Estructura de carpetas propuesta:

```bash
SECI/
├─ app.py                # Punto de entrada Streamlit (UI principal)
├─ config.py             # Configuración global, claves y flags de IA
├─ styles.py             # Inyección de estilos CSS (UI / UX)
├─ conocimiento_base.py  # Contexto experto y reglas de negocio (CONOCIMIENTO_BASE)
├─ services.py           # Acceso a datos externos (Facebook) y mocks
├─ ai.py                 # Lógica con Gemini: exteriorización e internalización
└─ README.md             # Este documento

## 2. Descripción de cada módulo

### 2.1 `app.py` – Interfaz y flujo SECI

  Es el **entrypoint** de Streamlit:

  - Inyecta estilos llamando a `inject_styles()` desde `styles.py`.
  - Inicializa el estado de sesión (`comentarios`, `propuestas`, `ultimo_post`).
  - Organiza la UI en 4 secciones que representan las fases del modelo SECI:

    1. **Socialización 🗣️**  
      - Botón `📡 Escuchar`.  
      - Llama a `obtener_comentarios()` (en `services.py`) para traer comentarios reales de un post de Facebook.  
      - Muestra la cantidad de opiniones y un “flujo bruto” de comentarios.

    2. **Exteriorización ⚙️**  
      - Botón `⚡ Procesar Insights`.  
      - Llama a `analizar_exteriorizacion(comentarios)` (en `ai.py`) para convertir comentarios en tickets técnicos.  
      - Renderiza cada ticket en tarjetas visuales (`ticket-card`) con:
        - título, tipo, prioridad,  
        - problema detectado, solución propuesta,  
        - viabilidad, esfuerzo e ítem.

    3. **Combinación 📚**  
      - Muestra las propuestas generadas en expansores.  
      - Permite “aprobar” una propuesta y disparar la generación de un post de roadmap.  
      - Llama a `generar_interiorizacion_hibrida(ticket)` (en `ai.py`).

    4. **Internalización 📢**  
      - Muestra una tarjeta simulando un post de “Yape Oficial” (texto + imagen).  
      - Representa el retorno del conocimiento explícito al usuario y al equipo (aprendizaje organizacional).

  `app.py` no contiene reglas de negocio complejas; se limita a **coordinar** módulos.

  ---

### 2.2 `config.py` – Configuración global

  Contiene:

  - Claves y parámetros principales:
    - `GEMINI_API_KEY`
    - `FB_PAGE_ACCESS_TOKEN`
    - `FB_POST_ID`
  - Configuración de página de Streamlit (`st.set_page_config`).
  - Setup de Gemini (`genai.configure(...)`) y un flag:
    - `IA_ACTIVA`: indica si la IA está disponible o si el sistema debe operar en modo demo.

  Este módulo encapsula todo lo que es **configuración del entorno**.  
  En producción, las claves deberían venir de **variables de entorno**.

  ---

### 2.3 `styles.py` – Estilos y diseño visual

  Define la función:

  ```python
  def inject_styles():
      ...

  Que inyecta, vía st.markdown(..., unsafe_allow_html=True), un bloque CSS con:

  Estilo global de la app (.stApp, .block-container).

  Cabecera general (.app-header, .app-logo, .app-steps).

  Tarjetas de etapa (.stage-card).

  Botones con gradiente.

  Tarjetas de tickets (.ticket-card) con:

  header,

  secciones separadas (Problema detectado, Solución propuesta),

  footer con métricas.

  Tarjeta del post de internalización (.post-card, .post-header, etc.).

  Este módulo aisla el tema visual de la lógica, lo que facilita iterar el diseño sin tocar la IA ni el flujo de datos.

2.4 conocimiento_base.py – Base de conocimiento experta

  Contiene una única constante:

  CONOCIMIENTO_BASE = """
  ...
  """


  Incluye:

  Descripción funcional de Yape (pagos, QR, recargas, créditos).

  Contexto regulatorio peruano (protección de datos, SBS/BCRP, límites, PLA/FT).

  Principios de seguridad y antifraude.

  Restricciones arquitectónicas de alto nivel (microservicios, alta disponibilidad, interoperabilidad, etc.).

  Principios de diseño de soluciones (simplicidad, quick wins, inclusión, privacy/security by design).

  Criterios de viabilidad, esfuerzo y prioridad.

  Qué no se debe proponer.

  Esta base se inyecta en los prompts de IA para que las respuestas:

  estén alineadas con el negocio y la regulación,

  sean coherentes con la arquitectura y la seguridad,

  se conviertan en conocimiento explícito accionable.

2.5 services.py – Integración externa y mocks

  Define dos funciones:

  obtener_comentarios()

  Llama a la Graph API de Facebook usando FB_POST_ID y FB_PAGE_ACCESS_TOKEN.

  Devuelve una lista de strings con los mensajes de los comentarios.

  Representa la fase de Socialización: captura de conocimiento tácito proveniente de usuarios.

  mock_data()

  Devuelve una lista de tickets de ejemplo.

  Se usa cuando la IA no está disponible o para demos offline.

  Este módulo concentra la interacción con fuentes externas y permite stub/mocking sencillo.

2.6 ai.py – Lógica de IA (Gemini)

  Contiene dos funciones principales:

  analizar_exteriorizacion(comentarios)

  Implementa la fase de Exteriorización del modelo SECI:

  Toma comentarios crudos (tácito).

  Usa Gemini en modo application/json.

  Prompt rico en contexto (usa CONOCIMIENTO_BASE).

  Pide un array JSON donde cada objeto tiene:

  titulo, tipo, problema, solucion, viabilidad, esfuerzo, prioridad.

  Resultado: una lista de tickets técnicos, es decir, conocimiento explícito estructurado.

  generar_interiorizacion_hibrida(ticket)

  Implementa la parte de Internalización, combinada con comunicación:

  Recibe un ticket aprobado.

  Usa Gemini para generar:

  texto_post: post de Facebook en español, empático y sin tecnicismos.

  prompt_imagen_en: prompt en inglés para una ilustración vectorial.

  Construye una URL a Pollinations AI para generar una imagen “flat vector”.

  Devuelve un diccionario listo para mostrarse como “post de roadmap” (texto + imagen).

3. Relación con el modelo SECI

  La app implementa SECI de forma operativa:

  Socialización (tácito → tácito)

  Usuarios expresan experiencias en Facebook.

  obtener_comentarios() captura ese conocimiento tácito distribuido.

  La UI muestra los comentarios crudos para contextualizar.

  Exteriorización (tácito → explícito)

  analizar_exteriorizacion() convierte opiniones dispersas en tickets técnicos estructurados.

  Cada ticket sintetiza un problema y una solución, con viabilidad, esfuerzo y prioridad.

  Combinación (explícito → explícito)

  En app.py, la sección de Combinación permite al “experto” revisar y aprobar propuestas.

  Se combinan:

  los tickets generados (nuevo explícito),

  con conocimiento experto (CONOCIMIENTO_BASE + criterio humano),

  dando como resultado propuestas listas para roadmap.

  Internalización (explícito → tácito)

  generar_interiorizacion_hibrida() transforma un ticket en un mensaje comprensible para la comunidad.

  El post generado (texto + imagen) sirve para:

  alinear expectativas de usuarios,

  cementar aprendizaje en el equipo,

  cerrar el ciclo de feedback.

  Este ciclo puede repetirse con nuevos comentarios, creando una espiral de conocimiento alineada con el modelo SECI.

4. Requisitos e instalación
  4.1 Dependencias principales

    Python 3.9+

    Librerías:

    streamlit

    requests

    google-generativeai

    Ejemplo de instalación:

    pip install streamlit requests google-generativeai

    4.2 Variables de entorno recomendadas

    En lugar de dejar las claves hardcodeadas, configura:

    export GEMINI_API_KEY="TU_API_KEY_DE_GEMINI"
    export FB_PAGE_ACCESS_TOKEN="TU_TOKEN_FB"
    export FB_POST_ID="ID_DEL_POST_DE_FACEBOOK"

5. Ejecución

  Dentro de la carpeta del proyecto:

  streamlit run app.py

  Luego abre el enlace que muestra Streamlit (por defecto http://localhost:8501).

6. Posibles extensiones

  Persistir tickets y posts en una base de datos (por ejemplo, SQLite o Firestore).

  Añadir un módulo de métricas (número de tickets aprobados, tiempos de respuesta, etc.).

  Incorporar otros canales de socialización (WhatsApp, formularios web, correos).

  Implementar autenticación básica para distinguir roles:

  analista de conocimiento,

  product owner,

  stakeholder invitado.

7. Propósito académico

  Este proyecto está diseñado como trabajo aplicado para el curso de Gestión del Conocimiento:

  Muestra cómo un modelo teórico (SECI) se puede traducir a un flujo de software real.

  Integra fuentes externas (Facebook), IA generativa y diseño de UI/UX.

  Sirve como MVP para discutir:

  formalización del feedback de clientes,

  toma de decisiones basada en conocimiento,

  implicancias éticas y regulatorias del uso de IA y datos de usuarios.# SECI
# Yape_Feedback_Loop
