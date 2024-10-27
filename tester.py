import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1600, 1200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("6 Frame Animation Example")

# Load animation frames
frame_count = 8  # Number of frames
frames = [pygame.image.load(f"C:/Users/turno/Downloads/run gun/pixil-frame-{i}.png") for i in range(frame_count)]

# Set up variables for animation
current_frame = 0
frame_rate = 100  # milliseconds per frame
last_update_time = pygame.time.get_ticks()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update animation frame
    current_time = pygame.time.get_ticks()
    if current_time - last_update_time > frame_rate:
        current_frame = (current_frame + 1) % frame_count  # Loop back to first frame
        last_update_time = current_time

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the current frame
    frame_x = (width // 3) - (frames[current_frame].get_width() // 3)
    frame_y = (height // 3) - (frames[current_frame].get_height() // 3)
    screen.blit(frames[current_frame], (frame_x, frame_y))

    # Update the display
    pygame.display.flip()
