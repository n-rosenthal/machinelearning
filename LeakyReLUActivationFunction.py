import numpy as np;
import matplotlib.pyplot as plt;
import matplotlib.animation as animation;

def leaky_ReLU(z: int|float, alpha: int|float) -> float:
    """
    Applies the Leaky Rectified Linear Unit (Leaky ReLU) activation function.

    Parameters:
    z (int|float): The input value to the Leaky ReLU function.
    alpha (int|float): The slope parameter of the Leaky ReLU function.

    Returns:
    float: The output of the Leaky ReLU function, which is the maximum of alpha * z and z.
    """
    return max(alpha * z, z);

def plot_leaky_relu(z: int|float, alpha: int|float) -> None:
    """
    Plots the Leaky ReLU function for a given input value z and slope parameter alpha.

    Parameters:
    z (int|float): The input value to the Leaky ReLU function.
    alpha (int|float): The slope parameter of the Leaky ReLU function.

    Returns:
    None
    """
    x = np.linspace(-10, 10, 1000);
    y = [leaky_ReLU(i, alpha) for i in x];
    plt.plot(x, y);
    
    plt.xlabel('x');
    plt.ylabel('Leaky ReLU(x)');
    plt.title('Leaky ReLU Function');
    plt.show();
    
    # Animate the plot
    fig, ax = plt.subplots();
    line, = ax.plot([], []);
    ax.set_xlim(-10, 10);
    ax.set_ylim(0, 10);
    ax.set_xlabel('x');
    ax.set_ylabel('Leaky ReLU(x)');
    ax.set_title('Leaky ReLU Function');

    def init():
        line.set_data([], []);
        return line,

    def animate(i):
        x = np.linspace(-10, 10, 1000);
        y = [leaky_ReLU(i, alpha) for i in x];
        line.set_data(x, y);
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=init, interval=20, blit=True,
                                   repeat_delay=1000, save_count=200);
    plt.show();
    
    # Save the plot as a PNG file
    plt.savefig('leaky_relu.png');
    
    # Close the plot
    plt.close();
    
    # Display the plot
    plt.show();
    
if __name__ == "__main__":
    plot_leaky_relu(0, 0.1);