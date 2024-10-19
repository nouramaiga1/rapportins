import streamlit as st

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



st.markdown("<h1 style='text-align: center;'>RECAPITULATIF DE LA COLLECTE</h1>", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")


col100, col101 = st.columns([2.5 , 1.75])

with col100:
    st.image("https://github.com/nouramaiga1/Photos-rapport/blob/main/identification_.jpeg?raw=true", width=700)

with col101:
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.markdown(
        """
        <h4 style="font-weight: normal;">Le Projet d'enrôlement et d'identification des entreprenants de Côte d'Ivoire a été lancé le 04 septembre 2024, après sa phase pilote à San Pedro. Cette initiative du Ministère du Commerce et de l'Industrie vise à pallier les insuffisances dues à l'absence de base de sondage pour les entreprises du secteur informel et à la mise à jour incomplète des informations sur ces entreprises. Les objectifs principaux de ce projet incluent la création d'une base de données exhaustive et la mise en place de solutions adaptées.</h4>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.write("")
st.write("")
st.markdown( """
    <style>
    .custom-text {
        line-height: 2;  /* Ajustez cette valeur selon vos besoins */
    }
    </style>
    <div class="custom-text">
        <h1>ASPECTS METHODOLOGIQUES ET CONCEPTS CLES</h1>
    """,
    unsafe_allow_html=True
)

# Créer deux colonnes
col31, col32 = st.columns(2)

# Ajouter un style CSS pour définir une hauteur minimale uniforme pour les boxes
st.markdown(
    """
    <style>
    .rounded-box {
        border-radius: 15px;
        border: 1px solid #ccc;
        padding: 15px;
        background-color: #fAfAfA;
        font-family: 'Montserrat', sans-serif;
        margin-bottom: 15px;
        margin-top: 40px;
        height: 400px;  /* Hauteur minimale égale pour toutes les boxes */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        line-height: 1,5;  /* Interligne harmonisé */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Insérer le premier et deuxième paragraphe dans la première colonne
with col31:
    st.markdown(
        """
        <div class="rounded-box">
            <h2>1. Contexte et objectifs globaux</h2>
            <p>Le projet d’identification et d’enrôlement des entreprenants en Côte d'Ivoire s'aligne avec la vision du Président Alassane Ouattara pour une croissance économique plus inclusive.</p>
            <p>Cette opération vise à renforcer l'économie nationale en intégrant les entreprises informelles. Ces entreprises pourront ainsi contribuer aux cotisations sociales (CMU, CNPS), accéder à des financements, des produits d'assurance, des services digitaux, et respecter la réglementation du travail.</p>
        </div>
        <div class="rounded-box">
            <h2>3. Population cible de l’enrôlement</h2>
            <p>La population ciblée par ce projet comprend toute personne exerçant des opérations économiques non enregistrées et non règlementées par l’Etat. Ces activités incluent, par exemple, les artisans, les commerçants de petits magasins, les tailleurs, les coiffeurs, et les travailleurs indépendants dans divers secteurs. Toutefois, ce projet exclut les vendeurs ambulants et toute personne géographiquement instable. L'exclusion de ces groupes vise à concentrer les efforts sur des groupes plus facilement intégrables et stabilisables dans le cadre du projet.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Insérer le troisième et quatrième paragraphe dans la deuxième colonne
with col32:
    st.markdown(
        """
        <div class="rounded-box">
            <h2>2. Objectifs spécifiques de la phase pilote</h2>
            <p>Les objectifs de cette première phase dans la ville de San Pédro ont été :</p>
            <ul>
                <li>La validation des méthodologies et des processus</li>
                <li>L'évaluation des outils et technologies utilisées</li>
                <li>La formation du personnel</li>
                <li>L'identification de problèmes liés à l'enrôlement et des goulots d'étranglement</li>
                <li>La planification des ajustements nécessaires</li>
            </ul>
        </div>
        <div class="rounded-box">
            <h2>4. Procédures de collecte de données</h2>
            <p>Lors de la collecte, l'agent identificateur :</p>
            <ul>
                <li>Se présente sur le lieu d'activité de l'entreprenant</li>
                <li>Collecte les informations de l'entreprenant (KYC) et de l'activité (KYB)</li>
                <li>Renseigne le formulaire</li>
                <li>Collecte les coordonnées GPS de l'activité</li>
                <li>Prend une photo de l'entreprenant et de l'activité</li>
                <li>Délivre une carte entreprenant pour chaque activité</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)

st.write("")
st.write("")
st.markdown("""
    <style>
    .custom-text {
        line-height: 2;  /* Ajustez cette valeur selon vos besoins */
    }
    </style>
    <div class="custom-text">
        <h1>PERFORMANCES A DATE</h1>
    """,
    unsafe_allow_html=True
)


import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

file_path1 = "https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/refs/heads/main/tablastlasst.csv"
data1 = pd.read_csv(file_path1)

df1 = pd.DataFrame(data1)
df1["Dates"] = pd.to_datetime(df1["Dates"])

col20, col21 = st.columns(2)

# Sélecteurs de dates pour le filtre
with col20:
    start_date = st.date_input("Date de début", min_value=df1["Dates"].min(), max_value=df1["Dates"].max(), value=df1["Dates"].min())

with col21:
    end_date = st.date_input("Date de fin", min_value=df1["Dates"].min(), max_value=df1["Dates"].max(), value=df1["Dates"].max())

# Filtrer les données selon la plage de dates sélectionnée
filtered_data = df1[(df1["Dates"] >= pd.to_datetime(start_date)) & (df1["Dates"] <= pd.to_datetime(end_date))]

# Update the figure with the filtered data
fig7 = go.Figure()

# Courbe pour le nombre d'agents
fig7.add_trace(go.Scatter(
    x=filtered_data["Dates"],
    y=filtered_data["Nombre d'agents"],
    mode="lines+markers",
    name="Nombre d'agents",
    line=dict(color='royalblue', width=4)
))

# Courbe pour le nombre de fiches enregistrées
fig7.add_trace(go.Scatter(
    x=filtered_data["Dates"],
    y=filtered_data["Nombre de fiches enregistrées"],
    mode="lines+markers",
    name="Nombre de fiches enregistrées",
    line=dict(color='firebrick', width=4)
))

# Courbe pour les objectifs visés
fig7.add_trace(go.Scatter(
    x=filtered_data["Dates"],
    y=filtered_data["Objectifs visés"],
    mode="lines+markers",
    name="Objectifs visés",
    line=dict(color='orange', width=4)
))

# Ajouter un titre et les labels
fig7.update_layout(
    title="Nombre d'agents et d'activités enregistrées par jour",
    xaxis_title="Dates",
    yaxis_title="Quantité"
)

st.plotly_chart(fig7)

percent_realization = (filtered_data['Nombre de fiches enregistrées'].sum() / filtered_data['Objectifs visés'].sum()) * 100

commentaire = """Du **{}** au **{}**, **325** agents ont réussi à enregistrer au total **{}** fiches sur l'objectif attendu de **{}** pour ce mois de lancement, soit **{:.2f}%** de réalisation.""".format(
start_date, end_date, "{:,.0f}".format(filtered_data['Nombre de fiches enregistrées'].sum()).replace(",", " "), "{:,.0f}".format(filtered_data['Objectifs visés'].sum()).replace(",", " "), percent_realization
    )
st.write(commentaire)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

file_path2 = "https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/refs/heads/main/takeitlastlast.csv"

data1 = pd.read_csv(file_path2)

# Vérifier que les colonnes nécessaires existent dans votre fichier Excel
if 'VILLES' in data1.columns and 'FICHES ENREGISTREES' in data1.columns:
    filtered_data = data1  # Utilisez la DataFrame 'data1' directement ou appliquez un filtre si nécessaire

    custom_order = ['Odienné', 'Man', 'Gagnoa', 'Bouaké', 'Korhogo']

    # Création de la figure
    fig20 = go.Figure()

    filtered_data['VILLES'] = pd.Categorical(filtered_data['VILLES'], categories=custom_order, ordered=True)

    filtered_data = filtered_data.sort_values(by='VILLES')



    # Ajouter les bâtonnets pour les fiches enregistrées
    fig20.add_trace(go.Bar(
        x=filtered_data["VILLES"],  # S'assurer que la colonne 'VILLES' existe
        y=filtered_data["FICHES ENREGISTREES"],  # S'assurer que la colonne 'FICHES ENREGISTREES' existe
        name="Fiches enregistrées",
        marker=dict(color='royalblue'),
        hoverinfo='y'  # Affiche le nombre de fiches enregistrées lors du survol
    ))


    fig20.add_trace(go.Bar(
    x=filtered_data["VILLES"],
    y=filtered_data["OBJECTIFS VISES"],
    name="Objectifs visés",
    marker=dict(color='red'),
    hoverinfo='y'  # Affiche le nombre d'objectifs restants lors du survol
))


    # Ajouter un titre et les labels
    fig20.update_layout(
        title="Avancement des fiches enregistrées par rapport aux objectifs",
        xaxis_title="Villes",
        yaxis_title="Nombre de fiches",
        barmode='group',  # Permet de superposer les barres
        legend_title="Statistiques"
    )



    # Afficher le graphique dans Streamlit
    st.plotly_chart(fig20)
else:
    st.error("Les colonnes 'VILLES' et 'FICHES ENREGISTREES' n'existent pas dans votre fichier Excel.")

import streamlit as st

# Create a string to store the dynamic comment
commento = """Du **04/09/2024** au **30/09/2024**, on a enregistré dans la ville d'**Odienné** un total de **4 450** fiches sur un objectif de **2 413**, soit **184,4%**.<br>
Du **06/09/2024** au **30/09/2024**, on a enregistré dans la ville de **Man** un total de **11 335** fiches sur un objectif de **7 948**, soit **142,6%**.<br>
Du **20/09/2024** au **30/09/2024**, on a enregistré dans la ville de **Gagnoa** un total de **4 060** fiches sur un objectif de **1 825**, soit **222,5%**.<br>
Du **24/09/2024** au **30/09/2024**, on a enregistré dans la ville de **Bouaké** un total de **7 188** fiches sur un objectif de **2 483**, soit **289,5%**.<br>
Du **27/09/2024** au **30/09/2024**, on a enregistré dans la ville de **Korhogo** un tatal de **2 593** fiches sur un objectif de **920**, soit **281,8%**.<br>

"""

# Display the resulting comment string with new lines
st.markdown(commento, unsafe_allow_html=True)


st.write("")
st.write("")

st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)

st.markdown("""
    <style>
    .custom-text {
        line-height: 2;  /* Ajustez cette valeur selon vos besoins */
    }
    </style>
    <div class="custom-text">
        <h1>RECAPITULATIF KYC ET KYB</h1>
    """,
    unsafe_allow_html=True
)


file_path = "https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/refs/heads/main/FINFINLAST.csv"
cols = ["status", "commune", "activity_sector", "CA", "form", "size", "stade_de_maturite", "employees_count", "location_zone", "genre", "tranche_age", "ages"]

@st.cache_data
def load_data(file_path, sheet_name, cols):
    return pd.read_csv(file_path, usecols=cols)


data = pd.read_csv(file_path, usecols=cols)

df = pd.read_csv(file_path, usecols=cols)

remplacements = {
    'très petite': 'Très petite',
    'Très Grande': 'Grande',
    'très Grande': 'Grande',
    'Très PETITE': 'Très petite',
    'très PETITE': 'Très petite',
    'très Petite': 'Très petite',
    'Très Petite': 'Très petite',
    'Très grande' : 'Grande',
    'petite': 'Petite',
    'grande' : 'Grande',
    'moyenne' : 'Moyenne',
    'PETITE' : "Petite",
    'feminin' : 'Feminin',
    'masculin' : 'Masculin'
}

data['size'] = data['size'].replace(remplacements)

data['CA'] = pd.to_numeric(data['CA'].str.replace(',', '').str.replace(' FCFA', ''), errors='coerce')


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

formatted_number = f"{number_of_rows:,.0f}".replace(",", " ")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Nombre d'enregistrements", value=formatted_number)
with col2:
    st.metric(label="Moyenne d'Âge", value=f"{average_age:,.1f} ans")


col3, col4 = st.columns(2)
with col3:
    st.metric(label="Chiffre d'Affaires Global", value=f"{total_ca:,.0f} FCFA")
with col4:
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
        <h4>DIFFERENTS SECTEURS D'ACTIVITE</h4>
    </div>
    """,
    unsafe_allow_html=True
)




# Convertir les données en DataFrame pour faciliter le traitement
sector_counts = category_counts.reset_index()
sector_counts.columns = ['Secteur', 'Nombre']  # Renommer les colonnes pour plus de clarté

# Calculer le total des occurrences pour obtenir les pourcentages
total_entries = sector_counts['Nombre'].sum()

# Ajouter une colonne pour les pourcentages
sector_counts['Pourcentage'] = (sector_counts['Nombre'] / total_entries) * 100

# Trier les secteurs par nombre et sélectionner le Top 5
top_5_sectors = sector_counts.head(5)

# Générer le texte dynamique pour le Top 5 avec les pourcentages
top_5_list = [f"- **{row['Secteur']}** : {row['Pourcentage']:.2f}%" for index, row in top_5_sectors.iterrows()]
top_5_text = "\n".join(top_5_list)  # Joindre les éléments avec des sauts de ligne HTML


# Commentaire final à afficher
commentaire = f"Les 5 principaux secteurs d'activité sont :\n\n{top_5_text}"

col35, col36 = st.columns(2)

fig = px.pie(
    names=category_counts.index,  # Catégories uniques
    values=category_counts.values,  # Quantités associées à chaque catégorie
    hole=0.3,  # Pour un donut chart (optionnel)
    title=f"REPARTITION PAR SECTEURS D'ACTIVITE"
)

fig.update_traces(textinfo='none', hoverinfo='label+percent')
fig.update_layout(showlegend=False)

with col35:
    st.plotly_chart(fig)

with col36:
    st.markdown(
        f"""
        <div class="custom-comment">
            <br><br><br><br>  <!-- Ajoutez autant de <br> que nécessaire pour l'espacement -->
            {commentaire}
        </div>
        """,
        unsafe_allow_html=True
    )







col13, col14 = st.columns(2)


st.markdown('</div>', unsafe_allow_html=True)

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
        <h4>DIFFERENTS STADES DE MATURITE</h4>
    </div>
    """,
    unsafe_allow_html=True
)

category_counts = data_filtree["stade_de_maturite"].value_counts()

col37, col38 = st.columns(2)

with col38:

    fig1 = px.pie(
        names=category_counts.index,  # Catégories uniques
        values=category_counts.values,  # Quantités associées à chaque catégorie
        hole=0.3,  # Pour un donut chart (optionnel)
        title=f"REPARTITION PAR STADE DE MATURITE"
    )

    fig1.update_traces(textinfo='none', hoverinfo='label+percent')

    st.plotly_chart(fig1)

# Placer le commentaire dans la colonne de droite (col37)
with col37:
    # Ajouter des lignes vides
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Générer un commentaire dynamique
    if not category_counts.empty:
        # Calculer le total pour le pourcentage
        total = category_counts.sum()

        # Créer un commentaire dynamique
        comments = ["La répartition en fonction du stade de maturité est la suivante :"]
        for category, count in category_counts.items():
            percentage = (count / total) * 100
            comments.append(f"**{category}** : {percentage:.2f}%")

        # Afficher le commentaire avec un retour à la ligne
        st.markdown("<br>".join(comments), unsafe_allow_html=True)
    else:
        st.write("Aucune donnée disponible pour afficher la répartition des stades de maturité.")


stage_options = data_filtree['stade_de_maturite'].unique()
selected_stage = st.selectbox("Sélectionnez un stade", stage_options)

col39, col40 = st.columns(2)


filtered_df = data_filtree[data_filtree['stade_de_maturite'] == selected_stage]


with col40:

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Générer un commentaire dynamique
    if not filtered_df.empty:
        # Calculer le top 5 des secteurs d'activité
        top_sectors = filtered_df['activity_sector'].value_counts().head(5)

        # Créer un commentaire dynamique
        comments = [f"Le top 5 des activités de **{selected_stage}** est :"]
        for sector, count in top_sectors.items():
            comments.append(f"**{sector}** : {count} ({(count / len(filtered_df)) * 100:.2f}%)")

        # Afficher le commentaire avec un retour à la ligne
        st.markdown("<br>".join(comments), unsafe_allow_html=True)
    else:
        st.write("Aucune donnée disponible pour afficher la répartition des secteurs d'activité.")

figa = px.pie(filtered_df, names='activity_sector', hole=0.4, title=f"REPARTITION DES SECTEURS PAR STADE DE MATURITE")

figa.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')

figa.update_layout(showlegend=False)


with col39:
    st.plotly_chart(figa)

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
        <h4>TYPES D'ACTIVITE</h4>
    </div>
    """,
    unsafe_allow_html=True
)

category_counts = data_filtree["form"].value_counts()

col45, col46 = st.columns([1,2])

fig2 = px.pie(
    names=category_counts.index,  # Catégories uniques
    values=category_counts.values,  # Quantités associées à chaque catégorie
    hole=0.3,  # Pour un donut chart (optionnel)
    title="REPARTITON PAR TYPES D'ACTIVITE"
)

fig2.update_traces(textinfo='none', hoverinfo='label+percent')

with col46:
    st.plotly_chart(fig2)

with col45:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    if not category_counts.empty:
        # Calculer le total pour le pourcentage
        total = category_counts.sum()

        # Créer un commentaire dynamique
        comments = []
        for category, count in category_counts.items():
            percentage = (count / total) * 100
            comments.append(f"Les **{category}s** sont représentés à **{percentage:.2f}%**")

        # Afficher le commentaire avec un retour à la ligne
        commentaire = " et ".join(comments)
        st.markdown(commentaire)
    else:
        st.markdown("Aucune donnée disponible pour afficher la répartition des types d'activité.")

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
        <h4>DIFFERENTES ZONES D'IMPLANTATION</h4>
    </div>
    """,
    unsafe_allow_html=True
)

