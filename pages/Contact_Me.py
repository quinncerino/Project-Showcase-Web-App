import streamlit as st
from send_email import send

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input(label = "Enter your email address:", key="email")
    raw_message = st.text_area(label = "Enter your message:", key="message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button(label = "Submit")
    if button:
        send(message)
        st.info("Your email was sent successfully.")