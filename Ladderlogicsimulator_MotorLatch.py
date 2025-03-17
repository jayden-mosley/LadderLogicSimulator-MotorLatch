# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

import tkinter as tk
from tkinter import Canvas

class LadderLogicSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Ladder Logic Simulation")
        
        # Motor state (initially OFF)
        self.motor_on = False
        self.latch = False  # Latching state
        
        # Create Canvas
        self.canvas = Canvas(self.root, width=400, height=300, bg="white")
        self.canvas.pack()
        
        # Create Buttons
        self.btn_start = tk.Button(self.root, text="Start", command=self.start_motor)
        self.btn_start.pack(side=tk.LEFT, padx=10, pady=10)
        self.btn_stop = tk.Button(self.root, text="Stop", command=self.stop_motor)
        self.btn_stop.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Draw initial ladder logic
        self.update_ladder()
    
    def update_ladder(self):
        self.canvas.delete("all")
        
        # Draw ladder rails
        self.canvas.create_line(50, 50, 50, 250, width=5)
        self.canvas.create_line(350, 50, 350, 250, width=5)
        
        # Draw Start button
        start_color = "green" if self.motor_on else "white"
        self.canvas.create_rectangle(100, 60, 180, 100, outline="black", fill=start_color)
        self.canvas.create_text(140, 80, text="START", font=("Arial", 12))
        
        # Draw Stop button (NC)
        self.canvas.create_rectangle(100, 130, 180, 170, outline="black", fill="white")
        self.canvas.create_text(140, 150, text="STOP (NC)", font=("Arial", 12))
        
        # Draw Latching contact
        latch_color = "green" if self.latch else "white"
        self.canvas.create_rectangle(100, 200, 180, 240, outline="black", fill=latch_color)
        self.canvas.create_text(140, 220, text="LATCH", font=("Arial", 12))
        
        # Draw Motor indicator
        motor_color = "green" if self.motor_on else "red"
        self.canvas.create_rectangle(250, 60, 330, 100, outline="black", fill=motor_color)
        self.canvas.create_text(290, 80, text="MOTOR", font=("Arial", 12))
        
        # Draw wiring
        self.canvas.create_line(50, 80, 100, 80, width=2)  # Start button wire
        self.canvas.create_line(180, 80, 250, 80, width=2)  # Start to Motor
        self.canvas.create_line(50, 150, 100, 150, width=2)  # Stop button wire
        self.canvas.create_line(180, 150, 250, 150, width=2)  # Stop to Motor
        self.canvas.create_line(250, 80, 350, 80, width=2)  # Motor to rail
        self.canvas.create_line(250, 150, 250, 80, width=2)  # Vertical connection
        self.canvas.create_line(180, 220, 250, 220, width=2)  # Latching wire
        self.canvas.create_line(250, 220, 250, 80, width=2)  # Latching to motor
    
    def start_motor(self):
        self.motor_on = True
        self.latch = True  # Enable latch
        self.update_ladder()
    
    def stop_motor(self):
        self.motor_on = False
        self.latch = False  # Disable latch
        self.update_ladder()

# Run the simulator
if __name__ == "__main__":
    root = tk.Tk()
    app = LadderLogicSimulator(root)
    root.mainloop()
