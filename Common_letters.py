if __name__ == '__main__':
    print("Write your sentence:")
    sentence = ""

    while sentence != "Close":
        sentence = str(input(">"))
        sentence_1 = sentence.replace(" ", "")
        char_frequncy = {}
        for char in sentence_1:
            if char in char_frequncy:
                char_frequncy[char] += 1
            else:
                char_frequncy[char] = 1

        char_frequncy_sorted = sorted(
            char_frequncy.items(),
            key=lambda kv: kv[1],
            reverse=True)
        if sentence != "Close":
            print(char_frequncy_sorted[0])
        else:
            continue

    else:
        print("CLosing...")
