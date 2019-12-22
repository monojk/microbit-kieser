# microbit-kieser
Python code for bbc:microbit box used as a timer for Kieser-Training


A Kieser-Training exercise has 10 passes of each  4 secs down + 2 secs pause + 4 secs up + 2 secs pause = 10 secs 


On the 5X5 display the progress is shown:

first 2 columns show the remaining number is passes of an exercise

The right part shows a moving arm

The middle LED blinks when you should start the exercise (countdown has finished)

    xx    x
    xx  x 
    xxx
    xx
    xx 

Button A : (re)starts the timer with a countdown delay of 3 seconds 

           (stops after 10 * seconds or if button B is pressed)

Button B : stops the timer and displays the elapsed seconds of training
