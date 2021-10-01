''' Write a program that finds colors in a string. You will be given a string on a single line containing substrings
(separated by a single space) from which you will be able to form the following colors:
Main colors: "red", "yellow", "blue"
Secondary colors: "orange", "purple", "green"
To form a color, you should concatenate the first and the last substrings and check if you can get any of the above
colors' names. If there is only one substring left, you should use it to do the same check.
You can only keep a secondary color if the two main colors needed for its creation could be formed from the given
substrings:
    • orange = red + yellow
    • purple = red + blue
    • green = yellow + blue
Note: You could find some of the main colors needed to keep a secondary color after it is found.
When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and
return them in the middle of the original string. If the string contains an odd number of substrings, you should put
the substrings one position ahead. '''

from collections import deque


substrings = deque(input().split())

primary_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]

collected_colors = []
while substrings:
    left_el = substrings.popleft()
    right_el = substrings.pop() if substrings else '' # if the substring is not empty
    color = left_el + right_el

    if color in primary_colors or color in secondary_colors:
        collected_colors.append(color)
        continue # else:
    color = right_el + left_el

    if color in primary_colors or color in secondary_colors:
        collected_colors.append(color)
    else:
        left_el = left_el[:-1]
        right_el = right_el[:-1]
        if left_el:
            substrings.insert(len(substrings) // 2, left_el) # the index at which we want to insert the string
        elif right_el:
            substrings.insert(len(substrings) // 2, right_el)

secondary_colors_base = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}
for color in collected_colors:
    if color in primary_colors:
        continue

    required_colors = secondary_colors_base[color]
    # for x in required_colors:
    #     if x in collected_colors:
    #         print(x)
    #     else:
    #         print('NO')
    is_valid = all([x in collected_colors for x in required_colors])

    if not is_valid:
        collected_colors.remove(color)

print(collected_colors)