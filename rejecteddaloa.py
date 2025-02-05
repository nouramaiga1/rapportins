import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests

# Charger les données contenant les URLs des images
data = pd.read_csv("https://raw.githubusercontent.com/nouramaiga1/pictures/refs/heads/main/rejectednodupdaloa.csv")

st.set_page_config(layout="wide")

st.write("## Photos des activités rejetées - Daloa")

# Sélectionner un validateur unique
validators = data['validator email'].unique()
selected_validator = st.selectbox("Sélectionnez le validateur", validators)

# Filtrer les données pour afficher uniquement les secteurs qui ont des images pour le validateur sélectionné
filtered_validator_data = data[data['validator email'] == selected_validator]

# Filtrer les secteurs d'activité qui ont des images (exclure les entrées sans photo)
valid_sectors = filtered_validator_data[filtered_validator_data['photo_url'].notnull()]['activity_sector'].unique()

# Sélectionner un secteur dans la liste filtrée
selected_sector = st.selectbox("Sélectionnez le secteur d'activité", valid_sectors)

# Appliquer le filtre final
filtered_data = filtered_validator_data[filtered_validator_data['activity_sector'] == selected_sector]

# Extraire les données nécessaires
image_urls = filtered_data['photo_url']
image_ids = filtered_data['id']
image_validators = filtered_data['validator email']

# Taille du patchwork (nombre d'images par ligne)
cols_per_row = 5
rows = len(image_urls) // cols_per_row + 1

with st.container():
    for row in range(rows):
        cols = st.columns(cols_per_row)

        # Charger chaque image pour la ligne
        for i in range(cols_per_row):
            index = row * cols_per_row + i
            if index >= len(image_urls):
                break

            # Récupérer l'image et ses informations
            image_url = image_urls.iloc[index]
            photo_id = image_ids.iloc[index]
            validator_email = image_validators.iloc[index]

            try:
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))

                # Afficher l'image avec IDU et validateur
                with cols[i]:
                    st.image(img, use_container_width=True, caption=f"{photo_id}")

            except Exception as e:
                st.write(f"Impossible de charger l'image : {e}")
