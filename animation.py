from vpython import *
import csv
from time import sleep

# Setup the canvas and the view
# By the way, this library has terrible documentation
scene = canvas(width=600, height=780, center=vector(0,1.5,0))
framerate = 60


# Open the file with the coordinates of lights, and setup the spheres
lights = []
with open('coords_2021.csv','r',encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    
    for row in reader:
        # Read coordinates
        x,y,z = [float(x.strip()) for x in row]

        # Display a white light
        light = sphere(pos=vector(x,z,y), radius=0.03, shininess=0)

        lights.append(light)

# Open the animation file and process it
animation = []
# rotating-rainbow
with open('sequences/moving-z-plane.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    total_frames = 0

    next(reader) # skip the header
    for row in reader:
        print(row[0])
        total_frames += 1
        colors = []
        for i in range(500):
            r = int(row[i*3 +1])/255
            g = int(row[i*3 +2])/255
            b = int(row[i*3 +3])/255
            colors.append(vector(r,g,b))
        animation.append(colors)

# Loop the animation
while True:
    for frame in range(total_frames):
        for l in range(500):
            lights[l].color = animation[frame][l]
        sleep(1/framerate)