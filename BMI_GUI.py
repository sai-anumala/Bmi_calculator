import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt # type: ignore
import csv

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Values must be positive.")

        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi <= 24.9:
            category = "Normal weight"
        elif 25 <= bmi <= 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

        # Save to file
        with open("bmi_data.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([weight, height, bmi, category])

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Function to display BMI trend
def show_trend():
    weights, heights, bmis = [], [], []
    try:
        with open("bmi_data.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                weights.append(float(row[0]))
                heights.append(float(row[1]))
                bmis.append(float(row[2]))

        plt.plot(bmis, label="BMI")
        plt.xlabel("Record Number")
        plt.ylabel("BMI")
        plt.title("BMI Trend")
        plt.legend()
        plt.show()
    except FileNotFoundError:
        messagebox.showerror("Error", "No data found. Calculate BMI first!")

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Height (m):").grid(row=1, column=0, padx=10, pady=5)



weight_entry = tk.Entry(root)
height_entry = tk.Entry(root)

weight_entry.grid(row=0, column=1, padx=10, pady=5)
height_entry.grid(row=1, column=1, padx=10, pady=5)

calc_button = tk.Button(root, text="Calculate BMI",command=calculate_bmi,)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

trend_button = tk.Button(root, text="Show BMI Trend", command=show_trend)
trend_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()