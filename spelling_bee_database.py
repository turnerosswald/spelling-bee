import random

sentences_dict = {
    "The happy cat chased the little mouse.": "cat",
    "The big red ball rolled down the hill.": "ball",
    "The small bird sang a sweet song.": "bird",
    "The fast rabbit hopped across the grass.": "rabbit",
    "The tall tree swayed in the gentle breeze.": "tree",
    "The shiny car zoomed down the street.": "car",
    "The cute puppy played with a colorful toy.": "puppy",
    "The bright sun shone in the clear sky.": "sun",
    "The friendly dolphin jumped in the blue ocean.": "dolphin",
    "The playful kitten pounced on the soft pillow.": "kitten"
}

def get_random_sentence():
    return random.choice(list(sentences_dict.keys()))

def get_answer(sentence):
    return sentences_dict[sentence]