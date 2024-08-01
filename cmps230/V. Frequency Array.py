def frequency_array(N, M, inputList):
    # Initialize the frequency array with zeros
    freq = [0] * (M + 1)
    
    # Count the frequency of each number in inputList
    for number in inputList:
        freq[number] += 1
    
    # Print the frequencies for numbers 1 to M
    for i in range(1, M + 1):
        print(freq[i])

# Read input
N, M = map(int, input().split())
inputList = list(map(int, input().split()))

# Solve the problem
frequency_array(N, M, inputList)
