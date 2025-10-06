import sys
from rich import print 
from time import sleep
import time

def printLyrics():
    lines = [
        ("I wanna da-", 0.06),#1
        ("I wanna dance in the lights", 0.05),#2
        ("I wanna ro-", 0.07),#3
        ("I wanna rock your body", 0.08),#4
        ("I wanna go", 0.08),#5
        ("I wanna go for a ride", 0.068),#6
        ("Hop in the music and", 0.07),#7
        ("Rock your body", 0.08),#8
        ("Rock that body", 0.069),#9
        ("come on, come on", 0.035),#10
        ("Rock that body", 0.05),#11
        ("(Rock your body)", 0.03),#12
        ("Rock that body", 0.049),#13
        ("come on, come on", 0.035),#14
        ("Rock that body", 0.08),#15
    ]
    
    slowdown_factor = 1.2

    for line, original_duration in lines:
        total_duration = original_duration * slowdown_factor
        delay_per_char = total_duration / len(line)
        for char in line:
            if line == '(Rock your body)':
                print(f"[orange4]{char}[/orange4]", end='', flush=True)
            else:
                print(f"[bold][gold3]{char}[/bold][/gold3]", end='', flush=True)
            sleep(delay_per_char)
        print()
        sleep(0.4)        
    printLyrics()