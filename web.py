import streamlit as st

st.set_page_config(layout = 'wide')

col1, col2 = st.columns(2) #create 2 column object instances

with col1:
    st.image('images/photo.png')  #method that produces an image object instance

with col2:
    st.title("Quinn Cerino")
    content = """
    Hi, I'm Quinn Cerino! I'm an undergraduate student majoring in Computer Science at ECU. I'm currently 
    a sophomore and I'm currently learning/working with Python and C++ to create my projects!
    """

    st.info(content)