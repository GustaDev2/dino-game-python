import pygame
import random
import sys # Para sair do jogo

# Inicialização do Pygame
pygame.init()

# Configurações da Tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Jump")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0) # Para o dinossauro e pedras, por simplicidade

# FPS
clock = pygame.time.Clock()
FPS = 60

# Dinossauro
DINO_SIZE = 30
dino_x = 50
dino_y = SCREEN_HEIGHT - DINO_SIZE - 10 # Posição inicial no chão
dino_y_velocity = 0
JUMP_STRENGTH = -15 # Negativo para ir para cima
GRAVITY = 1
is_jumping = False

# Pedras
STONE_SIZE = 20
STONE_SPEED = 5
stones = [] # Lista para guardar as pedras

def create_stone():
    """Cria uma nova pedra fora da tela à direita."""
    stone_x = SCREEN_WIDTH
    stone_y = SCREEN_HEIGHT - STONE_SIZE - 10 # No chão
    return pygame.Rect(stone_x, stone_y, STONE_SIZE, STONE_SIZE)

def game_over_screen():
    """Mostra a tela de Game Over e espera por uma ação."""
    font = pygame.font.SysFont(None, 50)
    text = font.render("Game Over! Pressione R para reiniciar", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False # Sai do loop de game over para reiniciar
                if event.key == pygame.K_ESCAPE: # Permite sair do jogo na tela de game over
                    pygame.quit()
                    sys.exit()
        clock.tick(FPS)


def game_loop():
    global dino_y, dino_y_velocity, is_jumping, stones, score

    # Reseta variáveis do jogo para um novo jogo
    dino_y = SCREEN_HEIGHT - DINO_SIZE - 10
    dino_y_velocity = 0
    is_jumping = False
    stones = []
    score = 0
    stone_spawn_timer = 0
    STONE_SPAWN_RATE = 120 # A cada X frames, uma nova pedra (ajuste conforme necessário)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping:
                    is_jumping = True
                    dino_y_velocity = JUMP_STRENGTH

        # Lógica do Pulo
        if is_jumping:
            dino_y_velocity += GRAVITY
            dino_y += dino_y_velocity
            if dino_y >= SCREEN_HEIGHT - DINO_SIZE - 10: # Se atingiu o chão
                dino_y = SCREEN_HEIGHT - DINO_SIZE - 10
                is_jumping = False
                dino_y_velocity = 0

        # Gerar Pedras
        stone_spawn_timer += 1
        if stone_spawn_timer >= STONE_SPAWN_RATE:
            stones.append(create_stone())
            stone_spawn_timer = 0
            # Aumentar a dificuldade (opcional)
            # if STONE_SPAWN_RATE > 60: STONE_SPAWN_RATE -= 2


        # Mover e remover Pedras
        for stone_rect in stones[:]: # Itera sobre uma cópia para poder remover
            stone_rect.x -= STONE_SPEED
            if stone_rect.right < 0: # Se saiu da tela pela esquerda
                stones.remove(stone_rect)
                score += 1 # Pontua quando a pedra sai da tela

        # Detecção de Colisão
        dino_rect = pygame.Rect(dino_x, dino_y, DINO_SIZE, DINO_SIZE)
        for stone_rect in stones:
            if dino_rect.colliderect(stone_rect):
                game_over_screen() # Mostra tela de game over
                return # Sai do game_loop para reiniciar no main_menu ou fechar

        # Desenho
        screen.fill(WHITE) # Fundo branco
        pygame.draw.rect(screen, RED, dino_rect) # Dinossauro (simples retângulo)

        for stone_rect in stones:
            pygame.draw.rect(screen, BLACK, stone_rect) # Pedras (simples retângulo)

        # Desenhar pontuação
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip() # Atualiza a tela inteira
        clock.tick(FPS)

# Menu principal ou loop de reinício
while True:
    game_loop() # Inicia o jogo
    # Após game_loop retornar (game over), ele volta aqui para reiniciar