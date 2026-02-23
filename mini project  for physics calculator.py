def calculate_force(mass, acceleration):
    return mass * acceleration

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def calculate_potential_energy(mass, height, g=9.81):
    return mass * g * height

def physics_calculator():
    while True:
        print("\nPhysics Calculator")
        print("1. Force (F = m * a)")
        print("2. Kinetic Energy (KE = 0.5 * m * v²)")
        print("3. Gravitational Potential Energy (PE = m * g * h)")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 4:
                print("Exiting calculator.")
                break
                
            if choice not in [1, 2, 3]:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
                continue
                
            mass = float(input("Enter mass (kg): "))
            if mass < 0:
                raise ValueError("Mass cannot be negative")
                
            if choice == 1:
                acceleration = float(input("Enter acceleration (m/s²): "))
                result = calculate_force(mass, acceleration)
                print(f"Force = {result:.2f} N")
                
            elif choice == 2:
                velocity = float(input("Enter velocity (m/s): "))
                result = calculate_kinetic_energy(mass, velocity)
                print(f"Kinetic Energy = {result:.2f} J")
                
            elif choice == 3:
                height = float(input("Enter height (m): "))
                if height < 0:
                    raise ValueError("Height cannot be negative")
                result = calculate_potential_energy(mass, height)
                print(f"Potential Energy = {result:.2f} J")
                
        except ValueError as e:
            print(f"Error: {e}. Please enter valid numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
if __name__ == "__main__":
    physics_calculator()