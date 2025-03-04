def ReLU(z: int|float) -> float:
    """
    Applies the Rectified Linear Unit (ReLU) activation function.

    Parameters:
    z (int|float): The input value to the ReLU function.

    Returns:
    float: The output of the ReLU function, which is the maximum of 0 and z.
    """
    return max(0, z);

import numpy as np;
import matplotlib.pyplot as plt;
import matplotlib.animation as animation;

def plot_relu(z: int|float) -> None:
    """
    Plots the ReLU function for a given input value z.

    Parameters:
    z (int|float): The input value to the ReLU function.

    Returns:
    None
    """
    x = np.linspace(-10, 10, 1000);
    y = [ReLU(i) for i in x];
    plt.plot(x, y);
    
    plt.xlabel('x');
    plt.ylabel('ReLU(x)');
    plt.title('ReLU Function');
    plt.show();
    
    # Animate the plot
    fig, ax = plt.subplots();
    line, = ax.plot([], []);
    ax.set_xlim(-10, 10);
    ax.set_ylim(0, 10);
    ax.set_xlabel('x');
    ax.set_ylabel('ReLU(x)');
    ax.set_title('ReLU Function');

    def init():
        line.set_data([], []);
        return line,

    def animate(i):
        x = np.linspace(-10, 10, 1000);
        y = [ReLU(i) for i in x];
        line.set_data(x, y);
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True);
    plt.show();
    
    # Save the plot as a PNG file
    plt.savefig('relu.png');
    
    # Close the plot
    plt.close();
    
def main():
    plot_relu(0);
    
if __name__ == "__main__":
    main();