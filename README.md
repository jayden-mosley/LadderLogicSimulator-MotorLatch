# LadderLogicSimulator-MotorLatch
This is a simple ladder logic simulation built using Python and Tkinter. It visually represents a Start/Stop circuit with latching logic for PLC.

## How It Works
Press "Start" → The motor turns ON and remains ON (latching enabled).
Press "Stop" → The motor turns OFF, breaking the circuit.
The UI updates dynamically to show the current state.

![Ladder Logic Simulator](Screen Shot 2025-03-17 at 13.25.45.png)

1) LadderLogicSimulator Class
Encapsulates the entire logic:

Initializes the Tkinter window & Canvas.
Draws the ladder logic diagram.
Handles Start & Stop button logic.

2) update_ladder()
Clears and redraws the circuit.
Displays Start, Stop, Latch, and Motor.
