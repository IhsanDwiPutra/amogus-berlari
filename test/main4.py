import pygame

WIDTH,HEIGHT = 800,600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Amogus Berlari")

# --- Warna ---
putih = (255, 255, 255)
hitam = (0, 0, 0)

# --- Class ---
class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 400, 41, 50)
        self.velocity_y = 0
        self.gravity = 0.8
        self.jump_power = -15
        self.on_ground = False
    
    def jump(self):
        if self.on_ground:
            self.velocity_y += self.jump_power
    
    def update(self):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
        
        if self.rect.y >= 400:
            self.rect.y = 400
            self.velocity_y = 0
            self.on_ground = True
    
    def draw(self):
        gambar_player_asli = pygame.image.load("..\data\image\player.png").convert_alpha()
        gambar_player = pygame.transform.scale(gambar_player_asli, (41,50))
        screen.blit(gambar_player, self.rect)

player = Player()

# --- FPS ---
clock = pygame.time.Clock()
FPS = 60

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
    
    player.update()
    
    screen.fill(putih)
    pygame.draw.rect(screen, hitam, (0, 450, WIDTH, 200))
    
    player.draw()
    
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()