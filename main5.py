import pygame

WIDTH, HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ayam Berlari")

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
        pass



player = Player()

# --- Warna ---
putih = (255, 255, 255)
hitam = (0, 0, 0)

# --- Font ---
font_game = pygame.font.Font(None, 36)

score = 0

# --- FPS ---
time = pygame.time.Clock()
FPS = 60

# --- Waktu ---
start_ticks = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                player.jump()
    
    waktu = (pygame.time.get_ticks() - start_ticks) // 1000
    
    player.update()
    
    score += 1
    score_text = font_game.render(f"Score: {score}", True, hitam)
    waktu_text = font_game.render(f"Waktu: {waktu}", True, hitam)
    
    screen.fill(putih)
    pygame.draw.rect(screen, hitam, (0, 450, WIDTH, 5))
    
    player.draw()
    
    screen.blit(score_text, (10, 10))
    screen.blit(waktu_text, (10, 40))
    
    pygame.display.update()
    time.tick(FPS)

pygame.quit()