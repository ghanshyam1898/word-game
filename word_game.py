if __name__ == '__main__':
    with open("DICTIONORY", 'r') as myfile:
        data = myfile.read()
        words = data.split("\n")
    told = []
    word = 'rgbsfvsdc'
    
    while True:
        while word not in words and word not in told:
            word = raw_input("Enter your word : ")
        
        for item in words:
            if item[0] == word[len(word)-1] and item not in told:
                if len(item) > 3 and "'" not in item:
                    told.append(item)
                    told.append(word)
                    print "My word is " + item
                    print "\n\n"
                    break
        word = 'rgbsfvsdc'
