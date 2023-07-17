import pygame
import pygame.freetype

# 初始化
pygame.init()

# 設定
SIZE = WIDTH, HEIGHT = 320, 480
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 建立視窗
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("電子計算機")
clock = pygame.time.Clock()

# 設定字體
font = pygame.font.Font('fonts/simhei.ttf', 24)

# 初始化變數
equation = ""
result = ""

# 定義按鈕
buttons = {
    "1": pygame.Rect(10, 320, 70, 50), "2": pygame.Rect(90, 320, 70, 50), "3": pygame.Rect(170, 320, 70, 50),
    "4": pygame.Rect(10, 260, 70, 50), "5": pygame.Rect(90, 260, 70, 50), "6": pygame.Rect(170, 260, 70, 50),
    "7": pygame.Rect(10, 200, 70, 50), "8": pygame.Rect(90, 200, 70, 50), "9": pygame.Rect(170, 200, 70, 50),
    "0": pygame.Rect(90, 380, 70, 50), "+": pygame.Rect(250, 380, 70, 50), "-": pygame.Rect(250, 320, 70, 50),
    "*": pygame.Rect(250, 260, 70, 50), "/": pygame.Rect(250, 200, 70, 50), "=": pygame.Rect(170, 380, 70, 50),
    "C": pygame.Rect(10, 380, 70, 50)
}

# 畫按鈕, 並且填入文字, 而且置中
def draw_button(screen, rect, text, font):
    pygame.draw.rect(screen, WHITE, rect, border_radius=5)
    text_draw = font.render(text, True, BLACK, WHITE)
    text_rect = text_draw.get_rect(center=rect.center)
    screen.blit(text_draw, text_rect)

# 計算方程式
def calculate(equation):
    try:
        return str(eval(equation))
    except ZeroDivisionError:
        return "Error"
    except Exception as e:
        return "Error"

# 遊戲主迴圈
running = True
while running:
    screen.fill(BLACK)

    # 處理事件，按下視窗的叉叉，就結束遊戲
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # 如果按下滑鼠左鍵
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for key, rect in buttons.items():
                if rect.collidepoint(event.pos):
                    if key == "=":
                        result = calculate(equation)
                        equation = ""
                    elif key == "C":
                        equation = ""
                        result = ""
                    else:
                        equation += key

    # 畫按鈕
    for key, rect in buttons.items():
        draw_button(screen, rect, key, font)

    # 顯示方程式和結果
    text = font.render("計算方式: " + equation, True, WHITE, BLACK)
    screen.blit(text, (10, 100))
    text = font.render("結果: " + result, True, WHITE, BLACK)
    screen.blit(text, (10, 140))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
