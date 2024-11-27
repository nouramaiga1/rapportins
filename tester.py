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


# CSS pour la gestion responsive des images et colonnes
st.markdown("""
    <style>
    /* Style pour le conteneur d'image responsive */
    .responsive-image-container {
        width: 100%;
        max-width: 700px;
        margin: 0 auto;
    }

    /* Style pour l'image responsive */
    .responsive-image-container img {
        width: 100%;
        height: auto;
        display: block;
    }

    /* Ajustements pour mobile */
    @media (max-width: 768px) {
        .responsive-image-container {
            max-width: 100%;
            padding: 0 10px;
        }

        /* Ajuster les colonnes sur mobile */
        .element-container {
            width: 100% !important;
        }

        /* Ajuster les marges sur mobile */
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(
     """
    <style>
    .responsive-image-0{
        width: 100%; /* Ajuste à la largeur du conteneur */
        height: 1000px; /* Hauteur fixe */
        object-fit: cover; /* Remplit la hauteur spécifiée */
    }
        .responsive-image-1 {
        width: 100%;
        height: 500px;
        object-fit: cover;
    }
        .responsive-image-2 {
        width: 100%;
        height: 1000px;
        object-fit: cover;
    }
        .responsive-image-3 {
        width: 100%;
        height: 600px;
        object-fit: cover;
    }
        .responsive-image-4 {
        width: 100%;
        height: 800px;
        object-fit: cover;
    }
        .responsive-image-5 {
        width: 100%;
        height: 1300px;
        object-fit: cover;
    }
        .responsive-image-6 {
        width: 100%;
        height: 600px;
        object-fit: cover;
    }
        .responsive-image-7 {
        width: 100%;
        height: 1000px;
        object-fit: cover;
    }    .responsive-image-8 {
        width: 100%;
        height: 1000px;
        object-fit: cover;
    }
        .responsive-image-9 {
        width: 100%;
        height: 500px;
        object-fit: cover;
    }
        .responsive-image-10 {
        width: 100%;
        height: 500px;
        object-fit: cover;
    }
        .responsive-image-11 {
        width: 100%;
        height: 500px;
        object-fit: cover;
    }
        .responsive-image-12 {
        width: 100%;
        height: 1000px;
        object-fit: cover;
    }
        .responsive-image-13 {
        width: 100%;
        height: 1000px;
        object-fit: cover;
    }
        .responsive-image-14 {
        width: 100%;
        height: 500px;
        object-fit: cover;
    }
    </style>


    """,
            unsafe_allow_html=True
        )

# Création des colonnes avec ratio responsive
col100, col101 = st.columns([2.5, 1.75])

with col100:
    # Utilisation de markdown pour l'image responsive
    st.markdown("""
        <div class="responsive-image-container">
            <img src="https://github.com/nouramaiga1/Photos-rapport/blob/main/identification_.jpeg?raw=true"
                 alt="Identification">
        </div>
    """, unsafe_allow_html=True)

with col101:
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
    texte1 = st.container(border=True)
    with texte1:
        st.write(
            """
            ### 1. Contexte et objectifs globaux

            Le projet d’identification et d’enrôlement des entreprenants en Côte d'Ivoire s'aligne avec la vision du Président Alassane Ouattara pour une croissance économique plus inclusive.

            Cette opération vise à renforcer l'économie nationale en intégrant les entreprises informelles. Ces entreprises pourront ainsi contribuer aux cotisations sociales (CMU, CNPS), accéder à des financements, des produits d'assurance, des services digitaux, et respecter la réglementation du travail.

            """
        )
        st.write("")

    texte3 = st.container(border=True)
    with texte3:
        st.write(
            """
            ### 3. Population cible de l’enrôlement
            La population ciblée par ce projet comprend toute personne exerçant des opérations économiques non enregistrées et non règlementées par l’Etat. Ces activités incluent, par exemple, les artisans, les commerçants de petits magasins, les tailleurs, les coiffeurs, et les travailleurs indépendants dans divers secteurs. Toutefois, ce projet exclut les vendeurs ambulants et toute personne géographiquement instable. L'exclusion de ces groupes vise à concentrer les efforts sur des groupes plus facilement intégrables et stabilisables dans le cadre du projet.
            """
        )


# Insérer le troisième et quatrième paragraphe dans la deuxième colonne
with col32:
    texte2 = st.container(border=True)
    with texte2:
        st.write(
            """
            ### 2. Objectifs spécifiques de la phase pilote
            Les objectifs de cette première phase dans la ville de San Pédro ont été :
            - La validation des méthodologies et des processus
            - L'évaluation des outils et technologies utilisées
            - La formation du personnel
            - L'identification de problèmes liés à l'enrôlement et des goulots d'étranglement
            - La planification des ajustements nécessaires
            """
        )

    texte4 = st.container(border=True)
    with texte4:
        st.write(
            """
            ### 4. Procédures de collecte de données
            Lors de la collecte, l'agent identificateur :
            - Se présente sur le lieu d'activité de l'entreprenant
            - Collecte les informations de l'entreprenant (KYC) et de l'activité
            - Renseigne le formulaire
            - Collecte les coordonnées GPS de l'activité
            - Prend une photo de l'entreprenant et de l'activité
            - Délivre une carte entreprenant pour chaque activité
            """
        )


st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)




import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go




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


file_path = "https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/refs/heads/main/RECAPOCTLASTLAST.csv"
cols = ["commune", "activity_sector", "CA", "form", "size", "stade_de_maturite", "employees_count", "genre", "tranche_age", "ages","Entrepreneur identity_document_type","is_cnps_declared","terminal_type","type etal","type vivrier"]

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

st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)

#Mon container
st.markdown(
    """
    <style>
    .thick-border-container {
        border: 5px solid #4CAF50; /* Thicker border */
        border-radius: 15px; /* Optional: rounded corners */
        padding: 20px; /* Padding inside the container */
        margin: 10px 0; /* Space outside the container */
        background-color: #F2F3F4; /* Optional: background color */
    }
    </style>
    """,
    unsafe_allow_html=True
)



habitudes = st.container()

with habitudes:
    st.markdown("<h2>Les habitudes de nos entreprenants</h2>", unsafe_allow_html=True)

    category_counts = data_filtree["Entrepreneur identity_document_type"].value_counts()

    data['Entrepreneur identity_document_type'] = data['Entrepreneur identity_document_type'].replace({'passeport': 'PASSEPORT'})

    # Assurez-vous de commencer par fusionner les catégories avant de créer la figure
    if not category_counts.empty:
        # Fusionner "passeport" et "PASSEPORT"
        category_counts.index = category_counts.index.str.replace("passeport", "PASSEPORT", case=False)

        # Recalculer les totaux pour les catégories combinées
        category_counts = category_counts.groupby(category_counts.index).sum()

        # Créer la figure après avoir fusionné les catégories
        cola1, cola2,bah = st.columns(3)


        figu = px.pie(
            names=category_counts.index,  # Catégories uniques
            values=category_counts.values,  # Quantités associées à chaque catégorie
            hole=0.3,  # Pour un donut chart (optionnel)
            title="REPARTITION PAR DOCUMENT D'IDENTITE"
        )

        category_counts = data_filtree["is_cnps_declared"].value_counts()

        ah = px.pie(
        names=category_counts.index,  # Catégories uniques
        values=category_counts.values,  # Quantités associées à chaque catégorie
        hole=0.3,  # Pour un donut chart (optionnel)
        title="STATUT CNPS"
    )
        ah.update_traces(textinfo='none', hoverinfo='label+percent')

        category_counts = data_filtree["terminal_type"].value_counts()
        figcnps = px.pie(
        names=category_counts.index,  # Catégories uniques
        values=category_counts.values,  # Quantités associées à chaque catégorie
        hole=0.3,  # Pour un donut chart (optionnel)
        title="TYPE DE TELEPHONE PORTABLE"
    )
        figu.update_traces(textinfo='none', hoverinfo='label+value')



        with cola2:
            figudisp = st.container(border=True)
            with figudisp:
                st.plotly_chart(figu)
            ahdisp = st.container(border=True)
            with ahdisp:
                st.plotly_chart(ah)


        with cola1:
            st.markdown(
            """
            <div>
                <img src="https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/femmesouriante.jpeg" class="responsive-image-0">
            </div>
            """,
            unsafe_allow_html=True
        )



        with bah:
            figcnpsdisp = st.container(border=True)
            with figcnpsdisp:
                st.plotly_chart(figcnps)


            # Calculer le total pour les pourcentages
            total = category_counts.sum()

            st.write("La grande partie des entreprenants n'ont aucun document d'identité lors de l'enrôlement.")
            st.write("Les entreprenants ont tendance à ne pas déclarer leurs activités à la CNPS.")
            st.write("Ils sont familiers des technologies mobiles, la majorité possédant des smartphones.")


    else:
        st.markdown("Aucune donnée disponible pour afficher la répartition des types d'activité.")

    st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)



secteurs = st.container()

with secteurs :

    st.markdown("<h2>Une multitude de secteurs d'activité</h2>", unsafe_allow_html=True)

    # Use Streamlit's Native `st.container`

    var1, var2, var3 = st.columns([1.5, 1, 1])

    with var2:
            category_counts = data_filtree["activity_sector"].value_counts()
            # Generate the Chart
            figure = px.pie(
            names=category_counts.index,
            values=category_counts.values,
            hole=0.3,
            title="REPARTITION PAR SECTEUR D'ACTIVITE"
            )
            figure.update_traces(textinfo='none', hoverinfo='label+percent')
            figure.update_layout(showlegend=False)
            vari2 = st.container(border=True)
            with vari2:
                st.plotly_chart(figure)


    with var1:
        vari1 = st.container(border=True)
        with vari1:
            # Calculer le top 5 des secteurs d'activité
            top5_sectors = category_counts.nlargest(5)

            # Calculer le nombre d'employés moyen pour chaque secteur du top 5
            average_employees_per_sector = {
                sector: data_filtree[data_filtree['activity_sector'] == sector]['employees_count'].mean()
                for sector in top5_sectors.index
            }

            # Calculer le total pour obtenir les pourcentages
            total_entries = category_counts.sum()
            top5_percentages = (top5_sectors / total_entries) * 100

            # Créer le texte dynamique pour le top 5
            top5_list = [
                f"- **{sector}** : {percentage:.2f}%"
                for sector, percentage in zip(top5_sectors.index, top5_percentages)
            ]
            top5_text = "\n".join(top5_list)  # Joindre les éléments avec des sauts de ligne HTML

            # Commentaire final
            commentaire = f"Les principaux secteurs d'activité sont :\n\n{top5_text}\n\n"

            # Espace avant le nombre moyen d'employés
            st.write("\n" * 3)  # Ajoute 3 lignes vides


            st.write("")
            st.markdown(commentaire)
            st.write("")

            # Afficher le nombre moyen d'employés pour les secteurs du top 5
            average_employees_text = "\n".join(
            [f"- **{sector}** : {average_employees_per_sector[sector]:.2f} employés" for sector in top5_sectors.index]
            )
            st.markdown(f"Le nombre moyen d'employés pour ces secteurs est :\n{average_employees_text}")


    with var3:
         st.markdown(
            """
            <div>
                <img src="https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/marchegeneral.png" class="responsive-image-1">
            </div>
            """,
            unsafe_allow_html=True
        )






    st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)


    st.markdown("<h2>Des activités pour la plupart matures</h2>", unsafe_allow_html=True)

    category_counts = data_filtree["stade_de_maturite"].value_counts()

    col37, col38 = st.columns([1, 2])

    with col37:
        st.markdown(
            """
            <div>
                <img src="https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/mcher.jpeg" class="responsive-image-2">
            </div>
            """,
            unsafe_allow_html=True
        )


    with col38:
        kol1, kol2 = st.columns(2)
        with kol1:
            fig1disp =st.container(border=True)
            fig1 = px.pie(
            names=category_counts.index,  # Catégories uniques
            values=category_counts.values,  # Quantités associées à chaque catégorie
            hole=0.3,  # Pour un donut chart (optionnel)
            title=f"REPARTITION PAR STADE DE MATURITE"
        )
            fig1.update_layout(showlegend=False, width=450, height=450)
            fig1.update_traces(textinfo='none', hoverinfo='label+percent')
            with fig1disp:
                st.plotly_chart(fig1)

        with kol2:
            kol2disp = st.container(border=True)
            with kol2disp:
                st.write("Le pourcentage élevé d'activités matures montre qu'une part importante des entreprises a su perdurer, ce qui est souvent le signe d'une certaine résilience et d'une adaptabilité aux conditions du marché.")
                st.write("Les activités établies entre 2 et 5 ans représentent les entreprises qui ont dépassé les premières phases critiques de démarrage et qui sont en phase de consolidation. Cela indique une bonne stabilité pour les entreprises qui réussissent à passer le cap des deux premières années.")
                st.write("La présence des activités récentes indique un certain dynamisme entrepreneurial avec un nombre significatif de nouvelles entreprises. Il pourrait aussi refléter un environnement économique favorable à la création de nouvelles activités.")


        separ1, separ2, separ3 = st.columns(3)

        with separ1:
            figadisp = st.container(border=True)
            filtered_df = df[df["stade_de_maturite"] == "Moins de 2 ans"]
            figa = px.pie(filtered_df, names='activity_sector', hole=0.4, title=f"MOINS DE DEUX ANS")
            figa.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')
            figa.update_layout(showlegend=False, width=400, height=400)
            with figadisp:
                st.plotly_chart(figa)


        with separ2:
            figentredisp = st.container(border=True)
            filtered_df = df[df["stade_de_maturite"] == "Entre 2 et 5 ans"]
            figentre = px.pie(filtered_df, names='activity_sector', hole=0.4, title=f"ENTRE DEUX ET CINQ ANS")
            figentre.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')
            figentre.update_layout(showlegend=False, width=400, height=400)
            with figentredisp:
                st.plotly_chart(figentre)


        with separ3:
            figplusdisp = st.container(border=True)
            filtered_df = df[df["stade_de_maturite"] == "Plus de 5 ans"]
            figplus = px.pie(filtered_df, names='activity_sector', hole=0.4, title=f"PLUS DE CINQ ANS")
            figplus.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')
            figplus.update_layout(showlegend=False, width=400, height=400)
            with figplusdisp :
                st.plotly_chart(figplus)


st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)



st.markdown("<h2>Une majorité de commerces</h2>", unsafe_allow_html=True)


category_counts = data_filtree["form"].value_counts()

col45, col46 = st.columns(2)

fig2 = px.pie(
    names=category_counts.index,  # Catégories uniques
    values=category_counts.values,  # Quantités associées à chaque catégorie
    hole=0.3,  # Pour un donut chart (optionnel)
    title="REPARTITON PAR TYPE D'ACTIVITE"
)

fig2.update_traces(textinfo='none', hoverinfo='label+percent')

with col46:
    fig2disp = st.container(border=True)
    with fig2disp:
        st.plotly_chart(fig2)
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



with col45:

    st.markdown(
        """
        <div>
            <img src="https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/yaounde.jpeg" class="responsive-image-3">
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)




