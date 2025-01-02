import random
import time

quotes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "I tried to fix a bug... now I have 10.",
    "There are 10 types of people in the world: those who understand binary and those who don't.",
    "I'm not lazy; I'm just on energy-saving mode.",
    "404: Quote not found.",
    "Commit early, commit often, and commit to nothing.",
    "Debugging is like being the detective in a crime movie where you are also the murderer.",
    "I have a love-hate relationship with semicolons; mostly hate.",
    "It's not a bug; it's an undocumented feature.",
    "Give a person a program, frustrate them for a day. Teach a person to program, frustrate them for a lifetime."
]

if __name__ == "__main__":
    while True:
        print(random.choice(quotes))
        time.sleep(5)  # Wait 5 seconds before printing the next quote
