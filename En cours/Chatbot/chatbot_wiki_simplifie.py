# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 08:57:11 2020

@author: antoi
"""

# import des librairies
import nltk
import numpy as np
import random
import string # to process standard python strings
import re

# import du texte & nettoyages
f=open('chatbot.txt','r',errors = 'ignore', encoding = "utf8")
raw=f.read()
raw=raw.lower()# converts to lowercase
# quelques modifications : 
raw = re.sub(r"\ufeff", "", raw)
raw = re.sub(r"\[.{1,2}\]", "", raw)

# Création d'une liste de phrases (= tokenization)
nltk.download('punkt') # first-time use only
nltk.download('wordnet') # first-time use only
sent_tokens = nltk.sent_tokenize(raw)

# Entraînement d'une matrice TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
from stop_words import get_stop_words
english_stop_words = get_stop_words('english')

TfidfVec = TfidfVectorizer(stop_words = english_stop_words)
tfidf = TfidfVec.fit(sent_tokens)
# on crée la matrice TF-IDF sur le texte de la page wiki
phrases_tf = tfidf.transform(sent_tokens)

# on définit la fonction qu'on appellera dans le chatbot : elle renvoie 
# la phrase la plus proche de celle posée par l'utilisateur
from sklearn.metrics.pairwise import cosine_similarity

def reponse_wiki(phrase_user):
    # on a besoin d epasser la chaîne de caractère dans une liste :
    phrase_user = [phrase_user]
    # On calcule les valuers TF-IDF pour la phrase de l'utilisateur
    user_tf = tfidf.transform(phrase_user)
    # on calcule la similarité entre la question posée par l'utilisateur
    # et l'ensemble des phrases de la page wiki
    similarity = cosine_similarity(user_tf, phrases_tf).flatten()
    # on sort l'index de la phrase étant la plus similaire
    index_max_sim = np.argmax(similarity)
    # Si la similarité max ets égale à 0 == pas de correspondance trouvée
    if(similarity[index_max_sim] == 0):
        robo_response = "I didn't find this info, sorry"
    # Sinon, on sort la phrase correspondant le plus : 
    else:
        robo_response = sent_tokens[index_max_sim]
    return robo_response

# On a plus qu'à utiliser cette fonction dans un chatbot : 
print("""Hi! I can answer your questions about chatbots!
      Type quit to quit""")
flag = True
while (flag == True):
    phrase_user = input("> ")
    phrase_user = phrase_user.lower()
    if (phrase_user == "quit"):
        print ("Bye!")
        flag = False
    else:
        print(reponse_wiki(phrase_user))