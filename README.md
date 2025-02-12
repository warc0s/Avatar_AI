# Avatar AI

## Descripción
Avatar AI es una aplicación web que te permite generar avatares de fantasía únicos y personalizados gracias al poder de la Inteligencia Artificial (Stable Diffusion). La aplicación utiliza el modelo **Realistic Vision V6.0 B1**, un full finetune de Stable Diffusion 1.5 Hyper que permite generar imágenes realistas en tan solo 4-6 pasos, en comparación con los +20 pasos requeridos por el Stable Diffusion 1.5 tradicional.

---

## Parte 1: Modelos

### Modelo Base Utilizado
- **Nombre:** Realistic Vision V6.0 B1  
- **Enlace:** [https://civitai.com/models/4201/realistic-vision-v60-b1?modelVersionId=501240](https://civitai.com/models/4201/realistic-vision-v60-b1?modelVersionId=501240)

### Características Principales
- **Full Finetune:** Basado en Stable Diffusion 1.5 Hyper, optimizado para generar imágenes en 4-6 pasos.
- **Enfoque Realista:** Especializado en producir imágenes con un alto grado de realismo, ideal para retratos y escenas detalladas.
- **Eficiencia:** Permite una generación de imágenes mucho más rápida que el modelo tradicional de Stable Diffusion 1.5.

---

## Parte 2: Interfaz de Usuario

### Tecnologías Utilizadas
- **Framework:** Streamlit
- **Librerías Adicionales:** (añadir aqui lo usado)

### Características de la Interfaz
La interfaz se ha diseñado con una temática fantástica para la creación de avatares y combina controles en español con la generación de prompts en inglés, optimizados para el modelo Realistic Vision V6.0 B1.

#### Selección de Raza
- **Tipo de Control:** Lista desplegable / Botones
- **Opciones Disponibles:**
  - Elfo/a
  - Dragón
  - Robot
  - Humano
  - Enano
  - *(Otros…)*

#### Estilo Artístico
- **Tipo de Control:** Lista desplegable / Botones
- **Opciones Disponibles:**
  - Estilo Cómic
  - Realista
  - Acuarela
  - Impresionista
  - *(Otros…)*

#### Accesorios
- **Tipo de Control:** Casillas de verificación / Botones
- **Opciones Disponibles:**
  - Armadura
  - Alas
  - Armas
  - Sombrero
  - Gafas
  - *(Otros accesorios…)*

#### Personalización Adicional
- **Controles Adicionales:**  
  - Posibilidad de ajustar colores, poses y expresiones.
  - **Caja de Texto para Prompts Adicionales:** Permite ingresar descripciones adicionales en inglés para complementar el prompt principal (ejemplo: “with hat”, “in a futuristic style”, etc.).  
    > **Nota:** Aunque las opciones de selección se muestran en español, el prompt final enviado a la API se genera en inglés, combinando las opciones elegidas y el texto personalizado.

#### Botón "Generar Avatar"
- **Descripción:**  
  Al hacer clic en "Generar Avatar", se recopilan todos los parámetros seleccionados (raza, estilo artístico, accesorios y personalización adicional) y se envían a la API de Stable Diffusion utilizando el modelo Realistic Vision V6.0 B1.  
  Se genera un prompt en inglés que integra todas las opciones, garantizando la generación de imágenes realistas y detalladas en tan solo 4-6 pasos. La imagen resultante se muestra en pantalla una vez finalizado el proceso.

---

## Capturas de Pantalla
Incluye diversas capturas de pantalla de la aplicación en funcionamiento, mostrando:
- La pantalla de selección de opciones (raza, estilo, accesorios y personalización).
- La interfaz de generación y visualización del avatar.
- Ejemplos de diferentes combinaciones y resultados obtenidos.

---

## Muestra de Avatares Generados
Una galería con imágenes de avatares generados por la aplicación, evidenciando la diversidad de resultados posibles gracias a la combinación de estilos y personalizaciones, aprovechando al máximo las capacidades del modelo Realistic Vision V6.0 B1.

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
