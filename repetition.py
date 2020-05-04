

# lists
# a list can hold multiple values

# defining a list called numbers with no values
numbers = []

print(numbers)

numbers.append(10)

print(numbers)

numbers.append(15)

print(numbers)

numbers.append(-15)

print(numbers)

# initialize a list while creating it
myList = [2, 5, -4, 25, 100]

print("myList =", myList)



# printing the values of myList one at a time

print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])
print(myList[4])

# using a for loop to print these values easily
print("using for loop")
for val in myList:
    print(val)



# lets use a for loop to add all values in myList

total = 0

for val in myList:
    total = total + val

print(total)




# if we need a for loop to iterate through a 
# range of numbers from 1 to 100, we can use the range function
# instead of defining a list from 0 to 99

# add all nmbers from 1 to 100

total = 0

for i in range(1, 100):
    total = total + i

print("sum of numbers from 1 to 100 =", total)



# list with strings

fruits = ["banana", "apple", "grape", "pineapple"]

for fruit in fruits:
    print(fruit)


'''
# define a range of numbers

r1 = range(5)

print(r1[0], r1[1], r1[2], r1[3], r1[4])

'''
