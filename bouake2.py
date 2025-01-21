import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests




# Charger les données contenant les URLs des images
data = pd.read_csv("https://raw.githubusercontent.com/nouramaiga1/pictures/refs/heads/main/bouakepictures2.csv")

st.set_page_config(layout="wide")

st.write("## Photos des Activités - Bouake 2")

# Ajouter un sélecteur pour la taille de l'activité
sizes = data['size'].unique()
selected_size = st.selectbox("Sélectionnez la taille", sizes)

filtered_data = data[(data['size'] == selected_size)]

# Extraire les URLs des images après filtrage
image_urls = filtered_data['photo_url']
image_ids = filtered_data['id']

# Taille du patchwork (nombre d'images par ligne)
cols_per_row = 5  # Vous pouvez ajuster ce nombre
rows = len(image_urls) // cols_per_row + 1


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
