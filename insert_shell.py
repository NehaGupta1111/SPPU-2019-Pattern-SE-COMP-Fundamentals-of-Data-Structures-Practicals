def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def display_top_five(arr):
    print("Top five scores:")
    for score in sorted(arr)[-5:]:
        print(score)

# Driver code
num_students = int(input("Enter the number of students: "))
percentages = []

for i in range(num_students):
    percentage = float(input(f"Enter the percentage of student {i + 1}: "))
    percentages.append(percentage)

# Using Insertion Sort
insertion_sort_percentages = percentages.copy()
insertion_sort(insertion_sort_percentages)
print("Array after Insertion Sort:", insertion_sort_percentages)
display_top_five(insertion_sort_percentages)

# Using Shell Sort
shell_sort_percentages = percentages.copy()
shell_sort(shell_sort_percentages)
print("\nArray after Shell Sort:", shell_sort_percentages)
display_top_five(shell_sort_percentages)
