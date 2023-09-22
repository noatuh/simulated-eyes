import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Get screen dimensions
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Create a full-screen window with no border
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN | pygame.NOFRAME)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Eye parameters
eye_width = screen_width // 10  # Doubled the width
eye_height = screen_width // 5  # Doubled the height
eye_x_spacing = screen_width // 4
left_eye_x = (screen_width // 2) - eye_x_spacing
right_eye_x = (screen_width // 2) + eye_x_spacing
eye_y = screen_height // 2
eye_move_speed = screen_width // 300
eye_max_offset = screen_width // 30

# Behavior states
blink_time = random.randint(2000, 5000)
blink_duration = 300
blink_timer = 0
eyes_open = True
move_timer = 0
move_time = random.randint(2000, 7000)
move_direction = random.choice([-1, 1])
eye_offset = 0
eye_position = 'center'  # Can be 'left', 'center', or 'right'

def draw_eyes():
    pygame.draw.ellipse(screen, WHITE, (left_eye_x + eye_offset - eye_width//2, eye_y - eye_height//2, eye_width, eye_height))
    pygame.draw.ellipse(screen, WHITE, (right_eye_x + eye_offset - eye_width//2, eye_y - eye_height//2, eye_width, eye_height))

clock = pygame.time.Clock()
while True:
    dt = clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    # Blinking logic
    blink_timer += dt
    if blink_timer >= blink_time:
        eyes_open = not eyes_open
        if eyes_open:
            blink_time = random.randint(2000, 5000)
        else:
            blink_time = blink_duration
        blink_timer = 0

    # Eye movement logic
    move_timer += dt
    if move_timer >= move_time:
        if eye_position == 'center':
            move_direction = random.choice([-1, 1])
        elif eye_position == 'left':
            move_direction = 1
        else:
            move_direction = -1
        
        move_time = random.randint(1000, 3000)
        move_timer = 0

    if -eye_max_offset <= eye_offset + move_direction * eye_move_speed <= eye_max_offset:
        eye_offset += move_direction * eye_move_speed
        if eye_offset == eye_max_offset:
            eye_position = 'right'
        elif eye_offset == -eye_max_offset:
            eye_position = 'left'
        else:
            eye_position = 'center'

    screen.fill(BLACK)
    if eyes_open:
        draw_eyes()
    pygame.display.flip()
 