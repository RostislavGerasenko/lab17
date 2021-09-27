N = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(N)]
out = min(arr[1::2])
print(f"The minimal element of those with even numbers is {out}")
