import sys
import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = re.search(r"(\d{1,2}):?(\d{2})?\s*(am|pm)\s*to\s*(\d{1,2}):?(\d{2})?\s*(am|pm)", s, flags=re.IGNORECASE)
    if pattern:
        hour1 = int(pattern.group(1))
        minute1 = pattern.group(2)
        period1 = pattern.group(3).lower()

        hour2 = int(pattern.group(4))
        minute2 = pattern.group(5)
        period2 = pattern.group(6).lower()

        if not (0 < int(minute1) < 59) and not (0 < int(minute2) < 59):
            raise ValueError

        if period1 == "pm" and hour1 != 12:
            hour1 += 12
        elif period1 == "am" and hour1 == 12:
            hour1 = 0

        if period2 == "pm" and hour2 != 12:
            hour2 += 12
        elif period2 == "am" and hour2 == 12:
            hour2 = 0
        
        
        if minute2:
            return f"{hour1}:00 to {hour2}:{minute2}"
        elif minute1:
            return f"{hour1}:{minute1} to {hour2}:00"
        else:
            return f"{hour1}:00 to {hour2}:00"
    else:
        raise ValueError




if __name__ == "__main__":
    main()