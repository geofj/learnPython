# The code below aims to replace 'b' with 'x' in the list elements.
#
# However, the output of the code is still ['a', 'b', 'c'].
#
# Try to fix the code so 'b' is replaced with 'x'.
#
# elements = ['a', 'b', 'c']
# new = 'x'
# new = elements[1]
# print(elements)

elements = ['a', 'b', 'c']
new = 'x'
elements[1] = new
# new variable appends index 1 of elements list
print(elements)