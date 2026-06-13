import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.corpus import stopwords

# Forzar la descarga y carga de stopwords en español para evitar fallos de entorno
try:
    stop_words_es = stopwords.words('spanish')
except:
    import nltk
    nltk.download('stopwords')
    stop_words_es = stopwords.words('spanish')

# Configuración básica de la página web
st.set_page_config(page_title="SEO Keyword Clusterer", layout="wide")
st.title("🤖 Agrupador Inteligente de Palabras Clave (SEO)")
st.subheader("Optimiza tu arquitectura web agrupando keywords en segundos")

# Texto predeterminado con palabras clave reales para que pruebes la herramienta al instante
keywords_predeterminadas = (
    "comprar zapatillas running\n"
    "zapatillas running baratas\n"
    "mejores zapatillas running\n"
    "cómo elegir zapatillas de correr\n"
    "comprar cafe en grano\n"
    "cafe en grano online\n"
    "mejor cafe en grano gourmet\n"
    "curso de seo gratis\n"
    "aprender seo online\n"
    "mejor curso de seo para principiantes"
)

# Cuadro de texto donde el usuario mete sus palabras clave
keywords_input = st.text_area(
    "Pega tus palabras clave aquí (una por línea):",
    value=keywords_predeterminadas,
    height=250
)

# Barra deslizante para elegir el número de grupos (clústeres)
num_clusters = st.slider("¿En cuántos grupos quieres organizar las keywords?", min_value=2, max_value=5, value=3)

# Lógica que se ejecuta al hacer clic en el botón
if st.button("🚀 Agrupar Palabras Clave"):
    if keywords_input.strip() == "":
        st.warning("Por favor, introduce al menos algunas palabras clave.")
    else:
        # Convertir el texto del usuario en una lista limpia de Python
        keywords_list = [kw.strip() for kw in keywords_input.split('\n') if kw.strip() != ""]
        
        if len(keywords_list) < num_clusters:
            st.error(f"Tienes menos palabras clave ({len(keywords_list)}) que el número de grupos seleccionados ({num_clusters}). Baja el número de grupos.")
        else:
            with st.spinner("Procesando y agrupando con Machine Learning..."):
                # 1. Transformar el texto a datos numéricos (TF-IDF Vectorizer)
                vectorizer = TfidfVectorizer(stop_words=stop_words_es)
                X = vectorizer.fit_transform(keywords_list)
                
                # 2. Entrenar el modelo matemático K-Means
                model = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=100, n_init=10, random_state=42)
                model.fit(X)
                
                # 3. Organizar los resultados en una tabla de Pandas
                results_df = pd.DataFrame({
                    'Palabra Clave': keywords_list,
                    'Grupo ID': model.labels_
                })
                
                # Dar un formato visual amigable a los nombres de los grupos
                results_df['Grupo ID'] = results_df['Grupo ID'].apply(lambda x: f"Grupo Temático {x + 1}")
                results_df = results_df.sort_values(by='Grupo ID')
                
                st.success("¡Agrupación completada con éxito!")
                
                # Mostrar la tabla interactiva en la web
                st.write("### 📊 Palabras Clave Clasificadas:")
                st.dataframe(results_df, use_container_width=True)
                
                # Botón de descarga directa en formato CSV (compatible con Excel)
                csv = results_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Descargar Resultados (CSV)",
                    data=csv,
                    file_name="keywords_agrupadas_seo.csv",
                    mime="text/csv"
                )
