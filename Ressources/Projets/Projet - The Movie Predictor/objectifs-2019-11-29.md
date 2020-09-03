# Objectif du jour

Avoir un script python capable d'exporter ou d'importer la liste des films ou de people au format .csv

### Commandes à exécuter :

``$ python app.py movies export --file chemin_fichier_movies.csv``

``$ python app.py people export --file chemin_fichier_people.csv``

``$ python app.py movies import --file fichier_import_movies.csv``

### Ressources

* MariaDB Connector for Python : ``$ conda install mysql-connector-python``
* Faire des requêtes SQL "SELECT" : https://www.fbotutos.com/requete-select-mysql.html
* module CSV : https://docs.python.org/fr/3.7/library/csv.html
* Module de gestion des arguments en CLI : https://docs.python.org/fr/3.7/howto/argparse.html

