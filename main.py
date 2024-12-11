def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        #print(wordCount(file_contents))
        #print(charCount(file_contents))
        my_dictionary = {}
        my_dictionary = charCount(file_contents)
        my_list = charCountList(my_dictionary)

        for y in my_list:
            if(not y["char"].isalpha()):
                continue
            print(f"The '{y['char']}' character was found {y['num']} times")

def wordCount(text):
    words = []
    words = text.split()
    return len(words)

def charCount(text):
    char_count = {}
    text = text.lower()
    for x in text:
        if(x in char_count):
            char_count[x] += 1
            #print(x)
        else:
            char_count[x] = 1
            #print("add")
    return char_count

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]
def charCountList(char_dict):
    myList = []
    for x in char_dict:
        myList.append({'char':x,'num':char_dict[x]})
    #myList.sort(reverse=true, key=sort_on)
    myList.sort(key=sort_on)
    myList.reverse()
    return myList

main()