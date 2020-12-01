import board
import neopixel
import time
import random

pixel_pin = board.D18
ORDER = neopixel.RGB
num_pixels = 150
zones = 5
brightness = 1

pixels = neopixel.NeoPixel(pixel_pin, num_pixels,
	brightness=brightness, pixel_order=ORDER)

#pixels[0] = (255, 0, 0)

color1 = (245, 245, 245) #white
color2 = (255, 157, 212) #pink (green and blue reversed)
color3 = (171, 46, 59) #red (g & b reversed)
color4 = (98, 137,217) #blue (g & b reversed)
color5 = (0, 255, 0) #(60, 158, 78) #green (g & b reversed)

#pixels.fill(color2)
#pixels.show()
colors = [color1, color2, color3, color4, color5]

def cycle(secWait):
	index = 0
	random.shuffle(colors)
	for color in colors:
		for j in range(0, 30):
			cur_pixel = (index * 30) + j
			pixels[cur_pixel] = color
			print(cur_pixel, ": ", color)
			time.sleep(secWait)
		index += 1



#pixels[0] = (255, 0, 0)
#pixels.write()
while True:
	print("running")
	#pixels.fill((255, 0, 0))
	#pixels.write()
	#time.sleep(5)
	cycle(0.01)
	#pixels.show()
	time.sleep(15)
	#pixels.fill((0, 255, 0))
	#cycle(0.01)
	#pixels.show()
	#time.sleep(5)
	#print("stopping")


