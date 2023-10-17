def num_sum(row):
    total = 0
    for num in row:
        total += num
    return total


def sort_arr(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if num_sum(arr[j]) > num_sum(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr



N = int(input("Введіть розмірність масиву (NxN): "))
matrix = []


print("Введіть елементи масиву:")

for i in range(N):
    row = []
    row_input = input(f"Введіть {N} цілих чисел для рядка {i + 1}: ").split()
    for item in row_input:
        row.append(int(item))
    matrix.append(row)

sums = [num_sum(row) for row in matrix]

sorted_matrix = sort_arr(matrix)

print("Суми рядків:")
for row_sum in sums:
    print(row_sum)



print("Відсортований масив за зростанням суми чисел рядка:")
for row in sorted_matrix:
    print(row)