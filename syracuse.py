#! /usr/bin/env python3
# coding: utf-8


"""
Programme de calcul selon la conjecture de syracuse. Il ne s'utilise qu'en mode console pour le moment.
On a plusieurs choix sur le type de calcul à faire. Des statistiques et courbe sont associées aux calcul.
Auteur : Silanoc
Dernière mise à jour majeure : 29 novembre 2021
rappel : pour tester les doctest : python3 -m doctest -v syracuse.py

Ceci est la transformation de méthodes à objets
"""

####
# bibliothèque / Dépendences
####

# import matplotlib.pyplot as plt

####
# Modèle et calcul
####

class Nombre_etudie():
    def __init__(self,valeur):
        self.valeur_du_nombre = valeur
        self.liste_de_la_suite = []
        pass

    def transformation(self,nb_entree):
        """l'opération de base de la conjoncture de syracuse si le nombre est pair ou impaire

        attrs:
            - nb_entree(int) : le nombre à calculer

        returns:
            - nb_sortie(int) : le nombre issu de la transformation
        >>> transformation(8)
        4
        >>> transformation(9)
        28
        """
        if nb_entree % 2 == 0:
            # comme c'est un nombre pair que l'on divise permet d'eviter d'avoir un float
            nb_sortie = int(nb_entree / 2)
        else:
            nb_sortie = nb_entree * 3 + 1
        return nb_sortie


    def transformation_en_chaine(self, nb_depart):
        """ pour un nombre donné, cherche l'intégralité de la suite jusqu'à la fin avec 1. Utilise pour cela la fonction transformation()
        source pour les valeurs test : wikipédia

        attrs:
            - nb_depart(int) : le nombre à transformer de façon récursive

        returns:
            - liste_de_la_suite(liste) : le nombre de départ puis tous ceux issus du calcul jusqu'à 1 inclus
        >>> transformation_en_chaine(14)
        [14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> transformation_en_chaine(15)
        [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        """
        self.nb_travail = nb_depart
        self.liste_de_la_suite = [nb_depart]
        while self.nb_travail > 1:
            self.nb_travail = self.transformation(self.nb_travail)
            self.liste_de_la_suite.append(self.nb_travail)
        return self.liste_de_la_suite

######
# Visuel et commande
######

class Gestion_affichage():
    def __init__(self):
        self.intro()
    
    def intro(self):
        """a l'ouverture du programme"""
        print("bienvenue")
        self.choixinteractif()

    def fin(self):
        """Pour quitter le script"""
        print("Merci d'avoir utilisé mon programme. A une prochaine fois.")
        exit()

    def choixinteractif(self):
            """
            Permet de demander à l'utilisateur ce qu'il veut faire entre plusieurs choix.
            Cela passe par une invite "input", et les fonctions sont stockées dans un dictionnaire.
            Cela boucle sans fin jusqu'à demander à quitter le programme
            """
            user_answer = "a"
            user_answer = input("Que voulez vous faire :  \n toute la transformation d'un nombre (tapez 2)\n transformations pour une plage de nombre (tapez 3) \n ou quitter (tapez Q ou q) \n")
            while user_answer != "Q":
                menu = {"2":self.faire_transformationenchaine, "3":self.faire_chaineenserie, "q":self.fin, "Q":self.fin}
                menu.get(user_answer,self.passer)()
                user_answer=input("Que voulez vous faire : \n toute la transformation d'un nombre (tapez 2)\n transformations pour une plage de nombre (tapez 3)\n ou quitter (tapez Q ou q) \n")

    def demandenombre(self):
        """demande un nombre entier pour faire son analyse.
        Todo : Attention, si les float, str... ne sont pas accepté, les entiers négatif passent !
        args : 
            - aucune
        returns : 
            - nombre(integer)
        """
        nombre = input("Veuillez entrer un nombre entier positif \n")
        while nombre != int or nombre < 0 :
            try :
                nombre = int(nombre)
                return nombre
            except :
                nombre = input("Veuillez entrer un nombre entier positif \n")

    def faire_transformationenchaine(self):
        """ fait la totalité des calculs pour un nombre rentré au clavier.
        Pour ce nombre, fait l'analyse et print, trace le graphique de vol"""
        self.nombreatester = self.demandenombre()
        lenombreatransformer = Nombre_etudie(self.nombreatester)
        a = (lenombreatransformer.transformation_en_chaine(self.nombreatester))
        print(a)
        #print(analyse_un_vol(a))
        #graphique_un_vol(a)
    
    def faire_chaineenserie(self):
        """ fait la totalité des calculs pour une série de nombre consécutif dont les bornes sont rentrées au clavier.
        Pour ces nombres, fait l'analyse et print, trace le graphique de vol
        Todo : génére des erreurs
        """
        print("entrer deux nombre entier positif croissant")
        self.nombreatester1 = self.demandenombre()
        self.nombreatester2 = self.demandenombre()
        lenombreatransformer1 = Nombre_etudie(self.nombreatester1)
        lenombreatransformer2 = Nombre_etudie(self.nombreatester2)
        #b=chaine_en_serie(15,17)
        b = Nombre_etudie.chaine_en_serie(lenombreatransformer1,lenombreatransformer2)
        #print(b)
        #print(analyse_multi_vol(b)) #générer une ereuur "list index out of range"
        #graphique_multi_vol(b)

    def passer(self):
        """Pour gérer les réponses non-valides"""
        pass


