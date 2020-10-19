# Semaine du 19 octobre - Computer Vision

Cette semaine sera consacrée à la vision par ordinateur, à ses particularités et à ses outils comme la bibliothèque dédiée OpenCV.

Les travaux donneront lieu au rendu de 4 notebooks :
1. Application d'algorithmes de tracking d'objet à une vidéo
2. Application des principales fonctions de pré-traitements des images
3. Classification d'un dataset d'images par des méthodes hors Deep learning
4. Classification d'un dataset d'images par Deep learning

## I Généralités sur la vision par ordinateur

### Les problématiques de vision par ordinateur

Une vidéo de 11 minutes sur la vision par ordinateur [ici](https://www.youtube.com/watch?v=-4E2-0sxVUM).

A lire _en diagonal_ en guise d'introduction pour avoir une idée des problématiques principales résolues par le CV : [5 computer vision techniques](https://heartbeat.fritz.ai/the-5-computer-vision-techniques-that-will-change-how-you-see-the-world-1ee19334354b)

En résumé :

* Image classification : le problème le plus courant en CV, celui qui a lancé la révolution du Deep Learning avec le concours ImageNet

* Object detection : trouver plusieurs objets dans une scène, voir par exemple cette lecture sur les cascades de Haar [(ici)](https://pymotion.com/detection-objet-cascade-haar/) et une vidéo sur la détection d'objets avec cascades de Haar [(Haar cascade with OpenCV)](https://www.youtube.com/watch?v=88HdqNDQsEk)

* Object tracking : suivre des objets dans une vidéo d'une image à une autre (les objets doivent avoir été isolés avant)

* Semantic segmentation : attribuer des labels aux objets identifiés

* Instance segmentation : problème le plus riche, différencier tous les objets dans la scène au pixel près

Nous nous focaliserons sur la classification d'images cette semaine même si vous aurez la possibilité d'expérimenter du tracking d'objet.

### Computer Vision et Deep Learning

Les problèmes de Computer Vision (CV) ont commencé à être étudiés bien avant le Deep Learning et un ensemble de techniques propres aux images ont été développées.

Quelques sources comparant les techniques classiques de CV et le Deep Learning :
[ici](https://zbigatron.com/has-deep-learning-superseded-traditional-computer-vision-techniques/) et
[ici](https://www.cs.swarthmore.edu/~meeden/cs81/f15/papers/Andy.pdf) et
[ici](https://towardsdatascience.com/deep-learning-vs-classical-machine-learning-9a42c6d48aa)

Cherchez des librairies Python dédiées à ces différentes tâches.

Un article plus complet (sur Medium) : [ici](https://medium.com/overture-ai/part-2-overview-of-computer-vision-methods-69c56843c567)


## II Un exemple concret : le tracking d'objet avec OpenCV

### Installation de la bibliothèque OpenCV sous Python

* Créez un environnement dédié au Computer Vision utilisant Python 3.6

* Passez par pip et installez opencv-python dans cet environnement dédié

* Plus de détails [ici](https://pypi.org/project/opencv-python/)

* Il faudra installer aussi opencv-contrib-python [ici](https://pypi.org/project/opencv-contrib-python/)

**NOTE**: attention à la version de Python utilisée, je conseille de s'en tenir à la 3.6 pour éviter des problèmes avec OpenCV...

### Tracking avec les modèles d'OpenCV

Une fois OpenCV installée, expérimentez le tracking d'objet avec différents algorithmes en vous inspirant des exemples de code suivants :

https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/

https://www.learnopencv.com/goturn-deep-learning-based-object-tracking/

**Faites un notebook pour garder trace de vos expériences sur la ou les vidéos de votre choix (donnez le lien vers les vidéos utilisées). Essayez au moins 3 modèles.**

Suggestions :
- Les méthodes suivantes donnent des résultats intéressants :
    + CSRT
    + KCF
    + MOSSE
    + GoTurn (si vous arrivez à le faire tourner !)

- Partir d'une **courte** vidéo contenant des personnages se déplaçant (si pas d'idées, cherchez chaplin.mp4 ou filmez-vous !)
- Comparez les méthodes de tracking en termes de temps de calcul ? Lesquelles semblent compatibles avec un traitement en temps réel sur votre machine ?


**NOTE**: l'utilisation de GOTURN (seul modèle à base de Deep Learning disponible dans OpenCV) peut être délicate, ne pas perdre de temps avec si cela ne fonctionne pas du premier coup.

### Bonus : segmentation sémantique

Testez facilement la détection d'objets courants avec labels sur une image de votre choix ([ici un exemple avec le code](https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606)). Ludique et rapide.


## III Les techniques de pré-traitement des images ou Preprocessing (lundi 2ème moitié d'après-midi et mardi matin)

### Pré-traitements classiques

Voir la doc d'OpenCV [ici](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_table_of_contents_imgproc/py_table_of_contents_imgproc.html) pour les principales fonctions de preprocessing.

Ou cet excellent [article](https://www.analyticsvidhya.com/blog/2019/03/opencv-functions-computer-vision-python/).

**Faites un notebook dans lequel vous chargerez des images de votre choix et appliquerez au moins 5 des traitements suivants, avec visualisation du résultat à chaque fois :**

* changement de l'espace de couleurs

* redimensionnement de l'image

* rognage de l'image (cropping)

* seuillage (thresholding)

* filtrage (voir [ici](https://medium.com/@soumyapatilblogs/image-filtering-using-opencv-66b67e1bd968) par exemple)

* détection de traits (bords, coins)

* extraction de contours et segmentation

__NOTE IMPORTANTE__: si votre notebook tourne sans fin, insérer au tout début du notebook la ligne : % matplotlib auto


Quelques idées de traitements si vous manquez d'inspiration :
- Choisir 5 images contenant des flammes (exemples : bougie, feu de cheminée, incendie, etc.) et 5 images sans flammes, les sauver dans un sous-répertoire *images*
- Pour les images en couleurs chargées par défaut en BGR, les convertir en HSV et en YUV (cherchez la différence entre ses 3 représentations)
- En utilisant la bibliothèque python *glob*, appliquer une fonction de changement de taille d'image d'opencv à toutes les images précédentes et sauvegarder les images avec leur nouvelle taille dans le répertoire images avec un suffixe "_resized" et dans un encodage de votre choix (exemples : jpg, png, etc.). La fonction pourra soit réduire la taille en pourcentage, soit réduire indépendamment hauteur et largeur de l'image
- Réfléchir à comment utiliser les espaces de couleur pour segmenter les images contenant des flammes pour isoler les zones contenant les flammes (pensez au seuillage)
- Fabriquer des images binaires à partir de la segmentation précédente, avec en blanc les zones identifiées comme contenant des flammes

__Bonus : application à de la vidéo__

- Récupérez une vidéo contenant des flammes
- Chargez la vidéo dans OpenCV et la faire jouer dans une fenêtre
- Appliquez la segmentation binaire précédente à chaque frame et afficher la vidéo correspondante
- Une façon de le faire [ici](https://github.com/Simplon-IA-Bdx-1/opencv-fire-segmentation)

### Réduction de la dimensionnalité

La réduction de la dimensionnalité du dataset est cruciale avec les images. Elle peut se limiter à réduire la résolution de l'image et/ou à ignorer certains canaux dans l'espace des couleurs.

Regardez ce site d'introduction : [Dimensionality Reduction](https://idyll.pub/post/dimensionality-reduction-293e465c2a3443e8941b016d/)

Puis lisez [cet article](https://www.analyticsvidhya.com/blog/2018/08/dimensionality-reduction-techniques-python/) très complet sur 12 techniques de réduction de la dimensionnalité.

Un notebook exemple d'application de PCA dont on pourra s'inpirer par la suite : [Notebook PCA](https://www.kaggle.com/hamishdickson/preprocessing-images-with-dimensionality-reduction)

Résumé des principales techniques disponibles facilement dans scikit-learn :

* PCA

* ICA

* t-SNE

* UMAP

Pour mieux comprendre tSNe : [ici](https://distill.pub/2016/misread-tsne/)
Pour mieux comprendre UMAP (qui n'est pas juste de la visualisation) : [ici](https://pypi.org/project/umap-learn/)
Pour la différence entre PCA et ICA : [ici](http://compneurosci.com/wiki/images/4/42/Intro_to_PCA_and_ICA.pdf)

**Ajoutez dans le notebook précédent une réduction de la dimensionnalité de votre choix à vos images. Cela vous servira pour la classification d'images ensuite.**

## IV Classification d'image : Galaxy Zoo

Objectif : avec Keras, résoudre au mieux le problème de classification des images de galaxies en 3 classes (rondes, à disque ou pas une galaxie), à l'aide de techniques non Deep Learning et de Deep Learning (transfer learning / CNN "maison").

### Le dataset : Galaxy Zoo

Une base d'images extraites du projet [Galaxy Zoo](https://www.zooniverse.org/projects/zookeeper/galaxy-zoo/).

Les données sont téléchargeables ici : [galaxy zoo data](https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/data)

Combien y-a-t-il d'exemples ? Quelles sont les classes ? Sont-elles équilibrées ?

### Classification par modèles non Deep Learning (mardi après-midi)

Il n'y a pas que le Deep Learning pour faire de la classification d'images.

Inspection des données : commencez par visualiser une trentaine d'exemples d'images appartenant à des classes différentes pour en comprendre les particularités. En quoi ces images astronomiques différent-elles d'images de la vie courante ? Voyez-vous des différences exploitables entre les images de galaxies rondes et les galaxies à disque ?

**Faites un notebook qui contiendra les 3 parties suivantes :**
1. Pré-traitements pertinents pour le Galaxy zoo **ETAPE IMPORTANTE**
2. Classification avec une méthode ensembliste, par exemple XGBOOST, mesurez la performance
3. Classification par SVM ou k-NN pour classer le dataset mesurez la performance

Evaluez la performance de ces modèles, elle servira de référence (baseline) pour la suite.

Suggestions :
* Cherchez des stratégies pour réduire le nombre de dimensions et faciliter l'apprentissage d'un modèle
* A l'étape 1, on pourrait trouver les techniques suivantes (liste ni exhaustive ni prescriptive) :
  * traitements de l'image pour réduire sa taille tels que le rognage ou la réduction de résolution
  * traitements de l'image pour rendre plus le dataset plus facilement séparable, comme le changement d'espace de couleurs
  * application d'une réduction de dimensionnalité de type PCA ou autre
  * fabrication "créative" de features (exemple, le pixel au centre, des ratios d'intensité entre zones, etc.) pour améliorer les baselines
* A l'étape 1, essayez d'intercaler une PCA et comparez avec les résultats sans PCA

### Classification par Deep Learning

### Compression des images

Cherchez comment réduire la complexité du problème avec un mix des techniques déjà testées auparavant (exemples : rognage, redimensionnement, etc.).

A ce stade, il faudra s'être fixé les traitements en amont et leur implémentation (à la volée ou à partir de répertoires intermédiaires).

### Transfer learning

Le Transfer Learning consiste à reprendre en partie un modèle de CNN déjà entraîné. Concrétement et en général, on garde toute l'architecture de convolution telle quelle pour bénéficier de l'extraction de features déjà apprises et on remplace la partie classification (dernières couches du CNN) par des couches de classification à entraîner sur le dataset spécifique.

Le Transfer Learning passe donc par les étapes suivantes :

* Choix d'un modèle sur étagère (exemple VGG16, VGG19, Inception, Resnet50, etc.)

* Choix du périmètre de transfer learning en fonction de la taille du dataset (plus il est petit, moins on veut de paramètres à optimiser !)

* Ajout des couches de classification aux couches de convolution retenues

* Entraînement

Un bon tutoriel [ici](https://machinelearningmastery.com/how-to-use-transfer-learning-when-developing-convolutional-neural-network-models/)

### Data augmentation

Les datasets d'images coûtent chers à obtenir, surtout dans un domaine spécialisé. L'augmentation de données est une méthode importante pour améliorer l'entraînement des modèles de Deep Learning en leur fournissant des exemples réalistes fabriqués à partir des images originales.

Application au dataset Galaxy Zoo :

* Choisissez aléatoirement 9 images quelconques dans le dataset
* Générez des variantes avec les fonctions de Data Augmentation de Keras
    * Voir ImageDataGenerator()
    * Appliquez une translation aléatoire
    * Appliquez une rotation aléatoire
    * Appliquez feature standardization
    * Appliquez le ZCA whitening (des explications [ici](https://cbrnr.github.io/2018/12/17/whitening-pca-zca/))

**Note** : le Data Augmentation n'est pas une technique réservée aux problèmes de CV

#### Mise en oeuvre

Il y a 2 approches envisageables :
* Partir d'un réseau CNN pré-entraîné et appliquer du transfer Learning
* Définir son propre modèle CNN

Suggestions :
* Réfléchir à des stratégies d'amélioration des résultats : pré-traitement, feature engineering, combinaison de modèles/méthodes, etc.
* Définir et implémenter une architecture **simple** de CNN adaptée aux données réduites en termes de dimensions et de taille du dataset
* Explorer les temps de calcul en fonction de l'architecture et de l'étape de réduction des dimensions
* Entraîner le modèle (tester d'abord sur un sous-ensemble), évaluer avec une métriques adaptée
* Réfléchir à l'utilisation du data augmentation
* Implémenter le data augmentation, évaluer le gain
* Identifier les hyper-paramètres les plus prometteurs pour une optimisation du CNN
* Choisir une méthode d'optimisation des hyper-paramètres et l'appliquer à son modèle
* Chercher des modèles pré-entraînés qui pourraient servir pour ce problème de classification
* Réfléchir au périmètre d'architecture sur lequel appliquer le transfer learning
* Appliquer à l'entraînement d'un modèle, évaluer convergence et performance des prédictions
* Optimiser les hyper-paramètres pour le modèle provenant d'un modèle pré-entraîné

__Bonus :__
Dans un deuxième temps, on pourra chercher à identifier la présence d'une forme spiralée ou non lorsque la galaxie aura été identifiée comme appartenant à la classe 2, c'est-à-dire une galaxie à disque (voir [arbre de décision du problème](https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/overview/the-galaxy-zoo-decision-tree)).



### Un exemple de solution

Il s'agit du pipeline gagnant du challenge Galaxy Zoo : [sur github](https://github.com/benanne/kaggle-galaxies/blob/master/doc/documentation.pdf). Attention, le problème résolu dans ce cas était plus complexe que celui sur lequel vous avez travaillé. Néanmoins l'approche est très bien décrite et permet de s'inspirer.
