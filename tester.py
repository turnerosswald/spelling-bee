# set LMNT_API_KEY = 16c541892ab44d579c0cd110ce24bb5b
import asyncio
from lmnt.api import Speech
import pygame
import time

pygame.mixer.init()
async def main():
    async with Speech(api_key='16c541892ab44d579c0cd110ce24bb5b') as speech:  # Add your API key here
        synthesis = await speech.synthesize('Hello world. I hope you are having a good day. having', 'lily')
    with open('hello.mp3', 'wb') as f:
        f.write(synthesis['audio'])
    pygame.mixer.music.load('hello.mp3')
    pygame.mixer.music.play()

start_time = time.time()
asyncio.run(main())
end_time = time.time()
print(end_time-start_time)