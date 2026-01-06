import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Amogus Berlari")

# --- Background ---
WARNA_BG = (255, 255, 255)

# --- Tanah ---
WARNA_TANAH = (111, 92, 150)
tanah_lebar = 800
tanah_panjang = 100
tanah_x = 0
tanah_y = 550

# --- Player ---
WARNA_PLAYER = (255, 0, 0)
player_lebar = 50
player_panjang = 50
player_x = 50
player_y = 500
player_velocity_y = 0
gravity = 0.8
jump_power = -15 # Kekuatan loncat

time = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            if event.key == pygame.K_SPACE:
                if player_y >= 500:
                    player_velocity_y += jump_power
    
    player_velocity_y += gravity
    
    player_y += player_velocity_y
    print(player_y)
    
    if player_y > 500:
        player_y = 500
        player_velocity_y = 0
    
    
    screen.fill(WARNA_BG)
    
    pygame.draw.rect(screen, WARNA_TANAH, (tanah_x, tanah_y, tanah_lebar, tanah_panjang))
    pygame.draw.rect(screen, WARNA_PLAYER, (player_x, player_y, player_lebar, player_panjang))
    
    pygame.display.update()
    time.tick(60)