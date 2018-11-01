# Add your Python code here. E.g.
from microbit import *

rock = Image("09990:99999:99999:99999:00000:")
paper = Image("99999:99999:99999:99999:99999:")
scissors = Image("90009:09090:99999:90909:99999:")
lizard = Image("00000:00900:09990:00900:09990:")
spock = Image("00900:09990:90909:09990:90009:")
blank = Image("00000:00000:00000:00000:00000:")
while True:
    reading = accelerometer.get_x()
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(scissors, delay=1000)
        sleep = 1000
    elif reading > 600:
        display.show(rock, delay=1000)
    elif reading < -600:
        display.show(paper, delay=1000)
    elif button_a.is_pressed():
        display.show(lizard, delay=1000)
    elif button_b.is_pressed():
        display.show(spock, delay=1000)
    else:
        display.show(blank, delay=1000)
