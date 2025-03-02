import pygame
import sys

# Инициализируем Pygame
pygame.init()

a = 8

# Создаем окно
screen = pygame.display.set_mode((200*a, 150*a))

screen.fill((0, 255, 255))

# Устанавливаем название окна
pygame.display.set_caption("окно")

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(mouse_x, mouse_y)

