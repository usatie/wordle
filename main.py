import string



if __name__ == '__main__':
    words = []
    with open('english-words/words_alpha.txt', 'r') as f:
        words = [x for x in f.read().splitlines() if len(x) == 5]
    freq = {}
    for x in string.ascii_lowercase:
        freq[x] = len([word for word in words if x in word])

    for x in string.ascii_lowercase:
        freq[x] = float(freq[x]) / float(freq['q'])

    ranks = sorted(freq.items(), reverse=True, key=lambda x:x[1])

    while True:
        for item in ranks:
            print(item[0], item[1])
        value = input("Search for words containing... \n")
        target_words = words
        for x in value:
            target_words = [word for word in target_words if x in word]
        print('These are the candidates: ', target_words)
    