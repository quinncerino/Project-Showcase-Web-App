import streamlit as st
from csv import DictReader

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


st.write("Below you can find some of the apps and projects I have programmed. Feel free to contact me!")


col3, middle, col4 = st.columns([1.5, 0.5, 1.5])


with col3:
    with open("data.csv") as file:
        csv_reader = list(DictReader(file, delimiter=";"))
        for index, row in enumerate(csv_reader[:4]):
            st.header(row['title'])
            st.write(row['description'])
            st.image("images/" + row['image'])
            st.write(f"[Source Code]({row['url']})")


with col4:
    with open("data.csv") as file:
        csv_reader = list(DictReader(file, delimiter=";"))
        for index, row in enumerate(csv_reader[4:]):
            st.header(row['title'])
            st.write(row['description'])
            st.image("images/" + row['image'])
            st.write(f"[Source Code]({row['url']})")

