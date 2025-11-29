import streamlit as st

from config import IA_ACTIVA
from styles import inject_styles
from services import obtener_comentarios
from ai import analizar_exteriorizacion, generar_interiorizacion_hibrida

# Inyectar CSS
inject_styles()

# Header general
st.markdown("""
<div class="app-header">
  <div class="app-header-main">
    <div class="app-logo">🟣</div>
    <div>
      <div class="app-title">Yape Feedback Loop</div>
      <div class="app-subtitle">SECI + IA para convertir comentarios en decisiones de producto</div>
    </div>
  </div>
  <div class="app-steps">
    <span class="step-pill step-active">1 · Socialización</span>
    <span class="step-pill">2 · Exteriorización</span>
    <span class="step-pill">3 · Combinación</span>
    <span class="step-pill">4 · Internalización</span>
  </div>
</div>
""", unsafe_allow_html=True)

# Estado
if 'comentarios' not in st.session_state:
    st.session_state['comentarios'] = []
if 'propuestas' not in st.session_state:
    st.session_state['propuestas'] = []
if 'ultimo_post' not in st.session_state:
    st.session_state['ultimo_post'] = None

row1_col1, row1_col2 = st.columns(2, gap="large")
row2_col1, row2_col2 = st.columns(2, gap="large")

# 1. SOCIALIZACIÓN
with row1_col1:
    st.markdown('<div class="stage-card">', unsafe_allow_html=True)
    st.markdown("## 1. Socialización 🗣️")

    col_btn, col_metric = st.columns([1, 2])
    if col_btn.button("📡 Escuchar", use_container_width=True):
        with st.spinner("Conectando con Facebook..."):
            st.session_state['comentarios'] = obtener_comentarios()

    if st.session_state['comentarios']:
        col_metric.metric("Opiniones capturadas", len(st.session_state['comentarios']))
        
        with st.expander("Ver flujo de comentarios brutos", expanded=True):
            st.caption("A continuación se listan las opiniones recibidas sin procesar:")
            
            # Usamos enumerate(..., 1) para que el contador empiece en 1 y no en 0
            for i, comentario in enumerate(st.session_state['comentarios'], 1):
                st.markdown(f"""
                <div style="
                    background-color: #0f172a; 
                    padding: 12px 16px; 
                    border-radius: 8px; 
                    margin-bottom: 10px; 
                    border: 1px solid #1e293b; 
                    border-left: 4px solid #a855f7;
                    font-size: 0.95rem;
                    color: #e2e8f0;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                    <span style="
                        color: #cbd5e1; 
                        font-weight: bold; 
                        margin-right: 8px; 
                        opacity: 0.7;">
                        #{i}
                    </span>
                    {comentario}
                </div>
                """, unsafe_allow_html=True)
    else:
            st.caption("Aún no se han cargado comentarios en esta sesión.")

st.markdown('</div>', unsafe_allow_html=True)

# 2. EXTERIORIZACIÓN
with row1_col2:
    st.markdown('<div class="stage-card">', unsafe_allow_html=True)
    st.markdown("## 2. Exteriorización ⚙️")

    if st.session_state['comentarios'] and IA_ACTIVA:
        if st.button("⚡ Procesar Insights", use_container_width=True):
            with st.spinner("Analizando comentarios con IA..."):
                st.session_state['propuestas'] = analizar_exteriorizacion(
                    st.session_state['comentarios']
                )

    if st.session_state['propuestas']:

        for i, p in enumerate(st.session_state['propuestas']):
            titulo = p.get('titulo', f'Ticket {i+1}')
            tipo = p.get('tipo', 'N/A')
            prioridad = p.get('prioridad', 'N/A')
            problema = p.get('problema', '')
            viabilidad = p.get('viabilidad', '-')
            esfuerzo = p.get('esfuerzo', '-')

            prioridad_lower = str(prioridad).lower()
            if prioridad_lower not in ["alta", "media", "baja"]:
                prioridad_lower = "media"

            st.markdown(f"""
                <div class="ticket-card">
                  <div class="ticket-header">
                    <div class="ticket-title-row">
                      <span class="ticket-emoji">🎯</span>
                      <div class="ticket-title-text">{titulo}</div>
                    </div>
                    <div class="ticket-chips">
                      <span class="ticket-chip">{tipo}</span>
                      <span class="ticket-chip ticket-chip-prio-{prioridad_lower}">Prioridad: {prioridad}</span>
                    </div>
                  </div>

                  <div class="ticket-section">
                    <div class="ticket-section-title">Problema detectado</div>
                    <div class="ticket-section-body">{problema}</div>
                  </div>

                  <div class="ticket-footer">
                    <div class="ticket-footer-item">
                      <div class="ticket-metric-label">Viabilidad</div>
                      <div class="ticket-metric-value">{viabilidad}</div>
                    </div>
                    <div class="ticket-footer-item">
                      <div class="ticket-metric-label">Esfuerzo</div>
                      <div class="ticket-metric-value">{esfuerzo}</div>
                    </div>
                    <div class="ticket-footer-item">
                      <div class="ticket-metric-label">Ítem</div>
                      <div class="ticket-metric-value">{i+1}</div>
                    </div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.caption("Genera tickets a partir de los comentarios para verlos aquí.")

    st.markdown('</div>', unsafe_allow_html=True)

# 4. INTERNALIZACIÓN (Roadmap)
with row2_col1:
    st.markdown('<div class="stage-card">', unsafe_allow_html=True)
    st.markdown("## 4. Internalización 📢")

    if st.session_state['ultimo_post']:
        post = st.session_state['ultimo_post']

        st.markdown('<div class="post-card">', unsafe_allow_html=True)
        st.markdown("""
<div class="post-header">
  <div class="post-avatar">Y</div>
  <div>
    <div class="post-meta-title">Yape Oficial</div>
    <div class="post-meta-sub">Hace un momento · Público</div>
  </div>
</div>
""", unsafe_allow_html=True)

        st.write(post['texto_post'])
        if post.get('url_imagen'):
            st.image(post['url_imagen'], use_container_width=True)
        st.markdown(
            '<div class="post-footer-actions">👍 Me gusta &nbsp;&nbsp; 💬 Comentar &nbsp;&nbsp; ↗️ Compartir</div>',
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.caption("Aún no se ha generado ningún post de roadmap.")

    st.markdown('</div>', unsafe_allow_html=True)

# 3. COMBINACIÓN
with row2_col2:
    st.markdown('<div class="stage-card">', unsafe_allow_html=True)
    st.markdown("## 3. Combinación 📚")

    if st.session_state['propuestas']:
        for p in st.session_state['propuestas']:
            with st.expander(f"Validar: {p['titulo']}", expanded=True):
                st.markdown("**Solución propuesta**")
                st.write(p['solucion'])
                st.caption(f"Viabilidad estimada: **{p['viabilidad']}** · Esfuerzo: **{p['esfuerzo']}**")

                if st.button("✅ Aprobar y generar post", key=f"approve_{p['titulo']}"):
                    with st.spinner("Generando contenido de roadmap con IA..."):
                        st.session_state['ultimo_post'] = generar_interiorizacion_hibrida(p)
                        st.experimental_rerun()
    else:
        st.caption("Primero genera tickets en la fase de Exteriorización para poder validarlos aquí.")

    st.markdown('</div>', unsafe_allow_html=True)
