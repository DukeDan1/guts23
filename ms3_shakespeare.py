import urllib.request
import nltk

def data_in():
    url = 'https://www.gutenberg.org/cache/epub/100/pg100.txt'
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')
    return text

def process_data(text, lens):
    ngrams = [{}] * len(lens)
    print(ngrams)
    textarr = [x.strip().lower() for x in text.split()]
    for y in lens:
        # for each length value, get ngrams
        for gram in nltk.ngrams(textarr, y):
            if ' '.join(gram) in ngrams[y - lens[0]]:
                ngrams[y - lens[0]][' '.join(gram)] += 1
            else:
                ngrams[y - lens[0]][' '.join(gram)] = 1
            
    return ngrams

def main():
    LENGTHS = [2, 3, 4, 5]
    text = data_in()
    words = process_data(text, LENGTHS)
    # turn into 2D array and sort

    print("Top 10 ngrams:", end='\n\n')

    n = 0
    for x in words:
        print(f"Top 10 {LENGTHS[n]}-grams:", end='\n\n')
        wordList = [[k, v] for k, v in x.items()]
        wordList.sort(key=lambda x: x[1], reverse=True)
        for xx in range(0, 10):
            print(str(xx + 1)+":", wordList[xx][0], "- occurrences:", wordList[xx][1])
        n+=1
        print()

        

main()
