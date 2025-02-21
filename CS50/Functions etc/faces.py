import sys
sys.stdout.reconfigure(encoding='utf-8')
def faces(input):
    word = input
    word = convert(word)
    print(word)
def convert(word):
    word = word.replace(":)", "🙂")
    word = word.replace(":(", "🙁")
    return word
# Example usage
faces("Hello :)")
faces("Goodbye :(")
faces("Hello :) Goodbye :(")