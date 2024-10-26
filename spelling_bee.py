import pygame
import sys
from spelling_bee_database import get_random_sentence, get_answer

# Initialize Pygame
pygame.init()

# Initialize the mixer for audio
pygame.mixer.init()

# Load audio files
audio_files = [
    pygame.mixer.Sound("C:/Users/turno/OneDrive/Documents/cs-hw/open project/answer audios/first_ans.mp3"),
    pygame.mixer.Sound("C:/Users/turno/OneDrive/Documents/cs-hw/open project/answer audios/second_ans.mp3"),
    pygame.mixer.Sound("C:/Users/turno/OneDrive/Documents/cs-hw/open project/answer audios/third_ans.mp3"),
    pygame.mixer.Sound("C:/Users/turno/OneDrive/Documents/cs-hw/open project/answer audios/final_ans.mp3")
]

# Set up the display to full screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("User Input Example")

# Load the background image
background_image = pygame.image.load("pixil-frame-0 (3).png")
background_image = pygame.transform.scale(background_image, (width, height))

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
blue = (0, 0, 255)

# Font for rendering text
font = pygame.font.Font(None, 36)
input_box_width = width * 0.5
input_box_height = height * 0.04
input_box_x = (width - input_box_width) / 2
input_box_y = height - input_box_height - 20 

# Input box
input_box = pygame.Rect(input_box_x, input_box_y, input_box_width, input_box_height)
color_inactive = gray
color_active = blue
color = color_inactive
active = False
text = ''

# Timer setup
sentence_display_time = 5000
sentence_visible = True

# Scoring and lives variables
points = 0
lives = 3
correct_answers = 0

# Start with a random sentence
current_sentence = get_random_sentence()
answer = get_answer(current_sentence)

def draw_text(surface, text, pos, font, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=pos)
    surface.blit(text_surface, text_rect.topleft)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RETURN and active:
                if text.lower() == answer:
                    points += lives
                    correct_answers += 1
                    text = ''
                    lives = 3  # Reset lives only when answered correctly

                    # Play the corresponding audio based on correct answers
                    if correct_answers <= 4:
                        audio_files[correct_answers - 1].play()  # Play the appropriate audio file

                    # Check for win condition
                    if correct_answers >= 4:
                        pygame.time.delay(2000)
                        print("You Win!")
                        pygame.quit()
                        sys.exit()
                    
                    # Get a new sentence and answer
                    current_sentence = get_random_sentence()
                    answer = get_answer(current_sentence)
                else:
                    lives -= 1
                    text = ''
                    if lives <= 0:
                        print("Lives are zero. Getting a new sentence...")
                        lives = 3  # Reset lives for the next sentence
                        current_sentence = get_random_sentence()
                        answer = get_answer(current_sentence)
            elif active:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Draw the input box
    pygame.draw.rect(screen, color, input_box, 2)

    # Render the current text in the input box
    draw_text(screen, text, (input_box.x + input_box.width / 2, input_box.y + input_box.height / 2), font, black)

    # Check if the sentence should still be visible
    if sentence_visible:
        draw_text(screen, current_sentence, (width / 2, height / 5), font, white)
        draw_text(screen, f"Spell: {answer}", (width / 2, height / 5 + 40), font, white)

    # Render the points at the top right corner
    draw_text(screen, f"Points: {points}", (2*width/3, height/2), font, white)

    # Render lives at the top right corner
    draw_text(screen, f"Lives left: {lives}", (width/3, height/2), font, white)

    # Update the display
    pygame.display.flip()
