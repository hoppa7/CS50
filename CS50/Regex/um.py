import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    ums = len(re.findall(r"\bum\b", s, flags=re.IGNORECASE))
    return ums

if __name__ == "__main__":
    main()

