import tkinter as tk
from tkinter import messagebox

def calculate_operating_time():
    try:
        fault_current = float(fault_current_entry.get())
        pickup_current = float(pickup_current_entry.get())
        tms = float(tms_entry.get())
        curve_type = curve_type_var.get()

        if fault_current <= pickup_current:
            messagebox.showerror("Invalid Input", "Fault current must be greater than pickup current.")
            return

        # Calculate time based on the selected curve
        I_ratio = fault_current / pickup_current
        if curve_type == "SI":
            time = tms * (0.14 / ((I_ratio ** 0.02) - 1))
        elif curve_type == "VI":
            time = tms * (13.5 / ((I_ratio ** 1) - 1))
        elif curve_type == "EI":
            time = tms * (80 / ((I_ratio ** 2) - 1))
        else:
            messagebox.showerror("Error", "Invalid curve type selected.")
            return

        result_label.config(text=f"Operating Time: {time:.2f} seconds")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# GUI Setup
root = tk.Tk()
root.title("Overcurrent Protection Calculator")

# Input Fields
tk.Label(root, text="Fault Current (A):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
fault_current_entry = tk.Entry(root)
fault_current_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Pickup Current (A):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
pickup_current_entry = tk.Entry(root)
pickup_current_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Time Multiplier Setting (TMS):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tms_entry = tk.Entry(root)
tms_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Curve Type:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
curve_type_var = tk.StringVar(value="SI")
tk.OptionMenu(root, curve_type_var, "SI", "VI", "EI").grid(row=3, column=1, padx=10, pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate_operating_time)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="Operating Time: ")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Run the Application
root.mainloop()