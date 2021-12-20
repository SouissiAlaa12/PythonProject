# question 1
def read_words():
    with open("D:/Esen/BI/LPE-BI_Mini-projet Python/Projet/english-common-words.txt") as ecw:
        l_wor = []
        for line in ecw:
            if len(line) >= 3:
                l_wor.append(line.upper().strip("\n"))
    return l_wor

# question 2
def read_sequences():
    with open("D:/Esen/BI/LPE-BI_Mini-projet Python/Projet/human-proteome.fasta") as hp:

        d_pr = {}
        d_id = ""
        for line in hp:
            if line.startswith(">"):
                d_id = line.split("|")[1]
                d_pr[d_id] = ""
            else:
                d_pr[d_id] += line.strip("\n")

    return d_pr
print(read_sequences())


# question 3
def search_words_in_proteome(d_pr, l_wor):
    d_fw = {}
    for w in l_wor:
        count = 0
        for i in d_pr:
            if w in d_pr[i]:
                count += 1
        if count != 0:
            d_fw[w] = count

    return d_fw


# question 4
def find_most_frequent_word(d_fw):
    freq_word = max(d_fw.values())
    for word in d_fw:
        if d_fw[word] == freq_word:
            print(f"{word} is the most frequent word with {freq_word} time ")



# question 5
def search_words_in_proteom(d_pr, l_wor):
    d_fw = {}
    for w in l_wor:
        for i in d_pr:
            nb = d_pr[i].count(w)
            if nb > 0:
                if not d_fw.get(w, False):
                    d_fw[w] = 0
                d_fw[w] += nb
        print(f"{w} appears {d_fw.get(w, 0)} times")
    return d_fw


if __name__ == '__main__':
    print("**** The number of words found ****")
    words = read_words()
    print(f"{len(words)} word ")
    print("**** The number of sequences found ****")
    sequence = read_sequences()
    print(f"{len(sequence)} sequence")
    print("**** The sequence of O95139 ****")
    print(sequence.get("O95139"))
    print("**** The most frequent word in the human proteome is ****")
    find_most_frequent_word(search_words_in_proteome(sequence, words))