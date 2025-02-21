def main(): 
    hours, minutes = convert()
    hours, minutes = int(hours), int(minutes)

    if (7 <= hours < 8) or (hours == 8 or hours == 7 and minutes == 0):
        return "breakfast time"
    elif (12 <= hours < 13) or (hours == 12 or hours == 13 and minutes == 0):
        return "lunch time"
    elif (18 <= hours < 19) or (hours == 18 or hours == 19 and minutes == 0):
        return "dinner time"
    else:
        return

def convert():
    x = input("What time is it?").split(":")
    return x
    
answer = main()
print(answer)