N = int(input("Size of the array: "))
arr = [int(input(f"Element number {i+1} of the array: ")) for i in range(N)]
seen = {}
for index, item in enumerate(arr):
    if item in seen:
        print(f"The repeating elements are elements number {seen[item] + 1} and {index + 1}")
        break
    seen[item] = index
