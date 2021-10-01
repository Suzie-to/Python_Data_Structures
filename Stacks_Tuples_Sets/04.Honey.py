''' Worker-bees collect nectar. When a worker-bee has found enough nectar, she returns to the hive to drop off the load.
The worker-bees pass the nectar to waiting bees so they can really start the honey-making process.
You will receive 3 sequences:
    • a sequence of integers, representing working bees,
    • a sequence of integers, representing nectar,
    • a sequence of symbols – "+", "-", "*" or "/", representing the honey-making process.
Your task is to check if the bee has collected enough nectar to return to the hive and to keep track of the total honey
waiting bees have made with the collected nectar.
Step one: you should check if the bee has collected enough nectar. You should take the first bee and try to match it
with the last nectar:
    • If the nectar value is more or equal to the value of the bee, it is considered collected, and the bee returns to
    the hive to drop off the load (step two).
    • If the nectar value is less than the value of the bee, you should remove the nectar and try to match the bee with
    the next nectar's value.
Step two: you should calculate the honey made with the passed nectar. When you find a bee and nectar that have matched
(step one), you should take the first symbol in the sequence of symbols ("+", "-", "*" or "/") and make the
corresponding calculation as follows:
"{matched bee} {symbol} {matched nectar}"
The result represents the honey that is made from the passed nectar. The calculation should always return the absolute
value of the result. After the calculation, remove the bee, the nectar, and the symbol.
Stop making honey when you are out of bees or nectar.
There always will be enough symbols in the sequence of symbols
Input
    • On the first line, you will be given the values of bees - integers, separated by a single space
    • On the second line, you will be given the nectar's values - integers, separated by a single space
    • On the third line, you will be given symbols - "+", "-", "*" or "/", separated by a single space
Output
    • On the first line - print the total honey made:
        ◦ "Total honey made: {total honey}"
    • On the next two lines print the bees or the nectar that are left, if there are any, otherwise skip the line:
        ◦ "Bees left: {bee1}, {bee2}, … {beeN}"
        ◦ "Nectar left: {nectar1}, {nectar2}, … {nectarN}" '''

from collections import deque

bees = deque([int(x) for x in input().split()])  # FIFO tail
nectar = [int(x) for x in input().split()]  # LIFO stack
signs = deque(input().split())  # honey making process

total_honey = 0
while bees and nectar:
    curr_bee = bees.popleft()
    curr_nectar = nectar.pop()

    if curr_nectar >= curr_bee:
        sign = signs.popleft()
        if sign == '+':
            total_honey += abs(curr_bee + curr_nectar)
        elif sign == '*':
            total_honey += abs(curr_bee * curr_nectar)
        elif sign == '/':
            if curr_nectar > 0:
                total_honey += abs(curr_bee / curr_nectar)
        elif sign == '-':
            total_honey += abs(curr_bee - curr_nectar)
    else:
        bees.appendleft(curr_bee)
print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join([str(bee) for bee in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")