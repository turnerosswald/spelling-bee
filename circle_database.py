import random

# Speech text (can be used if needed)
texts = [
    'Tigers are amazing animals known for their bright orange fur with black stripes. They live in parts of Asia, like forests and grasslands, where they can hide while hunting for food. Tigers are the biggest cats in the world and are very strong. They play an important role in nature by helping to keep the number of other animals in check. Sadly, there are fewer tigers today because of problems like losing their homes and being hunted by people. Many groups are working hard to protect tigers and their habitats, so future generations can see these beautiful cats in the wild. By helping tigers, we also help keep nature healthy and balanced!'
    , 'Dolphins are smart and friendly animals that live in the ocean. They are mammals, just like us, which means they breathe air and have babies. Dolphins have a sleek body and a big smile, making them look happy all the time! They live in groups called pods and love to play together. Dolphins communicate using sounds like clicks and whistles, which helps them find food and stay close to their friends. They eat fish and squid, using their sharp teeth to catch their meals. Dolphins are also known for jumping out of the water and doing tricks, making them fun to watch!'
    , 'Buildings are structures where people live, work, and play. They come in many shapes and sizes. Some buildings, like houses, are made for families to live in. Others, like schools are educational, are where students learn. Tall buildings, called skyscrapers, reach high into the sky and are often found in big cities. Buildings are made from materials like bricks, wood, and glass. They have roofs to keep out rain and windows that let in sunlight. Every building is important because it helps make our towns and cities special!'
    , 'Carpets are soft floor coverings that add comfort and warmth to our homes. They come in many colors, patterns, and materials. People use carpets in living rooms, bedrooms, and hallways. Some carpets are made from wool, while others are made from synthetic fibers. Carpets can make a room feel cozy and can help reduce noise. Regular cleaning is important to keep carpets looking nice and free from dirt.'
    , 'Chairs are pieces of furniture that we use to sit on. They come in many styles, such as wooden, plastic, or upholstered. Some chairs have arms, while others do not. Chairs are found in every room of the house, including the dining room, living room, and bedrooms. They can be used for relaxing, eating, or working. Comfortable chairs can make a big difference when we spend a lot of time sitting.'
    , 'Fruits are tasty foods that grow on plants. They can be sweet or sour and come in many colors. Common fruits include apples, bananas, and oranges. Fruits are healthy because they have vitamins and fiber. You can eat fruits fresh, or they can be used in salads and smoothies.'
    , 'Shoes are important items that people wear on their feet. They come in many styles, such as sneakers, sandals, and boots. Shoes help protect our feet from dirt and injuries. They can also keep our feet warm in cold weather. Many people choose shoes based on comfort and fashion. Wearing the right shoes can make walking and running easier.'
    , 'Soda is a popular drink that many people enjoy. It is fizzy and comes in various flavors, such as cola, lemon-lime, and root beer. Soda is often sweetened with sugar or artificial sweeteners. While it can be refreshing, too much soda is not good for your health. Many people drink soda with meals or during special occasions. Some people even use soda in recipes, like cakes or marinades.'
    , 'Computers are powerful tools that help us with many tasks. They can perform calculations, store information, and connect us to the internet. Many people use computers for schoolwork, games, and communication. They come in different types, including desktops, laptops, and tablets. Computers have become important in our daily lives, making tasks easier and faster.'
    , 'Phones are devices that allow us to communicate with others. They come in many forms, such as smartphones and regular mobile phones. Smartphones have features like cameras, apps, and internet access, making them very useful. People use phones to call friends, send texts, and browse the web. They have changed the way we connect with the world and stay in touch with family.'
    , 'Paper is a thin material made from trees. It is used for writing, printing, and drawing. People use paper in many forms, like notebooks, books, and envelopes. There are different types of paper, such as recycled paper and glossy paper. Paper helps us share information and create art. It is important for students and artists alike, making it a key part of our daily lives.'
    ]     

