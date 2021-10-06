#! /usr/bin/env python3
# coding: utf-8

import matplotlib.pyplot as plt

####
# Les fonctions de calcul
####


def transformation(nb_entree):
	"""l'operation de base de la conjoncture de syracuse,

	attrs:
		- nb_entree(int) : le nombre a calculer

	returns:
		- nb_sortie(int) : le nombre issu de la transformation
	"""
	if nb_entree % 2 == 0:
		# comme c'est un nombre pair que l'on divise permet d'eviter d'avoir un float
		nb_sortie = int(nb_entree/2)
	else:
		nb_sortie = nb_entree*3+1
	return nb_sortie


def transformation_en_chaine(nb_depart):
	""" pour un nombre donné, cherche l'intergralité de la suite jusqu'a se fin avec 1. utilse pour cela la fonction transformation()

	- attrs:
	nb_depart(int) : le nombre a transfirmer de façon recursive

	- returns:
		liste_de_la_suite(liste) : le nombre de depart puis tous ceux issus du calcul jusqu'à 1 inclus

	"""
	nb_travail = nb_depart
	liste_de_la_suite = [nb_depart]
	while nb_travail > 1:
		nb_travail = transformation(nb_travail)
		liste_de_la_suite.append(nb_travail)
	return liste_de_la_suite


def chaine_en_serie(debut, fin):
	""" permet de lancer la transformation en chaine pour de nombreux nombre à l'aide d'une boucle for
	- attrs:
	debut(int): borne inférieur de l'échantillon de calcul
	fin(int): borne inférieur de l'échantillon dde calcul

	- returns:
		liste_des série(liste) : liste de liste, comportant la série pour chaque nombre calculé

	"""
	liste_des_serie=[]
	for i in range (debut,fin+1):
		liste_des_serie.append(transformation_en_chaine(i))
	return liste_des_serie

##################
# quelques routines pour tester/expérimenter le code - peut être supprimées plus tard
##################

def testerjusteunetransformation():
	print(transformation(17))
	print(transformation(-17))

def testertransformationenchaine():
	a=(transformation_en_chaine(178))
	print(a)
	b=range(1,len(a)+1)
	fig,ax = plt.subplots()
	ax.plot(b,a)
	ax.grid()
	plt.show()

def testerchaineenserie():
	b=chaine_en_serie(15,25)
	print(b)
	fig, ax = plt.subplots()  # Create a figure and an axes.
	for i in range(len(b)):
		ax.plot(b[i], label=str(i))  # Plot some data on the axes.
	ax.set_xlabel('x label')  # Add an x-label to the axes.
	ax.set_ylabel('y label')  # Add a y-label to the axes.
	ax.set_title("Simple Plot")  # Add a title to the axes.
	ax.legend()  # Add a legend.
	plt.show()

######
# Visuel
####

def choixinteractif():
	"""
	Permet de demander à l'utilisateur ce qu'il veut faire entre plusieurs choix.
	Cela passe par une invite "input", et les fonctions sont stockées dans un dictionnaire.
	Cela boucle sans fin jusqu'à demander à quitter le programme
	"""
	user_answer="a"
	user_answer=input("Que voulez vous faire : \n tester transformation d'un nombre (tapez 1) \n toute la transformation d'un nombre (tapez 2)\n transformations pour une plage de nombre (tapez 3) \n ou quitter (tapez Q ou q) \n")
	while user_answer != "Q":
		menu={"1":testerjusteunetransformation,"2":testertransformationenchaine, "3":testerchaineenserie, "q":fin, "Q":fin}
		menu.get(user_answer,passer)()
		user_answer=input("Que voulez vous faire : \n tester transformation d'un nombre (tapez 1) \n toute la transformation d'un nombre (tapez 2)\n transformations pour une plage de nombre (tapez 3)\n ou quitter (tapez Q ou q) \n")

def passer():
	"""Pour gérer les réponses non-valides"""
	pass

def fin():
	"""Pour quitter le script"""
	print("Merci d'avoir utilisé mon programme. A une prochaine fois.")
	exit()

########################
# déclancher le script
########################

def main():
	"""pour exprimer ce qui va se passer"""
	choixinteractif()


if __name__ == "__main__":
	main()
else:
	pass
