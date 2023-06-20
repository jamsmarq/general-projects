from os import system as os_system, name as os_name
from tabulate import tabulate

def clear_screen():
    os_system('cls' if os_name == 'nt' else 'clear')

def main():
    print("""This program will create a multiplcation table of the number\nof your choice. Just enter a valid positive whole number.
    """)

    while True:
        while True:
            try:
                starting_number = int(input("Enter the starting number (press ENTER for 1): "))

                # validate if the starting number is positive whole number
                if starting_number > 0:
                    break
                else:
                    clear_screen()
                    print("\nERROR: Please enter a positive whole number.")
                
            except ValueError:
                clear_screen()
                print("\nERROR: Please enter a valid whole number.")

        while True:
            try:
                user_input = int(input("Enter the end number (n): "))

                # check if the user input is a positive whole number
                if user_input > 0:
                    break
                else:
                    clear_screen()
                    print("\nERROR: Please enter a positive whole number.")
                
            except ValueError:
                    clear_screen()
                    print("\nERROR: Please enter a valid whole number.")
        
        if starting_number < user_input:
            break
        else:
            clear_screen()
            print("\nERROR: Starting number cannot exceed or equal N.")

    multiplication_table = []
    table_format = "Normal"
    table_width = len(str(user_input * user_input)) + 2
    table_header = [""] + list(range(starting_number, user_input + 1))

    for i in range(starting_number, user_input + 1):
        row = [i]
        for j in range(starting_number, user_input + 1):
            row.append(i * j)
        multiplication_table.append(row)
    
    while True:
        clear_screen()
        print(f"\nMultiplication table of \033[1m{starting_number}\033[0m to \033[1m{user_input}\033[1m ({table_format}):")
        print(tabulate(multiplication_table, headers=table_header, tablefmt="grid"))
    
        print("\n\033[1mDisplay Options:\033[0m")
        print("1: Display in \033[1mTriangular\033[0m format")
        print("2: Display in \033[1mDiagonal\033[0m format")
        print("3: Display in \033[1mNormal\033[0m format")
        print("4: Highlight a specific row number")
        print("5: Highlight a specific column number")

        print("\n\033[1mOther Options:\033[0m")
        print("6: Enter new starting and end numbers")
        print("7: Exit the program")
    
        user_option = input("\nEnter option (submit 'q' to exit): ")
    
        if user_option == "q":
            break

        elif user_option == "1":
            table_format = "Triangular"
            multiplication_table.clear()
            table_header = [" "] * user_input

            for i in range(starting_number, user_input + 1):
                row = [i * j for j in range(starting_number, i + 1)]
                multiplication_table.append(row)

        elif user_option == "2":
            table_format = "Diagonal"
            multiplication_table.clear()
            table_header = [""] + list(range(starting_number, user_input + 1))

            for i in range(starting_number + 1, user_input + 1):
                row = [""] + [""] * (i - 1) + [i * j for j in range(i, user_input + 1)]
                multiplication_table.append(row)

        elif user_option == "3":
            table_format = "Normal"
            multiplication_table.clear()
            table_header = [""] + list(range(starting_number, user_input + 1))
        
            for i in range(starting_number, user_input + 1):
                row = [i]
                for j in range(starting_number, user_input + 1):
                    row.append(i * j)
                multiplication_table.append(row)
        
        elif user_option == "4":
            pass

        else:
            continue

if __name__ == "__main__":
    main()