# Avatar AI

<p align="center">
  <img src="https://raw.githubusercontent.com/warc0s/Avatar_AI/refs/heads/main/logo.webp" alt="Avatar AI" width="80%">
</p>

## Descripción
Avatar AI es una aplicación web que te permite generar avatares únicos y personalizados gracias al poder de Stable Diffusion. La aplicación utiliza modelos optimizados para generar avatares detallados, en una variedad de estilos, razas y accesorios.

- **Realistic Vision V6.0 B1** para imágenes realistas.
- **Waifu Reaper** para imágenes en estilo anime.
- **Disney Pixar Cartoon Type A** para un estilo Cartoon Pixar.
- **PixelMonster** para un estilo Pixel Art.

---

## Parte 1: Modelos

### Modelo Realista
- **Nombre:** Realistic Vision V6.0 B1  
- **Enlace:** [https://civitai.com/models/4201/realistic-vision-v60-b1?modelVersionId=501240](https://civitai.com/models/4201/realistic-vision-v60-b1?modelVersionId=501240)

### Modelo Anime
- **Nombre:** Waifu Reaper  
- **Enlace:** [https://civitai.com/models/24131/waifu-reaper?modelVersionId=648218](https://civitai.com/models/24131/waifu-reaper?modelVersionId=648218)

### Modelo Cartoon Pixar
- **Nombre:** Disney Pixar Cartoon Type A  
- **Enlace:** [https://civitai.com/models/65203/disney-pixar-cartoon-type-a](https://civitai.com/models/65203/disney-pixar-cartoon-type-a)

### Modelo Pixel Art
- **Nombre:** PixelMonster  
- **Enlace:** [https://civitai.com/models/1034297/pixelmonster](https://civitai.com/models/1034297/pixelmonster)

> **Importante:** Descarga los modelos necesarios y colócalos en la carpeta `models` de Automatic1111 Stable Diffusion WebUI.

---

## Parte 2: Interfaz de Usuario

### Tecnologías Utilizadas
- **Framework:** Streamlit

### Características de la Interfaz
La interfaz se ha diseñado con una temática para la creación de avatares y combina controles en español con la generación de prompts en inglés, optimizados para los modelos utilizados.

#### Selección de Raza
- **Tipo de Control:** Lista desplegable  
- **Opciones Disponibles:**
  - Elfo/a
  - Dragón
  - Robot
  - Humano
  - Enano

#### Selección de Género
- **Tipo de Control:** Lista desplegable  
- **Opciones Disponibles:**
  - Hombre
  - Mujer  
  *Nota: El género solo es seleccionable para las razas "Humano", "Elfo/a" o "Enano". Si se elige "Dragón" o "Robot", el control de género no estará disponible.*

#### Estilo Artístico
- **Tipo de Control:** Lista desplegable  
- **Opciones Disponibles:**
  - **Realista:** Utiliza el modelo Realistic Vision V6.0 B1.
  - **Anime:** Utiliza el modelo Waifu Reaper.  
    *Nota: Este estilo solo es compatible con la raza "Humano", debido al entrenamiento del modelo.*
  - **Cartoon Pixar:** Utiliza el modelo Disney Pixar Cartoon Type A.
  - **Pixel Art:** Utiliza el modelo PixelMonster.

#### Accesorios
- **Tipo de Control:** Casillas de verificación  
- **Opciones Disponibles:**
  - Armadura
  - Alas
  - Armas
  - Sombrero
  - Gafas

#### Personalización Adicional
- **Control:** Caja de Texto para Prompts Adicionales  
  Permite ingresar descripciones adicionales en inglés para complementar el prompt principal (ejemplo: “with hat”, “in a futuristic style”, etc.).

  > **Nota:** Aunque las opciones de selección se muestran en español, el prompt final enviado a la API se genera en inglés, combinando las opciones elegidas y el texto personalizado.

#### Botón "Generar Avatar"
- **Descripción:**  
  Al hacer clic en "Generar Avatar", se recopilan todos los parámetros seleccionados (raza, género, estilo artístico, accesorios y personalización adicional) y se envían a la API local de Stable Diffusion WebUI utilizando el modelo correspondiente. Se genera un prompt en inglés que integra todas las opciones, garantizando la generación de avatares detallados. La imagen resultante se muestra en pantalla y se ofrece la opción de descargarla.

## Requisitos y Ejecución

- **Servidor Stable Diffusion:**  
  Recuerda iniciar el servidor de Automatic1111 (stable-diffusion-webui) en modo `--api` para que Streamlit pueda comunicarse correctamente y generar imágenes.

- **Modelos:**  
  Descarga todos los modelos (Realistic Vision V6.0 B1, Waifu Reaper, Disney Pixar Cartoon Type A y PixelMonster) y colócalos en la carpeta `models`.

- **Ejecución de la Aplicación:**  
  Una vez tengas el servidor en modo API, ejecuta la aplicación Streamlit para comenzar a generar avatares.

---

## Capturas de Pantalla
[PROXIMAMENTE] mostrando:
- La pantalla de selección de opciones (raza, estilo, accesorios y personalización).
- La interfaz de generación y visualización del avatar.
- Ejemplos de diferentes combinaciones y resultados obtenidos.

---

## Muestra de Avatares Generados

<p align="center">
  <img src="https://github.com/warc0s/Avatar_AI/blob/main/avatar_examples/joined_image.png?raw=true" alt="Avatares Generados" width="100%">
</p>

  > **Nota:** Puedes revisarlos todos uno a uno dentro de la carperta "avatar_examples".

## Autores 

<table>
  <tr>
    <td align="center" width="400">
      <div style="border: 3px solid #FFD700; border-radius: 15px; padding: 20px; background-color: rgba(255, 215, 0, 0.05);">
        <div style="border: 2px solid #FFD700; border-radius: 50%; padding: 3px; margin: 0 auto;">
          <a href="https://warcos.dev">
            <img src="https://github.com/warc0s.png" width="220" alt="Marcos García" style="border-radius: 50%; border: 2px solid #FFF; box-shadow: 0 0 10px rgba(255, 215, 0, 0.4);">
          </a>
        </div>
        <h2 style="color: #FFD700; margin: 15px 0; font-family: 'Helvetica Neue', sans-serif;">Marcos García Estévez</h2>
        <div style="display: flex; gap: 10px; justify-content: center; margin-top: 15px;">
          <a href="https://github.com/warc0s">
            <img src="https://custom-icon-badges.demolab.com/badge/-GitHub-1a1a1a?style=for-the-badge&logo=github&logoColor=FFD700" alt="GitHub">
          </a>
          <a href="https://warcos.dev">
            <img src="https://custom-icon-badges.demolab.com/badge/-Portfolio-1a1a1a?style=for-the-badge&logo=browser&logoColor=FFD700" alt="Portfolio">
          </a>
        </div>
      </div>
    </td>
    
  <td align="center" width="400">
    <div style="border: 3px solid #FFD700; border-radius: 15px; padding: 20px; background-color: rgba(255, 215, 0, 0.05);">
      <div style="border: 2px solid #FFD700; border-radius: 50%; padding: 3px; margin: 0 auto;">
        <a href="https://github.com/DavidMoCe">
          <img src="https://github.com/DavidMoCe.png" width="220" alt="David Moreno Cerezo" style="border-radius: 50%; border: 2px solid #FFF; box-shadow: 0 0 10px rgba(255, 215, 0, 0.4);">
        </a>
      </div>
      <h2 style="color: #FFD700; margin: 15px 0; font-family: 'Helvetica Neue', sans-serif;">David Moreno Cerezo</h2>
      <div style="display: flex; gap: 10px; justify-content: center; margin-top: 15px;">
        <a href="https://github.com/DavidMoCe">
          <img src="https://custom-icon-badges.demolab.com/badge/-GitHub-1a1a1a?style=for-the-badge&logo=github&logoColor=FFD700" alt="GitHub">
        </a>
        <a href="https://www.linkedin.com/in/david-moreno-cerezo/">
          <img src="https://custom-icon-badges.demolab.com/badge/-LinkedIn-1a1a1a?style=for-the-badge&logo=linkedin&logoColor=FFD700" alt="LinkedIn">
        </a>
      </div>
    </div>
  </td>
  </tr>
</table>
