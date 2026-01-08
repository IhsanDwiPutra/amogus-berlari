import pygame
import random

pygame.init()
pygame.mixer.init()


# --- Layar ---
TITLE = "Amogus Berlari"
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# --- Icon ---
icon_game = pygame.image.load("image\\icon.ico")
pygame.display.set_icon(icon_game)

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

class Awan:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH, 50, 60, 50)
        self.speed = 5
        
        gambar_asli = pygame.image.load("image\\awan.png").convert_alpha()
        self.gambar = pygame.transform.scale(gambar_asli, (150, 100))
    
    def update(self):
        self.rect.x -= self.speed
        
        if self.rect.x < -150:
            self.rect.x = random.randint(800, 1100)
            self.rect.y = random.randint(50, 100)
            self.speed = random.randint(1, 10)
    
    def draw(self):
        screen.blit(self.gambar, self.rect)

class BackgorundBerjalan:
    def __init__(self):
        gambar_asli = pygame.image.load("image\\gurun.jpg").convert_alpha()
        self.gambar = pygame.transform.scale(gambar_asli, (802, 400))
        
        self.y = 100
        self.x1 = 0
        self.x2 = WIDTH
        self.speed = 2
    
    def update(self):
        self.x1 -= self.speed
        self.x2 -= self.speed
        
        if self.x1 < -WIDTH:
            self.x1 = WIDTH
        
        if self.x2 < -WIDTH:
            self.x2 = WIDTH
    
    def draw(self):
        screen.blit(self.gambar, (self.x1, self.y))
        screen.blit(self.gambar, (self.x2, self.y))

# --- Objek ---
player = Player()
kaktus = Musuh()
awan1 = Awan()
bg_jalan = BackgorundBerjalan()

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
high_skor = 0

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
                    awan1 = Awan()
                    skor = 0
                    kalah_sound.stop()
                    # Gunakan fadeout biar tidak kaget
                    pygame.mixer.music.fadeout(500) # Kecilkan suara perlahan selama 0.5 detik
                    play_music(game_musik)
                    
                else:
                    player.jump()
    
    # === Logika ===
    if game_state == "main":
        bg_jalan.update()
        player.update()
        kaktus.update(skor)
        awan1.update()
        
        skor += 1
        
        if player.rect.colliderect(kaktus.rect):
            kalah_sound.play()
            game_state = "kalah"
            pygame.mixer.music.fadeout(500)
            
            if skor > high_skor:
                high_skor = skor
    
    # === Gambar ===
    screen.fill(putih)
    bg_jalan.draw()
    skor_text = main_font.render(f"Skor: {skor}", True, hitam)
    high_skor_text = main_font.render(f"High Skor: {high_skor}", True, hitam)
    
    kalah_text = kalah_font.render("GAME OVER", True, (255, 0, 0))
    skor_anda_text = main_font.render(f"Skor Anda: {skor}", True, (255, 255, 0))
    high_skor_end_text = main_font.render(f"Skor Tertinggi: {high_skor}", True, (255, 255, 0))
    
    if game_state == "menu":
        screen.blit(gambar_bg, (0, 0))
        
        # Efek Kedip
        if pygame.time.get_ticks() % 1000 < 500:
            tekan_spasi_text = main_font.render("Tekan Spasi untuk Mulai", True, hitam)
            screen.blit(tekan_spasi_text, (250, 500))
    else:
        bg_jalan.draw()
        awan1.draw()
        pygame.draw.rect(screen, (248, 247, 187), (0, 450, WIDTH, 200))
        kaktus.draw()
        player.draw()
            
        if game_state != "kalah":
            screen.blit(skor_text, (10, 10))
            screen.blit(high_skor_text, (600, 10))
        else:
            screen.blit(kalah_text, (300, 200))
            screen.blit(skor_anda_text, (300, 250))
            screen.blit(high_skor_end_text, (300, 300))
    
    # === Logika Update ===
    pygame.display.flip()
    time.tick(FPS)
pygame.quit()