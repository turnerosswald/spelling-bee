import tkinter as tk
import random
import time  # Import the time module to track answer times
from circle_database import get_question, get_answer, get_number_of_questions, get_topics, get_texts
import asyncio
from lmnt.api import Speech
import pygame

class CircleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Circle Growth Game")

        # Setup canvas
        self.canvas = tk.Canvas(root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight(), bg="lightgray")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        pygame.mixer.init()
        # Initialize variables
        self.circle_size = 30
        self.score = 0
        self.circles = []
        self.current_question = ""
        self.question_index = 0
        self.attempts = 0
        self.max_attempts = 3
        self.topics = get_topics()
        self.current_topic = random.choice(self.topics)
        self.question_order = self.get_new_question_order()
        self.start_time = None  # Variable to track when the question is presented

        # Animation variables
        self.text_x = self.canvas.winfo_width()
        self.text_speed = 5
        self.moving_text_label = tk.Label(self.canvas, text="", font=("Helvetica", 14), bg="lightgray")
        self.moving_text_label.place(x=self.text_x, y=10)

        # UI elements
        self.score_label = tk.Label(self.canvas, text=f"Score: {self.score}", font=("Helvetica", 14))
        self.start_game_button = tk.Button(self.canvas, text="Start Game", command=self.start_game, font=("Helvetica", 14))
        self.play_again_button = tk.Button(self.canvas, text="Play Again", command=self.play_again, font=("Helvetica", 14), state=tk.DISABLED)
        self.answer_entry = tk.Entry(self.canvas, font=("Helvetica", 14))
        self.question_label = tk.Label(self.canvas, text="", font=("Helvetica", 14), bg="lightgray")

        # Bind keys for actions
        self.root.bind('<Return>', self.enter_key_check)
        self.root.bind('<Escape>', lambda event: self.root.destroy())

        # Center start game button
        self.root.after(100, self.center_start_game_button)

    def start_game(self):
        self.reset_game_state()
        self.canvas.delete("all")
        self.text_x = self.canvas.winfo_width()
        self.update_ui_elements()
        self.next_question()

        self.moving_text_label.config(text=get_texts()[self.topics.index(self.current_topic)])
        self.animate_text()

        self.play_again_button.config(state=tk.DISABLED)
        self.create_circle()
        

    def next_question(self):
        if self.question_index < len(self.question_order):
            question_number = self.question_order[self.question_index]
            self.current_question = get_question(self.current_topic, question_number)
            self.answer_entry.delete(0, tk.END)
            self.question_label.config(text=self.current_question)
            self.attempts = 0
            self.start_time = time.time()  # Record the start time when the question is presented
        else:
            self.question_label.config(text="Game Over! All questions answered.")
            self.answer_entry.config(state=tk.DISABLED)
            self.play_again_button.config(state=tk.NORMAL)

    def center_start_game_button(self):
        self.canvas.create_window(self.root.winfo_width() // 2, self.root.winfo_height() // 2, window=self.start_game_button)

    def update_ui_elements(self):
        self.canvas.create_window(self.root.winfo_width() - self.root.winfo_width() // 10, self.root.winfo_height() // 10, window=self.score_label)
        self.canvas.create_window(self.root.winfo_width() // 2, self.root.winfo_height() - self.root.winfo_width() // 15, window=self.answer_entry)
        self.canvas.create_window(self.root.winfo_width() // 2, self.root.winfo_height() - self.root.winfo_height() // 5, window=self.question_label)
        self.canvas.create_window(self.root.winfo_width() // 10, self.root.winfo_height() - self.root.winfo_height() // 10, window=self.play_again_button)

    def enter_key_check(self, event):
        if self.question_index < len(self.question_order):
            self.check_answer()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = get_answer(self.current_topic, self.current_question).lower()

        if user_answer == correct_answer:
            elapsed_time = time.time() - self.start_time  # Calculate time taken to answer
            points = max(100 - int(elapsed_time * 10), 10)  # More points for faster answers, minimum 10 points
            self.score += points
            self.score_label.config(text=f"Score: {self.score}")
            self.question_index += 1
            self.create_large_circle()
            self.create_circle()
            self.next_question()
        else:
            self.attempts += 1
            if self.attempts < self.max_attempts:
                self.question_label.config(text=f"{self.current_question} | Wrong! Try again. Attempts left: {self.max_attempts - self.attempts}")
            else:
                self.question_label.config(text=f"{self.current_question} | Wrong! The answer was '{correct_answer}'.")
                self.question_index += 1
                self.next_question()

        self.answer_entry.delete(0, tk.END)

    def play_again(self):
        self.root.destroy()
        root = tk.Tk()
        CircleGame(root)
        root.mainloop()

    def reset_game_state(self):
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.answer_entry.delete(0, tk.END)
        self.question_label.config(text="")
        self.circle_size = 30
        self.current_topic = random.choice(self.topics)
        self.question_order = self.get_new_question_order()
        self.circles = []

    def get_new_question_order(self):
        return list(range(get_number_of_questions(self.current_topic)))

    def create_circle(self):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x0 = (canvas_width / 2) - (self.circle_size / 2)
        y0 = (canvas_height / 2) - (self.circle_size / 2)
        x1 = (canvas_width / 2) + (self.circle_size / 2)
        y1 = (canvas_height / 2) + (self.circle_size / 2)
        color = self.random_color()
        circle = self.canvas.create_oval(x0, y0, x1, y1, fill=color, outline="black", width=2)
        self.circles.append(circle)

    def create_large_circle(self):
        large_circle_size = self.circle_size + 20
        self.circle_size += 20
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        x0 = (canvas_width / 2) - (large_circle_size / 2)
        y0 = (canvas_height / 2) - (large_circle_size / 2)
        x1 = (canvas_width / 2) + (large_circle_size / 2)
        y1 = (canvas_height / 2) + (large_circle_size / 2)

        color = self.random_color()
        circle = self.canvas.create_oval(x0, y0, x1, y1, fill=color, outline="black", width=2)
        self.circles.append(circle)

    def random_color(self):
        return f'#{random.randint(0, 0xFFFFFF):06x}'

    async def speak_text(self, text):
        """Speak the given text using the Speech API."""
        async with Speech(api_key='16c541892ab44d579c0cd110ce24bb5b') as speech:  # Add your API key here
            synthesis = await speech.synthesize(text, 'lily')
            with open('temp_audio.mp3', 'wb') as f:
                f.write(synthesis['audio'])
            # Here you can add code to play the audio file if you have a player setup
            pygame.mixer.music.load('temp_audio.mp3')
            pygame.mixer.music.play()

    def animate_text(self):
        self.text_x -= self.text_speed
        if self.text_x < -self.moving_text_label.winfo_width():
            # Reset position
            self.text_x = self.canvas.winfo_width()
            # Speak the text again when it resets
            asyncio.run(self.speak_text(self.moving_text_label.cget("text")))  # Call speech synthesis
        
        self.moving_text_label.place(x=self.text_x, y=10)
        self.root.after(40, self.animate_text)

if __name__ == "__main__":
    root = tk.Tk()
    game = CircleGame(root)
    root.mainloop()
