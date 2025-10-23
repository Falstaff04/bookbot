# python

def word_count(text):
    num_words = 0
    words = text.split()
    num_words = len(words)
    return num_words
    

def char_numbs(text_count):
    text_lower = text_count.lower()
    letters={}
    for letter in text_lower:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters
    

def sorted_char(counts):
    items = []
    for c, n in counts.items():
        items.append({"char": c, "num": n})

    def sort_on(items):
        return items["num"]    
    items.sort(reverse= True, key=sort_on)
    return items