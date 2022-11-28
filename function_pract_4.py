# function that finds the max number in a set of numbers given in parameters

def max_num(a,b,c):
  return max([a,b,c])

# Invoke max_num to test

print(max_num(8,2,3))
print(max_num(10,62,77))
print(max_num(15,30,2))

# Write a Python function called mult_list()  to multiply all the numbers in a list.

def mult_list(lst):

  #if list is empty, return 0
  if len(lst) == 0:
    return 0

  #product starts with first element of list
  prod = lst[0]

  #go through list elements and multiply them together
  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i

  return prod
    
# Invoke mult_list to test

print(mult_list([1,2,3]))
print(mult_list([]))
print(mult_list([2, 5, 10]))

# Write a Python function called rev_string() to reverse a string.

def rev_string(my_str):
  return my_str[::-1]

# Invoke rev_string to test

print(rev_string("is"))
print(rev_string("this"))
print(rev_string("working?"))

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(x,a,b):
  return x in range(a,b+1)

# Invoke num_within to test
     
print(num_within(2,0,4))     
print(num_within(7,1,7))     
print(num_within(10,1,4))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

# Invoke to test pascal()
pascal(2)
pascal(5)