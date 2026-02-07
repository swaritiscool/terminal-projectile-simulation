"""
Projectile Motion ASCII Simulator

This program simulates projectile motion in a terminal using a text grid.
The user provides:
- launch angle (degrees)
- initial velocity

The projectile trajectory is rendered frame by frame using ASCII characters.

Physics model:
x = ux * t
y = uy * t - (1/2) * g * t^2

Grid:
- Height = grid_res
- Width = grid_res * 3
"""

import time
import os
import math

matrix = []
grid_res = 32
x_res = grid_res * 3

print("\n" + "=" * 40)
print("      PROJECTILE MOTION SIM")
print("=" * 40)

theta = int(input("Enter angle in degrees: "))
u = int(input("Enter velocity: "))

theta = theta * math.pi / 180
ux = u * math.cos(theta)
uy = u * math.sin(theta)

print("\nSimulation starting...")
print(f"Angle (rad): {theta:.2f}")
print(f"Velocity components -> ux: {ux:.2f}, uy: {uy:.2f}")
print("=" * 40)
for i in range(3):
    print(3-i)
    time.sleep(0.5)

def clear():
    matrix.clear()
    for i in range(0, grid_res):
        matrix.append([])
        for j in range(0, x_res):
            matrix[i].append([' '])

def point(y, x, var="a"):
    y_pos = grid_res - 1 - int(y)
    if y_pos < (grid_res - 1) * -1 or y_pos > grid_res - 1 or y_pos < 0:
        return
    elif int(x) >= x_res or int(x) < 0:
        return
    matrix[grid_res - 1 - int(y)][int(x)] = str(var)

def render():
    for i in matrix:
        for j in i:
            print(j[0], end=" ")
        print()
    print()

clear()
t = 0
dt = 0.1

while True:
    render()
    x = ux * t
    y = uy * t - 1/2 * 10 * t**2
    point(y, x)
    t += dt
    time.sleep(0.05)
    os.system('cls')
