import pygame

pygame.init()

WHITE = (255, 255, 255)
font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Byrobot Python Piano", True, (0, 128, 0))

pyscreen = pygame.display.set_mode((1024,768), 0, 32)
pyscreen.fill(WHITE)
pyscreen.blit(text,(512 - text.get_width() // 2, 384 - text.get_height() // 2))
pygame.display.flip()

run = True

c4 = pygame.mixer.Sound('c4.wav')
d4 = pygame.mixer.Sound('d4.wav')
e4 = pygame.mixer.Sound('e4.wav')
f4 = pygame.mixer.Sound('f4.wav')
g4 = pygame.mixer.Sound('g4.wav')
a4 = pygame.mixer.Sound('a4.wav')
b4 = pygame.mixer.Sound('b4.wav')
c5 = pygame.mixer.Sound('c5.wav')



while run:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

            elif event.key == pygame.K_u:
                c4.play()

            elif event.key == pygame.K_y:
                d4.play()

            elif event.key == pygame.K_t:
                e4.play()

            elif event.key == pygame.K_r:
                f4.play()

            elif event.key == pygame.K_e:
                g4.play()

            elif event.key == pygame.K_w:
                a4.play()

            elif event.key == pygame.K_q:
                b4.play()

            elif event.key == pygame.K_a:
                c5.play()

            
pygame.quit()
