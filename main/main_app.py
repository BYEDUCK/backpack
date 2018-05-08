from main import *
from tkinter import *


class DataContainer:

    def __init__(self):
        self.iterations = 0
        self.cardinality = 0
        self.cardinality = 0
        self.mutation = 0
        self.crossing = 0
        self.items = 0
        self.savingToFile = 0


container = DataContainer()
bground = "#4fa334"
fground = "white"
labelsFont = "none 12 bold"
entriesFont = "none 11"


def start():
    container.iterations = int(iterEntry.get())
    container.cardinality = int(cardinalityEntry.get())
    container.mutation = int(mutateEntry.get())
    container.crossing = int(crossEntry.get())
    container.items = int(itemsEntry.get())
    container.savingToFile = var.get()
    insertion.destroy()


if __name__ == "__main__":
    insertion = Tk()
    insertion.title("Insert start parameters")
    insertion.configure(bg=bground)

    iterLabel = Label(insertion, text="Enter number of iterations:",
                      bd=5, fg=fground, bg=bground,
                      font=labelsFont)
    cardinalityLabel = Label(insertion, text="Enter population's cardinality:",
                             bd=5, fg=fground, bg=bground,
                             font=labelsFont)
    mutateLabel = Label(insertion, text="Enter mutation probability (in promils):",
                        bd=5, fg=fground, bg=bground,
                        font=labelsFont)
    crossLabel = Label(insertion, text="Enter crossing probability (in percents):",
                       bd=5, fg=fground, bg=bground,
                       font=labelsFont)
    itemsLabel = Label(insertion, text="Enter number of items:",
                       bd=5, fg=fground, bg=bground,
                       font=labelsFont)

    iterEntry = Entry(insertion, width=5, font=entriesFont)
    cardinalityEntry = Entry(insertion, width=5, font=entriesFont)
    mutateEntry = Entry(insertion, width=5, font=entriesFont)
    crossEntry = Entry(insertion, width=5,  font=entriesFont)
    itemsEntry = Entry(insertion, width=5,  font=entriesFont)

    var = IntVar()
    savingToFileCheckButton = Checkbutton(insertion, text="Saving results to file", variable=var)

    buttonStart = Button(insertion, text="GO!", command=start)

    iterLabel.grid(row=0, column=0, sticky=W)
    iterEntry.grid(row=0, column=1, sticky=E)

    cardinalityLabel.grid(row=1, column=0, sticky=W)
    cardinalityEntry.grid(row=1, column=1, sticky=E)

    mutateLabel.grid(row=2, column=0, sticky=W)
    mutateEntry.grid(row=2, column=1, sticky=E)

    crossLabel.grid(row=3, column=0, sticky=W)
    crossEntry.grid(row=3, column=1, sticky=E)

    itemsLabel.grid(row=4, column=0, sticky=W)
    itemsEntry.grid(row=4, column=1, sticky=E)

    savingToFileCheckButton.grid(row=5, columnspan=2, sticky=W)

    buttonStart.grid(row=6, column=1, sticky=E)

    insertion.mainloop()
    
    window = Tk()
    window.title("Genetic algorithm byDUCK")
    app = Application(container.iterations, master=window)
    myAlgorithm = GeneticAlgorithm(container.iterations, container.cardinality,
                                   container.mutation, container.crossing,
                                   container.items, container.savingToFile, app=app)
    winner = myAlgorithm.start()

    print("END")
