import asyncio
from lmnt.api import Speech
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

async def main():
    # Retrieve the API key from environment variables
    api_key = os.getenv('LMNT_API_KEY')

    # Check if the API key was loaded correctly
    if not api_key:
        raise ValueError("LMNT_API_KEY not found. Please make sure it's set in your .env file.")

    async with Speech(api_key=api_key) as speech:
        synthesis = await speech.synthesize("photosynthesis", 'lily')

    # Save the audio file
    with open('hello.mp3', 'wb') as f:
        f.write(synthesis['audio'])

asyncio.run(main())