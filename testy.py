import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

file_path = "https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/refs/heads/main/RECAPOCTLAST.csv"
cols = ["commune", "activity_sector", "CA", "form", "size", "stade_de_maturite", "employees_count", "genre", "tranche_age", "ages","Entrepreneur identity_document_type","is_cnps_declared","terminal_type","type etal","type vivrier"]

@st.cache_data
def load_data(file_path, sheet_name, cols):
    return pd.read_csv(file_path, usecols=cols)

data = pd.read_csv(file_path, usecols=cols)

df = pd.read_csv(file_path, usecols=cols)

villes_disponibles = ["Toutes les villes"] + list(data["commune"].unique())
ville_selectionnee = st.selectbox("Sélectionnez une ville:", villes_disponibles)

if ville_selectionnee == "Toutes les villes":
    data_filtree = data
else:
    data_filtree = data[data["commune"] == ville_selectionnee]

category_counts = data_filtree["activity_sector"].value_counts()

number_of_rows = len(data_filtree)

total_ca = data_filtree['CA'].sum()

average_ca = data_filtree['CA'].mean()

average_age = data_filtree['ages'].mean()

average_employee = data_filtree['employees_count'].mean()

formatted_number = f"{number_of_rows:,.0f}".replace(",", " ")

col1, col2, colonne = st.columns(3)
with col1:
    st.metric(label="Nombre d'enregistrements", value=formatted_number)
with col2:
    st.metric(label="Moyenne d'Âge", value=f"{average_age:,.1f} ans")
with colonne:
    st.metric(label="Nombre d'employés moyen", value=f"{average_employee:,.1f}")


col3, col4, colonnie = st.columns(3)
with col3:
    st.metric(label="Chiffre d'Affaires Global", value=f"{total_ca:,.0f} FCFA")
with col4:
    st.metric(label="Moyenne du Chiffre d'Affaires", value=f"{average_ca:,.0f} FCFA")


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
        <h4>UNE MAJORITE SANS DOCUMENT D'IDENTITE</h4>
    </div>
    """,
    unsafe_allow_html=True
)
category_counts = data_filtree["Entrepreneur identity_document_type"].value_counts()

data['Entrepreneur identity_document_type'] = data['Entrepreneur identity_document_type'].replace({'passeport': 'PASSEPORT'})

# Assurez-vous de commencer par fusionner les catégories avant de créer la figure
if not category_counts.empty:
    # Fusionner "passeport" et "PASSEPORT"
    category_counts.index = category_counts.index.str.replace("passeport", "PASSEPORT", case=False)

    # Recalculer les totaux pour les catégories combinées
    category_counts = category_counts.groupby(category_counts.index).sum()

    # Créer la figure après avoir fusionné les catégories
    cola1, cola2 = st.columns(2)

    figu = px.pie(
        names=category_counts.index,  # Catégories uniques
        values=category_counts.values,  # Quantités associées à chaque catégorie
        hole=0.3,  # Pour un donut chart (optionnel)
        title="REPARTITION PAR DOCUMENT D'IDENTITE"
    )

    figu.update_traces(textinfo='none', hoverinfo='label+percent')

st.markdown(
    """
    <style>
    .rounded-box {
        border: 2px solid #DCDCDC;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        background-color: #F9F9F9;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }
    .box-title {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="rounded-box">
        <div class="box-title">Section 1: Exemple de Figure</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Ajoutez votre figure Streamlit sous la box
import matplotlib.pyplot as plt

figu, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
st.pyplot(figu)


def create_box(title, content):
    # Ajoutez une box arrondie avec un titre
    st.markdown(
        f"""
        <div class="rounded-box">
            <div class="box-title">{title}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    # Affichez le contenu Streamlit dans la box
    content()
