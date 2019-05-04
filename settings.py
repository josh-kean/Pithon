import pygame

class GameSettings:
    def __init__(self):
        pass

    def randomRange(axis, number_width, display_width, display_height):
        if axis == 'x':
            return random.randrange(number_width, display_width-number_width, number_width)
        if axis == 'y':
            return random.randrange(number_width,display_height-number_width,number_width)
    def numDisplay(number, x, y):
        gameDisplay.blit(number, (x, y))

    #add code to score that makes a box around text
    def score(count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Score: " +str(count), True, black)
        gameDisplay.blit(text, [display_width/2,25])

def KeyBoard(event, x_change, y_change, number_width):
    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_LEFT and x_change == 0:
            x_change = -number_width
            y_change = 0
        elif event.key == pygame.K_RIGHT and x_change == 0:
            x_change = number_width
            y_change = 0
        elif event.key == pygame.K_UP and y_change == 0:
            y_change = -number_width
            x_change = 0
        elif event.key == pygame.K_DOWN and y_change == 0:
            y_change = number_width
            x_change = 0
    return [x_change, y_change]