st.markdown("<h2>Une majorité de très petites activités enregistrées</h2>", unsafe_allow_html=True)



category_counts = data_filtree["size"].value_counts()

col47, col48 = st.columns([1,2])

with col47:
        st.markdown(
            """
            <div>
                <img src="https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/brode.png" class="responsive-image-14">
            </div>
            """,
            unsafe_allow_html=True
        )

fig3 = px.pie(
    names=category_counts.index,  # Catégories uniques
    values=category_counts.values,  # Quantités associées à chaque catégorie
    hole=0.3,  # Pour un doughnut chart
    title="REPARTITION PAR TAILLE D'ACTIVITE"
)
fig3.update_layout(showlegend=False, width=450, height=450)
fig3.update_traces(textinfo='none', hoverinfo='label+percent')


with col48:
    kol8, kol9 = st.columns(2)
    with kol8:
        fig3disp = st.container(border=True)
        with fig3disp:
           st.plotly_chart(fig3)

    with kol9:
            definitionsdisp = st.container(border=True)
    with definitionsdisp:
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
        st.write("")
        st.write("")
        st.write("")
        st.write(definitions)
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        # Calculer la répartition en pourcentage pour chaque secteur d'activité

        filtered_df = df[df["size"] == "Très petite"]
        sector_counts = filtered_df['activity_sector'].value_counts().head(5)  # Sélectionner le Top 5
        total_activities = filtered_df.shape[0]
        fig1000 = px.pie(
            filtered_df,
            names='activity_sector',
            hole=0.4,
            title=f"Très petites activités",
        )
        fig1000.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')
        fig1000.update_layout(showlegend=False, width=400, height=400)

        filtered_df = df[df["size"] == "Petite"]
        sector_counts = filtered_df['activity_sector'].value_counts().head(5)  # Sélectionner le Top 5
        total_activities = filtered_df.shape[0]
        fig1001 = px.pie(
            filtered_df,
            names='activity_sector',
            hole=0.4,
            title=f"Petites activités",
        )
        fig1001.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')
        fig1001.update_layout(showlegend=False, width=400, height=400)

        filtered_df = df[df["size"] == "Moyenne"]
        sector_counts = filtered_df['activity_sector'].value_counts().head(5)  # Sélectionner le Top 5
        total_activities = filtered_df.shape[0]
        fig1002 = px.pie(
            filtered_df,
            names='activity_sector',
            hole=0.4,
            title=f"Activités moyennes",
        )
        fig1002.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')
        fig1002.update_layout(showlegend=False, width=400, height=400)

        filtered_df = df[df["size"] == "Grande"]
        sector_counts = filtered_df['activity_sector'].value_counts().head(5)  # Sélectionner le Top 5
        total_activities = filtered_df.shape[0]
        fig1003 = px.pie(
            filtered_df,
            names='activity_sector',
            hole=0.4,
            title=f"Grandes activités",
        )
        fig1003.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')
        fig1003.update_layout(showlegend=False, width=400, height=400)

