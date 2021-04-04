from database import ajout_xp
import random
import sys
import time
import os
import pygame

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 50)
pygame.display.set_caption("Space invaders")
width, height = 1800, 1000
screen=pygame.display.set_mode((width, height))
bg = pygame.transform.scale(pygame.image.load(os.path.join("images", "space.png")), (width, height))
fps=60
fpsclock=pygame.time.Clock()
blanc=(255,255,255)
noir=(0,0,0)
vert=(0,255,0)

cooldown = 50
alien_img = ["images/monstre5.png","images/alien.gif"]

class Argent:
    """
    Classe qui crée la monnaie du jeu
    """
    def __init__(self):
        """
            Définition de la position, l'image du coin
        """
        self.x = random.randrange(0,width-50)
        self.y = height - 50
        self.img = pygame.transform.scale(pygame.image.load('images/coin.png'), (50, 50)) 
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

    def affichage(self):
        """
            Affiche l'argent
        """
        screen.blit(self.img, (self.x,self.y))
        self.rect.topleft = (self.x, self.y)

    def collision(self, obj,coins):
        """
            Vérifie si il y a une collision entre le joueur et l'argent si il y en a une l'argent est retirer
            Pré:    Obj : le joueur sur l'écrant qui est la classe Joueur
                    coins : tableaux contenant l'argent
        """
        if self.rect.colliderect(obj.rect) :
            obj.argents += 1
            if self in coins:
                coins.remove(self)

class Tir:
    """
        Classe qui crée le tir
    """
    def __init__(self,x,y):
        """
            Pré: x,y qui sont la position du joueur sur l'écran
        """
        self.x = x+10
        self.y = y
        self.img = pygame.transform.scale(pygame.image.load('images/shot.gif'), (30, 100)) 
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

    def dep(self):
        """
            Déplacement du tir
        """
        self.y -= 50

    def affichage(self):
        """
            Affichage du tir
        """
        screen.blit(self.img, (self.x,self.y))
        self.rect.topleft = (self.x, self.y)

    def collision(self, ennemis,tirs):
        """
            Pré:    ennemis : tableaux qui contient les ennemis
                    tire :  tableaux qui contient les tirs
            Test la collision entre les tirs et les ennemis
        """
        if self.y < 0:
            tirs.remove(self)
        else:
            self.dep()
            self.affichage()
            for ennemi in ennemis:
                if ennemi.rect.colliderect(self):
                    ennemi.vie = 0
                    if self in tirs:
                        tirs.remove(self)

class Ennemi:
    """
        Classe qui crée l'ennemi
    """
    def __init__(self, x, y):
        """
            Placment de l'ennemi plus sa vie 
            Pré:    x,y : positionnement de l'ennemi sur l'écran
        """
        self.x = x
        self.y = y
        self.vie = 1
        self.img = pygame.transform.scale(pygame.image.load(alien_img[random.randrange(0,2)]), (70, 70)) 
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

    def dep(self):
        """
            déplacement des ennemis
        """
        self.y += 2
    
    def affichage(self):
        """
            Affichage des ennemis
        """
        screen.blit(self.img, (self.x,self.y))
        self.rect.topleft = (self.x, self.y)

    def collision(self, obj,ennemis):
        """
            Pré:    ennemis : tableaux qui contient les ennemis
                    obj : joueur
            Test collision entre ennemis et le joueur
            Test si les ennemis sont toujours sur l'écran
        """
        if self.rect.colliderect(obj.rect) :
            obj.nbr_vies -= 1
            if self in ennemis:
                ennemis.remove(self)

        if self.y > height:
            if self in ennemis:
                ennemis.remove(self)

class Joueur:
    def __init__(self):
        """
            Classe du joueur 
            contient son placement, image, argent, cooldown, vitesse
        """
        self.x = (width  / 2) - 60
        self.y = height - 50
        self.img = pygame.transform.scale(pygame.image.load('images/ship.gif'), (50, 50)) 
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.nbr_vies = 1
        self.img_vie = pygame.image.load('images/coeur.png')
        self.cooldown = 0
        self.argents = 30
        self.step = 7

    def dep(self, pas):
        """
            Pré: pas : sa vitesse de déplacement
            déplacement du joueur
        """
        self.x += pas * self.step

    def affichage(self):
        """
            affiche le joueur
        """
        screen.blit(self.img, (self.x,self.y))
        self.rect.topleft = (self.x, self.y)
        
    def affichage_vie(self, i):
        """
            affiche la vie du joueur
        """
        screen.blit(self.img_vie, (10 + i * 40, 10))

    def hors_ecran(self):
        """
            test si le joueur dépasse les bords de l'écran
        """
        if self.x > width-self.img.get_size()[0] :
            self.x = width-self.img.get_size()[0]
        elif self.x < 0 :
            self.x = 0

