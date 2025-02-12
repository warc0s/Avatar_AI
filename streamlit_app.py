import streamlit as st
import requests
import base64
import random
from io import BytesIO

# Configuración de la página: debe ser la primera llamada de Streamlit
st.set_page_config(page_title="Avatar AI", layout="wide")

# --- Custom CSS para mejorar el diseño ---
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
    }
    .css-18e3th9, .css-1d391kg {  
        background-color: #ffffff;
    }
    .sidebar .sidebar-content {
        background: #ffffff;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Diccionarios para opciones de raza y accesorios ---
race_options = {
    "Elfo/a": "elf",
    "Dragón": "dragon",
    "Robot": "robot",
    "Humano": "human",
    "Enano": "dwarf"
}

accessories_options = {
    "Armadura": "armor",
    "Alas": "wings",
    "Armas": "weapons",
    "Sombrero": "hat",
    "Gafas": "glasses"
}

# --- Función para construir el prompt optimizado ---
def generate_avatar_prompt(selected_race, selected_accessories, extra_text):
    # Comenzar con la raza
    prompt = f"closeup portrait of a highly detailed {race_options[selected_race]} avatar"
    
    # Si hay accesorios, se añaden de forma natural
    if selected_accessories:
        prompt += " wearing " + " and ".join(selected_accessories)
    
    # Se añaden detalles adicionales, si se han indicado
    if extra_text.strip():
        prompt += f" with {extra_text.strip()}"
    
    # Toque final: ambiente perfecto, marco decorativo y luz ambiental suave
    prompt += ", set in a perfect environment, framed by an ornate decorative border, with soft ambient lighting, extremely detailed"
    return prompt

# --- Función para generar la imagen vía la API local de Stable Diffusion ---
def generate_image(prompt, style):
    base_url = "http://127.0.0.1:7860"
    endpoint = "/sdapi/v1/txt2img"
    full_url = f"{base_url}{endpoint}"

    # Negative prompt fijo (no modificar)
    negative_prompt = (
        "(nsfw, naked, nude, deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime, mutated hands and fingers:1.4), "
        "(deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, disconnected limbs, mutation, mutated, ugly, disgusting, amputation"
    )
    seed = random.randint(0, 2**32 - 1)
    
    # Seleccionar el modelo según el estilo elegido
    if style == "Anime":
        model_checkpoint = "waifuReaper_testMod22Crow.safetensors [2146b17441]"
    else:  # Realista
        model_checkpoint = "realisticVisionV60B1_v51HyperVAE.safetensors [f47e942ad4]"

    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "width": 512,
        "height": 512,
        "sampler_name": "DPM++ SDE",
        "steps": 6,
        "cfg_scale": 1.5,
        "seed": seed,
        "override_settings": {
            "sd_model_checkpoint": model_checkpoint
        }
    }
    try:
        response = requests.post(url=full_url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.error(f"Error al conectar con la API: {e}")
        return None

    try:
        response_json = response.json()
        images = response_json.get("images")
        if not images or len(images) == 0:
            st.error("No se recibió ninguna imagen en la respuesta.")
            return None
        # Decodificar la primera imagen (base64)
        image_data = base64.b64decode(images[0])
        return image_data
    except Exception as e:
        st.error(f"Error al procesar la respuesta: {e}")
        return None

# --- Función principal de la aplicación ---
def main():
    st.title("Avatar AI")
    st.markdown(
        """
        Genera avatares de fantasía únicos utilizando modelos de **Realistic Vision V6.0 B1** o **Waifu Reaper** (Anime).<br>
        Selecciona la raza, los accesorios y añade detalles adicionales en inglés.
        """,
        unsafe_allow_html=True,
    )

    # Inicializar session_state para almacenar la imagen
    if "image_bytes" not in st.session_state:
        st.session_state["image_bytes"] = None

    # --- Sidebar: Opciones de Personalización ---
    st.sidebar.header("Opciones de Personalización")
    selected_race = st.sidebar.selectbox("Selecciona la Raza:", list(race_options.keys()))

    # Selector para el estilo
    selected_style = st.sidebar.selectbox("Estilo", ["Realista", "Anime"])
    
    st.sidebar.markdown("### Accesorios")
    selected_accessories = []
    for accessory in accessories_options.keys():
        if st.sidebar.checkbox(accessory):
            selected_accessories.append(accessories_options[accessory])
    
    extra_text = st.sidebar.text_input("Detalles adicionales (en inglés):", "")

    # Generar el prompt final
    final_prompt = generate_avatar_prompt(selected_race, selected_accessories, extra_text)
    st.markdown("### Prompt generado:")
    st.code(final_prompt, language="none")

    # --- Botón para generar el avatar ---
    if st.button("Generar Avatar"):
        with st.spinner("Generando imagen..."):
            image_bytes = generate_image(final_prompt, selected_style)
            if image_bytes:
                st.session_state["image_bytes"] = image_bytes

    # Mostrar la imagen y el botón de descarga (la imagen se mantiene en pantalla incluso tras descargar)
    if st.session_state["image_bytes"]:
        st.image(st.session_state["image_bytes"], caption="Avatar Generado", width=512)
        st.download_button(
            label="Descargar Imagen",
            data=st.session_state["image_bytes"],
            file_name="avatar.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()
