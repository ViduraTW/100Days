
import List



#this prints it out for how ever many fruits are in the list
#it does it by creating a temporary variable for it


for fruit in List.fruits:
    print(fruit)
    print(fruit + " pie")

#the indentation is very important so that any code after doesnt immediatley get joined with the for loop

print(List.fruits)


#within the range function it goes from the first number to the last
#the first number is the starting point
#the second number is the endpoint
#the third number is how many it is increasing by

total = 0

for number in range(1, 101, 2):
    total += number

print(total)










