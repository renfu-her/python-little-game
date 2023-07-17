import pygame
import random

# 初始化 Pygame
pygame.init()

# 創建一個遊戲窗口
screen = pygame.display.set_mode((640, 480))

# 創建蛇
snake = [pygame.Rect(0, 0, 20, 20)]

# 創建食物
food = pygame.Rect(320, 240, 20, 20)
while food.collidelist(snake) != -1:
    food.x = random.randint(0, 620)
    food.y = random.randint(0, 460)

# 設置計時器
clock = pygame.time.Clock()
move_timer = 0
move_direction = "right"

# 遊戲主迴圈
running = True
while running:
    # 處理輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 按鍵控制蛇的方向
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and move_direction != "down":
                move_direction = "up"
            elif event.key == pygame.K_DOWN and move_direction != "up":
                move_direction = "down"
            elif event.key == pygame.K_LEFT and move_direction != "right":
                move_direction = "left"
            elif event.key == pygame.K_RIGHT and move_direction != "left":
                move_direction = "right"

    # 檢查計時器
    move_timer += clock.tick(10)
    if move_timer > 100:
        # 當計時器超過 100 毫秒時，更新蛇的位置
        if move_direction == "up":
            snake[0].y -= 20
        elif move_direction == "down":
            snake[0].y += 20
        elif move_direction == "left":
            snake[0].x -= 20
        elif move_direction == "right":
            snake[0].x += 20
        snake[0].x = snake[0].x % 640
        snake[0].y = snake[0].y % 480
        for i in range(len(snake) - 1, 0, -1):
            snake[i].x = snake[i - 1].x
            snake[i].y = snake[i - 1].y
        move_timer = 0

    # 繪製蛇和食物
    screen.fill((0, 0, 0))
    for block in snake:
        pygame.draw.rect(screen, (255, 0, 0), block)
    pygame.draw.rect(screen, (0, 255, 0), food)

    # 當蛇吃掉食物時，增加蛇的長度
    if snake[0].colliderect(food):
        snake.append(snake[-1].copy())
        while food.collidelist(snake) != -1:
            food.x = random.randint(0, 620)
            food.y = random.randint(0, 460)

    # 檢查蛇是否碰到自己
    for block in snake[1:]:
        if snake[0].colliderect(block):
            # running = False
            print('Game Over')

    # 更新屏幕
    pygame.display.flip()

# 退出 Pygame
pygame.quit()