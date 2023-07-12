import pygame
import random
import time

# 遊戲設定
grid_size = 26
cell_size = 20
score = 0
window_size = grid_size * cell_size
score_size = 50;

FPS = 10

# 顏色設定
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# 初始化 pygame 和建立視窗
pygame.init()
screen = pygame.display.set_mode((window_size, window_size + score_size))
clock = pygame.time.Clock()
font = pygame.font.Font('fonts/simhei.ttf', 30)

class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[int(grid_size / 2), int(grid_size / 2)]]
        self.direction = 'UP'

    def draw(self):
        for element in self.elements:
            pygame.draw.rect(screen, WHITE, (element[0]*cell_size, element[1]*cell_size, cell_size, cell_size))

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])

    def update(self):
        if self.direction == 'UP':
            if len(self.elements) > 1:
                for i in range(len(self.elements)-1, 0, -1):
                    self.elements[i] = list(self.elements[i-1])
                self.elements[0][1] -= 1
            else:
                self.elements[0][1] -= 1
        if self.direction == 'DOWN':
            if len(self.elements) > 1:
                for i in range(len(self.elements)-1, 0, -1):
                    self.elements[i] = list(self.elements[i-1])
                self.elements[0][1] += 1
            else:
                self.elements[0][1] += 1
        if self.direction == 'LEFT':
            if len(self.elements) > 1:
                for i in range(len(self.elements)-1, 0, -1):
                    self.elements[i] = list(self.elements[i-1])
                self.elements[0][0] -= 1
            else:
                self.elements[0][0] -= 1
        if self.direction == 'RIGHT':
            if len(self.elements) > 1:
                for i in range(len(self.elements)-1, 0, -1):
                    self.elements[i] = list(self.elements[i-1])
                self.elements[0][0] += 1
            else:
                self.elements[0][0] += 1

snake = Snake()

class Fruit:
    def __init__(self):
        self.pos = [random.randint(1, grid_size-2), random.randint(1, grid_size-2)]

    def draw(self):
        pygame.draw.rect(screen, RED, (self.pos[0]*cell_size, self.pos[1]*cell_size, cell_size, cell_size))

fruit = Fruit()

class Wall:
    def update(self):
        # 畫出牆壁
        for i in range(grid_size):
            pygame.draw.rect(screen, GREEN, (i*cell_size, 0, cell_size, cell_size))
            pygame.draw.rect(screen, GREEN, (i*cell_size, (grid_size-1)*cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, GREEN, (0, i*cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, GREEN, ((grid_size-1)*cell_size, i*cell_size, cell_size, cell_size))

wall = Wall()

class ScoreWall:
    def update(self):
        text = font.render("分數: " + str(score), True, GRAY)
        screen.blit(text, (0, window_size + 10))

score_wall = ScoreWall()        

class EndGame:
    def update(self, end_game = False):
        if end_game == True:
            text_lines = "Game Over!\n空白鍵重新開始".split("\n")
            for i, line in enumerate(text_lines):
                text = font.render(line, True, GRAY)
                text_rect = text.get_rect(center=(window_size / 2, window_size / 2 + i * 30))
                screen.blit(text, text_rect)

end_game = EndGame()

# 遊戲主迴圈
running = True
end_running = False
while running:
    screen.fill(BLACK)

    wall.update()
    score_wall.update()
    
    # 蛇與水果的碰撞
    if snake.elements[0] == fruit.pos:
        snake.add_to_snake()
        score += 10
        fruit = Fruit()

    snake.update()
    snake.draw()
    fruit.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != 'DOWN':
                snake.direction = 'UP'
            if event.key == pygame.K_DOWN and snake.direction != 'UP':
                snake.direction = 'DOWN'
            if event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                snake.direction = 'LEFT'
            if event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                snake.direction = 'RIGHT'
        # 重新開始遊戲
        if event.type == pygame.KEYDOWN and end_running == True:
            if event.key == pygame.K_SPACE:
                end_running = False
                snake = Snake()
                fruit = Fruit()

    # 檢查蛇是否撞到邊界或自身
    if snake.elements[0][0] == 0 or snake.elements[0][1] == 0 or snake.elements[0][0] == grid_size-1 or snake.elements[0][1] == grid_size-1 or snake.elements[0] in snake.elements[1:]:
        # running = False
        end_running = True
        end_game.update(end_running)

    end_game.update(end_running)    
        
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
