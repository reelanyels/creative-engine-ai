# UPDATE 02-04-2026: FORZANDO V1 PRODUCCION
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
# ... (asegúrate de que abajo diga version="v1")

# 1. Configuración de la API Key desde los Secrets de Streamlit
api_key = st.secrets["GEMINI_API_KEY"]

# 2. Inicializar el modelo (Usando el puente LangChain para evitar el NotFound)
# Cambia la línea del modelo por esta:
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash", # <--- Agregamos 'models/' al principio
    google_api_key=api_key
)

st.title("THE CREATIVE ENGINE")
st.subheader("Generador de Conceptos para Productores")

# 3. Inputs de la Interfaz
concepto = st.text_input("Escribe una palabra o sentimiento (ej: Silencio, Caos, Berlín):")
genero = st.selectbox("Elige el estilo musical:", ["Melodic House", "Vocal House", "Deep House", "Techno"])

# 4. Lógica de Generación
if st.button("GENERAR", key="boton_unico_creative"):
    if concepto:
        with st.spinner("Procesando señal creativa..."):
            # Creamos el prompt para la IA
            prompt = f"""
            Actúa como un director creativo de música electrónica. 
            Basado en el concepto '{concepto}', genera para un track de {genero}:
            1. Un título sugerido.
            2. Una breve descripción de la atmósfera (vibe).
            3. Una estructura de letra o frases vocales cortas (estilo Rufus du Sol/Elderbrook).
            4. Una paleta de colores en HEX para el arte de portada.
            """
            
            try:
                # AQUÍ USAMOS 'llm' EN LUGAR DE 'model'
                response = llm.invoke(prompt)
                st.write("---")
                st.markdown(response.content)
            except Exception as e:
                st.error(f"Hubo un error de conexión: {e}")
    else:
        st.warning("Por favor, introduce un concepto para empezar.")