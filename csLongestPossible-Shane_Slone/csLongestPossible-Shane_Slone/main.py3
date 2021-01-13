def csLongestPossible(str_1, str_2):
    input_str = str_1 + str_2
    if input_str == "":
        return ""
    result = ""
    for char in input_str:
        if result.find(char) == -1:
            result += char
    result = list(result)
    result.sort()
    return "".join(result)

