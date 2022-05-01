from ast import While
import random
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui


#    Première partie Générer les mails que l'on va utiliser par la suite

def generateName():
     # Ouverture des fichier de noms et prenoms
     nomFile = open("noms.txt", "r")
     prenomFile = open("prenoms.txt", "r")

     # Récupération du contenu des fichiers et fermeture des fichiers
     noms = nomFile.read().lower().split()
     nomFile.close()
     prenoms = prenomFile.read().lower().split()
     prenomFile.close()

     # Création d'une adresse random "nom.prenom9999999999"
     Adresse = random.choice(prenoms) + random.choice(noms) + str(random.randrange(99999999999))

     # Retourne l'adresse crée pour l'utiliser
     return Adresse




#    Création d'une la liste d'adresse mail
def CreerListe():
     for i in range(2000):
          SaveEmail("mails.txt" , generateName()+"@cuvox.de")
     



# Enregistrer un email dans un fichier
def SaveEmail(fichier , email):
     # ouvrir le fichier contenant les email en mode lecture / ajout de contenu
     fichier = open(fichier, "a")

     # On enregistre l'adresse en parametre dans le fichier
     fichier.write(email + '\n') 
     fichier.close()



#Supprimer un email d'un fichier
def SupprimerMail(fichier, email):
     # Ouverture du fichier pour recuperer tous les éléments
     FileDefault = open(fichier, "r")
     
     # Récupération du contenu du fichier et fermeture du fichier
     emails = FileDefault.read().lower().split()
     FileDefault.close()

     #on ouvre le fichier en mode ecriture et on réécrit les élément que si ca ne correspond pas a ce qu'on veut supprimer, ca le supprime du coup
     FileCorrected = open(fichier, "w")

     for unemail in emails:
          if unemail != email:
               FileCorrected.write(unemail + '\n')
     
     FileCorrected.close()



#    Seconde partie voter sur le site en utilisant les mails crées

def VoterEnligne(email):
     try:
          url = "https://velfiepitch.com/concours/affichage/3F70D08B4366/candidat/D3BAC02C24EF"
          driver = webdriver.Firefox()
          driver.get(url)    

          driver.find_element(By.XPATH ,'//*[@id="vote_19769"]/div[2]/div[13]/div[1]/div/div/div[2]/div').click()
          time.sleep(1)
          pyautogui.press('9')
          # # create action chain object
          action = ActionChains(driver)
          
          # Bombarde la flèche pour passer la video tant que le texte n'est pas "voter !"
          tempsAttente = 0.2
          while(driver.find_element(By.XPATH ,'//*[@id="label_bt_submit_vote"]').text != "VOTER !"):
               action.key_down(Keys.RIGHT).key_up(Keys.RIGHT).perform()
               time.sleep(tempsAttente)

          # clic sur le bouton pour voter
          time.sleep(0.5)
          driver.find_element(By.XPATH ,'//*[@id="label_bt_submit_vote"]').click()

          # On rentre l'email puis on valide
          driver.find_element(By.XPATH, '//*[@id="mailbox"]').send_keys(email)
          time.sleep(1)
          driver.find_element(By.XPATH, '//*[@id="label_bt_validemail"]').click()

          driver.close()

          SaveEmail("mailsvotes.txt", email)
          SupprimerMail("mails.txt", email)

          print("L'email " + email + " a bien voté sur le site")
     
     except:
          print("Une erreur est survenue pendant le vote en ligne")
          pass


#    Dernière partie Lire les mails recu sur le mail principal (gmail) et valider la participation en cliquant sur le lien



# Test du programme

# EnregistrerRedirectionMail(generateName())


# EmailFile = open("mails.txt", "r")
# emails = EmailFile.read().lower().split()
# EmailFile.close()

VoterEnligne("bonjourbonjour@cuvox.de")
# http://www.fakemailgenerator.com/#/cuvox.de/bonjourbonjour/

# EnregistrerRedirectionMail(generateName())

