import pygame
import random
import time


# Main game loop
print("would u like to start?")
start = input("yes or no? ").lower().strip()
if start == ("yes"):
    print ("game starting.")
    print ("game starting..")
    print ("game starting...")
    x = 1

elif start == ("no"):
    print("game not starting")

else:
    print ("invalid argument")



if x == 1:
    running = True
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
pygame.quit()
# This is a simple Pygame window that runs until closed by the user.