def decode(file):
    tuples_list = []
    last_words = []
    with open(file, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                sentence = line.split(' ')
                if len(sentence) == 2:
                    tuple_maker = (int(sentence[0]), sentence[1])
                    tuples_list.append(tuple_maker)

    tuples_list.sort(key=lambda x: x[0])
    current_level = 1
    count = 0
    for number, word in tuples_list:
        count += 1
        if count == current_level:
            last_words.append(word)
            current_level += 1
            count = 0
    return last_words


file_path = 'message.txt'

file_last_words = decode(file_path)
print(' '.join(file_last_words))

