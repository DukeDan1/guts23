import urllib.request

url = 'https://www.gutenberg.org/cache/epub/100/pg100.txt'
response = urllib.request.urlopen(url)
text = response.read().decode('utf-8')
words = {}

for x in text.split('\n'):
    line = x.split()
    for word in line:
        word = word.lower()
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

# turn into 2D array and sort
wordList = [[k, v] for k, v in words.items()]
wordList.sort(key=lambda x: x[1], reverse=True)

for x in range(0, 100):
    print(str(x + 1)+":", wordList[x][0], wordList[x][1])