import pygame
import random
import os

from database import ajout_xp


class Joueur:

    def __init__(self):
        """
        Class créant le joueur , permet aussi de le controler et de faire déplacer son laser
        Pré:-
        Post:-
        """
        self.x = 487
        self.y = 620
        self.vie = 60
        self.img = joueur
        self.laser_img = laser_joueur
        self.mask = pygame.mask.from_surface(self.img)
        self.vie_max = 60
        self.lasers = []
        self.cool_down_counter = 0

    def dessin(self, fenetre):
        """
        affichage du joueur des lasers et de la bar de vie sur l'écran
        Pré:fenetre
        Post:-
        """
        fenetre.blit(self.img, (self.x, self.y))
        for laser in self.lasers:
            laser.dessin(fenetre)
        self.barre_vie(fenetre)

    def deplacement_laser(self, vel, objs):
        """
        deplacement des lasers plus test si il y a des collisions
        Pré: vel: int , objs : object
        """
        self.cooldown()
        for laser in self.lasers:
            laser.deplacement(vel)
            if laser.hors_ecran(height):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        global score
                        score += 20
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def cooldown(self):
        """
        Permet de gerer le timing du tir du joueur
        Pré: -
        Post: -
        """
        if self.cool_down_counter >= COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def tir(self):
        """
        Créer l'objet Tir
        """
        if self.cool_down_counter == 0:
            laser = Laser(self.x + 10, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def barre_vie(self, fenetre):
        """
        affiche la barre de vie
        Pré: display
        Post: -
        """
        pygame.draw.rect(fenetre, (0, 255, 0), (self.x, self.y + self.img.get_height() + 10, self.img.get_width()
                                                * (self.vie / self.vie_max), 10))


class Ennemi:

    def __init__(self, x, y):
        """
        Classe Ennemi sert à l'affichage, déplacement ennemi et ses lasers
        Pré: x,y :int
        Post: -
        """
        self.x = x
        self.y = y
        self.laser_img = laser_ennemi
        self.img = ennemi
        self.mask = pygame.mask.from_surface(self.img)
        self.lasers = []

    def deplacement(self, vel):
        """
        effectue le déplacement des Ennemis
        :param vel:int
        """
        self.y += vel

    def dessin(self, fenetre):
        """
        affiche l'ennemi
        :param fenetre: display
        """
        fenetre.blit(self.img, (self.x, self.y))
        for laser in self.lasers:
            laser.dessin(fenetre)

    def deplacement_laser(self, vel, obj):
        """
        deplace les lasers tirer par l'ennemi
        :param vel:int
        :param obj:objects
        """
        for laser in self.lasers:
            laser.deplacement(vel)
            if laser.hors_ecran(height):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.vie -= 10
                self.lasers.remove(laser)

    def tir(self):
        """
        Créer le tir
        """
        laser = Laser(self.x + 20, self.y + 30, self.laser_img)
        self.lasers.append(laser)


class Laser:

    def __init__(self, x, y, img):
        """
        Classe mettant en place le tir effectuer soit par le joueur ou l'ennemmi
        Pré: x,y :int , img: display
        Post: -
        """
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def dessin(self, fenetre):
        """
        Affichage du laser
        Pré: fenetre: display
        Post: -
        """
        fenetre.blit(self.img, (self.x, self.y - 20))

    def deplacement(self, vel):
        """
        deplacement du laser
        Pré: vel: int
        Post: -
        """
        self.y += vel

    def hors_ecran(self, height):
        """
        teste si le laser est hors de l'écran ou pas
        Pré: height : int
        Post: boolean
        """
        return not (self.y <= height and self.y >= -30)

    def collision(self, obj):
        """
        teste si il y a une collision
        :param obj: object
        :return: boolean
        """
        return collision(self, obj)


pygame.init()
pygame.font.init()
width, height = 1000, 780

bg = pygame.transform.scale(pygame.image.load(os.path.join("images", "space.png")), (width, height))

score = -100

fenetre = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space invaders")

joueur = pygame.image.load(os.path.join("images", "ship.gif"))
ennemi = pygame.image.load(os.path.join("images", "alien.gif"))
laser_joueur = pygame.image.load(os.path.join("images", "shot.gif"))
laser_ennemi = pygame.image.load(os.path.join("images", "shot_alien.png"))

COOLDOWN = 45


def collision(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def main(pseudo_choisi):
    fps = 60
    vel = 6
    jeu = True
    clock = pygame.time.Clock()
    vague = 0
    global score
    font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 100)
    joueur = Joueur()
    ennemis = []
    longueur_vague = 3
    vel_ennemi = 1
    perdu = False
    vel_laser = 9
    global COOLDOWN

    def reaffichage():

        fenetre.blit(bg, (0, 0))
        vague_texte = font.render(f"Vague: {vague}", 1, (255, 255, 255))
        score_texte = font.render(f"Score: {score}", 1, (255, 255, 255))
        fenetre.blit(vague_texte, (10, 10))
        fenetre.blit(score_texte, (10, 50))
        for ennemi in ennemis:
            ennemi.dessin(fenetre)
        joueur.dessin(fenetre)
        if perdu:
            lost_label = lost_font.render("Game Over", 1, (255, 255, 255))
            fenetre.blit(lost_label, (width / 2 - lost_label.get_width() / 2, height / 2 - lost_label.get_height() / 2))
            pygame.quit()
            print(vague)
            ajout_xp(score, vague, pseudo_choisi)

        pygame.display.update()

    while jeu:

        clock.tick(fps)

        reaffichage()

        if joueur.vie <= 0:
            perdu = True

        if len(ennemis) == 0:
            longueur_vague += 3
            vague += 1
            score += 100
            for i in range(longueur_vague):
                ennemi = Ennemi(random.randrange(70, width - 70), random.randrange(-1000 + vague * -100, -200))
                ennemis.append(ennemi)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and joueur.x + vel + 32 < width:
            joueur.x += vel

        if keys[pygame.K_LEFT] and joueur.x - vel > 0:
            joueur.x -= vel

        if keys[pygame.K_ESCAPE]:
            score = -100
            jeu = False

        if keys[pygame.K_SPACE]:
            joueur.tir()

        for ennemi in ennemis:
            ennemi.deplacement(vel_ennemi)
            ennemi.deplacement_laser(vel_laser, joueur)
            if random.randrange(0, fps * 3) == 1:
                ennemi.tir()
            if collision(ennemi, joueur):
                joueur.vie -= 20
                score += 20
                ennemis.remove(ennemi)
            elif ennemi.y > height:
                ennemis.remove(ennemi)

        joueur.deplacement_laser(-vel_laser, ennemis)