category_counts = data_filtree["location_zone"].value_counts()

col49, col50 = st.columns(2)

fig10 = px.pie(
    names=category_counts.index,  # Catégories uniques
    values=category_counts.values,  # Quantités associées à chaque catégorie
    hole=0.3,  # Pour un donut chart (optionnel)
    title="REPARTITION PAR ZONES D'IMPLANTATION"
)

fig10.update_traces(textinfo='none', hoverinfo='label+percent')

with col50:
    st.plotly_chart(fig10)

with col49:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    # Générer un commentaire dynamique
    if not category_counts.empty:
        # Calculer le total pour le pourcentage
        total = category_counts.sum()

        # Créer un commentaire dynamique
        comments = ["La répartition en fonction des zones d'implantation est la suivante :"]
        for category, count in category_counts.items():
            percentage = (count / total) * 100
            comments.append(f"**{category}** : {percentage:.2f}%")

        # Afficher le commentaire avec un retour à la ligne
        st.write("<br>".join(comments), unsafe_allow_html=True)
    else:
        st.write("Aucune donnée disponible pour afficher la répartition des zones d'implantation.")

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
        <h4>DIFFERENTES TAILLES D'ACTIVITE</h4>
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
        <h4>REPARTITION PAR GENRE:</h4>
        <h5>Presqu'autant de femmes que d'hommes interrogés</h5>
    </div>
    """,
    unsafe_allow_html=True
)

st.image("https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/refs/heads/main/Affou.jpeg")

data['genre'] = data['genre'].replace({'masculin': 'Masculin', 'feminin': 'Feminin'})

category_counts = data_filtree["genre"].value_counts()

col51, col52 = st.columns(2)

colors = ['blue' if genre == 'Masculin' else 'red' for genre in category_counts.index]


fig4 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    color_discrete_sequence=colors,
    title="REPARTITION PAR GENRE"
)


fig4.update_traces(textinfo='none', hoverinfo='label+percent')

with col52:
    st.plotly_chart(fig4)


with col51:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    # Commentaire dynamique
    commentaire = "La répartition par genre est la suivante :\n"
    for genre, count in category_counts.items():
        pourcentage = (count / category_counts.sum()) * 100
        # Ajouter un séparateur de milliers avec un espace
        commentaire += f"- **{genre}** : {'{:,.0f}'.format(count).replace(',', ' ')} ({pourcentage:.2f}%)\n"

    st.write(commentaire)


size_options = data_filtree['size'].unique()
selected_size = st.selectbox("Sélectionnez une taille", size_options)

col53, col54 = st.columns(2)
colors1 = ['blue' if genre == 'Masculin' else 'red' for genre in category_counts.index]

filtered_df = data_filtree[data_filtree['size'] == selected_size]


# Calculate the percentages
feminin_percentage = (filtered_df[filtered_df['genre'] == 'Feminin'].shape[0] / filtered_df.shape[0]) * 100
masculin_percentage = (filtered_df[filtered_df['genre'] == 'Masculin'].shape[0] / filtered_df.shape[0]) * 100

# Add the annotation
commentaire1 = f"Pour les **{selected_size}s** activités, on a **{feminin_percentage:.2f}% de femmes** et **{masculin_percentage:.2f}% d'hommes**"

fig6 = px.pie(filtered_df, names='genre', hole=0.4, title=f"REPARTITION DES TAILLES D'ACTIVITE PAR GENRE",
              color_discrete_sequence=colors1)

fig6.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')

with col54:
    st.plotly_chart(fig6)

with col53:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write(commentaire1)


# Calculer la répartition en pourcentage pour chaque secteur d'activité
sector_counts = filtered_df['activity_sector'].value_counts().head(5)  # Sélectionner le Top 5
total_activities = filtered_df.shape[0]

# Générer le commentaire pour le Top 5 des secteurs d'activité
commenta = "Le top 5 des {}s activités est:\n".format(selected_size)
for sector, count in sector_counts.items():
    percentage = (count / total_activities) * 100
    commenta += f"- **{sector}** : {percentage:.2f}%\n"


fig1000 = px.pie(
    filtered_df,
    names='activity_sector',
    hole=0.4,
    title=f"Répartition des {selected_size}s activités par secteurs d'activité",
)

fig1000.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')

fig1000.update_layout(showlegend=False)

colx1, colx2 = st.columns(2)
with colx2:
    st.plotly_chart(fig1000)
with colx1:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write(commenta, unsafe_allow_html=True)


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
        <h4>FOCUS PAR GENRE</h4>
    </div>
    """,
    unsafe_allow_html=True
)

