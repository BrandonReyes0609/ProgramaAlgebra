

import requests
import random

# Genera username y password
def ramdom_word():
    word = ''
    for i in range(10):
        word += random.choice("abcdefghigklmnopqrstuvwxyz123456789")
    return word

#"Manda la petición"
def send_post(url, username, password):
    data = {"password:":password}
    try:
        r = requests.post(url, data=data)
        if(r.status_code == 200):
            print("ok - Enviado: username "+username+"password "+ password)
        else:
                return "Error"
    except requests.exceptions.RequestException as e: #Falta
        return "Error"

# o hace hasta el infinito
    while True:
        username = ramdom_word()
        password = ramdom_word()
        send_post("https://web.whatsapp.com/emoji_suggestions/es.json?v=2.2236.10" + username)