# Questions and answers
questions_dict = {
    "tigers": [
        ["What color is a tiger's fur?", "orange"],
        ["Where do tigers live?", "asia"],
        ["What is special about tigers compared to other cats?", "biggest"],
        ["Why are tigers important to nature?", "balance"],
        ["What is causing fewer tigers to exist today?", "hunting"]
    ],
    "dolphins": [
        ["What do dolphins live in?", "ocean"],
        ["What do dolphins eat?", "fish"],
        ["What type of animal are dolphins?", "mammal"],
        ["What sounds do dolphins make?", "clicks"],
        ["What do dolphins do when they jump out of the water?", "tricks"]
    ],
    "buildings": [
        ["What do buildings provide?", "shelter"],
        ["What type of building is a school?", "education"],
        ["What are tall buildings called?", "skyscrapers"],
        ["What material is commonly used in buildings?", "bricks"],
        ["What keeps rain out of buildings?", "roofs"],
        ["What do windows let in?", "sunlight"]
    ],
    "carpets": [
        ["What do carpets add to homes?", "comfort"],
        ["What are carpets made from?", "wool"],
        ["Where do people use carpets?", "bedrooms"],
        ["What do carpets help reduce?", "noise"],
        ["What keeps carpets looking nice?", "cleaning"],
        ["What colors do carpets come in?", "colors"]
    ],
    "chairs": [
        ["What do we use chairs for?", "sit"],
        ["What materials can chairs be made of?", "wooden"],
        ["Where are chairs found in the house?", "rooms"],
        ["What can comfortable chairs improve?", "sitting"],
        ["What styles do chairs come in?", "styles"],
        ["What type of chair has arms?", "armchairs"]
    ],
    "fruits": [
        ["What are fruits described as?", "tasty"],
        ["Where do fruits grow?", "plants"],
        ["Name a common fruit.", "apple"],
        ["What do fruits have that is healthy?", "vitamins"],
        ["How can you eat fruits?", "fresh"],
        ["What can fruits be used in?", "salads"]
    ],
    "shoes": [
        ["What do people wear on their feet?", "shoes"],
        ["Name a style of shoes.", "sneakers"],
        ["What do shoes help protect?", "feet"],
        ["What can shoes keep our feet warm in?", "cold"],
        ["What do people choose shoes based on?", "comfort"],
        ["What can wearing the right shoes make easier?", "walking"]
    ],
    "soda": [
        ["What type of drink is soda?", "fizzy"],
        ["Name a flavor of soda.", "cola"],
        ["What is soda often sweetened with?", "sugar"],
        ["Is too much soda good for your health?", "no"],
        ["When do people often drink soda?", "meals"],
        ["What can some people use soda in?", "recipes"]
    ],
    "computers": [
        ["What are powerful tools that help us?", "computers"],
        ["What can computers perform?", "calculations"],
        ["What do people use computers for?", "schoolwork"],
        ["What types of computers are there?", "desktops"],
        ["What do computers connect us to?", "internet"],
        ["What have computers made easier?", "tasks"]
    ],
    "paper": [
        ["What is paper made from?", "trees"],
        ["What is one use of paper?", "writing"],
        ["Name a type of paper.", "recycled"],
        ["What helps us share information?", "paper"],
        ["Who uses paper?", "students"],
        ["What can people create with paper?", "art"]
    ]
}

def get_number_of_questions(topic):
    """Return the number of questions for the given topic."""
    if topic in questions_dict:
        return len(questions_dict[topic])
    return 0

def get_question(topic, n):
    """Return the nth question for the given topic."""
    if topic in questions_dict and 0 <= n < len(questions_dict[topic]):
        return questions_dict[topic][n][0]  # Return the question
    return None

def get_answer(topic, question):
    """Return the answer for the given question in the specified topic."""
    if topic in questions_dict:
        for q, a in questions_dict[topic]:
            if q == question:
                return a  # Return the answer
    return None

def get_topics():
    """Return a list of topics available in the database."""
    return list(questions_dict.keys())

def get_texts():
    return texts