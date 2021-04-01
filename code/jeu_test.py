import pygame
import random
import sys
import time
import os
from pygame import mixer

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
    def __init__(self):
        self.x = random.randrange(0,width-50)
        self.y = height - 50
        self.img = pygame.transform.scale(pygame.image.load('images/coin.png'), (50, 50)) 
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

    def affichage(self):
        screen.blit(self.img, (self.x,self.y))
        self.rect.topleft = (self.x, self.y)

    def collision(self, obj):
        if self.rect.colliderect(obj.rect) :
            obj.argents += 1
            if self in coins:
                coins.remove(self)

class Tir:
    def __init__(self,x,y):
        self.x = x+10
        self.y = y
        self.img = pygame.transform.scale(pygame.image.load('images/shot.gif'), (30, 100)) 
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

    def dep(self):
        self.y -= 50

    def affichage(self):
        screen.blit(self.img, (self.x,self.y))
        self.rect.topleft = (self.x, self.y)

    def collision(self):
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
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vie = 1
        self.img = pygame.transform.scale(pygame.image.load(alien_img[random.randrange(0,2)]), (70, 70)) 
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)

    def dep(self):
        self.y += 2
    
    def affichage(self):
        screen.blit(self.img, (self.x,self.y))
        self.rect.topleft = (self.x, self.y)

    def collision(self, obj):
        if self.rect.colliderect(obj.rect) :
            obj.nbr_vies -= 1
            if self in ennemis:
                ennemis.remove(self)

        if self.y > height:
            if self in ennemis:
                ennemis.remove(self)

class Joueur:
    def __init__(self):
        self.x = (width  / 2) - 60
        self.y = height - 50
        self.img = pygame.transform.scale(pygame.image.load('images/ship.gif'), (50, 50)) 
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.nbr_vies = 3
        self.img_vie = pygame.image.load('images/coeur.png')
        self.cooldown = 0
        self.argents = 30
        self.step = 7

    def dep(self, pas):
        self.x += pas * self.step

    def affichage(self):
        screen.blit(self.img, (self.x,self.y))
        self.rect.topleft = (self.x, self.y)
        
    def affichage_vie(self, i):
        screen.blit(self.img_vie, (10 + i * 40, 10))

    def hors_ecran(self):
        if self.x > width-self.img.get_size()[0] :
            self.x = width-self.img.get_size()[0]
        elif self.x < 0 :
            self.x = 0

def jeu():
    tour = 0
    fin = False
    nbr_ennemi = 0
    global ennemis, tirs, coins
    coins = []
    ennemis = []  
    tirs = []
    shop = False
    joueur = Joueur()
    tour_fin = False
    while not fin:
        screen.blit(bg,(0,0))
        texte_tour = myfont.render('Tour '+ str(tour), True, (255,255,255))
        texte_argent = myfont.render('Argent '+ str(joueur.argents), True, (255,255,255))
        screen.blit(texte_tour,(10,100))
        screen.blit(texte_argent,(10,150))
        
        for coin in coins:
            coin.collision(joueur)
            coin.affichage()

        joueur.hors_ecran()
        joueur.affichage()
        for i in range(joueur.nbr_vies) :
            joueur.affichage_vie(i)

        if len(ennemis) == 0:
            if tour == 0:
                tour +=1
                tour_fin = True
                nbr_ennemi = 10
            elif shop == True:
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
                    if joueur.argents >= 10:
                        joueur.nbr_vies +=1
                        joueur.argents -= 10
                    else:
                        screen.blit(erreur,(300,800))

                if key_input[pygame.K_F2]:
                    if joueur.argents >= 15:
                        joueur.step += 1
                        joueur.argents -= 15
                    else:
                        screen.blit(erreur,(300,800))

                if key_input[pygame.K_F3]:
                    if joueur.argents >= 20:
                        cooldown -=1
                        joueur.argents -= 20
                    else:
                        screen.blit(erreur,(300,800))

                if key_input[pygame.K_F4]:
                    shop = False
                    tour_fin = True
            else:
                shop = True
                tour += 1
                nbr_ennemi += 10
                    


        if tour_fin:
            tour_fin = False
            for i in range(nbr_ennemi):
                ennemis.append(Ennemi(random.randrange(0,width-50),-random.randrange(0,800)))

            
        for ennemi in ennemis:
            ennemi.dep()
            ennemi.collision(joueur)
            ennemi.affichage()
            if ennemi.vie == 0:
                r = random.randrange(0, 5)
                if r == 1:
                    coins.append(Argent())
                if ennemi in ennemis:
                    ennemis.remove(ennemi)
              
        if joueur.nbr_vies == 0 :
            fin = True

        for tir in tirs:
            tir.collision()

        joueur.cooldown +=1
        key_deplacement(joueur)

        pygame.display.update()
        fpsclock.tick(fps)

def key_deplacement(joueur):
    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_SPACE]:
        if joueur.cooldown >= cooldown:
            joueur.cooldown = 0
            tirs.append(Tir(joueur.x,joueur.y))
    if key_input[pygame.K_RIGHT]:
        joueur.dep(1)
        
    if key_input[pygame.K_LEFT]:
        joueur.dep(-1)

    if key_input[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

def main():
    while True:
        jeu()
        screen.fill(vert)
        for eve in pygame.event.get():
            if eve.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
    
