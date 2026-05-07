# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# a_int = int(a)

# Cannot convert directly to integer

# Convert to float
a_float = float(a)

# Convert to float first, then integer
a_float_to_int = int(float(a))

# Slice only the number part
a_slice = a[1:6]

# This line is using string slicing to take only part of the text from the variable 


# Convert sliced value to float
a_slice_float = float(a_slice)

# Testing variable b

# Convert to integer
b_int = int(b)

# Convert to float
b_float = float(b)

# Slice the number
b_slice = b[0:2]

# Testing variable c

# Cannot convert because it contains letters
# c_int = int(c)   # ValueError
# c_float = float(c)   # ValueError

# Slice only the numeric portion
c_slice = c[0:3]

# Convert sliced value to integer
c_slice_int = int(c_slice)

# Testing variable d

# Cannot convert because it contains letters
# d_int = int(d)   # ValueError
# d_float = float(d)   # ValueError

# Slice only the number
d_slice = d[7:8]

# Convert sliced value to integer
d_slice_int = int(d_slice)

# Using strip() to remove spaces
print(a.strip())
print(d.strip())

# Print values and data types
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))