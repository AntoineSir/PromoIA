# Amélioration grâce à l'IA d'une application existante

Il s'agit du cas pratique 1 (évaluation E2) du titre professionnel de "Développeur en intelligence artificielle".

## Contexte

Triof est une start-up de tri et de recyclage des déchets spécialisée dans le traitement des déchets plastiques. Elle a développé une machine qu'elle loue aux entreprise : grâce à cette dernières les salariés peuvent déposer leurs déchets plastiques afin qu'ils soient recyclés en fil d'impression 3D. Malheureusement on a remarqué que les personnes n'indiquaient pas toujours bien quel déchet ils inséraient or cela a un impact négatif sur la qualité du filameent. Triof vous sollicite pour proposer une solution intégrant de l'IA afin de pallier ce problème.

## Préliminaire

Après avoir analyser le fonctionnement de l'application, présenter en quelques lignes (une page maximum) votre compréhension du problème, les solutions qui vous paraissent adaptées et comment vous les mettriez en place. 

## Première approche : une solution IA Cloud

Proposer une solution à l'aide du service Custom Vision d'Azure pour régler le problème.  
Indications :
1. Créer sur Azure un groupe de ressource ainsi qu'une ressource Cognitive Services
2. Sur le portail Custom Vision (https://www.customvision.ai/), initier un projet en le reliant à votre ressource tout juste créée.
3. Entraîner un modèle de reconnaissance d'image permettant d'identifier les 3 types de déchets plastiques distingués par l'application.
4. Publier votre modèle afin de pouvoir le mobiliser via API
5. Intégrer un appel API dans l'application mettant en place la solution qui vous parait le plus mieux : précocher le type de déchet plastique, suggérer le type de déchet, etc...

## Deuxième approche : une amélioration via une solution locale

Un autre problème auquel la machine de Triof fait face est l'insertion par les salariés de déchets plastiques **sales** ce qui entraîne là encore, un fil d'impression de moindre qualité.

Proposer cette fois une solution sans recourir aux services IA Cloud pour résoudre ce problème.

Indications:
- Vous êtes relativement libres sur cette partie mais l'idée est de construire un modèle permettant de classifier, en plus du type de déchet, la propreté du déchet.
- Vous pourrez soit construire votre propre modèle soit utiliser du *transfer learning* à partir de modèles de computer vision pré-implémentés.
- Une étape cruciale va être la constitution de votre jeu de données d'entraînement. Plusieurs solutions sont possibles notamment le scraping. Quoi qu'il en soit, n'oubliez pas l'existence de la *data augmentation*...
