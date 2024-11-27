import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
from io import BytesIO
import requests

st.set_page_config(layout="wide")


st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="main-content">', unsafe_allow_html=True)



st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    /* Appliquer Montserrat à tout le contenu */
    html, body, h1, h2, h3, h4, h5, h6, p, div, span, li, td, th, .css-1v3fvcr {
        font-family: 'Montserrat', sans-serif;
    }

    /* Style pour les boîtes à coins arrondis */
    .rounded-box {
        background-color: #f0f0f5; /* Couleur de fond des boîtes */
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }

    .main-container {
        max-width: 1800px; /* Ajuste cette valeur selon tes besoins */
        margin: 0 auto;
        padding: 30px;
        width: 100%;
    }


    /* Ajuster la largeur maximale du contenu */
    .main-content {
        max-width: 2000px; /* Ajuste cette valeur selon tes besoins */
        margin: 0 auto;    /* Centrer le contenu */
        padding: 0px;     /* Ajouter du padding pour que le contenu ne soit pas collé au bord */
        width: 100%;
    }

    .main-content > * {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)



st.markdown("<h1 style='text-align: center;'>FOCUS VENTES SUR ETAL</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")

file_path1 = "https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/refs/heads/main/Booky.csv"
data1 = pd.read_csv(file_path1)

villes_disponibles = ["Toutes les villes"] + list(data1["commune"].unique())
ville_selectionnee = st.selectbox("Sélectionnez une ville:", villes_disponibles)

if ville_selectionnee == "Toutes les villes":
    data_filtree = data1
else:
    data_filtree = data1[data1["commune"] == ville_selectionnee]

category_counts = data_filtree["precision activite"].value_counts()

number_of_rows = len(data_filtree)

total_ca = data_filtree['CHIFFRE'].sum()

average_ca = data_filtree['CHIFFRE'].mean()

formatted_number = f"{number_of_rows:,.0f}".replace(",", " ")

col1, col2, colonne = st.columns(3)
with col1:
    st.metric(label="Nombre d'enregistrements", value=formatted_number)
    st.metric(label="Chiffre d'Affaires Global", value=f"{total_ca:,.0f} FCFA")

with col2 :
    st.metric(label="Moyenne du Chiffre d'Affaires", value=f"{average_ca:,.0f} FCFA")

st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .custom-box {
        border-radius: 15px;
        border: 1px solid #ccc;
        padding: 15px;
        background-color: #fAfAfA;
        font-family: 'Montserrat', sans-serif;
        margin-bottom: 15px;
        margin-top: 40px;
    }
    </style>
    <div class="custom-box">
        <h4>DIFFERENTS TYPES DE VENTE SUR ETAL</h4>
    </div>
    """,
    unsafe_allow_html=True
)

category_counts = data_filtree["precision activite"].value_counts()

cola5, cola6 = st.columns(2)

with cola5:
    st.write("")
    st.write("")
    st.write("")

    figure = px.pie(
        names=category_counts.index,  # Catégories uniques
        values=category_counts.values,  # Quantités associées à chaque catégorie
        hole=0.3,  # Pour un donut chart (optionnel)
        title=f"REPARTITION PAR TYPE DE VENTE SUR ETAL"
    )

    figure.update_traces(textinfo='none', hoverinfo='label+percent')
    figure.update_layout(showlegend=False)

    st.plotly_chart(figure)


# Calculer le total pour obtenir les pourcentages
total_entries = category_counts.sum()
top5_sectors = category_counts.nlargest(5)

top5_percentages = (top5_sectors / total_entries) * 100

# Créer le texte dynamique pour le top 5
top5_list = [
    f"- **{sector}** : {percentage:.2f}% "
    for sector, percentage in zip(top5_sectors.index, top5_percentages)
]
top5_text = "\n".join(top5_list)  # Joindre les éléments avec des sauts de ligne HTML

# Commentaire final
commentaire = f"Les principaux secteurs d'activité sont :\n\n{top5_text}\n\n"

# Espace avant le nombre moyen d'employés
st.write("\n" * 3)  # Ajoute 3 lignes vides

# Afficher le commentaire des secteurs
with cola6:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown(commentaire)
    st.write("")


st.markdown(
    """
    <style>
    .custom-box {
        border-radius: 15px;
        border: 1px solid #ccc;
        padding: 15px;
        background-color: #fAfAfA;
        font-family: 'Montserrat', sans-serif;
        margin-bottom: 15px;
        margin-top: 40px;
    }
    </style>
    <div class="custom-box">
        <h4>DIFFERENTES TAILLES DES VENTES SUR ETAL</h4>
    </div>
    """,
    unsafe_allow_html=True
)

category_counts = data_filtree["size"].value_counts()

col47, col48 = st.columns(2)

fig3 = px.pie(
    names=category_counts.index,  # Catégories uniques
    values=category_counts.values,  # Quantités associées à chaque catégorie
    hole=0.3,  # Pour un doughnut chart
    title="REPARTITION PAR TAILLE D'ACTIVITE"
)

fig3.update_traces(textinfo='none', hoverinfo='label+percent')

with col47:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    # **Générer un commentaire dynamique basé sur le doughnut chart**

    # Calculer le pourcentage de chaque taille d'activité
    total_count = category_counts.sum()
    size_percentages = (category_counts / total_count) * 100

    # Créer une liste pour stocker les descriptions de chaque taille avec leur pourcentage
    size_descriptions = [f"- **{size}** représente {percentage:.2f}% des activités."
                     for size, percentage in zip(category_counts.index, size_percentages)]

    # Joindre les descriptions en un texte complet
    commentaire = "\n".join(size_descriptions)

    definitions = """
    ### Quelques définitions

    **Taille d'activité :** On peut dire qu'une unité économique est dite :

    - **Très petite** lorsque son CA est compris entre 1 XOF et 2 400 000 XOF.
    - **Petite** lorsque son CA est compris entre 2 400 001 XOF et 3 600 000 XOF.
    - **Moyenne** lorsque son CA est compris entre 3 600 001 XOF et 4 000 000 XOF.
    - **Grande** lorsque son CA est supérieur à 4 000 000 XOF.
    """
    st.write(definitions)


with col48:
    st.plotly_chart(fig3)
    st.markdown(f"La répartition des tailles d'activité est la suivante :\n\n{commentaire}")
