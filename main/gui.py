from tkinter import *
from tkinter.ttk import Progressbar
from numpy import round
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


class Application(Frame):

    bground = "#4fa334"
    fground = "white"
    infoLabelsFont = "none 12 bold"
    valueLabelsFont = "none 12"
    infoLabelsWidth = 20
    valueLabelsWidth = 7

    def create_widgets(self):
        self.std_info_label["text"] = "Standard deviation: "
        self.var_info_label["text"] = "Variance: "
        self.avg_info_label["text"] = "Average: "
        self.min_info_label["text"] = "Min: "
        self.max_info_label["text"] = "Max: "

        self.std_value_label["text"] = "0"
        self.var_value_label["text"] = "0"
        self.avg_value_label["text"] = "0"
        self.min_value_label["text"] = "0"
        self.max_value_label["text"] = "0"

        self.progress["length"] = 300
        self.progress["maximum"] = self.iterations

        self.std_info_label.grid(row=0, column=0, sticky=E)
        self.var_info_label.grid(row=1, column=0, sticky=E)
        self.avg_info_label.grid(row=2, column=0, sticky=E)
        self.min_info_label.grid(row=3, column=0, sticky=E)
        self.max_info_label.grid(row=4, column=0, sticky=E)

        self.std_value_label.grid(row=0, column=1)
        self.var_value_label.grid(row=1, column=1)
        self.avg_value_label.grid(row=2, column=1)
        self.min_value_label.grid(row=3, column=1)
        self.max_value_label.grid(row=4, column=1)

        canvas = FigureCanvasTkAgg(self.figure, self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=5, columnspan=2)

        self.progress.grid(row=6, columnspan=2)

    def __init__(self, iterations=100, master=None):
        Frame.__init__(self, master)
        self.iterations = iterations  # default
        self.configure(bg=self.bground)
        self.figure = Figure(figsize=(7, 5), dpi=100)
        self.graph = self.figure.add_subplot(111)
        self.std_info_label = Label(self, bg=self.bground, fg=self.fground,
                                    font=self.infoLabelsFont, width=self.infoLabelsWidth)
        self.var_info_label = Label(self, bg=self.bground, fg=self.fground,
                                    font=self.infoLabelsFont, width=self.infoLabelsWidth)
        self.avg_info_label = Label(self, bg=self.bground, fg=self.fground,
                                    font=self.infoLabelsFont, width=self.infoLabelsWidth)
        self.min_info_label = Label(self, bg=self.bground, fg=self.fground,
                                    font=self.infoLabelsFont, width=self.infoLabelsWidth)
        self.max_info_label = Label(self, bg=self.bground, fg=self.fground,
                                    font=self.infoLabelsFont, width=self.infoLabelsWidth)
        self.std_value_label = Label(self, bg=self.bground, fg=self.fground,
                                     font=self.valueLabelsFont, width=self.valueLabelsWidth)
        self.var_value_label = Label(self, bg=self.bground, fg=self.fground,
                                     font=self.valueLabelsFont, width=self.valueLabelsWidth)
        self.avg_value_label = Label(self, bg=self.bground, fg=self.fground,
                                     font=self.valueLabelsFont, width=self.valueLabelsWidth)
        self.min_value_label = Label(self, bg=self.bground, fg=self.fground,
                                     font=self.valueLabelsFont, width=self.valueLabelsWidth)
        self.max_value_label = Label(self, bg=self.bground, fg=self.fground,
                                     font=self.valueLabelsFont, width=self.valueLabelsWidth)
        self.progress = Progressbar(self)
        self.pack()
        self.create_widgets()

    def values_changed(self, std, var, avg, minimum, maximum):
        self.std_value_label["text"] = repr(round(std, 2))
        self.var_value_label["text"] = repr(round(var, 2))
        self.avg_value_label["text"] = repr(round(avg, 2))
        self.min_value_label["text"] = repr(round(minimum, 2))
        self.max_value_label["text"] = repr(round(maximum, 2))
        self.progress.step()
        self.master.update()

    def set_iterations(self, iterations):
        self.iterations = iterations
