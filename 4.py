N = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(N)]
# Default value if no other element is a local maximum
last = 1
# Last element is special as no element comes after it.
# An alternative hack is to append -inf to end of array
if arr[N-1] > arr[N-2]:
    last = N
else:
    for i in reversed(range(1, N)):
        if arr[i-1] < arr[i] > arr[i+1]:
            last = i + 1
            break
print(f"The last local maximum in the array is the element number {last}")
