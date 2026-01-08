import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 600    
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Amogus Berlari")

# --- WARNA ---
merah = (255, 0, 0)
putih = (255, 255, 255)

running = True

# --- FPS ---
time = pygame.time.Clock()
FPS = 60

# --- CLASS AMOGUS (CETAKAN ROBOT AMOGUS) ---
class Amogus:
    def __init__(self):
        # Ini adalah Setup awal si Amogus
        self.rect = pygame.Rect(50, 400, 50, 50) # Kotak (X=50, Y=300, L=40, T=60)
        self.velocity_y = 0 # Kecepatan vertikal awal
        self.gravity = 0.8 # Kekuatan gravitasi
        self.jump_power = -15 # Kekuatan loncat
        self.on_ground = False # Penanda apakah sedang napak tanah?
    
    def jump(self):
        # Cuma boleh loncat kalau sedang di tanah
        if self.on_ground:
            self.velocity_y = self.jump_power
            self.on_ground = False
    
    def update(self):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
        
        if self.rect.y >= 400:
            self.rect.y = 400
            self.velocity_y = 0
            self.on_ground = True
    
    def draw(self):
        # Gambar kotak Amogus warnah Hijau
        pygame.draw.rect(screen, (0, 255, 0), self.rect)

# --- Class Kaktus ---
class Kaktus:
    def __init__(self):
        self.rect = pygame.Rect(800, 400, 30, 50)
        self.speed = 5 # Kecepatan gerak ke kiri
    
    def update(self):
        self.rect.x -= self.speed
        
        if self.rect.x < -30:
            self.rect.x = random.randint(800, 1000)
            print(self.rect.x)
    
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

# --- SETUP GAME ---
amogus = Amogus() # Mencetak 1 Amogus dari cetakan class di atas
kaktus = Kaktus() # Cetak musuh baru

score = 0
font_game = pygame.font.Font(None, 36)

# --- GAME LOOP ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                amogus.jump()
    
    # UPDATE
    amogus.update()
    kaktus.update()
    
    score += 1
    
    if amogus.rect.colliderect(kaktus.rect):
        print("Tersentuh")
    
    # DRAW
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, putih, (0, 450, 800, 10))
    
    amogus.draw()
    kaktus.draw()
    
    score_text = font_game.render(f"Score: {score}", True, (255, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    time.tick(FPS)

pygame.quit()