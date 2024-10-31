import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests

# Charger les données contenant les URLs des images
data = pd.read_csv("https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/refs/heads/main/CONFIRMED.csv")

st.set_page_config(layout="wide")

# Ajouter un sélecteur pour l'email du validator
validator_emails = data['validator email'].unique()
selected_email = st.selectbox("Sélectionnez votre email", validator_emails)

# Ajouter un sélecteur pour la date
# Convertir les dates en format datetime pour faciliter la sélection
data['created_at'] = pd.to_datetime(data['created_at'])
dates = data['created_at'].dt.date.unique()  # Extraire les dates uniques
selected_date = st.date_input("Sélectionnez la date", value=min(dates), min_value=min(dates), max_value=max(dates))

# Filtrer les données par email et par date
filtered_data = data[(data['validator email'] == selected_email) & (data['created_at'].dt.date == selected_date)]

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
                    st.image(img, use_column_width=True, caption=photo_id)  # Aucune légende ici

            except Exception as e:
                st.write(f"Impossible de charger l'image : {e}")
