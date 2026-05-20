import streamlit as st
col1, col2, col3 = st.columns(3)

with col1:
    st.image("apple.png", use_container_width=True)
    st.title("### Apple")
    st.link_button("Acessar", "https://www.apple.com/br/")

with col2:
    st.image("netflix.png", use_container_width=True)
    st.title("### Netflix")
    st.link_button("Acessar", "https://www.netflix.com/br/")

with col3:
    st.image("spacex.png", use_container_width=True)
    st.title("### SpaceX")
    st.link_button("Acessar", "https://www.spacex.com/")
