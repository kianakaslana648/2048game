import pygame
import sys
from game2048 import Game2048

# Initialize Pygame
pygame.init()

# Constants
SIZE = 400
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR = (187, 173, 160)
TILE_COLOR = {
    0: (204, 192, 179),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

FONT_COLOR = (119, 110, 101)
FONT = pygame.font.Font(None, 55)
BUTTON_FONT = pygame.font.Font(None, 35)

# Set up the display
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("2048 Game")

def draw_grid(game):
    screen.fill(BACKGROUND_COLOR)
    for r in range(GRID_LEN):
        for c in range(GRID_LEN):
            tile_value = game.grid[r][c]
            tile_rect = pygame.Rect(c * (SIZE / GRID_LEN), r * (SIZE / GRID_LEN), SIZE / GRID_LEN - GRID_PADDING, SIZE / GRID_LEN - GRID_PADDING)
            pygame.draw.rect(screen, TILE_COLOR.get(tile_value, (60, 58, 50)), tile_rect)
            if tile_value != 0:
                label = FONT.render(f'{tile_value}', True, FONT_COLOR)
                label_rect = label.get_rect(center=tile_rect.center)
                screen.blit(label, label_rect)
    pygame.display.update()

def show_message(message):
    screen.fill(BACKGROUND_COLOR)
    label = FONT.render(message, True, FONT_COLOR)
    label_rect = label.get_rect(center=(SIZE // 2, SIZE // 2 - 50))
    screen.blit(label, label_rect)

    restart_button = pygame.Rect(SIZE // 2 - 75, SIZE // 2 + 10, 150, 50)
    quit_button = pygame.Rect(SIZE // 2 - 75, SIZE // 2 + 70, 150, 50)

    pygame.draw.rect(screen, (0, 255, 0), restart_button)
    pygame.draw.rect(screen, (255, 0, 0), quit_button)

    restart_label = BUTTON_FONT.render("Restart", True, FONT_COLOR)
    quit_label = BUTTON_FONT.render("Quit", True, FONT_COLOR)

    restart_label_rect = restart_label.get_rect(center=restart_button.center)
    quit_label_rect = quit_label.get_rect(center=quit_button.center)

    screen.blit(restart_label, restart_label_rect)
    screen.blit(quit_label, quit_label_rect)

    pygame.display.update()

    return restart_button, quit_button

def main():
    game = Game2048()
    clock = pygame.time.Clock()
    pygame.key.stop_text_input()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    game.move_up()
                elif event.key == pygame.K_s:
                    game.move_down()
                elif event.key == pygame.K_a:
                    game.move_left()
                elif event.key == pygame.K_d:
                    game.move_right()
        
        draw_grid(game)

        if not game.can_move():
            restart_button, quit_button = show_message("Game Over!")
            break
        
        if game.has_won():
            restart_button, quit_button = show_message("You Win!")
            break
        
        clock.tick(10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    main()
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()
