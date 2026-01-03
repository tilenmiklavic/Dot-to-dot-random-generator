from tkinter import *
from PIL import Image, ImageDraw
import random
import math

root = Tk()

cHeight = 595
cWidith = 842
numPoints = 50 #input("Število točk: ")
POINT_CLEARANCE = 15

points = []

image = Image.new(mode="RGB", size=(cWidith, cHeight), color="white")
draw = ImageDraw.Draw(image)

def isInRadius(point1, point2, radius):
    return math.sqrt((abs(point1[0] - point2[0]) ** 2 + abs(point1[1] - point2[1]) ** 2)) < radius

def doesOverlap(point, points, distance):
    return any(isInRadius(point, p, distance) for p in points)

def drawPoints(numPoints):

    while len(points) < numPoints:
        x = random.randrange(10, cWidith-10)
        y = random.randrange(10, cHeight-10)
        potentialPoint = (x, y)

        if doesOverlap(potentialPoint, points, POINT_CLEARANCE):
            continue

        points.append(potentialPoint)

        draw.ellipse((x, y, x + 3, y + 3) ,fill="black", width=3)
        draw.text((x-3, y-11), text=(str(len(points))), fill="black", size=10)
    return

drawPoints(int(numPoints))

image.show()
image.save('output' + str(random.randint(1, cWidith * cHeight)) +'.pdf')