class Vrac():
    def chaine_en_serie(debut, fin):
        """ permet de lancer la transformation en chaine pour de nombreux nombre à l'aide d'une boucle for

        attrs:
            - debut(int): borne inférieur de l'échantillon de calcul
            - fin(int): borne inférieur de l'échantillon dde calcul

        returns:
            - liste_des série(liste) : liste de liste, comportant la série pour chaque nombre calculé
        >>> chaine_en_serie(14,15)
        [[14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]]
        """
        liste_des_serie = []
        for i in range(debut, fin+1):
            liste_des_serie.append(transformation_en_chaine(i))
        return liste_des_serie


    #####
    # les fonctions d'analyse
    #####

    def analyse_un_vol(vol):
        """analyse les caractéristiques d'un vol.
        le vocabulaire est issus de la page wikipédia.

        attrs:
            - vol(chaine): la chaine à analyser, c'est à dire une liste d'entier. Elle est typiquement issue de transformation_en_chaine()

        returns:
            - analyse_totale : une liste avec les variables analysés sous forme de f-string puis les valeurs brutes
        >>> analyse_un_vol([15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1])
        ['temps de vol : 18 - altitude maximale : 160 - temps de vol en altitude : 10', 160, 18, 10]
        """
        altitude_maximal = max(vol)
        temps_de_vol = len(vol)

        temps_de_vol_en_altitude = 0
        for i in range(0, len(vol)):
            if vol[i] > vol[0]:
                temps_de_vol_en_altitude += 1
        temps_de_vol_en_altitude -= 1  # je comprends pas pq, mais permet de retomber sur l'exemple de wikipedia

        analyse_textuelle = f"temps de vol : {temps_de_vol} - altitude maximale : {altitude_maximal} - temps de vol en altitude : {temps_de_vol_en_altitude}"
        analyse_totale = [analyse_textuelle, altitude_maximal, temps_de_vol, temps_de_vol_en_altitude]

        return analyse_totale

    def graphique_un_vol(vol):
        """Fonction servant à afficher un graphique du vol pour 1 seul nombre.

        attrs :
            - vol(liste): la chaine à analyser, c'est à dire une liste d'entier. Elle est typiquement issue de transformation_en_chaine() 

        returns:
            - pas de valeur, se contente d'afficher le graphique
        """

        b=range(1, len(vol) + 1)
        fig, ax = plt.subplots()
        ax.plot(b, vol)
        ax.grid()
        ax.legend(f"graphique de vol pour le nombre {vol[0]}")
        ax.set_xlabel('temps de vol')  # Add an x-label to the axes.
        ax.set_ylabel('altitude')
        plt.show()


    def analyse_multi_vol(liste_de_vol):
        """analyse les caractéristiques de plusieurs vol.
        Todo : trouver pourquoi elle ne fonctionne pas !

        attrs:
            - vol(chaine): la chaine à analyser, c'est à dire une liste de liste d'entier. liste issue de chaine_en_serie()

        returns:
            - analyse_totale : une liste avec les variables analysés sous forme de f-string puis les valeurs brutes
        >>> analyse_multi_vol([14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1])
        'ne fonctionne pas'
        """

        # liste des altitudes, liste des temps de vol
        liste_altitudes = []
        liste_temps_vol = []
        for i in range(0, len(liste_de_vol)):
            liste_altitudes.append(max(liste_de_vol[i]))    
            liste_temps_vol.append(len(liste_de_vol[i]))
        # liste des vols en altitute
        liste_vol_en_altitude = []
        for i in range(0, len(liste_de_vol)):
            temps_de_vol_en_altitude = 0
            for j in range(0, len(liste_de_vol)):
                if liste_de_vol[i][j] > liste_de_vol[i][0]:
                    temps_de_vol_en_altitude += 1
            #temps_de_vol_en_altitude-=1 #je comprends pas pq, mais permet de retomber sur l'exemple de wikipedia
            # WARNING erreur sur ce calcul. Ca fonctionne très bien sur un seul nombre, mais pas sur une série !
            liste_vol_en_altitude.append(temps_de_vol_en_altitude)
        # analyse par chiffre et analyse textuelle par chiffre
        analyse_par_chiffre = []
        liste_analyse_textuelle = []
        for i in range(0, len(liste_de_vol)):
            analyse_par_chiffre.append([liste_de_vol[i][0], liste_altitudes[i], liste_temps_vol[i], liste_vol_en_altitude[i]])
            print(analyse_par_chiffre)
            # phrase supprimé en attendant la correction
            # phrase=f"pour le nombre {analyse_par_chiffre[i][0]}, l'altitude maximale est {analyse_par_chiffre[i][1]}, le temps de vol est {analyse_par_chiffre[i][2]} et le vol en altitude vaut {analyse_par_chiffre[i][3]}"
            phrase = f"pour le nombre {analyse_par_chiffre[i][0]}, l'altitude maximale est {analyse_par_chiffre[i][1]}, le temps de vol est {analyse_par_chiffre[i][2]}"
            liste_analyse_textuelle.append(phrase)
        return analyse_par_chiffre, liste_analyse_textuelle
        # plus grande altitude, temps de vol, vol en altitude
        

    def graphique_multi_vol(liste_de_vol):
        """Fonction servant à afficher un graphique du vol pour plusieurs nombres

        attrs :
            - vol(liste): liste de liste de chiffre, typiquement issue du calcul 

        returns:
            - pas de valeur, se contente d'afficher le graphique
        """
        fig, ax = plt.subplots()  # Create a figure and an axes.
        for i in range(len(liste_de_vol)):
            ax.plot(liste_de_vol[i], label=str(i))  # Plot some data on the axes.
        ax.set_xlabel('temps de vol')  # Add an x-label to the axes.
        ax.set_ylabel('altitude')  # Add a y-label to the axes.
        ax.set_title("graphique de vol pour une plage de  nombre")  # Add a title to the axes.
        ax.legend("graphique de vol pour une plage de  nombre")  # Add a legend.
        plt.show()

    
########################
# déclancher le script
########################

def main():
    """pour exprimer ce qui va se passer"""
    affiche = Gestion_affichage()
    
    
    """ nb = Nombre_etudie(15)
    print(nb.valeur_du_nombre)
    nb.transformation_en_chaine(nb.valeur_du_nombre)
    print(nb.liste_de_la_suite) """

if __name__ == "__main__":
    main()
else:
    pass