N = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(N)]
diff = arr[1] - arr[0]
if all(arr[i]-arr[i-1] == diff for i in range(1, N)):
    print(f"Array is an arithmetic sequence with the difference {diff}")
else:
    print("Array is not an arithemtic sequence")
