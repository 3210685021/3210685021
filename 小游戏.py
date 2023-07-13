import pygame
import random
 # 游戏窗口尺寸
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
 # 方块尺寸
BLOCK_SIZE = 30
 # 方块颜色
COLORS = [
    (0, 0, 0),  # 黑色
    (255, 0, 0),  # 红色
    (0, 255, 0),  # 绿色
    (0, 0, 255),  # 蓝色
    (255, 255, 0),  # 黄色
    (255, 165, 0),  # 橙色
    (128, 0, 128),  # 紫色
]
 # 方块形状
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
]
 def draw_block(screen, x, y, color):
    pygame.draw.rect(screen, color, (x, y, BLOCK_SIZE, BLOCK_SIZE))
 def draw_board(screen, board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != 0:
                draw_block(screen, col * BLOCK_SIZE, row * BLOCK_SIZE, COLORS[board[row][col]])
 def check_collision(board, shape, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col] != 0:
                if x + col < 0 or x + col >= len(board[0]) or y + row >= len(board) or board[y + row][x + col] != 0:
                    return True
    return False
 def merge_shape(board, shape, x, y):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col] != 0:
                board[y + row][x + col] = shape[row][col]
 def clear_rows(board):
    full_rows = []
    for row in range(len(board)):
        if all(board[row]):
            full_rows.append(row)
     for row in full_rows:
        del board[row]
        board.insert(0, [0] * len(board[0]))
 def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
     board = [[0] * (WINDOW_WIDTH // BLOCK_SIZE) for _ in range(WINDOW_HEIGHT // BLOCK_SIZE)]
    shape = random.choice(SHAPES)
    x, y = WINDOW_WIDTH // BLOCK_SIZE // 2 - len(shape[0]) // 2, 0
    score = 0
     while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(board, shape, x - 1, y):
                        x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not check_collision(board, shape, x + 1, y):
                        x += 1
                elif event.key == pygame.K_DOWN:
                    if not check_collision(board, shape, x, y + 1):
                        y += 1
                elif event.key == pygame.K_SPACE:
                    while not check_collision(board, shape, x, y + 1):
                        y += 1
         if not check_collision(board, shape, x, y + 1):
            y += 1
        else:
            merge_shape(board, shape, x, y)
            clear_rows(board)
            shape = random.choice(SHAPES)
            x, y = WINDOW_WIDTH // BLOCK_SIZE // 2 - len(shape[0]) // 2, 0
            if check_collision(board, shape, x, y):
                pygame.quit()
                return
         screen.fill((255, 255, 255))
        draw_board(screen, board)
        draw_block(screen, x * BLOCK_SIZE, y * BLOCK_SIZE, COLORS[shape[0][0]])
        pygame.display.update()
        clock.tick(5)
 if __name__ == "__main__":
    main()