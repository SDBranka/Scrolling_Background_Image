import pygame
from pygame.locals import *
import sys
import os

def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

# define display surface			
DISPLAY_WIDTH, DISPLAY_HEIGHT = 576, 1024
HW, HH = DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2
AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT

os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

# setup pygame
pygame.init()
CLOCK = pygame.time.Clock()
DISPLAY_SCREEN = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Scrolling Background Image")
FPS = 120

background_surface = pygame.image.load("mountains.png").convert()
x = 0

# main loop
while True:
	events()

	rel_x = x % background_surface.get_rect().width
	DISPLAY_SCREEN.blit(background_surface, (rel_x - background_surface.get_rect().width, 0))
	if rel_x < DISPLAY_WIDTH:
		DISPLAY_SCREEN.blit(background_surface, (rel_x, 0))
	x -= 1
	pygame.draw.line(DISPLAY_SCREEN, (255, 0, 0), (rel_x, 0), (rel_x, DISPLAY_HEIGHT), 3)
	
	pygame.display.update()
	CLOCK.tick(FPS)