import pygame

running = True
size = width, height = 1000, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Наступи на товарища")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("white"))
    pygame.display.flip()
pygame.quit()
