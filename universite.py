class Etudiant():
    def __init__(self,nom_etudiant,cours_etudiant,ecole_etudiant,age_etudiant):
        self.nom = nom_etudiant
        self.cours = cours_etudiant
        self.ecole = ecole_etudiant
        self.age = age_etudiant

class Cours():
    def __init__ (self,nom_cours,duree_cours,prof_cours,age_requis_cours):
        self.nom = nom_cours
        self.duree = duree_cours
        self.prof = prof_cours
        self.age = age_requis_cours

class Professeur():
    def __init__(self,nom_professeur,cours_professeur,niveau_cours_professeur):
        self.nom = nom_professeur
        self.cours = cours_professeur
        self.niveau = niveau_cours_professeur
        