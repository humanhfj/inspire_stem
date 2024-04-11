from tkinter import *

window = Tk()

# Adjust size
window.geometry("800x800")

window.title("Sensors Tutorial")

temp = 20
hum = 68

lbl = Label(window, text="Temperature : {0}".format(temp))

lbl.grid(column=200, row=100)

lb2 = Label(window, text="Humidity: {0}".format(hum))

lb2.grid(column=200, row=100)

window.mainloop()