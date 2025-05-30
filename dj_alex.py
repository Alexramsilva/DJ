# -*- coding: utf-8 -*-
"""DJ Alex.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TsHK25sKZXCUZU_tMeH5LugkJRePD0Fa
"""

import streamlit as st

# Lista de canciones
canciones = [
    {
        "titulo": "Ëcoute chérie",
        "artista": "Vendredi sur Mer",
        "url": "https://www.youtube.com/embed/Fc9YMzOoEr4"
    },
    {
        "titulo": "Feel u",
        "artista": "okayceci",
        "url": "https://www.youtube.com/embed/goigX3c-s4U"
    },
    {
        "titulo": "Crawler",
        "artista": "Joyhauser",
        "url": "https://www.youtube.com/embed/AxBPg9PGQgw"
    },
    {
        "titulo": "Stiefelblitz",
        "artista": "Jarhe 90",
        "url": "https://www.youtube.com/embed/S4msmM49RKY"
    },
    {
        "titulo": "Die Liebe Kommt nicht aus Berlin",
        "artista": "Brutalismus 3000",
        "url": "https://www.youtube.com/embed/BY1qkoUhcWQ"
    },
    {
        "titulo": "Antonio soffiantini detto tunin",
        "artista": "Carlo Savani",
        "url": "https://www.youtube.com/embed/KrqTPEow7rk"
    },
    {
        "titulo": "Jewells",
        "artista": "Cranes",
        "url": "https://www.youtube.com/embed/L8QE4k0T980"
    },
    {
        "titulo": "Running up that hill",
        "artista": "Kate Bush",
        "url": "https://www.youtube.com/embed/HYwNM1t9ltI"
    },
    {
        "titulo": "Interlude",
        "artista": "Reverend Baron",
        "url": "https://www.youtube.com/embed/nuRT3fm3KYE"
    },
    {
        "titulo": "Electrocution",
        "artista": "Automatic",
        "url": "https://www.youtube.com/embed/rvIlqj3bPXc"
    },
    {
        "titulo": "Highway",
        "artista": "Automatic",
        "url": "https://www.youtube.com/embed/T6yMjmlfw7M"
    },
    {
        "titulo": "I Can´t live in a living room",
        "artista": "Red Zebra",
        "url": "https://www.youtube.com/embed/Xvb_oRBjbcw"
    },
    {
        "titulo": "Supernature",
        "artista": "Cerrone",
        "url": "https://www.youtube.com/embed/7XMpqVmaQpg"
    },
    {
        "titulo": "Higher",
        "artista": "Ary",
        "url": "https://www.youtube.com/embed/WtAz6jc2mr0"
    },
    {
        "titulo": "Paris/Orly",
        "artista": "Deux",
        "url": "https://www.youtube.com/embed/XXIPOK1rc88"
    },
    {
        "titulo": "Game and Performance",
        "artista": "Deux",
        "url": "https://www.youtube.com/embed/E_lnQDnC3zU"
    },
    {
        "titulo": "Espresso",
        "artista": "Sabrina Carpenter",
        "url": "https://www.youtube.com/embed/51zjlMhdSTE"
    },
    {
        "titulo": "No habrá nadie en el mundo",
        "artista": "Bulka",
        "url": "https://www.youtube.com/embed/JETyhLQFJW4"
    },
    {
        "titulo": "Mlitary Fashion Show",
        "artista": "And One",
        "url": "https://www.youtube.com/embed/vwnLp67rrzY"
    },
    {
        "titulo": "Babes ofthe 80s",
        "artista": "Lebanon Hanover",
        "url": "https://www.youtube.com/embed/8kXFnLI1bzc"
    },
    {
        "titulo": "Pain",
        "artista": "Boy Hasher",
        "url": "https://www.youtube.com/embed/HYsTVlznT8I"
    },
    {
        "titulo": "Tu Luz",
        "artista": "Azul Violeta",
        "url": "https://www.youtube.com/embed/RXV3Omh13bE"
    },
    {
        "titulo": "Brain Freeze",
        "artista": "Everyone Says Hi",
        "url": "https://www.youtube.com/embed/qKMybUSh_gI"
    },
    {
        "titulo": "The Adults are talking",
        "artista": "The Strokes",
        "url": "https://www.youtube.com/embed/o4qsjmLxhow"
    },
    {
        "titulo": "Fuckoff in not the only you have to show",
        "artista": "CSS",
        "url": "https://www.youtube.com/embed/BVGHHci1oh4"
    },
    {
        "titulo": "Taube",
        "artista": "ZweiLaster",
        "url": "https://www.youtube.com/embed/sbsMwPKGM"
    },
    {
        "titulo": "Aéro Dynamik",
        "artista": "Kraftwerk",
        "url": "https://www.youtube.com/embed/OMSFr2-QeR8"
    },
    {
        "titulo": "Spare me the decision",
        "artista": "Nation of Language",
        "url": "https://www.youtube.com/embed/Qla9jQXhDIA"
    },
    {
        "titulo": "Oblivon",
        "artista": "Grimes",
        "url": "https://www.youtube.com/embed/S8HrvII7gU0"
    },
    {
        "titulo": "Templation",
        "artista": "New Order",
        "url": "https://www.youtube.com/embed/R_8kiU8T2bs"
    },
    {
        "titulo": "No te alejes tanto de mi",
        "artista": "Luis Alberto Spinetta",
        "url": "https://www.youtube.com/embed/cmDgth96PDw"
    },
    {
        "titulo": "Mil horas",
        "artista": "Los abuelos de la nada",
        "url": "https://www.youtube.com/embed/1To_Wz5RWi0"
    },
    {
        "titulo": "Arrancacorazones",
        "artista": "Attaque 77",
        "url": "https://www.youtube.com/embed/oblZatYQpGc"
    },
    {
        "titulo": "Loco (tu forma de ser)",
        "artista": "Los Auténticos Decadentes",
        "url": "https://www.youtube.com/embed/fgXDHQm5eq4"
    },
    {
        "titulo": "No me arrepiento de este amor",
        "artista": "Attaque 77",
        "url": "https://www.youtube.com/embed/qN3Y3Z5-3sw"
    },
    {
        "titulo": "Hablando a tu corazón",
        "artista": "Charly Garcia",
        "url": "https://www.youtube.com/embed/Z7AERldCALc"
    },
    {
        "titulo": "Gato",
        "artista": "Maya Delilah",
        "url": "https://www.youtube.com/embed/OBVFdprVDSo"
    },
    {
        "titulo": "Discoschnupfen",
        "artista": "BIBIZA",
        "url": "https://www.youtube.com/embed/kmlQxgm8d7g"
    },
    {
        "titulo": "Outfit Check",
        "artista": "Ritter Lean",
        "url": "https://www.youtube.com/embed/yt7pqmkfjUI"
    },
    {
        "titulo": "Bisschen mehr als freundshaft",
        "artista": "Max&Joy",
        "url": "https://www.youtube.com/embed/rsmPE5KmUv8"
    },
    {
        "titulo": "Vuelvo al sur",
        "artista": "Gotan Project",
        "url": "https://www.youtube.com/embed/0Otelte6m5Q"
    },
    {
        "titulo": "Vamos Companeros",
        "artista": "Harmonia & Eno",
        "url": "https://www.youtube.com/embed/AxYzWamhB6Q"
    },
    {
        "titulo": "Lip Flip",
        "artista": "aya",
        "url": "https://www.youtube.com/embed/yKYomCBGQ_k"
    },
    {
        "titulo": "Chunga´s Revenue",
        "artista": "Gotan Project",
        "url": "https://www.youtube.com/embed/FWj2-iyTF8c"
    },
    {
        "titulo": "Attenti al Lupo",
        "artista": "Lucio Dalla",
        "url": "https://www.youtube.com/embed/kFfhBX7ET-4"
    },
    {
        "titulo": "Herz ist Trumf",
        "artista": "Trio",
        "url": "https://www.youtube.com/embed/NUU3ci9KUdg"
    },
    {
        "titulo": "Wieviel Menschen waren glucklich, dass du gelebt?",
        "artista": "Hilegard knef",
        "url": "https://www.youtube.com/embed/LmVNZHGAX-Y"
    },
    {
        "titulo": "Verstarker",
        "artista": "Blumfeld",
        "url": "https://www.youtube.com/embed/H6qtPaMX3d0"
    },
    {
        "titulo": "Shattered Dreams",
        "artista": "Johny Hates Jazz",
        "url": "https://www.youtube.com/embed/Kz5scjSQ_WE"
    },
    {
        "titulo": "Abusey Junction",
        "artista": "Kokoroko",
        "url": "https://www.youtube.com/embed/tSv04ylc6To"
    },
    {
        "titulo": "De Repente",
        "artista": "alici",
        "url": "https://www.youtube.com/embed/37ctpubCYTg"
    },
    {
        "titulo": "Rennfahrer",
        "artista": "Modular",
        "url": "https://www.youtube.com/embed/-kI5deFP9J8"
    },
    {
        "titulo": "New Cinnamon Girls",
        "artista": "The Model Rockets",
        "url": "https://www.youtube.com/embed/h5q0B6oTZNc"
    },
    {
        "titulo": "Eyes without face",
        "artista": "Billie Idol",
        "url": "https://www.youtube.com/embed/G_GxaoOJFTY"
    },
    {
        "titulo": "Rosa venus",
        "artista": "Fobia",
        "url": "https://www.youtube.com/embed/RlHOgYJjVMo"
    },
    {
        "titulo": "Plus de sens",
        "artista": "Angèle",
        "url": "https://www.youtube.com/embed/ytVhqQDWOT4"
    },
    {
        "titulo": "A little more",
        "artista": "Angèle",
        "url": "https://www.youtube.com/embed/D4C8SnX5xSg"
    },


]

st.title("El Playlist (oficial) del tio Alex")

# Seleccionar canción
opciones = [f"{c['titulo']} - {c['artista']}" for c in canciones]
seleccion = st.selectbox("Elige una canción:", opciones)

# Slider de volumen
volumen = st.slider('Volumen', min_value=0, max_value=100, value=50)

# Buscar URL seleccionada
cancion_actual = next(c for c in canciones if f"{c['titulo']} - {c['artista']}" == seleccion)

# Mostrar reproductor
st.markdown(f"""
    <iframe width="700" height="400"
    src="{cancion_actual['url']}?autoplay=1&volume={volumen}"
    frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
    </iframe>
""", unsafe_allow_html=True)

st.caption("El volumen puede que necesites ajustarlo directamente en YouTube. ")

# Personalización de diseño
st.markdown("""
<style>
    .stApp {
        background-color:  #00FF00;
    }
    .css-1d391kg {
        color:  #faf7f8;
    }
</style>
""", unsafe_allow_html=True)