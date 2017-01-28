# Get the number of elements and number of operations
n, m = map(int, raw_input().strip().split(' '))

# Initialize a list with all zeroes
elements = [0] * n

# Go through m operations
for i in range(m):
    # Get the indices and the value k to be added
    a, b, k = map(int, raw_input().strip().split(' '))
    
    # Offset for zero-indexing
    a -= 1
    b -= 1
    
    # Calculate the slope
    elements[a] += k
    
    # Bounds check
    if b+1 < len(elements):
        elements[b+1] -= k

maximum_element = 0
temp = 0

# Calculate the accumulated slope
for i in elements:
    temp = temp + i
    if (maximum_element < temp):
        maximum_element = temp
    
# Print the maximum
print maximum_element