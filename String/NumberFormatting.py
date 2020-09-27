#integer numbers with minimum width
print("{:5d}".format(12))

#reserved width rule is not applicable for numbers longer than padding
print("{0:2d}".format(12345))

#padding for float numbers
print("{0:8.3f}".format(123.456789))

#integer numbers with minimum width filled with zeros
print("{0:05d}".format(12))

#padding for float numbers filled with zeros
print("{0:08.3f}".format(12.453489))

#Number formatting with alignment (<=left, >=right, ^=center, = symbol forces the signed(+,-) to leftmost position
#by default all numbers align right except string

print("{0:<6.2f}".format(12.3567))

#integers with left alignment with zeros can cause problems, it prints 12000 instead of 12
print("{0:<05d}".format(12))

# = forces the sign to leftmost position
print("{:=8.3f}".format(-12.2346))