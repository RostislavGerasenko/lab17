N = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(N)]
K = int(input("Number of the first element to find the average of: ")) - 1
# L is not reduced by 1 due to Python slicing not counting last element
L = int(input("Number of the last element to find the average of: "))
avg = sum(arr[K:L])/len(arr[K:L])
print(f"The average value of the subarray: {avg}")
