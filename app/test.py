# please keep in mind that while working with lists in these kinds of algorithmic questions, do not mess ith the original list!
# this is going to make your job much more difficult! we don't want that.
# keep in mind that, a;ways think about all possible edge cases. but when you begin to code, don't make it very complicated, at first,
# think about normal cases. when you covered all normal cases, then you can go ahead and implement the logic for special cases as well.

# what special cases could we have in binary search algorithm?
# 1- the list is empty
# 2- the list has more than one occurrence of what you are looking for
# 3- the number does not exist in the list
# and more case that I can't think of right now!

# first you have to say what you wanna do in english, then go ahead and implement it through code.
# and again remember that, as much as you can, please avoid messing with the original list! you can simply define limits in each itteration
# and work with them rather than working and modifying the original list!


def guess_num(list1):
    n = int(input("what number are you looking for?"))
    list1.sort(reverse=True)
    start, stop = 0, len(list1) - 1
    t = 0
    while True:
        middle = (start + stop) // 2

        print(start, stop)
        if list1[middle] == n:
            t += 1
            if list1[middle-1] == n:
                for m in range(middle-1, start-1, -1):
                    if list1[m] != n:
                        return m+1, f"You reached at the answer after {t} tries!"
            elif list1[middle+1] == n:
                return middle, f"You reached at the answer after {t} tries!"
            return middle, f"You reached at the answer after {t} tries!"

        elif list1[middle] > n:
            start = middle+1
            t += 1
        elif list1[middle] < n:
            stop = middle-1
            t += 1

        if start > stop or len(list1) == 0:
            return "Sorry there is no such number in the list!"


print(guess_num(list1=[1, 4, 6, 13, 42, 76, 13, 13, 13, 13]))
