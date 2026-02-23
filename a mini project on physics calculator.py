from operator import mul
import tkinter as tk
from tkinter import ttk, messagebox

def calculate_work(force, distance):
    return mul(force, distance)

def calculate_force(mass, acceleration):
    return mul(mass, acceleration)

def calculate_power(voltage,current):
    return mul(voltage,current)

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mul(mass, velocity ** 2)

def compute():
    try:
        calc_type = calc_var.get()
        result_label.config(text="")  # Clear previous result
        
        if calc_type == "Work":
            force = float(force_entry.get())
            distance = float(distance_entry.get())
            if force < 0 or distance < 0:
                raise ValueError("Force and distance cannot be negative")
            result = calculate_work(force, distance)
            result_label.config(text=f"Work = {result:.2f} J")
            
        elif calc_type == "Force":
            mass = float(mass_entry.get())
            acceleration = float(acceleration_entry.get())
            if mass < 0:
                raise ValueError("Mass cannot be negative")
            result = calculate_force(mass, acceleration)
            result_label.config(text=f"Force = {result:.2f} N")
            
        elif calc_type == "Power":
            voltage = float(voltage_entry.get())
            current = float(current_entry.get())
            if voltage < 0 or current < 0:
                raise ValueError("Voltage and current cannot be negative")
            result = calculate_power(voltage, current)
            result_label.config(text=f"Power = {result:.2f} W")
            
        elif calc_type == "Kinetic Energy":
            mass = float(ke_mass_entry.get())
            velocity = float(velocity_entry.get())
            if mass < 0:
                raise ValueError("Mass cannot be negative")
            result = calculate_kinetic_energy(mass, velocity)
            result_label.config(text=f"Kinetic Energy = {result:.2f} J")
            
    except ValueError as e:
        messagebox.showerror("Error", f"Error: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def update_fields(*args):
    calc_type = calc_var.get()
    # Hide all frames
    work_frame.pack_forget()
    force_frame.pack_forget()
    power_frame.pack_forget()
    ke_frame.pack_forget()
    # Show relevant frame
    if calc_type == "Work":
        work_frame.pack(pady=10)
    elif calc_type == "Force":
        force_frame.pack(pady=10)
    elif calc_type == "Power":
        power_frame.pack(pady=10)
    elif calc_type == "Kinetic Energy":
        ke_frame.pack(pady=10)
    result_label.config(text="")  # Clear result when changing calculation

# Create main window
root = tk.Tk()
root.title("Physics Calculator")
root.geometry("300x400")

# Calculation selection
calc_label = tk.Label(root, text="Select Calculation:")
calc_label.pack(pady=5)
calc_var = tk.StringVar(value="Work")
calc_menu = ttk.Combobox(root, textvariable=calc_var, values=["Work", "Force", "Power", "Kinetic Energy"])
calc_menu.pack(pady=5)
calc_var.trace("w", update_fields)

# Frames for input fields
work_frame = tk.Frame(root)
force_frame = tk.Frame(root)
power_frame = tk.Frame(root)
ke_frame = tk.Frame(root)

# Work inputs
tk.Label(work_frame, text="Force (N):").pack()
force_entry = tk.Entry(work_frame)
force_entry.pack()
tk.Label(work_frame, text="Distance (m):").pack()
distance_entry = tk.Entry(work_frame)
distance_entry.pack()

# Force inputs
tk.Label(force_frame, text="Mass (kg):").pack()
mass_entry = tk.Entry(force_frame)
mass_entry.pack()
tk.Label(force_frame, text="Acceleration (m/s²):").pack()
acceleration_entry = tk.Entry(force_frame)
acceleration_entry.pack()

# Power inputs
tk.Label(power_frame, text="Voltage (V):").pack()
voltage_entry = tk.Entry(power_frame)
voltage_entry.pack()
tk.Label(power_frame, text="Current (A):").pack()
current_entry = tk.Entry(power_frame)
current_entry.pack()

# Kinetic Energy inputs
tk.Label(ke_frame, text="Mass (kg):").pack()
ke_mass_entry = tk.Entry(ke_frame)
ke_mass_entry.pack()
tk.Label(ke_frame, text="Velocity (m/s):").pack()
velocity_entry = tk.Entry(ke_frame)
velocity_entry.pack()

# Compute button
compute_button = tk.Button(root, text="Calculate", command=compute)
compute_button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

# Show Work frame by default
work_frame.pack(pady=10)

# Start the GUI
root.mainloop()