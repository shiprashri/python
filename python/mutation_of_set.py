# Read initial set A
num_elements_A = int(input())
set_A = set(map(int, input().split()))

# Read number of operations N
N = int(input())

# Process each operation
for _ in range(N):
    # Read operation name and length of the other set (not used in this case)
    operation_info = input().split()
    operation_name = operation_info[0]
    len_other_set = int(operation_info[1])
    
    # Read elements of the other set (not used in this case)
    other_set = set(map(int, input().split()))
    
    # Perform the operation on set A
    if operation_name == 'intersection_update':
        set_A.intersection_update(other_set)
    elif operation_name == 'update':
        set_A.update(other_set)
    elif operation_name == 'symmetric_difference_update':
        set_A.symmetric_difference_update(other_set)
    elif operation_name == 'difference_update':
        set_A.difference_update(other_set)

# Calculate the sum of elements in set A
sum_A = sum(set_A)

# Output the result
print(sum_A)
