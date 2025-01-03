# Here's a basic structure to get you started:

def main():  # Main function to run the program
    # Print welcome message
    print("Welcome to the AI Calculator")

    while True:
        try:
            # Get user input
            a = (input("Let's figure out the sum of two numbers! Enter the first number: "))
            b = (input("Enter second number: "))

            # Perform operations
            print("Sum of two numbers is: ", add_numbers(a, b))

            # Get user input
            a = (input("Let's figure out the difference of two numbers! Enter the first number: "))
            b = (input("Enter anothernumber: "))

            # Perform operations
            print("Difference of two numbers is: ", subtract_numbers(a, b))

            # Print exit message
            print("Thank you for using the AI Calculator")
        except ValueError:
            print("Please enter a valid number")
        finally:
            # Ask if the user wants to continue
            continue_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if continue_calculation != "yes":
                break
    print("Goodbye!")

def add_numbers(a, b):
    # Function to add two numbers
     return int(a) + int(b)

def subtract_numbers(a, b):
    # Function to subtract two numbers
    return int(a) - int(b)


    # Main execution
if __name__ == "__main__":
    main()

# Run your script and observe its output.
