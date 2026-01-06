import pygame
import random

WIDTH, HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ayam Berlari")

# --- Warna ---
putih = (255, 255, 255)
hitam = (0, 0, 0)
hijau = (0, 255, 0)

# --- Class ---
class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 400, 50, 50)
        self.velocity_y = 0
        self.gravity = 0.8
        self.jump_power = -15
        self.on_ground = False
    
    def jump(self):
        if self.on_ground == True:
            self.velocity_y += self.jump_power
            self.on_ground = False
    
    def update(self):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
        
        if self.rect.y >= 400:
            self.rect.y = 400
            self.velocity_y = 0
            self.on_ground = True
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

class Kaktus:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH, 400, 40, 50)
        self.speed = 5
    
    def update(self):
        self.rect.x -= self.speed
        
        if self.rect.x < -30:
            self.rect.x = random.randint(800, 1100)
    
    def draw(self):
        pygame.draw.rect(screen, hijau, self.rect)


player = Player()
kaktus = Kaktus()

# --- Font ---
font_game = pygame.font.Font(None, 36)

score = 0

# --- FPS ---
time = pygame.time.Clock()
FPS = 60

# --- Waktu ---
start_ticks = pygame.time.get_ticks()

running = True

# --- Status Game ---
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
            if event.key == pygame.K_SPACE:
                # LOGIKA: Kalau game jalan -> Loncat
                if not game_over:
                    player.jump()
                # LOGIKA: Kalau game over -> Restart
                else:
                    game_over = False
                    score = 0
                    start_ticks = pygame.time.get_ticks()
                    player = Player()
                    kaktus = Kaktus()
    
    # === UPDATE LOGIC ===
    if not game_over:
        waktu = (pygame.time.get_ticks() - start_ticks) // 1000
        
        player.update()
        kaktus.update()
        
        # Cek Tabrakan
        if player.rect.colliderect(kaktus.rect):
            game_over = True
        
        # Tambah Skor
        score += 1
    
    # === DRAWING ===
    screen.fill(putih)
    pygame.draw.rect(screen, hitam, (0, 450, WIDTH, 5))
    
    player.draw()
    kaktus.draw()
    
    # UI Teks
    score_text = font_game.render(f"Score: {score}", True, hitam)
    waktu_text = font_game.render(f"Waktu: {waktu}", True, hitam)
    
    screen.blit(score_text, (10, 10))
    screen.blit(waktu_text, (10, 40))
    
    # === GAMBAR LAYAR KALAH ===
    if game_over:
        kalah_text = font_game.render("AYAM GORENG! (Tekan Spasi)", True, (255, 0, 0))
        screen.blit(kalah_text, (250, 250))
    
    
    
    pygame.display.update()
    time.tick(FPS)

pygame.quit()