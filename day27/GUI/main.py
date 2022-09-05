import tkinter
from turtle import Turtle


def convert_to_mile():
    km = round(float(entry_mile.get()) * 1.609, 2)
    entry_km.delete(0, tkinter.END)
    entry_km.insert(-1, km)


def convert_to_km():
    mile = round(float(entry_km.get()) / 1.60934, 2)
    entry_mile.delete(0, tkinter.END)
    entry_mile.insert(-1, mile)

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

mile_label = tkinter.Label(text="Miles: ", font=("Arial", 8, "bold"))
mile_label.grid(column=0, row=0)

km_label = tkinter.Label(text="Kilometres: ", font=("Arial", 8, "bold"))
km_label.grid(column=0, row=1)

entry_mile = tkinter.Entry(width=20)
entry_mile.grid(column=1, row=0)

entry_km = tkinter.Entry(width=20)
entry_km.grid(column=1, row=1)

button_mile = tkinter.Button(text="mile", command=convert_to_mile)
button_mile.grid(column=2, row=0)

button_km = tkinter.Button(text="km", command=convert_to_km)
button_km.grid(column=2, row=1)










# tim = Turtle()
# tim.write("Some text")


window.mainloop()
