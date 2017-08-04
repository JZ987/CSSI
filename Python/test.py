some_numbers =[2, 52, 19, 46, 1000]

for number in some_numbers:
    number = (number + 10) / 2
    print str(number)

print "------------------------------"
presidents = ["George Washington", "John Adams", "Thomas Jefferson",
              "James Madison", "James Monroe", "John Quincy Adams"]

for president in presidents:
    print president[::-1]

print "------------------------------"
numbers = range(10, -1, -1)

for number in numbers:
    print "{} bottles of milk on the wall".format(number)

print "------------------------------"
user_input = raw_input("Input anything: ")

number_of_lower_case = 0
number_of_upper_case = 0

for word in user_input.split():
    for letter in word:
        if letter == 'a':
            number_of_lower_case += 1;
        elif letter == 'A':
            number_of_upper_case += 1;

print "Number of letter A {}".format(number_of_upper_case)
print "Number of letter a {}".format(number_of_lower_case)

print "------------------------------"
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

total = 0;

for row in matrix:
    for col in row:
        total += col;

print "The sum of the matrix is {}".format(total)

print "------------------------------"
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
new_array =[]
index = 0
row = 0
col = 0
while row < 3:
    temp = []
    col = 0
    while col < 4:
        temp.append(array[index])
        index += 1
        col += 1
    new_array.append(temp)
    row += 1

print new_array
