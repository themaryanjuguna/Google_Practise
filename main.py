#Goldenratio
ratio = ((1 + (5**(1 / 2))) / 2)
print(ratio)

color = "Yellow"
thing = "sunshine"
print(color + " is the color of " + thing)

output = "Automating with Python is fun!"
print(output)

#calculates how many seconds there are in a week, if a week is 7 days.  Print the result on the screen.
seconds_per_day = 86400
week = 7
print(86400 * 7)

#Fill in the blanks to calculate the area of a triangle of base 5, height 3 and output the result.  Reminder:  the area of a triangle is (base*height)/2
base = 5
height = 3
area = (base * height) / 2

print(area)

#Use Python to calculate how many different passwords can be formed with 6 lower case English letters.  For a 1 letter password, there would be 26 possibilities.  For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities.  Using this information, print the amount of possible passwords that can be formed with 6 letters.

#In this scenario, we have a directory with 5 files in it. Each file has a different size: 2048, 4357, 97658, 125, and 8. Fill in the blanks to calculate the average file size by having Python add all the values for you, and then set the files variable to the number of files. Finally, output a message saying "The average size is: " followed by the resulting number. Remember to use the str() function to convert the number into a string.

total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is: " + str(average))


#In this scenario, two friends are eating dinner at a restaurant. The bill comes in the amount of 47.28 dollars. The friends decide to split the bill evenly between them, after adding 15% tip for the service. Calculate the tip, the total amount to pay, and each friend's share, then output a message saying "Each person needs to pay: " followed by the resulting number.

bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total/2
print("Each person needs to pay: " + str(share))


#This code is supposed to take two numbers, divide one by another so that the result is equal to 1, and display the result on the screen. Unfortunately, there is an error in the code. Find the error and fix it, so that the output is correct.

numerator = 10
denominator = 10
result = numerator / denominator
print(result)


number = input("enter a positive number: ")

for i in range(1,3):
    print(number * i)

