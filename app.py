import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Get the screen resolution
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

# Create a borderless, fullscreen window
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN | pygame.NOFRAME)

# Eye properties
eye_width = screen_width // 4
eye_height = screen_height // 2
eye_gap = screen_width // 8
pupil_radius = eye_width // 5

# Pupil initial positions and target positions
left_pupil_position = [screen_width // 4, screen_height // 2]
right_pupil_position = [3 * screen_width // 4, screen_height // 2]
left_pupil_target = [screen_width // 4, screen_height // 2]
right_pupil_target = [3 * screen_width // 4, screen_height // 2]

# Movement speed for pupils
pupil_speed = 5

# Clock for frame rate control
clock = pygame.time.Clock()

def draw_eyes():
    pygame.draw.ellipse(screen, WHITE, (screen_width // 4 - eye_width // 2, screen_height // 2 - eye_height // 2, eye_width, eye_height))
    pygame.draw.ellipse(screen, WHITE, (3 * screen_width // 4 - eye_width // 2, screen_height // 2 - eye_height // 2, eye_width, eye_height))
    pygame.draw.circle(screen, BLACK, left_pupil_position, pupil_radius)
    pygame.draw.circle(screen, BLACK, right_pupil_position, pupil_radius)

def set_new_target_synced():
    boundary = pupil_radius + 20
    x_offset = random.randint(-eye_width // 2 + boundary, eye_width // 2 - boundary)
    y_offset = random.randint(-eye_height // 2 + boundary, eye_height // 2 - boundary)
    left_pupil_target[0] = screen_width // 4 + x_offset
    left_pupil_target[1] = screen_height // 2 + y_offset
    right_pupil_target[0] = 3 * screen_width // 4 + x_offset
    right_pupil_target[1] = screen_height // 2 + y_offset

def move_pupils_smoothly_synced():
    if abs(left_pupil_position[0] - left_pupil_target[0]) > pupil_speed:
        if left_pupil_position[0] < left_pupil_target[0]:
            left_pupil_position[0] += pupil_speed
            right_pupil_position[0] += pupil_speed
        else:
            left_pupil_position[0] -= pupil_speed
            right_pupil_position[0] -= pupil_speed

    if abs(left_pupil_position[1] - left_pupil_target[1]) > pupil_speed:
        if left_pupil_position[1] < left_pupil_target[1]:
            left_pupil_position[1] += pupil_speed
            right_pupil_position[1] += pupil_speed
        else:
            left_pupil_position[1] -= pupil_speed
            right_pupil_position[1] -= pupil_speed

blink_timer = 0
movement_timer = 0
blink_duration = 20
movement_duration = 60

set_new_target_synced()

while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Check for the "q" key press
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
    
    blink_timer += 1
    movement_timer += 1
    
    if blink_timer > 100 and blink_timer < (100 + blink_duration):
        pass
    else:
        draw_eyes()
    
    if movement_timer > movement_duration:
        set_new_target_synced()
        movement_timer = 0
    
    move_pupils_smoothly_synced()
    
    if blink_timer > 200:
        blink_timer = 0
    
    pygame.display.flip()
    clock.tick(60)