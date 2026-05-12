import matplotlib.pyplot as plt 

class Plot:
    def __init__(self):
        plt.style.use("ggplot")
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2)
  
    def plot_island_size(self, depths, times):
        self.ax1.set_title("Recursion time increasing depth")
        self.ax1.set_xlabel("Depth (num of steps)")
        self.ax1.set_ylabel("Time")

        self.ax1.plot(depths, times, label="Used time")
        self.ax1.legend()

    def plot_island_depth(self, sizes, times):
        self.ax2.set_title("Recursion time increasing size")
        self.ax2.set_xlabel("Size N (for N x N grid)") 
        self.ax2.set_ylabel("Time")

        self.ax2.plot(sizes, times, label="Used time")
        self.ax2.legend()

    def show(self): plt.show()