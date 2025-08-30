""" from random import choice, sample
from platform import system, version

my_list = []

try:
    for i in range(10):
        info = int(input('Enter a number: '))
        my_list.append(info)
except ValueError:
    print('Invalid input. Please enter a number...')

total = sum(my_list)
number_marks = len(my_list)
average = total / number_marks

print(f'Your list of marks is: {my_list}')
print(f'And your average score is: {average}')
print(f'Randomly picking up a number from the list: {choice(my_list)}')
print(f'Randomly picking up three numbers from the list {sample(my_list, 3)}')

print(system())
print(version()) """

import pygame
 
run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
  for event in pygame.event.get():
   if event.type == pygame.QUIT\
   or event.type == pygame.MOUSEBUTTONUP\
   or event.type == pygame.KEYUP:
    run = False