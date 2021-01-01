from pathlib import Path
import sys


def wordcount(path):
    with path.open() as fh:
        lines = 0
        words = 0
        chars = 0
        for line in fh:
            chars += len(line)
            words += len(line.split())
            lines += 1
        print(f"chars={chars} words={words} lines={lines} {path}")


if __name__ == '__main__':
    for filename in sys.argv[1:]:
        wordcount(Path(filename))
