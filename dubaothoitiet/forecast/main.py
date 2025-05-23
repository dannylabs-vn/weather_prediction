import tkinter as tk
from tkinter import messagebox
import calculation

def validate_input():
    for entry in entry_fields:
        entry.configure(bg="white")

    for i, entry in enumerate(entry_fields):
        value = entry.get()
        if value == "":
            entry.configure(bg="red")
            messagebox.showerror("Error", "Please enter all information.")
            return False
        

    return True

def calculate_result():
    if not validate_input():
        return
    input_values = []
    for entry in entry_fields:
        value = entry.get()
        input_values.append(value)
    result = calculation.process_inputs(input_values)
    weather_label.configure(text="Weather: " + result)
window = tk.Tk()
window.title("Weather Prediction App")
entry_fields = []
input_names = ["Date (yyyy-mm-dd)","precipitation", "temp_max", "temp_min", "wind"]
for i in range(5):
    label = tk.Label(window, text=input_names[i] + ":")
    label.grid(row=i, column=0, padx=10, pady=10)
    entry = tk.Entry(window)
    entry.grid(row=i, column=1, padx=10, pady=10)
    entry_fields.append(entry)
calculate_button = tk.Button(window, text="Predict", command=calculate_result)
calculate_button.configure(bg="blue", fg="white")  # Set background color to blue and foreground (text) color to white
calculate_button.grid(row=5, columnspan=2, padx=10, pady=10)
weather_label = tk.Label(window, text="Weather: ")
weather_label.grid(row=7, columnspan=2, padx=10, pady=10)
window.mainloop()

