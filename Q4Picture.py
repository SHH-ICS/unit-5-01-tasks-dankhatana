# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame


pygame.init()


size = (400, 400)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("My Picture")


red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


pygame.draw.rect(screen, green, [50, 50, 100, 100])


pygame.draw.circle(screen, blue, [250, 150], 50)


pygame.draw.line(screen, red, [0, 0], [400, 400], 5)


pygame.display.flip()


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


pygame.quit()
