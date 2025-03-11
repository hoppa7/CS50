from datetime import datetime
import inflect
import sys

p = inflect.engine()

def main():
    print(mins_inflect(date_to_mins(input("Date of birth: "))))

def date_to_mins(date):
    try:
        now = datetime.now()

        date_format = "%Y-%m-%d"

        official_date_input = datetime.strptime(date, date_format)

        midnight_now = now.replace(hour=0, minute=0, second=0, microsecond=0)

        minutes_diff = round((midnight_now - official_date_input).total_seconds() / 60)

        return minutes_diff
    
    except ValueError:
       sys.exit("Invalid Input")

def mins_inflect(minutes):
    minutes_difference_ordinal_word = p.number_to_words(minutes)
    return (f"{minutes_difference_ordinal_word} minutes.")


if __name__ == "__main__":
    main()