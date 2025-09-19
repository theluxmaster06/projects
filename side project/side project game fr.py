import pygame

running = True
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Main game loop

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
pygame.quit()

# made by theluxmaster06
# this is a side project game in python with pygame

# this is a work in progress
# i will add more features later