kol10, kol11 = st.columns([1,2])
with kol11:
    figuresdisp = st.container(border=True)
    with figuresdisp:
        colx1, colx2 = st.columns(2)
        with colx1:
            st.plotly_chart(fig1000)
            st.plotly_chart(fig1002)

        with colx2:
            st.plotly_chart(fig1001)
            st.plotly_chart(fig1003)

with kol10:
         st.markdown(
            """
            <div>
                <img src="https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/marchegeneral.png" class="responsive-image-4">
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)


st.markdown("<h2>Plus de femmes que d'hommes interrogés</h2>", unsafe_allow_html=True)

kol12, kol13 = st.columns([1,2])


data['genre'] = data['genre'].replace({'masculin': 'Masculin', 'feminin': 'Feminin'})

category_counts = data_filtree["genre"].value_counts()


col51, col52, kol14 = st.columns(3)

colors = ['blue' if genre == 'Masculin' else 'red' for genre in category_counts.index]


fig4 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    color_discrete_sequence=colors,
    title="REPARTITION PAR GENRE"
)
fig4.update_traces(textinfo='none', hoverinfo='label+percent')
fig4.update_layout(showlegend=False, width=400, height=400)




df["genre"] = df["genre"].str.capitalize()


colors1 = ['blue' if genre == 'Masculin' else 'red' for genre in category_counts.index]

filtered_df = df[df['size'] == "Très petite"]


# Calculate the percentages
feminin_percentage = (filtered_df[filtered_df['genre'] == 'Feminin'].shape[0] / filtered_df.shape[0]) * 100
masculin_percentage = (filtered_df[filtered_df['genre'] == 'Masculin'].shape[0] / filtered_df.shape[0]) * 100

# Add the annotation

fig6 = px.pie(filtered_df, names='genre', hole=0.4, title=f"TRES PETITES ACTIVITES",
              color_discrete_sequence=colors1)
fig6.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')
fig6.update_layout(showlegend=False, width=400, height=400)


filtered_df = df[df['size'] == "Petite"]

petites = px.pie(filtered_df, names='genre', hole=0.4, title=f"PETITES ACTIVITES",
              color_discrete_sequence=colors1)
petites.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')
petites.update_layout(showlegend=False, width=400, height=400)

filtered_df = df[df['size'] == "Moyenne"]

moyennes = px.pie(filtered_df, names='genre', hole=0.4, title="ACTIVITES MOYENNES",
              color_discrete_sequence=colors1)
moyennes.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')
moyennes.update_layout(showlegend=False, width=400, height=400)
filtered_df = df[df['size'] == "Grande"]

grandes = px.pie(filtered_df, names='genre', hole=0.4, title="GRANDES ACTIVITES",
              color_discrete_sequence=colors1)
grandes.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')
grandes.update_layout(showlegend=False, width=400, height=400)

with kol14:
    fig4disp = st.container(border=True)
    with fig4disp:
       st.plotly_chart(fig4)
    petitesdisp = st.container(border=True)
    with petitesdisp:
        st.plotly_chart(petites)
    grandesdisp = st.container(border=True)
    with grandesdisp:
        st.plotly_chart(grandes)



with col51:
       st.markdown(
            """
            <div>
                <img src="https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/Affou.jpeg" class="responsive-image-5">
            </div>
            """,
            unsafe_allow_html=True
        )

with col52:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("Les femmes sont à la tête des très petites et petites activités.")
    st.write("En revanche, lorsqu'il est question des activtés de tailles moyenne et grande, les hommes sont mieux représentés.")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    fig6disp = st.container(border=True)
    with fig6disp:
        st.plotly_chart(fig6)

    moyennesdisp = st.container(border=True)
    with moyennesdisp:
            st.plotly_chart(moyennes)







st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)

st.markdown("<h2>Focus par genre</h2>", unsafe_allow_html=True)


genre_options = data_filtree['genre'].unique()
selected_gender = st.selectbox("Sélectionnez un genre", genre_options)


filtered_df = data_filtree[data_filtree['genre'] == selected_gender]

total_ca = filtered_df['CA'].sum()
average_ca = filtered_df['CA'].mean()
average_age = filtered_df['ages'].mean()
average_employee = filtered_df['employees_count'].mean()

fig5 = px.pie(filtered_df, names='activity_sector', hole=0.4, title=f"REPARTITION DES SECTEURS PAR GENRE")

fig5.update_traces(textinfo='none', hovertemplate='%{label}: %{value}<extra></extra>')

fig5.update_layout(showlegend=False, width=400, height=400)




colonna, colie, kol17 = st.columns(3)

with colonna:
    st.markdown(
        """
        <div>
            <img src="https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/fillemarchee.png" class="responsive-image-6">
        </div>
        """,
        unsafe_allow_html=True
    )


with colie:
    st.metric(label="Âge Moyen", value=f"{average_age:.1f} ans")
    st.metric(label="Chiffre d'Affaires Total", value=f"{total_ca:,.0f} FCFA")
    fig5disp = st.container(border=True)
    with fig5disp:
        st.plotly_chart(fig5)


with kol17:
    st.metric(label="Nombre d'enployés moyen", value=f"{average_employee:,.1f}")
    st.metric(label="Moyenne des Chiffres d'Affaires", value=f"{average_ca:,.0f} FCFA")
    commentdisp = st.container(border=True)
    with commentdisp:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
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
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")















st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)


st.markdown("<h2>Des entreprenants jeunes</h2>", unsafe_allow_html=True)


data['tranche_age'] = data['tranche_age']

category_counts = data_filtree["tranche_age"].value_counts()

col111, col55, kol18 = st.columns(3)

with col111:
    st.markdown(
        """
        <div>
            <img src="https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/jeune_.jpeg" class="responsive-image-7">
        </div>
        """,
        unsafe_allow_html=True
    )



fig11 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    title="REPARTITION PAR TRANCHE D'AGE"
)
fig11.update_layout(showlegend=False)
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
average_employeej = data_filtree_moins_de_40['employees_count'].mean()

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
commentariot = f"Voici les 5 principaux secteurs d'activité exercés par les jeunes avec leur pourcentage:\n\n{top_5_text}"


with col55:
    st.metric(label="Chiffre d'Affaires Total", value=f"{total_caj:,.0f} FCFA")
    st.metric(label="Âge Moyen", value=f"{average_agej:.1f} ans")
    st.plotly_chart(fig11)
    st.markdown(commentariot)
with kol18:
    st.metric(label="Moyenne des Chiffres d'Affaires", value=f"{average_caj:,.0f} FCFA")
    st.metric(label="Nombre moyen d'employés", value=f"{average_employeej:,.1f}")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write(commentaire)
    st.write("")
    st.write("")
    st.write("")
    st.plotly_chart(fig13)






















st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)

st.markdown("<h2>Top 1 activité : Vente sur étal</h2>", unsafe_allow_html=True)





vente_sur_etal_data = data[data["activity_sector"] == "VENTE SUR ETAL"]

number_of_rows_vente_sur_etal = len(vente_sur_etal_data)

total_ca_vente_sur_etal = vente_sur_etal_data['CA'].sum()

average_ca_vente_sur_etal = vente_sur_etal_data['CA'].mean()

average_age_vente_sur_etal = vente_sur_etal_data['ages'].mean()

formatted_number_vente_sur_etal = f"{number_of_rows_vente_sur_etal:,.0f}".replace(",", " ")

category_counts = vente_sur_etal_data["genre"].value_counts()

colors = ['blue' if genre == 'Masculin' else 'red' for genre in category_counts.index]

vente_sur_etal_data = data[data["activity_sector"] == "VENTE SUR ETAL"]

data['genre'] = data['genre'].replace({'masculin': 'Masculin', 'feminin': 'Feminin'})

category_counts = vente_sur_etal_data["genre"].value_counts()



colors = ['blue' if genre == 'Masculin' else 'red' for genre in category_counts.index]

fig001 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    color_discrete_sequence=colors,
    title="REPARTITION PAR GENRE"
)
fig001.update_traces(textinfo='none', hoverinfo='label+percent')
fig001.update_layout(showlegend=False, width=400, height=400)

vente_sur_etal_data = data[data["activity_sector"] == "VENTE SUR ETAL"]
category_counts = vente_sur_etal_data["tranche_age"].value_counts()
fig52 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    title="REPARTITION PAR TRANCHE D'AGE"
)
fig52.update_traces(textinfo='none', hoverinfo='label+percent')
fig52.update_layout(showlegend=False, width=400, height=400)

vente_sur_etal_data = data[data["activity_sector"] == "VENTE SUR ETAL"]
category_counts = vente_sur_etal_data["stade_de_maturite"].value_counts()
fig1 = px.pie(
     names=category_counts.index,  # Catégories uniques
    values=category_counts.values,  # Quantités associées à chaque catégorie
    hole=0.3,  # Pour un donut chart (optionnel)
    title=f"REPARTITION PAR STADE DE MATURITE"
)
fig1.update_traces(textinfo='none', hoverinfo='label+percent')
fig1.update_layout(showlegend=False, width=400, height=400)

col1, col2, cola = st.columns(3)

with col1:
    st.markdown(
        """
        <div>
            <img src="https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/ETALL.jpeg" class="responsive-image-8">
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.metric(label="Nombre d'enregistrements (VENTE SUR ETAL)", value=formatted_number_vente_sur_etal)
    st.metric(label="Chiffre d'Affaires Global (VENTE SUR ETAL)", value=f"{total_ca_vente_sur_etal:,.0f} FCFA")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("La vente sur étal, principale activité de nos entreprenants, est dominée par les femmes.")
    st.write("Elle est exercée dans la grande partie des cas par les moins de 40 ans.")
    st.write("La majorité des ventes sur étal ont plus de 5 ans, ce qui indique une pérennité des activités de ce secteur.")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.plotly_chart(fig1)
with cola:
    st.metric(label="Moyenne d'Âge (VENTE SUR ETAL)", value=f"{average_age_vente_sur_etal:,.1f} ans")
    st.metric(label="Moyenne du Chiffre d'Affaires (VENTE SUR ETAL)", value=f"{average_ca_vente_sur_etal:,.0f} FCFA")
    st.plotly_chart(fig001)
    st.plotly_chart(fig52)


st.subheader("Qu'est ce qui est vendu sur nos étals?")
st.write("")

vente_sur_etal_data = data[data["activity_sector"] == "VENTE SUR ETAL"]

category_counts = vente_sur_etal_data["type etal"].value_counts()

column1, column2, kol19 = st.columns(3)

with column2:
    # Limiter à un top 5 des catégories les plus fréquentes
    top5_category_counts = category_counts.nlargest(5)

    # Création d'un graphique en donut pour les catégories principales
    figetal = px.pie(
        names=top5_category_counts.index,  # Top 5 des catégories
        values=top5_category_counts.values,  # Quantités pour chaque catégorie
        hole=0.3,  # Pour un donut chart
        title="DIFFERENTS TYPES D'ETALS"
    )
    figetal.update_traces(textinfo='none', hoverinfo='label+percent')
    figetal.update_layout(showlegend=False)
    st.plotly_chart(figetal)

with column1:
    # Espacement visuel
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.write("Les étals regroupent une grande variété de marchandises et d'activités.")

    # Générer un commentaire dynamique pour le top 5
    if not top5_category_counts.empty:
        total_top5 = top5_category_counts.sum()
        comments = ["La répartition des types d'étals est la suivante :"]
        for category, count in top5_category_counts.items():
            percentage = (count / total_top5) * 100
            comments.append(f"**{category}** : {percentage:.2f}%")

        # Affichage des commentaires
        st.markdown("<br>".join(comments), unsafe_allow_html=True)
    else:
        st.write("Aucune donnée disponible pour afficher la répartition des types d'étal.")

with kol19:
    st.markdown(
        """
        <div>
            <img src="https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/tableafrica.png" class="responsive-image-10">
        </div>
        """,
        unsafe_allow_html=True
    )


st.subheader("Zoom sur les produits vivriers")


vente_sur_etal_data = data[data["activity_sector"] == "VENTE SUR ETAL"]

category_counts = vente_sur_etal_data["type vivrier"].value_counts()

column3, column4, kol20 = st.columns(3)

with column3:
    # Limiter à un top 5 des catégories les plus fréquentes
    top5_category_counts = category_counts.nlargest(5)

    # Création d'un graphique en donut pour les catégories principales
    figviv = px.pie(
        names=top5_category_counts.index,  # Top 5 des catégories
        values=top5_category_counts.values,  # Quantités pour chaque catégorie
        hole=0.3,  # Pour un donut chart
        title="REPARTITION PAR TYPE DE VIVRIERS"
    )
    figviv.update_traces(textinfo='none', hoverinfo='label+percent')
    figviv.update_layout(showlegend=False)
    st.plotly_chart(figviv)

with column4:
    # Espacement visuel
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # Générer un commentaire dynamique pour le top 5
    if not top5_category_counts.empty:
        total_top5 = top5_category_counts.sum()
        comments = ["Les vivriers sont répartis par types suivants :"]
        for category, count in top5_category_counts.items():
            percentage = (count / total_top5) * 100
            comments.append(f"**{category}** : {percentage:.2f}%")

        # Affichage des commentaires
        st.markdown("<br>".join(comments), unsafe_allow_html=True)
    else:
        st.write("Aucune donnée disponible pour afficher la répartition des types d'étal.")

with kol20:
    st.markdown(
    """
    <div>
        <img src="https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/leg.png" class="responsive-image-11">
    </div>
    """,
    unsafe_allow_html=True
    )



st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)