genre_options = data_filtree['genre'].unique()
selected_gender = st.selectbox("Sélectionnez un genre", genre_options)


filtered_df = data_filtree[data_filtree['genre'] == selected_gender]

total_ca = filtered_df['CA'].sum()
average_ca = filtered_df['CA'].mean()
average_age = filtered_df['ages'].mean()

st.metric(label="Âge Moyen", value=f"{average_age:.1f} ans")
col5, col6 = st.columns(2)

with col5:
    st.metric(label="Chiffre d'Affaires Total", value=f"{total_ca:,.0f} FCFA")
with col6:
    st.metric(label="Moyenne des Chiffres d'Affaires", value=f"{average_ca:,.0f} FCFA")

fig5 = px.pie(filtered_df, names='activity_sector', hole=0.4, title=f"REPARTITION DES SECTEURS PAR GENRE")

fig5.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')

fig5.update_layout(showlegend=False)


st.plotly_chart(fig5)



# **Ajouter un commentaire dynamique pour le Top 5 des secteurs d'activité avec les pourcentages**

# Compter le nombre d'occurrences par secteur d'activité
sector_counts = filtered_df['activity_sector'].value_counts().reset_index()
sector_counts.columns = ['Secteur', 'Nombre']  # Renommer les colonnes

# Calculer le total des occurrences pour calculer les pourcentages
total_entries = sector_counts['Nombre'].sum()

