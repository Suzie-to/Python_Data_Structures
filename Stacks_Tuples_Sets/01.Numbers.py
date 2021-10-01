''' First, you will be given two sequences of integers values on different lines. The values of the sequences are
    separated by a single space between them.
Keep in mind that each sequence should contain only unique values.
Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
    • "Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
    • "Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
    • "Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
    • "Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
    • "Check Subset" - check if any of the given sequences is a subset of the other. If it is, print "True". Otherwise,
        print "False".
At the end print the final sequences, separated by a comma and a space ", ". The values in each sequence should be
sorted in ascending order.'''

nums_set1 = set(int(x) for x in input().split())
nums_set2 = set(int(x) for x in input().split())

# print(nums_set1)
# print(nums_set2)

num_commands = int(input())

for i in range(num_commands):
    command = input().split()
    numbers = set([int(x) for x in command[2:]])

    if command[0] == "Add" and command[1] == "First":
        nums_set1 = nums_set1.union(numbers)

    elif command[0] == "Add" and command[1] == "Second":
        nums_set2 = nums_set2.union(numbers)

    elif command[0] == "Remove" and command[1] == "First":
        nums_set1.difference_update(numbers)

    elif command[0] == "Remove" and command[1] == "Second":
        nums_set2.difference_update(numbers)

    elif command[0] == "Check":
        if nums_set2.issubset(nums_set1) or nums_set1.issubset(nums_set2):
            print("True")
        else:
            print("False")

print(", ".join(str(x) for x in sorted(nums_set1)))
print(", ".join(str(x) for x in sorted(nums_set2)))
