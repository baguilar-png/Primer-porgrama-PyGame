import pygame
pygame.init()
ANCHO = 800
ALTO = 500
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Rectángulo con WASD")
reloj = pygame.time.Clock()
x = 375
y = 225
tamano = 50
velocidad = 5
ejecutando = True
while ejecutando:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			ejecutando = False
	teclas = pygame.key.get_pressed()
	if teclas[pygame.K_w]:
		y -= velocidad
	if teclas[pygame.K_s]:
		y += velocidad
	if teclas[pygame.K_a]:
		x -= velocidad
	if teclas[pygame.K_d]:
		x += velocidad
	ventana.fill((25, 30, 40))
	pygame.draw.rect(ventana, (80, 200, 255), (x, y, tamano, tamano))
	pygame.display.flip()
	reloj.tick(60)
pygame.quit()