st.markdown("<h2>Top 2 activité : Vêtements, chaussures, accessoires de mode</h2>", unsafe_allow_html=True)

colors = ['blue' if genre == 'Masculin' else 'red' for genre in category_counts.index]

vetements_data = data[data["activity_sector"] == "VETEMENTS/CHAUSSURES/ACCESSOIRE DE MODE"]

number_of_rows_vetements = len(vetements_data)

total_ca_vetements = vetements_data['CA'].sum()

average_ca_vetements = vetements_data['CA'].mean()

average_age_vetements = vetements_data['ages'].mean()

formatted_number_vetements = f"{number_of_rows_vetements:,.0f}".replace(",", " ")

category_counts = vetements_data["genre"].value_counts()

colors = ['blue' if genre == 'Masculin' else 'red' for genre in category_counts.index]

vetements_data = data[data["activity_sector"] == "VETEMENTS/CHAUSSURES/ACCESSOIRE DE MODE"]

data['genre'] = data['genre'].replace({'masculin': 'Masculin', 'feminin': 'Feminin'})



fig002 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    color_discrete_sequence=colors,
    title="REPARTITION PAR GENRE"
)
fig002.update_traces(textinfo='none', hoverinfo='label+percent')
fig002.update_layout(showlegend=False, width=400, height=400)

