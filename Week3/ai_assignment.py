# Here's a basic structure to get you started:

def main():  # Main function to run the program
    # Print welcome message
    print("Welcome to the AI Calculator")

    while True:
        try:
            # Get user input for the sum
            first_number = input("Let's figure out the sum of two numbers! Enter the first number: ")
            second_number = input("Enter the second number: ")

            # Perform operations
            print("Sum of two numbers is: ", add_numbers(first_number, second_number))

            # Get user input for the difference
            first_number = input("Let's figure out the difference of two numbers! Enter the first number: ")
            second_number = input("Enter another number: ")

            # Perform operations
            print("Difference of two numbers is: ", subtract_numbers(first_number, second_number))
            print("Thank you for using the AI Calculator")

        except ValueError:
            print("Please enter a valid number")
           
        finally:
            # Ask if the user wants to continue
            continue_calculation = input("Do you want to perform another calculation? (y/n): ").strip().lower()
            if continue_calculation != "y":
                break
            
    #Print Goodbye Messsage
    print("Goodbye!")

def add_numbers(first_number, second_number):
    # Function to add two numbers
    return int(first_number) + int(second_number)

def subtract_numbers(first_number, second_number):
    # Function to subtract two numbers
    return int(first_number) - int(second_number)

# Main execution
if __name__ == "__main__":
    main()