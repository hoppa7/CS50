import sys
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    if len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet.getFonts():
        n = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        result = figlet.renderText(n)
        print(result)

    elif len(sys.argv) == 1:
        n = input("Input: ")
        print("hello")
        result = figlet.renderText(n)
        print(result)
    
    else:
        print("Invalid usage")
        sys.exit()

main()