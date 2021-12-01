import pygame
import sys


pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()


WIDTH,HEIGHT = 500,500
WHITE = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
BLUISH = (75,75,255)
YELLOW =(255,255,0)
screen = pygame.display.set_mode((WIDTH,HEIGHT))

winksmile = pygame.image.load("winksmile.png")
winksmile = pygame.transform.scale(winksmile,(WIDTH,HEIGHT))

idle = pygame.image.load("idle.png")
idle = pygame.transform.scale(idle,(WIDTH,HEIGHT))

afraid = pygame.image.load("afraid.png")
afraid = pygame.transform.scale(afraid,(WIDTH,HEIGHT))

angry = pygame.image.load("angry.png")
angry = pygame.transform.scale(angry,(WIDTH,HEIGHT))

cry = pygame.image.load("cry.png")
cry = pygame.transform.scale(cry,(WIDTH,HEIGHT))

love = pygame.image.load("love.png")
love = pygame.transform.scale(love,(WIDTH,HEIGHT))

mask = pygame.image.load("mask.png")
mask = pygame.transform.scale(mask,(WIDTH,HEIGHT))

sad = pygame.image.load("sad.png")
sad = pygame.transform.scale(sad,(WIDTH,HEIGHT))

specks = pygame.image.load("specks.png")
specks = pygame.transform.scale(specks,(WIDTH,HEIGHT))

sunglass = pygame.image.load("sunglass.png")
sunglass = pygame.transform.scale(sunglass,(WIDTH,HEIGHT))

teeth = pygame.image.load("teeth.png")
teeth = pygame.transform.scale(teeth,(WIDTH,HEIGHT))

tounge = pygame.image.load("tounge.png")
tounge = pygame.transform.scale(tounge,(WIDTH,HEIGHT))

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif  event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_0: 
                screen.fill(WHITE)
                screen.blit(winksmile,(0,0))
                pygame.display.update()
                clock.tick(10)
            
            elif  event.key == pygame.K_1: 
                screen.fill(WHITE)
                screen.blit(sad,(0,0))
                pygame.display.update()
                clock.tick(10)

            elif  event.key == pygame.K_2: 
                screen.fill(WHITE)
                screen.blit(teeth,(0,0))
                pygame.display.update()
                clock.tick(10)

            elif  event.key == pygame.K_3: 
                screen.fill(WHITE)
                screen.blit(angry,(0,0))
                pygame.display.update()
                clock.tick(10)

            elif  event.key == pygame.K_4: 
                screen.fill(WHITE)
                screen.blit(afraid,(0,0))
                pygame.display.update()
                clock.tick(10)

            elif  event.key == pygame.K_5: 
                screen.fill(WHITE)
                screen.blit(cry,(0,0))
                pygame.display.update()
                clock.tick(10)

            elif  event.key == pygame.K_6: 
                screen.fill(WHITE)
                screen.blit(love,(0,0))
                pygame.display.update()
                clock.tick(10)

            elif  event.key == pygame.K_7: 
                screen.fill(WHITE)
                screen.blit(mask,(0,0))
                pygame.display.update()
                clock.tick(10)

            elif  event.key == pygame.K_8: 
                screen.fill(WHITE)
                screen.blit(sunglass,(0,0))
                pygame.display.update()
                clock.tick(10)

            elif  event.key == pygame.K_9: 
                screen.fill(WHITE)
                screen.blit(tounge,(0,0))
                pygame.display.update()
                clock.tick(10)


            
        elif  event.type == pygame.KEYUP:
                screen.fill(WHITE)
                screen.blit(idle,(0,0))
                pygame.display.update()
                clock.tick(10)





