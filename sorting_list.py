# a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
  


#  Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]



list=  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]



i = 0

for i  in  range (i, len(list)):
       for j in range (i+1,len(list))  :

         if (list[i]>list [j]) :
            temp = list [i]
            list [i] = list [j]
            list [j] = temp


print ("the sorted list based on last element are", list)