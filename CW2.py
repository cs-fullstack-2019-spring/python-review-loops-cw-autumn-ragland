def main():
    # problem1()
    # problem2()
    # problem3()
    # bonus()

# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Hint: Use 'continue' statement.
# Expected outcome (0 1 2 4 5)
def problem1():
    for numbers in range(6):
        if numbers != 3 and numbers != 6:
            print(numbers)
# Write a Python program to count the number of even and odd numbers from a series of numbers.
def problem2():
    evenTotal = 0
    oddTotal = 0
    for numbers in range(1,10):
        if numbers % 2 == 0:
            evenTotal += 1
        else:
            oddTotal += 1
    print("The number of even numbers is", evenTotal)
    print("The number of odd numbers is", oddTotal)
# Write a Python program that accepts a sequence of lines (blank line to terminate) as input and
# prints the lines as output after User enters a blank line to end.
# Do not use an array to hold the lines of text
# Hints: You can use "\n" if you want to add a line break between sentences
def problem3():
    userInput = ""
    newStrings = ""
    while (userInput != " "):
        userInput = input("Enter a sentence: ")
        newStrings += (userInput + "\n")
    print(newStrings)

if __name__ == '__main__':
    main()