# takes data from .txt file from line 2 and plot dynamic graph as and when data gets pushed to the file

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import numpy as np
import os

def plot_loss(log_file_name):
    fig, ax = plt.subplots()
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Loss')
    ax.set_title('Training Loss')
    line, = ax.plot([], [])  # Initialize a line object with no data

    # Store the second line of the file
    with open(log_file_name, 'r') as f:
        second_line = f.readlines()[1]

    def update(num):
        nonlocal second_line  # Declare second_line as nonlocal
        with open(log_file_name, 'r') as f:
            lines = f.readlines()

        # If the second line changes, clear the existing data
        if len(lines)>1 and lines[1] != second_line:
            line.set_data([], [])
            ax.relim()
            ax.autoscale_view(True,True,True)
            second_line = lines[1]  # Update the value of second_line only when it changes

        # Extract loss values
        losses = [float(line.split(':')[1]) for line in lines[2:]]

        line.set_data(range(len(losses)), losses)  # Update the data of the line object
        ax.relim()  # Recalculate limits
        ax.autoscale_view(True,True,True)  # Rescale the view

    # Keep a reference to the FuncAnimation object
    ani = animation.FuncAnimation(fig, update, frames=None, repeat=False)
    plt.show()
    return ani

# Call the function with your log file and keep a reference to the returned animation object
ani = plot_loss("log.txt")