# 🤖 SEO Keyword Clustering Tool (Machine Learning & NLP)

Una aplicación web de automatización SEO desarrollada en **Python** y **Streamlit** que resuelve uno de los mayores cuellos de botella en la fase de investigación de palabras clave (*Keyword Research*): el agrupamiento semántico masivo. 

La herramienta utiliza algoritmos de **Procesamiento de Lenguaje Natural (NLP)** y **Machine Learning** tradicional para clasificar miles de intenciones de búsqueda en segundos de forma 100% gratuita y local.

---

## 💡 El Problema que Resuelve
Al realizar auditorías SEO competitivas o extraer datos de herramientas como Ahrefs o Semrush, los consultores terminan con archivos CSV de miles de palabras clave completamente desordenadas. Organizar este caos manualmente en Excel para diseñar una arquitectura web o un plan de contenidos puede tomar **días enteros de trabajo monótono**.

**Esta herramienta automatiza ese proceso:** reduce una tarea de 8 horas de filtrado manual a un proceso algorítmico de **3 segundos**, optimizando la productividad de las agencias de marketing y eliminando costes derivados de APIs de terceros.

---

## 🛠️ Arquitectura Técnica y Decisiones de Diseño

Para optimizar el rendimiento y la viabilidad del proyecto, se seleccionaron tecnologías específicas basadas en la eficiencia de costes:

1. **Procesamiento de Texto (Stopwords):** Se utiliza la librería `NLTK` para filtrar y eliminar conectores gramaticales (artículos, preposiciones) en español, forzando al algoritmo a analizar únicamente los núcleos semánticos del negocio.
2. **Vectorización TF-IDF (`TfidfVectorizer`):** Transforma el texto humano en vectores numéricos legibles por la máquina. Calcula la relevancia de los términos aplicando *Term Frequency - Inverse Document Frequency*, penalizando palabras genéricas y premiando la especificidad.
3. **Algoritmo K-Means (`scikit-learn`):** Ejecuta un clustering no supervisado en un espacio multidimensional. Agrupa de forma nativa los vectores por cercanía semántica e intención.
4. **¿Por qué K-Means local en lugar de LLMs (como la API de OpenAI)?**
   * **Coste $0:** Procesar listas de 50.000 keywords con modelos de lenguaje grandes (LLMs) genera costes masivos por consumo de tokens. K-Means es gratuito.
   * **Velocidad de ejecución:** Resuelve el agrupamiento en milisegundos directamente en el servidor, sin latencia de red externa.

---

## 🚀 Características principales
* **Interfaz de usuario intuitiva:** Desarrollada puramente en Python con `Streamlit`.
* **Carga masiva:** Cuadro de texto preparado para procesar miles de líneas en un solo clic.
* **Control de profundidad:** Slider dinámico para que el SEO decida cuántos clústeres/categorías requiere según el tamaño de la arquitectura web.
* **Descarga directa:** Botón integrado para exportar los resultados clasificados a un archivo CSV limpio, compatible con Excel y Google Sheets.

---

## 📦 Requisitos e Instalación Local

Si deseas clonar este repositorio y ejecutarlo en tu entorno local, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com
   cd seo-keyword-clustering-tool
   ```

2. **Instalar dependencias necesarias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación web:**
   ```bash
   streamlit run app.py
   ```
