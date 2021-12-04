import pygame

ALTURAa, COMPRIMENTO = 900, 500

dis = pygame.display.set_mode((ALTURAa, COMPRIMENTO))


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.QUIT()


if __name__ == "__main__":
    main()
