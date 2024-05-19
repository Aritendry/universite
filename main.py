from universite import *

#declaration des variables

cours_etudiant=str("")
ecole_etudiant=str("")
age_etudiant=int(0)

#Creation des professeurs

professeur_anlgais = Professeur("Mr Jean-Claude","anglais","F","M")
professeur_francais = Professeur("Mr Batiste-Dupont","francais","C","F")
professeur_techno = Professeur("Mr John-Doe","techno","B","F")
professeur_chinois = Professeur("Mme Xio-Fei","chinois","A","M")

#Creation des cours

cours_anglais = Cours(professeur_anlgais.cours,180,professeur_anlgais.nom)
cours_francais = Cours(professeur_francais.cours,180,professeur_francais.nom)
cours_techno = Cours(professeur_techno.nom,180,professeur_techno.nom)
cours_chinois = Cours(professeur_chinois.cours,180,professeur_chinois.nom)

#creation des Etudiants

etuidiant_n1 = Etudiant("aritendry",cours_etudiant,ecole_etudiant,age_etudiant)