vetements_data = data[data["activity_sector"] == "VETEMENTS/CHAUSSURES/ACCESSOIRE DE MODE"]

category_counts = vetements_data["tranche_age"].value_counts()

fig70 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    title="REPARTITION PAR TRANCHE D'AGE"
)
fig70.update_traces(textinfo='none', hoverinfo='label+percent')
fig70.update_layout(showlegend=False, width=400, height=400)

vetements_data = data[data["activity_sector"] == "VETEMENTS/CHAUSSURES/ACCESSOIRE DE MODE"]
category_counts = vetements_data["stade_de_maturite"].value_counts()
fig71 = px.pie(
    names=category_counts.index,  # Catégories uniques
    values=category_counts.values,  # Quantités associées à chaque catégorie
    hole=0.3,  # Pour un donut chart (optionnel)
    title=f"REPARTITION PAR STADE DE MATURITE"
)
fig71.update_traces(textinfo='none', hoverinfo='label+percent')
fig71.update_layout(showlegend=False, width=400, height=400)

col1, col2, fatigue = st.columns(3)
with col1:
    st.metric(label="Nombre d'enregistrements", value=formatted_number_vetements)
    st.metric(label="Chiffre d'Affaires Global", value=f"{total_ca_vetements:,.0f} FCFA")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("La vente de vêtements, chaussures et accessoires de mode est pratiquée en majorité par des femmes.")
    st.write("La plupart des vendeurs sont jeunes, c'est-à-dire ont moins de 40 ans.")
    st.write("Les activités de ce secteurs ont tendance à être matures.")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.plotly_chart(fig71)
