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

# This is a simple Pygame window that runs until closed by the user.