# Ajouter une colonne 'Pourcentage' au DataFrame
sector_counts['Pourcentage'] = (sector_counts['Nombre'] / total_entries) * 100

# Trier les secteurs et sélectionner le Top 5
top_5_sectors = sector_counts.head(5)

# Générer un commentaire dynamique basé sur le Top 5 avec pourcentages
top_5_list = [f"- **{row['Secteur']}** : {row['Pourcentage']:.2f}%" for index, row in top_5_sectors.iterrows()]
top_5_text = "\n".join(top_5_list)  # Joindre les éléments avec un saut de ligne

# Commentaire final à afficher
commentaire = f"Pour le genre **{selected_gender}**, voici les 5 principaux secteurs d'activité avec leur pourcentage :\n\n{top_5_text}"

# Afficher le commentaire sous forme de markdown
st.markdown(commentaire)







st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

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
        <h4>REPARTITION PAR TRANCHE D'AGE:</h4>
        <h5>Une population d'entreprenants majoritairement jeune avec près de 59% de moins de 40ans</h5>
    </div>
    """,
    unsafe_allow_html=True
)


data['tranche_age'] = data['tranche_age']

category_counts = data_filtree["tranche_age"].value_counts()

col111, col55 = st.columns([1.5 ,2])

with col111:
    st.write("")
    st.image("https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/refs/heads/main/jeune_.jpeg", width=550)


fig11 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    title="REPARTITION PAR TRANCHE D'AGE"
)


fig11.update_traces(textinfo='none', hoverinfo='label+percent')


# Commentaire dynamique
commentaire = "La répartition par tranche d'âge est la suivante :\n"
for tranche_age, count in category_counts.items():
    pourcentage = (count / category_counts.sum()) * 100
    # Ajouter un séparateur de milliers avec un espace
    commentaire += f"- **{pourcentage:.2f}%** des entreprenants interrogés, soit **{'{:,.0f}'.format(count).replace(',', ' ')}** ont **{tranche_age}**.\n"


data_filtree_moins_de_40 = data_filtree[data_filtree['tranche_age'] != 'Plus de 40 ans']

total_caj = data_filtree_moins_de_40['CA'].sum()
average_caj = data_filtree_moins_de_40['CA'].mean()
average_agej = data_filtree_moins_de_40['ages'].mean()

with col55:
    col41, col42 = st.columns(2)
    with col41:
        st.metric(label="Chiffre d'Affaires Total", value=f"{total_caj:,.0f} FCFA")
        st.metric(label="Âge Moyen", value=f"{average_agej:.1f} ans")
    with col42:
        st.metric(label="Moyenne des Chiffres d'Affaires", value=f"{average_ca:,.0f} FCFA")
    st.markdown("---")
    st.plotly_chart(fig11)
    st.write(commentaire)


# Calculer la répartition des secteurs d'activité
category_counts = data_filtree_moins_de_40['activity_sector'].value_counts()

# Créer le pie chart
fig13 = px.pie(
    names=category_counts.index,  # Catégories uniques
    values=category_counts.values,  # Quantités associées à chaque catégorie
    hole=0.3,  # Pour un donut chart (optionnel)
    title="REPARTITION DES SECTEURS D'ACTIVITE DES JEUNES"
)

fig13.update_traces(textinfo='none', hoverinfo='label+percent')
fig13.update_layout(showlegend=False)





col43, col44 = st.columns([1.5 ,2])


# Convertir les données en DataFrame pour faciliter le traitement
sector_counts = category_counts.reset_index()
sector_counts.columns = ['Secteur', 'Nombre']  # Renommer les colonnes pour plus de clarté

# Calculer le total des occurrences pour obtenir les pourcentages
total_entries = sector_counts['Nombre'].sum()

# Ajouter une colonne pour les pourcentages
sector_counts['Pourcentage'] = (sector_counts['Nombre'] / total_entries) * 100

# Trier les secteurs par nombre et sélectionner le Top 5
top_5_sectors = sector_counts.nlargest(5, 'Nombre')  # Utiliser nlargest pour obtenir les 5 premiers

# Générer le texte dynamique pour le Top 5 avec les pourcentages
top_5_list = [f"- **{row['Secteur']}** : {row['Pourcentage']:.2f}%" for index, row in top_5_sectors.iterrows()]
top_5_text = "\n".join(top_5_list)  # Joindre les éléments avec des sauts de ligne HTML

# Commentaire final à afficher
commentaire = f"Voici les 5 principaux secteurs d'activité exercés par les jeunes avec leur pourcentage:\n\n{top_5_text}"

with col43:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.image("https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/refs/heads/main/fillemarchee.png",width=550)

with col44:
    st.write("")
    st.markdown("---")
    st.write("")
    st.plotly_chart(fig13)
    # Ajouter des lignes vides
    st.write("")

    # Commentaire final à afficher
    commentaire = f"Voici les 5 principaux secteurs d'activité exercés par les jeunes avec leur pourcentage:\n\n{top_5_text}"

    # Afficher le commentaire sous forme de markdown
    st.markdown(commentaire)


st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .special-box {
        border-radius: 15px;
        border: 1px solid #ccc;
        padding: 15px;
        background-color: #f5f5f5;
        font-family: 'Montserrat', sans-serif;
        margin-bottom: 15px;
        margin-top: 40px;
    }
    </style>
    <div class="special-box">
        <h4>TOP 1 ACTIVITES : VENTE SUR ETAL</h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.image("https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/ETALL.jpeg")


vente_sur_etal_data = data[data["activity_sector"] == "VENTE SUR ETAL"]

number_of_rows_vente_sur_etal = len(vente_sur_etal_data)

total_ca_vente_sur_etal = vente_sur_etal_data['CA'].sum()

average_ca_vente_sur_etal = vente_sur_etal_data['CA'].mean()

average_age_vente_sur_etal = vente_sur_etal_data['ages'].mean()

formatted_number_vente_sur_etal = f"{number_of_rows_vente_sur_etal:,.0f}".replace(",", " ")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Nombre d'enregistrements (VENTE SUR ETAL)", value=formatted_number_vente_sur_etal)
with col2:
    st.metric(label="Moyenne d'Âge (VENTE SUR ETAL)", value=f"{average_age_vente_sur_etal:,.1f} ans")


col3, col4 = st.columns(2)
with col3:
    st.metric(label="Chiffre d'Affaires Global (VENTE SUR ETAL)", value=f"{total_ca_vente_sur_etal:,.0f} FCFA")
with col4:
    st.metric(label="Moyenne du Chiffre d'Affaires (VENTE SUR ETAL)", value=f"{average_ca_vente_sur_etal:,.0f} FCFA")

category_counts = vente_sur_etal_data["genre"].value_counts()

colors = ['blue' if genre == 'Masculin' else 'red' for genre in category_counts.index]

vente_sur_etal_data = data[data["activity_sector"] == "VENTE SUR ETAL"]

data['genre'] = data['genre'].replace({'masculin': 'Masculin', 'feminin': 'Feminin'})

category_counts = vente_sur_etal_data["genre"].value_counts()

col01, col02 = st.columns(2)

colors = ['blue' if genre == 'Masculin' else 'red' for genre in category_counts.index]

fig001 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    color_discrete_sequence=colors,
    title="REPARTITION PAR GENRE"
)


fig001.update_traces(textinfo='none', hoverinfo='label+percent')

with col02:
    st.plotly_chart(fig001)


with col01:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    # Commentaire dynamique
    commentaire = "La répartition par genre des vendeurs sur étal est la suivante :\n"
    for genre, count in category_counts.items():
        pourcentage = (count / category_counts.sum()) * 100
        # Ajouter un séparateur de milliers avec un espace
        commentaire += f"- **{genre}** : {'{:,.0f}'.format(count).replace(',', ' ')} ({pourcentage:.2f}%)\n"

    st.write(commentaire)


vente_sur_etal_data = data[data["activity_sector"] == "VENTE SUR ETAL"]

category_counts = vente_sur_etal_data["tranche_age"].value_counts()

col60, col61 = st.columns(2)

fig52 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    title="REPARTITION PAR TRANCHE D'AGE"
)


fig52.update_traces(textinfo='none', hoverinfo='label+percent')

with col61:
    st.plotly_chart(fig52)

# Commentaire dynamique
commentaire = "La répartition par tranche d'âge est la suivante :\n"
for tranche_age, count in category_counts.items():
    pourcentage = (count / category_counts.sum()) * 100
    # Ajouter un séparateur de milliers avec un espace
    commentaire += f"- **{pourcentage:.2f}%** des entreprenants interrogés, soit **{'{:,.0f}'.format(count).replace(',', ' ')}** ont **{tranche_age}**.\n"


with col60:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write(commentaire)

vente_sur_etal_data = data[data["activity_sector"] == "VENTE SUR ETAL"]

category_counts = vente_sur_etal_data["stade_de_maturite"].value_counts()

col62, col63 = st.columns(2)

with col63:
    fig1 = px.pie(
        names=category_counts.index,  # Catégories uniques
        values=category_counts.values,  # Quantités associées à chaque catégorie
        hole=0.3,  # Pour un donut chart (optionnel)
        title=f"REPARTITION PAR STADE DE MATURITE"
    )

    fig1.update_traces(textinfo='none', hoverinfo='label+percent')

    st.plotly_chart(fig1)

# Placer le commentaire dans la colonne de gauche (col62)
with col62:
    # Ajouter des lignes vides
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Générer un commentaire dynamique
    if not category_counts.empty:
        # Calculer le total pour le pourcentage
        total = category_counts.sum()

        # Créer un commentaire dynamique
        comments = ["La répartition en fonction du stade de maturité est la suivante :"]
        for category, count in category_counts.items():
            percentage = (count / total) * 100
            comments.append(f"**{category}** : {percentage:.2f}%")

        # Afficher le commentaire avec un retour à la ligne
        st.markdown("<br>".join(comments), unsafe_allow_html=True)
    else:
        st.write("Aucune donnée disponible pour afficher la répartition des stades de maturité.")

st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .special-box {
        border-radius: 15px;
        border: 1px solid #ccc;
        padding: 15px;
        background-color: #f5f5f5;
        font-family: 'Montserrat', sans-serif;
        margin-bottom: 15px;
        margin-top: 40px;
    }
    </style>
    <div class="special-box">
        <h4>TOP 2 ACTIVITES : VETEMENTS/CHAUSSURES/ACCESSOIRES DE MODE</h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.image("https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/habitss.png")
st.write("")
st.write("")


vetements_data = data[data["activity_sector"] == "VETEMENTS/CHAUSSURES/ACCESSOIRE DE MODE"]

number_of_rows_vetements = len(vetements_data)

total_ca_vetements = vetements_data['CA'].sum()

average_ca_vetements = vetements_data['CA'].mean()

average_age_vetements = vetements_data['ages'].mean()

formatted_number_vetements = f"{number_of_rows_vetements:,.0f}".replace(",", " ")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Nombre d'enregistrements (VETEMENTS/CHAUSSURES/ACCESSOIRE DE MODE)", value=formatted_number_vetements)
with col2:
    st.metric(label="Moyenne d'Âge (VETEMENTS/CHAUSSURES/ACCESSOIRE DE MODE)", value=f"{average_age_vetements:,.1f} ans")


col3, col4 = st.columns(2)
with col3:
    st.metric(label="Chiffre d'Affaires Global (VETEMENTS/CHAUSSURES/ACCESSOIRE DE MODE)", value=f"{total_ca_vetements:,.0f} FCFA")
with col4:
    st.metric(label="Moyenne du Chiffre d'Affaires (VETEMENTS/CHAUSSURES/ACCESSOIRE DE MODE)", value=f"{average_ca_vetements:,.0f} FCFA")


vetements_data = data[data["activity_sector"] == "VETEMENTS/CHAUSSURES/ACCESSOIRE DE MODE"]

data['genre'] = data['genre'].replace({'masculin': 'Masculin', 'feminin': 'Feminin'})

category_counts = vetements_data["genre"].value_counts()

col03, col04 = st.columns(2)

colors = ['blue' if genre == 'Masculin' else 'red' for genre in category_counts.index]

fig002 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    color_discrete_sequence=colors,
    title="REPARTITION PAR GENRE"
)


fig002.update_traces(textinfo='none', hoverinfo='label+percent')

with col04:
    st.plotly_chart(fig002)


with col03:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    # Commentaire dynamique
    commentaire = "La répartition par genre des vendeurs de vêtements/chaussures/accessoires de mode est la suivante :\n"
    for genre, count in category_counts.items():
        pourcentage = (count / category_counts.sum()) * 100
        # Ajouter un séparateur de milliers avec un espace
        commentaire += f"- **{genre}** : {'{:,.0f}'.format(count).replace(',', ' ')} ({pourcentage:.2f}%)\n"

    st.write(commentaire)


vetements_data = data[data["activity_sector"] == "VETEMENTS/CHAUSSURES/ACCESSOIRE DE MODE"]

category_counts = vetements_data["tranche_age"].value_counts()

col60, col61 = st.columns(2)

fig70 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    title="REPARTITION PAR TRANCHE D'AGE"
)


fig70.update_traces(textinfo='none', hoverinfo='label+percent')

with col61:
    st.plotly_chart(fig70)

# Commentaire dynamique
commentaire = "La répartition par tranche d'âge est la suivante :\n"
for tranche_age, count in category_counts.items():
    pourcentage = (count / category_counts.sum()) * 100
    # Ajouter un séparateur de milliers avec un espace
    commentaire += f"- **{pourcentage:.2f}%** des entreprenants interrogés, soit **{'{:,.0f}'.format(count).replace(',', ' ')}** ont **{tranche_age}**.\n"


with col60:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write(commentaire)


vetements_data = data[data["activity_sector"] == "VETEMENTS/CHAUSSURES/ACCESSOIRE DE MODE"]

category_counts = vetements_data["stade_de_maturite"].value_counts()

col62, col63 = st.columns(2)

with col63:
    fig71 = px.pie(
        names=category_counts.index,  # Catégories uniques
        values=category_counts.values,  # Quantités associées à chaque catégorie
        hole=0.3,  # Pour un donut chart (optionnel)
        title=f"REPARTITION PAR STADE DE MATURITE"
    )

    fig71.update_traces(textinfo='none', hoverinfo='label+percent')

    st.plotly_chart(fig71)

# Placer le commentaire dans la colonne de gauche (col62)
with col62:
    # Ajouter des lignes vides
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Générer un commentaire dynamique
    if not category_counts.empty:
        # Calculer le total pour le pourcentage
        total = category_counts.sum()

        # Créer un commentaire dynamique
        comments = ["La répartition en fonction du stade de maturité est la suivante :"]
        for category, count in category_counts.items():
            percentage = (count / total) * 100
            comments.append(f"**{category}** : {percentage:.2f}%")

        # Afficher le commentaire avec un retour à la ligne
        st.markdown("<br>".join(comments), unsafe_allow_html=True)
    else:
        st.write("Aucune donnée disponible pour afficher la répartition des stades de maturité.")



st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .special-box {
        border-radius: 15px;
        border: 1px solid #ccc;
        padding: 15px;
        background-color: #f5f5f5;
        font-family: 'Montserrat', sans-serif;
        margin-bottom: 15px;
        margin-top: 40px;
    }
    </style>
    <div class="special-box">
        <h4>TOP 3 ACTIVITES : RESTAURANTS/MAQUIS/CAVES/BUVETTES</h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.image("https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/NOURRITURE.jpeg")


produits_agricoles_data = data[data["activity_sector"] == "RESTAURANT/MAQUIS/CAVE/BUVETTE"]

number_of_rows_produits_agricoles = len(produits_agricoles_data)

total_ca_produits_agricoles = produits_agricoles_data['CA'].sum()

average_ca_produits_agricoles = produits_agricoles_data['CA'].mean()

average_age_produits_agricoles = produits_agricoles_data['ages'].mean()

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Nombre d'enregistrements (RESTAURANT/MAQUIS/CAVE/BUVETTE)", value=number_of_rows_produits_agricoles)
with col2:
    st.metric(label="Moyenne d'Âge (RESTAURANT/MAQUIS/CAVE/BUVETTE)", value=f"{average_age_produits_agricoles:,.1f} ans")


col3, col4 = st.columns(2)
with col3:
    st.metric(label="Chiffre d'Affaires Global (RESTAURANT/MAQUIS/CAVE/BUVETTE)", value=f"{total_ca_produits_agricoles:,.0f} FCFA")
with col4:
    st.metric(label="Moyenne du Chiffre d'Affaires (RESTAURANT/MAQUIS/CAVE/BUVETTE)", value=f"{average_ca_produits_agricoles:,.0f} FCFA")

produits_agricoles_data = data[data["activity_sector"] == "RESTAURANT/MAQUIS/CAVE/BUVETTE"]

data['genre'] = data['genre'].replace({'masculin': 'Masculin', 'feminin': 'Feminin'})

category_counts = produits_agricoles_data["genre"].value_counts()

col05, col06 = st.columns(2)

colors = ['blue' if genre == 'Masculin' else 'red' for genre in category_counts.index]

fig003 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    color_discrete_sequence=colors,
    title="REPARTITION PAR GENRE"
)


fig003.update_traces(textinfo='none', hoverinfo='label+percent')

with col06:
    st.plotly_chart(fig003)


with col05:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    # Commentaire dynamique
    commentaire = "La répartition par genre des restaurateurs est la suivante :\n"
    for genre, count in category_counts.items():
        pourcentage = (count / category_counts.sum()) * 100
        # Ajouter un séparateur de milliers avec un espace
        commentaire += f"- **{genre}** : {'{:,.0f}'.format(count).replace(',', ' ')} ({pourcentage:.2f}%)\n"

    st.write(commentaire)



produits_agricoles_data = data[data["activity_sector"] == "RESTAURANT/MAQUIS/CAVE/BUVETTE"]

category_counts = produits_agricoles_data["tranche_age"].value_counts()

col70, col71 = st.columns(2)

fig72 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    title="REPARTITION PAR TRANCHE D'AGE"
)


fig72.update_traces(textinfo='none', hoverinfo='label+percent')

with col71:
    st.plotly_chart(fig72)

# Commentaire dynamique
commentaire = "La répartition par tranche d'âge est la suivante :\n"
for tranche_age, count in category_counts.items():
    pourcentage = (count / category_counts.sum()) * 100
    commentaire += f"- **{pourcentage:.2f}%** des entreprenants interrogés, soit **{count}** ont **{tranche_age}**.\n"

with col70:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write(commentaire)


produits_agricoles_data = data[data["activity_sector"] == "RESTAURANT/MAQUIS/CAVE/BUVETTE"]

category_counts = produits_agricoles_data["stade_de_maturite"].value_counts()

col72, col73 = st.columns(2)

with col73:
    fig73 = px.pie(
        names=category_counts.index,  # Catégories uniques
        values=category_counts.values,  # Quantités associées à chaque catégorie
        hole=0.3,  # Pour un donut chart (optionnel)
        title=f"REPARTITION PAR STADE DE MATURITE"
    )

    fig73.update_traces(textinfo='none', hoverinfo='label+percent')

    st.plotly_chart(fig73)

# Placer le commentaire dans la colonne de gauche (col72)
with col72:
    # Ajouter des lignes vides
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Générer un commentaire dynamique
    if not category_counts.empty:
        # Calculer le total pour le pourcentage
        total = category_counts.sum()

        # Créer un commentaire dynamique
        comments = ["La répartition en fonction du stade de maturité est la suivante :"]
        for category, count in category_counts.items():
            percentage = (count / total) * 100
            comments.append(f"**{category}** : {percentage:.2f}%")

        # Afficher le commentaire avec un retour à la ligne
        st.markdown("<br>".join(comments), unsafe_allow_html=True)
    else:
        st.write("Aucune donnée disponible pour afficher la répartition des stades de maturité.")


st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .special-box {
        border-radius: 15px;
        border: 1px solid #ccc;
        padding: 15px;
        background-color: #f5f5f5;
        font-family: 'Montserrat', sans-serif;
        margin-bottom: 15px;
        margin-top: 40px;
    }
    </style>
    <div class="special-box">
        <h4>MAP DES ACTIVITES</h4>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <iframe src="https://mafa-mapbox-v2.poc-demo.com/dashboard" width="100%" height="600"></iframe>
""", unsafe_allow_html=True)
