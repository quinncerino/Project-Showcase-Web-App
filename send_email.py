import smtplib  #email library
import ssl
import os


def send(message):
    host = "smtp.gmail.com"
    port = 465

    #start = message.rindex('\n') + 1
    username = "quinncerino@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "quinncerino@gmail.com"

    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)