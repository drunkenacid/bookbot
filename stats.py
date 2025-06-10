def count_words(file_contents):
    word_count = len(file_contents.split())
    return(word_count)

def character_count(file_contents):
    c_counts = {}
    new_list = []
    
    words = file_contents.split()
    
    for word in words:
        for letter in word:
            new_list.append(letter.lower())
    
    for i in new_list:
        if i in c_counts:
            c_counts[i] += 1
        else:
            c_counts[i] = 1
    list_sorted = sorted_list(c_counts)
           
    return(c_counts,list_sorted)

def value(dict):
    return dict["num"]

def sorted_list(c_counts):
    sorted_dict = []

    for letter in c_counts:
        new_dict = {}
        if letter.isalpha() == True:
            new_dict["char"] = letter
            new_dict["num"] = c_counts[letter]
            sorted_dict.append(new_dict)

    sorted_dict.sort(reverse=True, key=value)
    return(sorted_dict)