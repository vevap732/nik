import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class DynamicPlot(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        self.fig = Figure(figsize=(8, 6), dpi=72)
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)
        
        control_panel = QWidget()
        hbox = QHBoxLayout(control_panel)
        
        self.start_btn = QPushButton("Старт")
        self.start_btn.clicked.connect(self.on_start_clicked)
        hbox.addWidget(self.start_btn)
        
        self.stop_btn = QPushButton("Стоп")
        self.stop_btn.setEnabled(False)
        self.stop_btn.clicked.connect(self.on_stop_clicked)
        hbox.addWidget(self.stop_btn)
        
        layout.addWidget(control_panel)
        self.setLayout(layout)

        self.xdata = []
        self.ydata = []

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.ax = self.fig.add_subplot(111)

        self.ax.set_title("Динамический график")
        self.ax.grid(True)
        self.line, = self.ax.plot([], [], '-o')

        self.resize(800, 600)
        self.show()
    
    def on_start_clicked(self):
        self.timer.start(1000) 
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
    
    def on_stop_clicked(self):
        self.timer.stop()
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
    
    def update_plot(self):
        new_x = len(self.xdata)
        new_y = np.random.randn()

        self.xdata.append(new_x)
        self.ydata.append(new_y)

        self.line.set_data(self.xdata, self.ydata)

        self.ax.relim()
        self.ax.autoscale_view()

        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DynamicPlot()
    sys.exit(app.exec())
