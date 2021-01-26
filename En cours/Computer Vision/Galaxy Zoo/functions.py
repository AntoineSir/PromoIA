import matplotlib.pyplot as plt
import numpy as np
import cv2

def show_galaxies(gal_ids, n_gal=25, n_row=5, n_col=5):
    """Fonction qui affiche des galaxies sélectionnées au hasard
    parmi une liste d'id de galaxie"""
    selected = np.random.choice(gal_ids, n_gal, replace=False)
    plt.figure(figsize=(16,16))
    for i in range(n_gal):
        plt.subplot(n_row,n_col,i+1)
        img = cv2.imread(f"data/images_training_rev1/{selected[i]}.jpg")
        plt.imshow(img)
        plt.title(f"Id={selected[i]}", fontsize='small')