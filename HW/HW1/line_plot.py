"""
    A sample of using matplotlib
    Kevin Molloy (August 2023)

"""
from matplotlib import pyplot as plt

def main():
    X = [100, 200, 300,400]
    Y = [0.4, 0.5, 1, 0.9]

    plt.plot(X,Y,marker='s',lw=2)
    plt.xlabel("Input Size(n)", fontsize=16)
    plt.ylabel("Runtime(seconds)", fontsize=16)

    # You can interactively show the plot to the terminal using show()
    # or you can save it to a file using savefig. 

    # plt.show()
    plt.savefig(fname='plot_runtime.pdf', dpi=300,
                bbox_inches='tight',pad_inches=0.05)
if __name__ == "__main__":
    main()