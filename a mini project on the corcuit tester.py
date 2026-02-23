import random

def generate_voltage(min_val=1, max_val=10):
    """Generate a random voltage between min_val and max_val."""
    return random.randint(min_val, max_val)

def play_game(max_guesses=10):
    """Run the Circuit Tester Game."""
    correct_voltage = generate_voltage()
    guess_list = []
    attempts = 0
    
    print("Welcome to the Circuit Tester Game!")
    print(f"Guess the correct voltage (1 to 10). You have {max_guesses} attempts.")

    while attempts < max_guesses:
        try:
            guess = int(input("Enter your guess: "))
            
            # Validate guess range
            if guess < 1 or guess > 10:
                print("Error: Guess must be between 1 and 10.")
                continue
                
            guess_list.append(guess)
            attempts += 1
            
            # Check guess
            if guess == correct_voltage:
                print(f"Correct! You found the voltage ({correct_voltage}) in {attempts} attempts!")
                break
            elif guess > correct_voltage:
                print("Too high!")
            else:
                print("Too low!")
                
            # Show remaining attempts
            print(f"Attempts remaining: {max_guesses - attempts}")
                
        except ValueError:
            print("Error: Please enter a valid integer.")
            
    else:
        # If loop ends without breaking (max guesses reached)
        print(f"Game Over! The correct voltage was {correct_voltage}.")
        
    # Display guess history
    if guess_list:
        print("Your guesses:", guess_list)
    else:
        print("No valid guesses made.")
        
    # Ask to play again
    return input("Play again? (yes/no): ").lower().startswith('y')

def main():
    """Main game loop to allow replay."""
    while True:
        if not play_game():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()