def csRemoveTheVowels(input_str):
    if input_str == "":
        return ""
    result = ""
    vowels = "aeiouAEIOU"
    for char in input_str:
        if vowels.find(char) == -1:
            result += char
    return result
