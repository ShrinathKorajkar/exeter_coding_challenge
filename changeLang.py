import csv, os

os.chdir(os.path.dirname(__file__))

# READING THE WORDS TO CHANGE
findWordsfile = open('find_words.txt', 'r')
wordstochange = findWordsfile.readlines()
findWords = []
for words in wordstochange:
    findWords.append(words[:-1])
findWordsfile.close()

# READING THE DICTIONARY
frenchDic = open('french_dictionary.csv')
reader = csv.reader(frenchDic)
data = list(reader)
changedic = {}
countdic = {}
for datalist in data:
    changedic[datalist[0]] = datalist[1]
    countdic.setdefault(datalist[0], 0)
frenchDic.close()

# UPDATING THE FILE
textfile = open('t8.shakespeare.txt', 'r')
outputfile = open('t8.shakespeare.translated.txt', 'w')
outputfile.write('')
outputfile.close()
outputfile = open('t8.shakespeare.translated.txt', 'a')
for lines in textfile.readlines():
    addline = ""
    for word in lines.split():
        if word in findWords:
            addline += changedic.get(word) + " "
            countdic[word] += 1
        elif word[:-1] in findWords and word[:-1] in changedic.keys():
            addline += changedic.get(word[:-1]) + word[-1] + " "
            countdic[word[:-1]] += 1
        else:
            addline += word + " "
    outputfile.write(addline[:-1] + "\n")
textfile.close()
outputfile.close()

# UPADATING THE FREQUENCY
frequencyfile = open('frequency.csv', 'w', newline='')
writer = csv.writer(frequencyfile)
for key in changedic.keys():
    writer.writerow([key, changedic[key], countdic[key]])
frequencyfile.close()