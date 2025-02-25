import string

def main():
    n = input("Plate: ")
    if is_valid(n):
        return "Valid"
    else:
        return "Invalid"


def is_valid(n):
    mid_length = int(len(n) / 2)
    if not n[:2].isalpha():
        return False
    if not (2 <= len(n) <= 6):
        return False
    if not (n[mid_length:int(len(n))].isnumeric()):
        return False
    if any(char in string.punctuation for char in n):
        return False
    if n[mid_length].startswith("0"):
        return False
    else:
        return True

print(main())
