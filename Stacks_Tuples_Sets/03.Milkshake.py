''' First, you will be given two sequences of integers representing chocolates and cups of milk.
You have to start from the last chocolate and try to match it with the first cup of milk. If their values are equal,
you should make a milkshake and remove both ingredients. Otherwise, you should move the cup of milk at the end of the
sequence and decrease the value of the chocolate by 5 without moving it from its position.

If any of the values are equal to or below 0, you should remove them from the records before mixing it with the other
ingredient.

When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left, you need to
stop making chocolate milkshakes.

Input
    • On the first line of input, you will receive the integers representing the chocolate, separated by  ", ".
    • On the second line of input, you will receive the integers representing the cups of milk, separated by ", ".
Output
    • On the first line, print:
        ◦ If you successfully made 5 milkshakes: "Great! You made all the chocolate milkshakes needed!"
        ◦ Otherwise: "Not enough milkshakes."
    • On the second line - print:
        ◦ If there are chocolates left: "Chocolate: {chocolate1}, {chocolate2}, (…)"
        ◦ Otherwise: "Chocolate: empty"
    • On the third line - print:
        ◦ If there are cups of milk left: "Milk: {milk1}, {milk2}, {milk3}, (…)"
        ◦ Otherwise: "Milk: empty" '''

from collections import deque

choco_bars = deque(int(x) for x in input().split(", "))
milk_cups = deque(int(x) for x in input().split(", "))

milkshakes = 0

while choco_bars and milk_cups and milkshakes < 5:
    chocolate_bar = choco_bars.pop()
    milk_cup = milk_cups.popleft()

    if chocolate_bar <= 0 and milk_cup <= 0:
        continue
    elif chocolate_bar <= 0:
        milk_cups.appendleft(milk_cup)
        continue

    elif milk_cup <= 0:
        choco_bars.appendleft(chocolate_bar)
        continue

    elif chocolate_bar == milk_cup:
        milkshakes += 1
    else:
        milk_cups.append(milk_cup)
        choco_bars.append(chocolate_bar - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if choco_bars:
    print(f"Chocolate: {', '.join([str(x) for x in choco_bars])}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join([str(x) for x in milk_cups])}")
else:
    print("Milk: empty")
