# OPERATORS

# 01 arthamic operators
# 02 relational/comparision operators
# 03 assignment operators
# 04 logical operators
# 05 bitwise operators
# 06 identity operators
# 07 membership operators

# 01 Arithmetic Operators (+, -, *, /, %, **)
 # arthamic operator is use to perform mathematical operations like addition, subtraction, multiplication, division, etc.

a = 10
b = 5

print(a + b)  # Addition(add)
print(a - b)  # Subtraction(diff.)
print(a * b)  # Multiplication(mul)
print(a / b)  # Division(div)
print(a % b)  # Modulus(remainder)
print(a ** b)  # Exponentiation(power a^b)
print(a // b)  # Floor Division(quotient)


# 02 Relational/Comparison Operators (==, !=, >, <, >=, <=)
 # relational operator is use to compare two values and return a boolean result (True or False).
a = 10
b = 5

print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to


# 03 Assignment Operators (=, +=, -=, *=, /=, %=, **=, //=)
 # assignment operator is use to assign values to variables and perform operations on them.
a = 10
b = 5

print(a)  # Initial value of a

a += b  # a = a + b
print(a)  # Updated value of a

a -= b  # a = a - b
print(a)  # Updated value of a

a *= b  # a = a * b
print(a)  # Updated value of a

a /= b  # a = a / b
print(a)  # Updated value of a

a %= b  # a = a % b
print(a)  # Updated value of a

a **= b  # a = a ** b
print(a)  # Updated value of a

a //= b  # a = a // b
print(a)  # Updated value of a

# 04 Logical Operators (and, or, not)
 # logical operator is use to combine multiple boolean expressions and return a boolean result.

a = True
b = False

print(a and b)  # Logical AND (both must be True)
print(a or b)   # Logical OR (at least one must be True)
print(not a)    # Logical NOT (inverts the boolean value)

# 05 Bitwise Operators (&, |, ^, ~, <<, >>)
 # bitwise operator is use to perform operations on individual bits of integers.
a = 10  # 1010 in binary
b = 4   # 0100 in binary

print(a & b)  # Bitwise AND
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR
print(~a)     # Bitwise NOT
print(a << 1)  # Left shift
print(a >> 1)  # Right shift

# 06 Identity Operators (is, is not)
 # identity operator is use to compare the memory locations of two objects.
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True, both refer to the same object
print(a is not c)  # True, a and c refer to different objects
print(a is c)      # False, a and c have the same content but are different objects
print(a is not b)  # False, a and b refer to the same object

# 07 Membership Operators (in, not in)
 # membership operator is use to check if a value is present in a sequence (like a list, tuple, or string).
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)      # True, 3 is in the list
print(6 not in my_list)  # True, 6 is not in the list
print("MAYUR PATIL*" in my_list)  # False, string is not in the list
print("MAYUR PATIL*" not in my_list)  # True, string is not in the list

 
