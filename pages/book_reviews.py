import streamlit as st
import pandas as pd

st.set_page_config(layout="wide") #deixar a config da tela em full screen

st.write("# Book Reviews")

df_reviews = pd.read_csv("Assets/customer reviews.csv")
def_top100_books = pd.read_csv("Assets/Top-100 Trending Books.csv")

books = def_top100_books["book title"].unique().tolist() #unique traz os títulos unicos
books = st.sidebar.selectbox("Escolha um livro", books)

df_book =def_top100_books[def_top100_books["book title"] == books]
df_reviews_f = df_reviews[df_reviews["book name"] == books]

book_tittle = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_author = df_book["author"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_tittle)
st.subheader(book_genre)

review_count = len(df_reviews_f)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Preço", book_price)
col2.metric("Avaliação", book_rating)
col3.metric("Reviews", review_count)
col4.metric("Ano Publicação", book_year)

st.divider() #linha divisoria abaixo das colunas

for row in df_reviews_f.values:
    with st.chat_message("user"):
        st.write(f"**{row[2]}**")   #titulo da review
        st.write(row[5])            #conteudo da review