with col2:
    st.metric(label="Moyenne d'Âge", value=f"{average_age_vetements:,.1f} ans")
    st.metric(label="Moyenne du Chiffre d'Affaires", value=f"{average_ca_vetements:,.0f} FCFA")
    st.plotly_chart(fig002)
    st.plotly_chart(fig70)

with fatigue:
    st.markdown(
    """
    <div>
        <img src="https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/habitss.png" class="responsive-image-12">
    </div>
    """,
    unsafe_allow_html=True
    )





st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)

st.markdown("<h2>Top 3 activité : Couture</h2>", unsafe_allow_html=True)




produits_agricoles_data = data[data["activity_sector"] == "COUTURE"]

number_of_rows_produits_agricoles = len(produits_agricoles_data)

total_ca_produits_agricoles = produits_agricoles_data['CA'].sum()

average_ca_produits_agricoles = produits_agricoles_data['CA'].mean()

average_age_produits_agricoles = produits_agricoles_data['ages'].mean()

produits_agricoles_data = data[data["activity_sector"] == "COUTURE"]
data['genre'] = data['genre'].replace({'masculin': 'Masculin', 'feminin': 'Feminin'})
category_counts = produits_agricoles_data["genre"].value_counts()
colors = ['blue' if genre == 'Masculin' else 'red' for genre in category_counts.index]

