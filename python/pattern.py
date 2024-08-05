def print_door_mat(N, M):
    # Top half of the mat
    for i in range(1, N, 2):
        pattern = ".|." * i
        print(pattern.center(M, '-'))

    # Middle part with 'WELCOME'
    print("WELCOME".center(M, '-'))

    # Bottom half of the mat
    for i in range(N-2, -1, -2):
        pattern = ".|." * i
        print(pattern.center(M, '-'))

if __name__ == "__main__":
    # Read input from standard input
    input_str = input().strip()
    
    # Split the input string by space to get N and M
    N, M = map(int, input_str.split())

    # Print the door mat
    print_door_mat(N, M)
