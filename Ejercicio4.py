import pygame  

pygame.init()  

# Creamos la ventana
ventana = pygame.display.set_mode((720, 640))  
pygame.display.set_caption("HaxBall miami 5.0 - parte 2 players revolution, ahora es personal")  

ball = pygame.image.load("ball.png")#crea el objeto pelota
ballrect = ball.get_rect()#obtiene hitbox de pelota
speedball = [5, 5] #le doy velocidad inicial para que se pueda mover

# Pongo la pelota en el centro restandole el ancho del png de la bola
ballrect.move_ip((ventana.get_width()-(ball.get_width()))/2, (ventana.get_height()-(ball.get_width()))/2)

player1 = pygame.image.load("player1.png") #crea el objeto player1
player1rect = player1.get_rect() #hitbox del player1
player1rect.move_ip(300, 450) #pongo al player 1 aqui por ej

player2 = pygame.image.load("player2.png") #crea el objeto player2
player2rect = player2.get_rect() #hitbox del player2
player2rect.move_ip(380, 400) #pongo al player 2 aqui por ej



jugando = True  
while jugando:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:  # Si cierra la ventana
            jugando = False  # Terminamos el bucle

    #le damos vida al player1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1rect.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
        player1rect.move_ip(5, 0)
    if keys[pygame.K_UP]:
        player1rect.move_ip(0,-5)
    if keys[pygame.K_DOWN]:
        player1rect.move_ip(0,5)

     #le damos vida al player
    if keys[pygame.K_a]:
        player2rect.move_ip(-5, 0)
    if keys[pygame.K_d]:
        player2rect.move_ip(5, 0)
    if keys[pygame.K_w]:
        player2rect.move_ip(0,-5)
    if keys[pygame.K_s]:
        player2rect.move_ip(0,5)

        # Detectar colisiones con la pelota
    if ballrect.colliderect(player1rect):
        speedball[0] = -speedball[0]  # Rebotar horizontalmente
        speedball[1] = -speedball[1]  # Rebotar verticalmente

    if ballrect.colliderect(player2rect):
        speedball[0] = -speedball[0]  # Rebotar horizontalmente
        speedball[1] = -speedball[1]  # Rebotar verticalmente

    ballrect = ballrect.move(speedball)#se mueve la bola
    #se comprueba que toque los limites de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speedball[0] = -speedball[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speedball[1] = -speedball[1]

    ventana.fill((150, 255, 255))  # Color de fondo
    ventana.blit(ball, ballrect) #pelota agregada
    ventana.blit(player1, player1rect) #dibujo player 1
    ventana.blit(player2, player2rect) #dibujo player 2
    pygame.display.flip()  # Actualizamos la pantalla
    pygame.time.Clock().tick(60)  # Limitamos a 60 FPS


pygame.quit()  # Cerramos pygame