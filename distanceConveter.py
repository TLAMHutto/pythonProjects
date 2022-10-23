import tkinter as tk
from tkinter import ttk
# from windows import set_dpi_awareness

# set_dpi_awareness()

root = tk.Tk()
root.geometry("600x400")
root.title("Distance Converter")

meter_value = tk.StringVar()
feet_value = tk.StringVar()
def calculate_feet(*args):
    try:
        meter = float(meter_value.get())
        feet = meter * 3.28084
        feet_value.set(round(feet, 2))
    except ValueError:
        pass

main = ttk.Frame(root, padding=(30, 15))
main.grid()
meters_label = ttk.Label(main, text="Meters")
meter_input = ttk.Entry(main, width=10, font=("Segoe UI", 12), textvariable=meter_value)
feet_label = ttk.Label(main, text="Feet")
feet_display = ttk.Label(main, textvariable=feet_value, font=("Segoe UI", 12))
calc_button = ttk.Button(main, command=calculate_feet, text="Calculate")

meters_label.grid(row=0, column=0 , sticky="w")
meter_input.grid(row=0, column=1, sticky="ew")
feet_label.grid(row=1, column=0 , sticky="w")
feet_display.grid(row=1, column=1, sticky="ew")
calc_button.grid(row=2, column=0, columnspan=2, sticky="ew")

root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)

root.mainloop()