import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests

# Charger les données contenant les URLs des images
data = pd.read_csv("https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/refs/heads/main/lientest1.csv")

st.set_page_config(layout="wide")

# Extraire les URLs des images
image_urls = data['photo_url']

# Taille du patchwork (nombre d'images par ligne)
cols_per_row = 5  # Vous pouvez ajuster ce nombre
rows = len(image_urls) // cols_per_row + 1

st.write("## Patchwork des Activités")

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
            image_url = image_urls[index]

            try:
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))

                # Afficher l'image sans l'info-bulle
                with cols[i]:
                    st.image(img, use_column_width=True)  # Aucune légende ici


            except Exception as e:
                st.write(f"Impossible de charger l'image : {e}")
