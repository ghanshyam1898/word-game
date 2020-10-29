with open("DICTIONORY", 'r') as myfile:
    data = myfile.read()
    words = data.split("\n")

told = []
word = 'rgbsfvsdc'

while True:
    # receive a new valid word from user
    while word not in words and word not in told:
        word = raw_input("Enter your word : ")

    for item in words:
        # say the word ending with alphabet as the last alphabet of word user has told
        if item[0] == word[len(word)-1] and item not in told:
            # ignore words ending with 's and choose word with at least 4 alphabets
            if len(item) > 3 and not item.endswith("'s"):
                told.append(item)
                told.append(word)
                print "My word is " + item + "\n\n"
                break
    word = 'rgbsfvsdc'
