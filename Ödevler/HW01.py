
#HOMEWORK-1
#Create two list. The first list should consist of odd numbers. The second list is a also of even numbers.
#Merge these two lists. Multiply all values in the list by 2.
#Use a loop to print the data type of the values in the new list.

list1 = [8,10,22,34,68,82] #list of even numbers
list2 = [7,9,13,27,61,99] #list of odd numbers

list3=[ (a+b)*2 for a,b in zip(list1,list2)] # pooled to 2 lists and multiply all values in the list3 by 2.

print(type(list3),list3) #give a data type of the all values in the list3.

