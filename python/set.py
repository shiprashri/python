# Function to read a set of roll numbers from input
def read_roll_numbers():
    num_students = int(input())  # Read number of students
    roll_numbers = input().split()  # Read roll numbers and split into a list
    return set(map(int, roll_numbers))  # Convert list of strings to set of integers

# Read number of students subscribed to English newspaper and their roll numbers
num_english = read_roll_numbers()

# Read number of students subscribed to French newspaper and their roll numbers
num_french = read_roll_numbers()

# Finding the intersection of both sets
both_subscriptions = num_english.intersection(num_french)

# Counting the number of students in the intersection
number_of_both_subscriptions = len(both_subscriptions)

# Output the result
print(number_of_both_subscriptions)

# Finding the diffrence of both sets
unique = num_english.difference(num_french)

# Counting the number of students in the diffrence
number_of_unique_subscriptions = len(unique)

# Output the result
print(number_of_unique_subscriptions)


# Finding the symmetric_diffrence of both sets
only_one = num_english.symmetric_difference(num_french)

# Counting the number of students in the diffrence
present_in_one = len(only_one)

# Output the result
print(present_in_one)


