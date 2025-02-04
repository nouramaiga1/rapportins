import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests




# Charger les données contenant les URLs des images
data = pd.read_csv("https://raw.githubusercontent.com/nouramaiga1/pictures/refs/heads/main/rejected%20photos%20man.csv")

st.set_page_config(layout="wide")

st.write("## Photos des activités rejetées - Man")

sectors = data['activity_sector'].unique()
selected_sector = st.selectbox("Sélectionnez le secteur d'activité", sectors)

validators = data['validator email']
selected_validator = st.selectbox("Sélectionnez le validateur", validators)

filtered_data = data[(data['activity_sector'] == selected_sector)&(data['validator email'] == selected_validator)]

# Extraire les URLs des images après filtrage
image_urls = filtered_data['photo_url']
image_ids = filtered_data['id']
image_validator = filtered_data['validator email']

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

                # Afficher l'image
                with cols[i]:
                    st.image(img, use_container_width=True, caption=photo_id)

            except Exception as e:
                st.write(f"Impossible de charger l'image : {e}")
