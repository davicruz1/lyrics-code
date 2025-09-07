from time import sleep
import os
import sys

os.system("cls" if os.name == "nt" else "clear")

lyrics = [
    " "
]

def type_line(line, delay=0.05):
    for char in line:
        print(char, end="", flush=True)
        sleep(delay)
    print()  # quebra de linha

def printLyrics():
    for line in lyrics:
        type_line(line)
        sleep(2)  # pra pular de uma linha para outra

if __name__ == "__main__":
    printLyrics()

