# Projectile Motion ASCII Simulator

A tiny terminal based projectile motion simulator written in Python.
This project renders a moving projectile using a text grid and basic physics equations.

Built as a quick experiment to visualize motion in the terminal.

---

## Demo Concept

The projectile is simulated using classical motion equations:

x = ux * t
y = uy * t - (1/2)gt²

The program updates the grid frame by frame to animate the trajectory.

---

## Features

* Terminal based animation
* ASCII grid rendering
* User input for angle and velocity
* Real time motion simulation
* Simple physics model

---

## Requirements

Python 3.x

No external libraries required.

---

## Run the Program

Clone the repo and run:

```bash
python main.py
```

Then enter:

* launch angle (degrees)
* initial velocity

---

## Example Input

Angle: 45
Velocity: 10

---

## How It Works

The simulation:

1. Converts angle to radians
2. Splits velocity into x and y components
3. Updates position using time steps
4. Renders each frame to the terminal
5. Clears the screen to create animation

The grid resolution is fixed but can be modified in the code.

---

## File Structure

```
project/
│
├── main.py
└── README.md
```

---

## Future Improvements

Possible upgrades:

* Stop simulation when projectile hits ground
* Adjustable gravity
* Axis rendering
* Trails behind projectile
* Pygame visualization
* Variable grid resolution
* Real coordinate scaling

---

## License

MIT License
