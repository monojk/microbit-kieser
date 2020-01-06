from microbit import *
import music
import time

seconds = 120

nw = Image("00009:"
           "00090:"
           "00900:"
           "00000:"
           "00000")
sw = Image("00000:"
           "00000:"
           "00900:"
           "00090:"
           "00009")
s1 = Image("00000:"
           "00000:"
           "99900:"
           "00000:"
           "00000")
s2 = Image("00000:"
           "99900:"
           "99900:"
           "99000:"
           "00000")

def displayCycle(cycle):
    pixel = [ [9,9,9,9,9], [9,9,9,9,9] ]
    for i in range(cycle):
        if i < 5:
            pixel[0][i] = 0
        else:
            pixel[1][i-5] = 0
    for c in range(2):
        for r in range(5):
            display.set_pixel(c, r, pixel[c][r])

Images = [Image.CLOCK12, nw, Image.CLOCK3, sw, Image.CLOCK6, Image.CLOCK6, Image.CLOCK6,
          sw, Image.CLOCK3, nw, Image.CLOCK12, Image.CLOCK12]

def sleepFor(millisecs):
    global startLoopTime
    sleeptime = startLoopTime - running_time() + millisecs
    sleep(sleeptime)

def starte():
    global i, sound, Images, startTime, startLoopTime
    i = 0
    startLoopTime = running_time()
    display.show("0")
    sleepFor(500)
    display.show(s1)
    sleepFor(1500)
    display.show(s2)
    sleepFor(2500)         # a total of 3.5 seconds pause (countdown) for preparation
    display.show(Images[0])
    displayCycle(0)
    sleepFor(3500)
    if sound > 0:
        music.play(music.BA_DING)
    startTime = running_time()
    startLoopTime = startTime
    display.set_pixel(2, 2, 0)
    sleepFor(200)
    display.set_pixel(2, 2, 9)
    button_a.was_pressed()
    if button_b.was_pressed():
        i = -1

sound = 0
i = -1
while True:
    startLoopTime = running_time()
    # gesture = accelerometer.current_gesture()
    # if gesture == "shake":
    #    sound = 1 - sound   # Toggle between sound and mute
    if button_a.was_pressed():
        starte()
    elif i >= 0 and button_b.was_pressed():
        i = -1
        elapsed = int( (running_time() - startTime) / 1000 )
        while True:
            display.scroll(elapsed)
            if button_a.was_pressed():
                starte()
                break
            if button_b.was_pressed():
                break
            sleep(100)

    if i >= 0:
        imagenr = i % 12
        if imagenr == 0 or imagenr == 6:
            display.set_pixel(2, 2, 0)
            sleep(200)
            display.set_pixel(2, 2, 9)
        display.show(Images[imagenr])
        cycle = int(i / 12)
        displayCycle(cycle)
    else:
        display.show("0")

    if i < 0:
        sleep(100)          # shorter reaction time on start-button
    else:
        sleepFor(1000)      # 1 second

    if i >= 0:              # seconds counter
        i += 1

    if i >= seconds:
        if sound > 0:
            music.play(music.BA_DING)
        i = -1              # reset