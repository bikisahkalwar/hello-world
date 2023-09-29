# Function to print a pattern of stars
def print_stars_pattern(n):
    for i in range(1, n + 1):
        print("*" * i)

# Get the number of rows from the user
num_rows = int(input("Enter the number of rows: "))

# Call the function to print the pattern
print_stars_pattern(num_rows)
