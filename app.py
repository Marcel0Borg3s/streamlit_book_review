# blibliotecas: Streamlit | Pandas | Plotly
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide") #deixar a config da tela em full screen

df_reviews = pd.read_csv(r"E:\Programer\Python\Projetos\Asimov_v0\Streamlit\Assets\customer reviews.csv")
def_top100_books = pd.read_csv(r"E:\Programer\Python\Projetos\Asimov_v0\Streamlit\Assets\Top-100 Trending Books.csv")

# Slider de preço
price_max = float(def_top100_books["book price"].max())
price_min = float(def_top100_books["book price"].min())

price_range = st.sidebar.slider(
    "Price Range", price_min, price_max, value=(price_min, price_max),
    step=0.1
)

st.sidebar.markdown(f"**Preço selecionado:** de ${price_min:.2f} até ${price_max:.2f}")

# Slider de rating
rating_max = float(def_top100_books["rating"].max())
rating_min = float(def_top100_books["rating"].min())

rating_range = st.sidebar.slider(
    "Ratin Range", rating_min, rating_max, value=(rating_min, rating_max),
    step=0.1
)

st.sidebar.markdown(f"**Rating selecionado:** de {rating_min} até {rating_max}")

# Aplicar os filtros baseados nos sliders
df_books = def_top100_books[
    (def_top100_books["book price"] >= price_range[0]) &
    (def_top100_books["book price"] <= price_range[1]) &
    (def_top100_books["rating"] >= rating_range[0]) &
    (def_top100_books["rating"] <= rating_range[1])
]
st.dataframe(df_books)




