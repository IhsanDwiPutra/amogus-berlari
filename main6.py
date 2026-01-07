import pygame
import random

pygame.init()
pygame.mixer.init()

# --- Layar ---
TITLE = "Amogus Berlari"
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# --- Warna ---
putih = (255, 255, 255)
hitam = (0, 0, 0)

# --- Sound ---
kalah_sound = pygame.mixer.Sound("sound\\fail2.mp3")
lompat_sound = pygame.mixer.Sound("sound\\jump.wav")

# --- Kelas ---
class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 400, 40, 50)
        self.velocity_y = 0
        self.gravity = 0.8
        self.jump_power = -15
        self.on_ground = False
        
        gambar_asli = pygame.image.load("image\\player2.png").convert_alpha()
        self.gambar = pygame.transform.scale(gambar_asli, (41, 50))
    
    def jump(self):
        if self.on_ground == True:
            lompat_sound.play()
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
        screen.blit(self.gambar, self.rect)

class Musuh:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH, (450-80), 40, 80)
        self.speed = 5
        
        gambar_asli = pygame.image.load("image\\kaktus.png").convert_alpha()
        self.gambar = pygame.transform.scale(gambar_asli, (40, 80))
    
    def update(self, skor_saat_ini):
        tambahan_speed = skor_saat_ini // 200
        self.speed = 5 + tambahan_speed
        
        if self.speed > 15:
            self.speed = 15
        
        self.rect.x -= self.speed
        
        if self.rect.x < -30:
            self.rect.x = random.randint(WIDTH, 1100)
        
    def draw(self):
        screen.blit(self.gambar, self.rect)

# --- Objek ---
player = Player()
kaktus = Musuh()

# --- Background ---
gambar_asli_bg = pygame.image.load("image\\menu.png").convert_alpha()
gambar_bg = pygame.transform.scale(gambar_asli_bg, (900, 600))

# --- Musik ---
menu_musik = "music\\Eric_Skiff_A_Night_Of_Dizzy_Spells_NC.mp3"
game_musik = "music\\Hidden_Sanctuary_NC.mp3"
# Fungsi untuk ganti Musik (Best Practice)
def play_music(file_path):
    # Unload dulu biar bersih (opsional tapi aman)
    pygame.mixer.music.unload()
    # Load musik baru
    pygame.mixer.music.load(file_path)
    # Play (-1 artinya looping selamanya)
    pygame.mixer.music.play(-1)

# --- Font ---
kalah_font = pygame.font.Font(None, 50)
main_font = pygame.font.Font(None, 36)

# --- Skor ---
skor = 0

# --- FPS ---
time = pygame.time.Clock()
FPS = 60

# --- Pengaturan ---
game_state = "menu"
running = True

play_music(menu_musik)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                game_state = "menu"
                play_music(menu_musik)
                
            if event.key == pygame.K_SPACE:
                if game_state == "menu" or game_state == "kalah":
                    game_state = "main"
                    player = Player()
                    kaktus = Musuh()
                    skor = 0
                    kalah_sound.stop()
                    # Gunakan fadeout biar tidak kaget
                    pygame.mixer.music.fadeout(500) # Kecilkan suara perlahan selama 0.5 detik
                    play_music(game_musik)
                    
                else:
                    player.jump()
    
    # === Logika ===
    if game_state == "main":
        player.update()
        kaktus.update(skor)
        
        skor += 1
        
        if player.rect.colliderect(kaktus.rect):
            kalah_sound.play()
            game_state = "kalah"
            pygame.mixer.music.fadeout(500)
    
    # === Gambar ===
    if skor <= 2000:
        screen.fill(putih)
        skor_text = main_font.render(f"Skor: {skor}", True, hitam)
    else:
        screen.fill(hitam)
        skor_text = main_font.render(f"Skor: {skor}", True, putih)
    
    kalah_text = kalah_font.render("GAME OVER", True, (255, 0, 0))
    
    if game_state == "menu":
        screen.blit(gambar_bg, (0, 0))
    else:
        player.draw()
        kaktus.draw()
        
        if skor <= 2000:
            pygame.draw.rect(screen, (116, 116, 116), (0, 450, WIDTH, 200))
        else:
            pygame.draw.rect(screen, putih, (0, 450, WIDTH, 200))
            
        screen.blit(skor_text, (10, 10))
        
        if game_state == "kalah":
            screen.blit(kalah_text, (300, 200))
    
    # === Logika Update ===
    pygame.display.flip()
    time.tick(FPS)
pygame.quit()