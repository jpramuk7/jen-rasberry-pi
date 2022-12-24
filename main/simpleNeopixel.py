import board
import neopixel
import time
#the 30 here corresponds to the number of lights in the LED
pixels = neopixel.NeoPixel(board.D18, 30)

try:
    #set first pixel light to red
    pixels[0] = (255, 0, 0)

    #iterated through 9 pixels
    for x in range(0, 9):
        pixels[x] = (255, 0, 0)
        time.sleep(1)

    #turn on entire LED strip and set to green
    pixels.fill((0, 255, 0))

except KeyboardInterrupt:
    #reset all states and modes for all GPIOs, 
    #which can prevent you from having errors in future programs.
    GPIO.cleanup()