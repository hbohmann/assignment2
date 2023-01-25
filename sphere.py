'''
Assignment 2 
Hannah Bohmann
CS 021 / Spring 2023

This program prompts the user for the radius of a sphere and then processes to calculate the corresponding diameter, circumference, surface area, and volume.
'''

# Importing math library 
import math 

# Get the precise value for pi
PI = math.pi

# Get the asked radius of a sphere 
radius = float(input(" Enter the radius: "))


# Calculate the diameter
diameter = radius * 2

# Display output of the diameter 
print("Diameter: ", format(diameter, '.1f'))

# Calculate the circumference
circumference = radius * 2 * PI

# Display the circumference
print("Circumference: ", format(circumference,'.1f'))

# Calculate the surface area 
surface_area = radius ** 2 * PI * 4

# Display the surface area
print("Surface area: ", format(surface_area, '.1f'))

# Calculate the volume
volume = radius ** 3 * PI * (4 / 3)

# Display the volume 
print("Volume: ", format(volume, '.1f'))

