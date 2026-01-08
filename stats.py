def get_num_words(txt):
    # removes "whitespace" from the string, 
    # turns into a list of individual words
    words = txt.split()
    return len(words)

def get_char_freq(words):
    freq = {}
    # check if word is already present, 
    # if present then increase the count
    # if not then add 
    for word in words:
        clean_word = word.lower()
        if clean_word in freq:
            freq[clean_word] += 1
        else:
            freq[clean_word] = 1
    return freq

def sort_on(dict_item):
    # to guide python, sort the list specifically according to "num"
    return dict_item["num"]

def get_sorted(freq):
    srt = []
    # Dicts don't have specific order,
    # so to sort them we move them into a list of dicts
    for char, count in freq.items():
        srt.append({"char": char, "num": count})
    srt.sort(key=sort_on, reverse = True) # reverse = True ensures the list goes in descending order
    return srt


