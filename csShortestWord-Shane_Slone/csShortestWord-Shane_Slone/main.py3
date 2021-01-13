def csShortestWord(input_str):
    input_list = []
    input_list = input_str.split(" ")
    for i, word in enumerate(input_list):
        input_list[i] = word.strip(",.?!:;")
        if word.find("\t") != -1:
            input_list += word.split("\t")
    input_list.sort(key = lambda s: len(s))
    print(input_list)
    return len(input_list[0])
