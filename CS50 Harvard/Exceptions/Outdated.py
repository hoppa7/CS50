import string
def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    def is_valid(m , d):
        return (0 < m < 13 and 0 < d < 32)
    while True:
        try:
            n = input("Date: ")
            if "/" in n:
                date_list = n.split("/")
                if is_valid(int(date_list[0]), int(date_list[1])):
                    print(f"{date_list[2]}-{int(date_list[0]):02}-{int(date_list[1]):02}")
                    break
                else:
                    continue
            else:
                n_list = n.split(" ")
                n_list = ["".join(c for c in n_list if c not in string.punctuation) for n_list in n_list]
                month_num = months.index(n_list[0]) + 1
                if is_valid(int(month_num), int(n_list[1])):
                    print(f"{n_list[2]}-{month_num:02}-{int(n_list[1]):02}")
                    break
                else:
                    continue                    
        except ValueError:
            break
main()