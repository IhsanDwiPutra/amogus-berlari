import pygame

WIDTH, HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ayam Berlari")


# --- Class ---
class Ayam:
    def __init__(self):
        self.rect = pygame.Rect(50, 400, 40, 60)
        self.velocity_y = 0
        self.gravity = 0.8
        self.jump_power = -15
        self.on_ground = False
    
    def jump(self):
        if self.on_ground:
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
        self.rect = pygame.Rect(WIDTH, 400, 40, 60)
        self.speed = 5
    
    def update(self):
        self.rect.x -= self.speed
        
        if self.rect.x < -30:
            self.rect.x = WIDTH

    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)

# --- Membuat Objek ---
ayam = Ayam()
kaktus = Kaktus()

# --- FPS ---
waktu = pygame.time.Clock()
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
                ayam.jump()
    
    # --- Update ---
    ayam.update()
    kaktus.update()
    
    # --- Draw ---
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (0, (400 + 60), WIDTH, 5))
    
    ayam.draw()
    kaktus.draw()
    
    pygame.display.update()
    waktu.tick(FPS)

pygame.quit()