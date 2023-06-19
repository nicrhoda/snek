# imports 
import pygame, sys, time, random

# layout gameboard
board_x = 720
board_y = 480


# initialize pygame
pygame.init()
pygame.display.set_caption('Snek')
board = pygame.display.set_mode((board_x, board_y))

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


# set score and start positioning
snek_position = [100, 50]
snek_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
apple_position = [random.randrange(1, (board_x//10)) * 10, random.randrange(1, (board_y//10)) * 10]
apple_spawn = True
score = 0
dir = 'down'
move = dir
fps = pygame.time.Clock()


# logic for the game
def ded():
    font = pygame.font.SysFont('comic sans', 50)
    popup = font.render('rip', True, black)
    popupbox = popup.get_rect()
    popupbox.midtop = (board_x/2, board_y/2)
    board.fill(black)
    board.blit(popup, popupbox)
    display_score(0, black, 'comic sans', 20)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit

def display_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_board = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_board.get_rect()
    if choice == 1:
        score_rect.midtop = (board_x/10, 15)
    else:
        score_rect.midtop = (board_x/2, board_y/1.25)
    board.blit(score_board, score_rect)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move = 'up'
            if event.key == pygame.K_DOWN:
                move = 'down'
            if event.key == pygame.K_RIGHT:
                move = 'right'
            if event.key == pygame.K_LEFT:
                move = 'left'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    if move == 'up' and dir != 'down':
        dir = 'up'
    if move == 'down' and dir != 'up':
        dir = 'down'
    if move == 'right' and dir != 'left':
        dir = 'right'
    if move == 'left' and dir != 'right':
        dir = 'left'
    if dir == 'up':
        snek_position[1] -= 10
    if dir == 'down':
        snek_position[1] += 10
    if dir == 'right':
        snek_position[0] += 10
    if dir == 'left':
        snek_position[0] -= 10
    snek_body.insert(0, list(snek_position))
    if snek_position[0] == apple_position[0] and snek_position[1] == apple_position[1]:
        score += 1
        apple_spawn = False
    else:
        snek_body.pop()
    if not apple_spawn:
        apple_position = [random.randrange(1, (board_x//10)) * 10, random.randrange(1, (board_y//10)) * 10]
    apple_spawn = True

# game board
    board.fill(black)
    for pos in snek_body:
        pygame.draw.rect(board, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(board, red, pygame.Rect(apple_position[0], apple_position[1], 10, 10))
    if snek_position[0] < 0 or snek_position[0] > board_x-10:
        ded()
    if snek_position[1] < 0 or snek_position[1] > board_y-10:
        ded()
    for block in snek_body[1:]:
        if snek_position[0] == block[0] and snek_position[1] == block[1]:
            ded()
    display_score(1, white, 'comic sans', 20)
    pygame.display.update()
    fps.tick(20)

# high score and retry 

# hud for player score