STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):

    wordList = {}

    with open(file, "rt") as infile:
        text = infile.read()
        allWords = text.lower().replace('—', ' ').replace(':', ' ').replace(
            ',', ' ').replace('.', ' ').replace('/n', ' ').replace('"', ' ').split()

        for word in allWords:
            if word not in STOP_WORDS:
                if word in wordList:
                    wordList[word] += 1
                else:
                    wordList[word] = 1

        result = reversed((sorted(wordList, key=wordList.get)))
        width = max([len(el) for el in wordList])
        for el in result:
            print(f"{el:>{width}}  |  {wordList[el]:>2} {'*' * wordList[el]}")


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
