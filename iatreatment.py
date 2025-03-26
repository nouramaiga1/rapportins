import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests

# Charger les données contenant les URLs des images
data = pd.read_csv("https://raw.githubusercontent.com/nouramaiga1/rapportins/refs/heads/master/LESCONFIRMED.csv")

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    validator_emails = data['validator email'].unique()
    selected_email = st.selectbox("Validateur", validator_emails)

    initial_sizes = data['initial_size'].unique()
    selected_initial_size = st.selectbox("Taille initiale", initial_sizes)

with col2:
    ai_sizes = data['ai_size'].unique()
    selected_ai_size = st.selectbox("Taille IA", ai_sizes)

    sizes = data['size'].unique()
    selected_size = st.selectbox("Taille BO", sizes)


# Filtrer les données par email et par date
filtered_data = data[(data['validator email'] == selected_email), data["initial_size"] == selected_initial_size, data["ai_size"] == selected_ai_size, data["size"] == selected_size]

st.metric("Nombre de photos", len(filtered_data))

# Extraire les URLs des images après filtrage
image_urls = filtered_data['photo_url']
image_ids = filtered_data['id']

# Taille du patchwork (nombre d'images par ligne)
cols_per_row = 5  # Vous pouvez ajuster ce nombre
rows = len(image_urls) // cols_per_row + 1

st.write("## Photos des Activités")

# Créer un conteneur pour le patchwork
with st.container():
    for row in range(rows):
        cols = st.columns(cols_per_row)

        # Charger chaque image pour la ligne
        for i in range(cols_per_row):
            index = row * cols_per_row + i
            if index >= len(image_urls):
                break

            # Récupérer l'image
            image_url = image_urls.iloc[index]
            photo_id = image_ids.iloc[index]
            try:
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))

                # Afficher l'image sans l'info-bulle
                with cols[i]:
                    st.image(img, use_container_width=True, caption=photo_id)  # Aucune légende ici

            except Exception as e:
                st.write(f"Impossible de charger l'image : {e}")
