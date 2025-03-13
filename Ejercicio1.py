import pygame  

pygame.init()  

# Creamos la ventana
ventana = pygame.display.set_mode((780, 700))  
pygame.display.set_caption("HaxBall miami 5.0")  

jugando = True  
while jugando:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  # Si cierra la ventana
            jugando = False  # Terminamos el bucle

    ventana.fill((150, 255, 255))  # Color de fondo
    pygame.display.flip()  # Actualizamos la pantalla
    pygame.time.Clock().tick(60)  # Limitamos a 60 FPS

pygame.quit()  # Cerramos pygame