import pygame, os, time, random
dir = os.path.dirname(__file__)
pygame.init()
song = pygame.mixer.Sound(os.path.join(dir,'./alexa_ha.ogg'))
clock = pygame.time.Clock()
song.play()
while True:
    time.sleep(random.randrange(30,600))
    song.play()
    clock.tick(60)
pygame.quit()
