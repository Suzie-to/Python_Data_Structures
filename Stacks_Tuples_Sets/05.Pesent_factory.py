''' First, you will receive a sequence of integers representing the number of materials for crafting toys in one box.
After that, you will be given another sequence of integers – their magic level.
Your task is to mix materials with magic so you can craft presents, listed in the table below with the exact magic
level:


Present
Magic needed
Doll
150
Wooden train
250
Teddy bear
300
Bicycle
400

You should take the last box with materials and the first magic level value to craft a toy. Their multiplication
calculates the total magic level. If the result equals one of the levels described in the table above, you craft the
present and remove both materials and magic value. Otherwise:
    • If the product of the operation is a negative number, you should sum the values together, remove them both from
    their positions, and add the result to the materials.
    • If the product doesn't equal one of the magic levels in the table and is a positive number, remove only the magic
    value and increase the material value by 15.
    • If the magic or material (or both) equals 0, remove it (or both) and continue crafting the presents.
Stop crafting presents when you run out of boxes of materials or magic level values.
Your task is considered done if you manage to craft either one of the pairs:
    • a doll and a train
    • a teddy bear and a bicycle
Input
    • The first line of input will represent the values of boxes with materials - integers, separated by a single space
    • On the second line, you will be given the magic values - integers again, separated by a single space
Output
    • On the first line - print whether you've succeeded in crafting the presents:
    • "The presents are crafted! Merry Christmas!"
    • "No presents this Christmas!"
    • On the next two lines print the materials and magic that are left, if there are any (otherwise skip the line)
    • "Materials left: {material1}, {material2}, … {materialN}"
    • "Magic left: {magicValue1}, {magicValue2}, … {magicValueN}"
    • On the next lines print the presents you have crafted, ordered alphabetically in the format:
    • "{toy_name1}: {amount}
{toy_name2}: {amount}
...
{toy_nameN}: {amount}"
Constraints
    • All the materials' values will be integers in the range [1, 100]
    • Magic level values will be integers in the range [-10, 100]
    • In all cases, at least one present will be crafted '''

from collections import deque

boxes = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])

total_magic_level = 0

presents = {150: "Doll",
            250: "Wooden train",
            300: "Teddy bear",
            400: "Bicycle"
            }

crafted_presents = {}
while boxes and magic_values:
    box = boxes.pop()
    magic_level = magic_values.popleft()
    result = box * magic_level

    if box == 0 and magic_level:
        continue
    elif box == 0:
        magic_values.appendleft(magic_level)
    elif magic_level == 0:
        boxes.append(box)

    if result < 0:
        boxes.append(box + magic_level)

    elif result in presents:
        present = presents[result]

        if present in crafted_presents:
            crafted_presents[present] += 1
        else:
            crafted_presents[present] = 1
    else:
        boxes.append(box + 15)


completed = ('Doll' in crafted_presents and 'Wooden train' in crafted_presents) or \
            ('Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents)

if completed:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")


if boxes:
    print(f"Materials left: {', '.join(reversed([str(x) for x in boxes]))}")
if magic_values:
    print(f"Magic left: {', '.join(str(magic) for magic in magic_values)}")

for present, count in sorted(crafted_presents.items()):
    print(f"{present}: {count}")
