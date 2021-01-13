def csAnythingButFive(start, end):
    count = 0
    for i in range(start, end + 1):
        num = str(i)
        if num.find("5") == -1:
            count += 1
    return count
