import random
import sys
def main():
    while True:
        try:
            n = int(input("Level: "))
            num_random = random.randint(1, n)
            while True:    
                try:
                    n = int(input("Guess: "))
                    if n < 1:
                        raise ValueError
                    else:
 
                        if n > num_random:
                            print("Too large!")
                            continue
                        elif n < num_random:
                            print("Too small!")
                            continue
                        else:
                            print("Just right!")
                            sys.exit()
                except ValueError:
                    continue
        except ValueError:
            continue

if __name__ == "__main__":
    main()