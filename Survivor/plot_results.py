import matplotlib.pyplot as plt 

class Plot:
    def __init__(self):
        plt.style.use("ggplot")
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2)

    def show(self): plt.show()