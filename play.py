from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("hello.mp3")

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()

# infinite loop
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    print("s to play again")

    query = input("  ")
    if query == 'p':
        # Pausing the music
        mixer.music.pause()
    elif query == 's':
        mixer.music.play()
    elif query == 'r':
        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':
        # Stop the mixer
        mixer.music.stop()
        break