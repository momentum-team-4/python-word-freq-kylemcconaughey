STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with', '"', '-', ':', ',', ' ', ''
]
file = 'one-today.txt'


def print_word_freq(file):

    wordList = {}

    with open(file, "rt") as infile:
        for line in infile:
            for word in line.split():

                word = word.lower()
                word = word.replace('—', ' ')
                word = word.replace(':', ' ')
                word = word.replace(',', ' ')
                word = word.replace('.', ' ')
                word = word.replace('/n', ' ')
                word = word.replace('"', ' ')
                word = word.strip()

                if word not in STOP_WORDS:
                    if word in wordList:
                        wordList[word] += 1
                    else:
                        wordList[word] = 1

        for el in wordList:
            print(f"{el}: {'*' * wordList[el]}")


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
