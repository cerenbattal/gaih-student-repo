#first homework
# 1. Create a List and swap the second half of the list with the first half of the list and
#    print  this list on the screen.
#    [1, 2, 3, 4, 5, 6] -> [4, 5, 6, 1, 2, 3]

list = [1, 2, 3, 4, 5, 6]
listLength = len(list)

if listLength % 2 != 0:
    print("The list has odd number of elements!")
else:
    firstHalf = list[0:listLength/2]
    secondHalf = list[listLength/2:listLength]
    joinedList = secondHalf + firstHalf
    print("list: ", list)
    print("firstHalf: ", firstHalf)
    print("secondHalf: ", secondHalf)
    print("joinedList: ", joinedList)

# 2. Ask the user to input a single digit integer to a variable 'n'. Then, print out all of the even numbers
#    from 0 to n (including n)
#    input: 6 -> 0, 2, 4, 6

n = int(input("Enter a single digit integer: "))

for i in range(0, n+1):
    if i % 2 == 0:
        print(i)
