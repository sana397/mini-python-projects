import random
def run_test(test_number, number):
    # Correct square root (e.g., sqrt(16) = 4)
    correct_answer = int(number ** 0.5)
    
    # Ask question
    print(f"Test {test_number}: What is the square root of {number}?")
    
    # Keep asking until a positive number is entered
    while True:
        answer = input("Enter your answer: ")
        # Check if input is a number
        if answer.isdigit():  # Only allows whole numbers
            answer = int(answer)  # Convert to integer
            if answer > 0:  # Check if positive
                break
            else:
                print("Please enter a positive number!")
        else:
            print("Please enter a number!")
    
    # Check if answer is correct
    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect. The square root of {number} is {correct_answer}.")
        return 0

# Main program
total_score = 0
print("Welcome! You will take 5 tests to find square roots.")
# List of perfect squares
numbers = [4, 9, 16, 25, 36]
# Shuffle the list to get random order
random.shuffle(numbers)
# Run 5 tests with unique numbers
for test in range(1, 6):  # Run 5 tests
    total_score = total_score + run_test(test, numbers[test-1])
print(f"You got {total_score} out of 5 correct!")