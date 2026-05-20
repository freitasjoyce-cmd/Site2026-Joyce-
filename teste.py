import streamlit as st
col1, col2, col3 = st.columns(3)

with col1:
    st.image("apple.jpg", use_container_width=True)
    st.title("Apple")
    st.link_button("Acessar", "https://www.apple.com/br/")
    st.write("Empresa responsável por uma das maiores produções de eletrônicos do mundo")

with col2:
    st.image("netflix.jpg", use_container_width=True)
    st.title("Netflix")
    st.link_button("Acessar", "https://www.netflix.com/br/")
    st.write("Plataforma de filmes, séries e streaming online.")
with col3:
    st.image("spacex.jpg", use_container_width=True)
    st.title("SpaceX")
    st.link_button("Acessar", "https://www.spacex.com/")
    st.write("Empresa espacial que desenvolve foguetes e missões espaciais.")
