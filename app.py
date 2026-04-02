import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configurar Gemini
genai.configure(api_key=os.getenv("AIzaSyB57M1tiZuIJmb2-pnMjNGZ2dT-6VMS9Z0"))
model = genai.GenerativeModel('models/gemini-1.5-flash')

# --- Interfaz de Streamlit ---
st.set_page_config(page_title="Creative Engine", layout="centered")

# Estética minimalista (inspirada en VEIL)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    input, .stSelectbox, .stSlider { border: 1px solid #333 !important; }
    .stButton>button { 
        width: 100%; border-radius: 0px; border: 1px solid white; 
        background: transparent; color: white; height: 3em;
    }
    .stButton>button:hover { background: white; color: black; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔲 THE CREATIVE ENGINE")
st.caption("AI Curated Concepts for Electronic Music")

col1, col2 = st.columns(2)
with col1:
    genre = st.selectbox("GÉNERO", ["Melodic House", "Vocal House", "Deep Tech"])
    energy = st.slider("MOOD / VIBE", 1, 10, 5)
with col2:
    concept = st.text_input("CONCEPTO BASE", placeholder="Ej: Midnight")

if st.button("GENERAR"):
    # Prompt optimizado para tu estilo
    prompt = f"""
    Actúa como un director creativo de música electrónica (estilo RÜFÜS DU SOL, Elderbrook).
    Genera un concepto para un track de {genre} basado en '{concept}' con energía {energy}/10.
    
    Responde estrictamente en este formato:
    1. TÍTULOS: (3 opciones cortas en inglés)
    2. LYRIC HOOK: (4 líneas de letra abstracta y melancólica)
    3. VISUAL: (Una descripción para una portada minimalista en blanco y negro)
    4. PALETTE: (3 códigos HEX que contrasten)
    """
    
    with st.spinner("Procesando señal..."):
        response = model.generate_content(prompt)
        st.write("___")
        st.markdown(response.text)