fig003 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    color_discrete_sequence=colors,
    title="REPARTITION PAR GENRE"
)
fig003.update_traces(textinfo='none', hoverinfo='label+percent')
fig003.update_layout(showlegend=False, width=400, height=400)

produits_agricoles_data = data[data["activity_sector"] == "COUTURE"]
category_counts = produits_agricoles_data["tranche_age"].value_counts()
fig72 = px.pie(
    names=category_counts.index,
    values=category_counts.values,
    hole=0.3,
    title="REPARTITION PAR TRANCHE D'AGE"
)
fig72.update_traces(textinfo='none', hoverinfo='label+percent')
fig72.update_layout(showlegend=False, width=400, height=400)

produits_agricoles_data = data[data["activity_sector"] == "COUTURE"]
category_counts = produits_agricoles_data["stade_de_maturite"].value_counts()
fig73 = px.pie(
    names=category_counts.index,  # Catégories uniques
    values=category_counts.values,  # Quantités associées à chaque catégorie
    hole=0.3,  # Pour un donut chart (optionnel)
    title=f"REPARTITION PAR STADE DE MATURITE"
)
fig73.update_traces(textinfo='none', hoverinfo='label+percent')
fig73.update_layout(showlegend=False, width=400, height=400)


col1, col2, tired = st.columns(3)
with col2:
    st.metric(label="Nombre d'enregistrements", value=number_of_rows_produits_agricoles)
    st.metric(label="Chiffre d'Affaires Global", value=f"{total_ca_produits_agricoles:,.0f} FCFA")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("Contrairement aux autres principales activités, la couture est dominée par les hommes.")
    st.write("Elle est exercée par les jeunes, et compte en grande partie des activités matures.")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.plotly_chart(fig73)
with tired:
    st.metric(label="Moyenne d'Âge", value=f"{average_age_produits_agricoles:,.1f} ans")
    st.metric(label="Moyenne du Chiffre d'Affaires", value=f"{average_ca_produits_agricoles:,.0f} FCFA")
    st.plotly_chart(fig003)
    st.plotly_chart(fig72)

with col1:
        st.markdown(
    """
    <div>
        <img src="https://raw.githubusercontent.com/nouramaiga1/Photos-rapport/main/tailleur.jpeg" class="responsive-image-13">
    </div>
    """,
    unsafe_allow_html=True
    )







st.markdown("<hr style='border: 2px solid #ddd;'>", unsafe_allow_html=True)

st.markdown("<h2>Map des activités</h2>", unsafe_allow_html=True)


st.markdown("""
    <iframe src="https://mafa-mapbox-v2.poc-demo.com/dashboard" width="100%" height="600"></iframe>
""", unsafe_allow_html=True)
