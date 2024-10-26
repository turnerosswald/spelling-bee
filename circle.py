import tkinter as tk
import random
import time
from circle_database import*
import asyncio
from lmnt.api import Speech
import pygame

class CircleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Circle Game")

        self.width = self.root.winfo_screen_width()
        self.height = self.root.winfo_screenheight()

        self.canvas = tk.Canvas(root, self.width, self.height, bg = "lightgray")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        pygame.mixer.init()

        self.circle_size = 30
        self.score = 0
        self.circles = []
        self.current_question = ""
        self.question_index = 0
        self.attempts = 0
        self.max_attempts = 3
        self.topics = get_topics()
        self.current_topic = random.choice(self.topics)
        


if __name__ == "__main__":
    root = tk.tk()
    game = CircleGame(root)
    root.mainloop()