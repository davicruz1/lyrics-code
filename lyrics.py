from time import sleep
import os
import sys

# limpa a tela antes de começar (funciona em Windows/Linux/Mac)
os.system("cls" if os.name == "nt" else "clear")

lyrics = [
    "I wanna be your vacuum cleaner",
    "Breathing in your dust",
    "I wanna be your Ford Cortina",
    "I will never rust",
    "I just wanna be yours",
    "",
    "I wanna be your raincoat",
    "For those frequent rainy days",
    "I wanna be your dreamboat",
    "When you want to sail away",
    "Let me be yours",
    "",
    "I just wanna be yours..."
]

def type_line(line, delay=0.05):
    for char in line:
        print(char, end="", flush=True)
        sleep(delay)
    print()  # quebra de linha no final

def printLyrics():
    for line in lyrics:
        type_line(line)
        sleep(2)  # pequena pausa entre as linhas

if __name__ == "__main__":
    printLyrics()