class Jeu():
    def __init__(self):
        """
            Classe qui contien le jeu en lui même
        """
        self.tour = 0
        self.nbr_ennemi = 0
        self.fin = False
        self.shop = False
        self.tour_fin = False
        self.coins = []
        self.ennemis = []  
        self.tirs = []
        self.joueur = Joueur()

    def affichage_texte(self):
        """
            Affiche le texte sur l'écran
        """
        screen.blit(bg,(0,0))
        texte_tour = myfont.render('Tour '+ str(self.tour), True, (255,255,255))
        texte_argent = myfont.render('Argent '+ str(self.joueur.argents), True, (255,255,255))
        screen.blit(texte_tour,(10,100))
        screen.blit(texte_argent,(10,150))

    def affichage_coins(self):
        """
            Affiche l'argent et test la collision 
        """
        for coin in self.coins:
            coin.collision(self.joueur,self.coins)
            coin.affichage()

    def affichage_joueur(self):
        """
            Affiche le joueur test si il est sur l'écran affiche sa vie
        """
        self.joueur.hors_ecran()
        self.joueur.affichage()
        for i in range(self.joueur.nbr_vies) :
            self.joueur.affichage_vie(i)

    def fin_game(self):
        """
            Test si la partie est finis
            Test à quel tour on est 
            Test si on doit aller dans le shop et l'affiche
        """
        self.joueur.cooldown +=1
        if self.joueur.nbr_vies == 0 :
            self.fin = True
        if len(self.ennemis) == 0:
            if self.tour == 0:
                self.tour +=1
                self.tour_fin = True
                self.nbr_ennemi = 10
            elif self.shop == True:
                time.sleep(0.1)
                erreur = myfont.render('Pas assez d argents ', True, (255,0,0))
                shop_argent = myfont.render('1. Vie +1, 10$ ', True, (255,255,255))
                screen.blit(shop_argent,(300,200))
                shop_vitesse_deplacement = myfont.render('2. Vitesse de deplacement +1, 15$ ', True, (255,255,255))
                screen.blit(shop_vitesse_deplacement,(300,400))
                shop_vitesse_tir = myfont.render('3. Vitesse de Tir +1, 20$ ', True, (255,255,255))
                screen.blit(shop_vitesse_tir,(300,600))
                key_input = pygame.key.get_pressed()   
                if key_input[pygame.K_F1]:
                    if self.joueur.argents >= 10:
                        self.joueur.nbr_vies +=1
                        self.joueur.argents -= 10
                    else:
                        screen.blit(erreur,(300,800))

                if key_input[pygame.K_F2]:
                    if self.joueur.argents >= 15:
                        self.joueur.step += 1
                        self.joueur.argents -= 15
                    else:
                        screen.blit(erreur,(300,800))

                if key_input[pygame.K_F3]:
                    if self.joueur.argents >= 20:
                        self.joueur.cooldown -=1
                        self.joueur.argents -= 20
                    else:
                        screen.blit(erreur,(300,800))

                if key_input[pygame.K_F4]:
                    self.shop = False
                    self.tour_fin = True
            else:
                self.shop = True
                self.tour += 1
                self.nbr_ennemi += 10
    
        if self.tour_fin:
            self.tour_fin = False
            for i in range(self.nbr_ennemi):
                self.ennemis.append(Ennemi(random.randrange(0,width-50),-random.randrange(0,800)))

    def key_deplacement(self):
        """
            Test quel touche sont appuyer pour effectuer 
            Le déplacement du joueur,le tir et l'exit
        """
        key_input = pygame.key.get_pressed()   
        if key_input[pygame.K_SPACE]:
            if self.joueur.cooldown >= cooldown:
                self.joueur.cooldown = 0
                self.tirs.append(Tir(self.joueur.x,self.joueur.y))
        if key_input[pygame.K_RIGHT]:
            self.joueur.dep(1)
            
        if key_input[pygame.K_LEFT]:
            self.joueur.dep(-1)

        if key_input[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        for eve in pygame.event.get():
            if eve.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

    def affichage_ennemis(self):
        """
            Affiche les ennemis et test leur collision
            Regarde si il y a de l'argent qui tombe
        """
        for ennemi in self.ennemis:
            ennemi.dep()
            ennemi.collision(self.joueur,self.ennemis)
            ennemi.affichage()
            if ennemi.vie == 0:
                r = random.randrange(0, 5)
                if r == 1:
                    self.coins.append(Argent())
                if ennemi in self.ennemis:
                    self.ennemis.remove(ennemi)
        
    def affichage_tir(self):
        """
            Affiche les tirs du joueur
        """
        for tir in self.tirs:
            tir.collision(self.ennemis, self.tirs)

def jeu():
    """
        Contient tous les appels de la classe Jeu pour faire fonctionner le jeu
    """
    game = Jeu()
    while not game.fin:
        game.key_deplacement()
        game.affichage_texte()
        game.affichage_coins()
        game.affichage_joueur()
        game.affichage_ennemis()
        game.affichage_tir()
        game.fin_game()
        pygame.display.update()
        fpsclock.tick(fps)



def main(pseudo_choisi):
    """
        Contient l'appel de jeu()
    """
    jeu()
    
    screen.blit(bg, (0, 0))
    lost_label = myfont.render("Game Over", 1, (255, 255, 255))
    screen.blit(lost_label, (width / 2 - lost_label.get_width() / 2, height / 2 - lost_label.get_height() / 2))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    sys.exit()
    
    
    