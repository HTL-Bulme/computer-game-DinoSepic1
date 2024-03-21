import pygame
import random
import sys
pygame.init()

# Setting game window dimensions
window_width = 1200
window_height = 800
game_display = pygame.display.set_mode((window_width, window_height))

fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font(None, 36)
BLACK = (0, 0, 0)

# Loading the image and scale
bg_image = pygame.image.load('military-background2.jpg')
bg_image = pygame.transform.scale(bg_image, (window_width, window_height))

#score
score = 0 
def score_text(text, font, color, x, y):
    score_image = font.render(text, True, color)
    game_display.blit(score_image,(x,y))

# Set up timing
clock = pygame.time.Clock()
countdown_seconds = 10
countdown_timer = pygame.time.get_ticks() + (countdown_seconds * 1000)

#make the mouse cursor invizible
pygame.mouse.set_visible(False)

#für bullet holes
bullet_holes = []

#load image for button/target
button_image = pygame.image.load('the-enemy.jpg')

#generate random position
def generate_random_position():
    if pygame.MOUSEBUTTONDOWN:
        x = random.randint(0, window_width - button_image.get_width())
        y = random.randint(0, window_height - button_image.get_height())
    return x, y
button_position = generate_random_position()

# Main game loop
game = True
while game:
    # Drawing hintergrund at position (0,0)
    game_display.blit(bg_image, (0, 0))

    # Draw the button on the screen
    game_display.blit(button_image, button_position)

    #Stop game when exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


        #if abfrage ob mouse gedruckt wurde und auf dem platz gibt es ein bullethole
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.load("gunshotsound.wav")
            pygame.mixer.music.play(0)
            bullet_holes.append(pygame.mouse.get_pos())
    for bullet_hole in bullet_holes:
        pygame.draw.circle(game_display, 'black', bullet_hole, 5)

    if button_position[0] < pygame.mouse.get_pos()[0] < button_position[0] + button_image.get_width() and button_position[1] < pygame.mouse.get_pos()[1] < button_position[1] + button_image.get_height():
        if event.type == pygame.MOUSEBUTTONDOWN:
            score += 1
            print(score)
            button_position = generate_random_position()


    #score
    score_text(str(score), font, BLACK, int(window_width/2), 750)


    #countdown 10 seconds
    remaining_time = max(0, (countdown_timer - pygame.time.get_ticks()) // 1000)
    #contdown 10 seconds text
    countdown_text = font.render(f"Time: {remaining_time}", True, BLACK)
    countdown_rect = countdown_text.get_rect(center=(window_width // 2, 50))
    game_display.blit(countdown_text, countdown_rect)
    #nach 10 sec wird programm beendet
    if remaining_time == 0:
        game = False


    timer.tick(fps)


    #folgt mouse position mit rotem punkt
    mouse_position = pygame.mouse.get_pos()
    pygame.draw.circle(game_display, 'red', mouse_position, 5)


    pygame.display.update()

pygame.quit()