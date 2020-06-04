# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:39:08 2020

@author: antoi
"""
import re
import random
import string

good_by = r"au revoir|quit|ciao|hasta la vista|à \+"
msg_bot = ["salut!", "ok mais restez chez vous bordel", "à très vite!"]

msg_restez = ["restez chez vous", "restez chez vous, combien de fois dois-je le dire",
              "vous allez rester chez-vous oui?"]

meteo = r"quel temps fait-il à .*?|.*météo à .*?"

flag = True
print("""Bienvenue sur ce bot tout basique! \n Écrivez votre question : \n
Dites moi au revoir pour quitter""")
while (flag == True):
    text_user = input("> ")
    text_user = text_user.lower()
    if (re.search(good_by, text_user)):
        print(random.choice(msg_bot))
        flag = False
    elif (re.search(meteo, text_user)):
        text_user = re.sub(f"[{string.punctuation}]", " ", text_user)
        print(f"Il fait beau à {text_user.split()[-1]}")
    else:
        print(random.choice(msg_restez))


def reponse_chat(text_user):
    text_user = text_user.lower()
    if (re.search(good_by, text_user)):
        return random.choice(msg_bot)
    elif (re.search(meteo, text_user)):
        text_user = re.sub(f"[{string.punctuation}]", " ", text_user)
        return f"Il fait beau à {text_user.split()[-1]}"
    else:
        return random.choice(msg_restez)


