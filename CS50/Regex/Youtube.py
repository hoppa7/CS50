import re 
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = re.search(r'src="(https?:\/\/www\.(youtube)\.com\/embed\/.*?)"', s)
    if pattern:
        link = pattern.group(1)

        clean_link =  re.sub(r"www\.|\/embed|\.com", "", link)

        finish_link = re.sub(r"youtube", "youtu.be", clean_link)
        
        return finish_link

if __name__ == "__main__":
    main()