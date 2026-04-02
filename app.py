import streamlit as st
import google.generativeai as genai

# 1. Configuración de la API Key
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

st.title("THE CREATIVE ENGINE")
st.subheader("Generador de Conceptos para Productores")

# 2. Inputs de la Interfaz
concepto = st.text_input("Escribe una palabra o sentimiento (ej: Silencio, Caos, Berlín):")
genero = st.selectbox("Elige el estilo musical:", ["Melodic House", "Vocal House", "Deep House", "Techno"])

# 3. Lógica de Generación
if st.button("GENERAR", key="boton_final"):
    if concepto:
        with st.spinner("Procesando señal creativa..."):
            # FORZAMOS EL MODELO SIN 'models/' Y SIN VERSION BETA
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            prompt = f"""
            Actúa como un director creativo de música electrónica. 
            Basado en el concepto '{concepto}', genera para un track de {genero}:
            1. Un título sugerido.
            2. Una breve descripción de la atmósfera (vibe).
            3. Una estructura de letra o frases vocales cortas (estilo Rufus du Sol/Elderbrook).
            4. Una paleta de colores en HEX para el arte de portada.
            """
            
            try:
                # LLAMADA DIRECTA
                response = model.generate_content(prompt)
                st.write("---")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error de API: {e}")
                st.info("Si el error persiste, genera una NUEVA API KEY en Google AI Studio.")
    else:
        st.warning("Por favor, introduce un concepto.")