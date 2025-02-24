import random
def main():
    score = 0
    level = get_level()
    for i in range(10):
        try:
            difficulty = generate_integer(level)
            problem = input(f"{difficulty[0]} + {difficulty[1]} = ")
            user_answer = int(problem)
            if user_answer != sum(difficulty):
                print("EEE")
            else:
                print("Correct")
                score += 1
                for _ in range(2):
                    problem = input(f"{difficulty[0]} + {difficulty[1]} = ")
                    user_answer = int(problem)
                    if user_answer != sum(difficulty):
                        print("EEE")
                    else:
                        print("Correct")
                        score += 1
                        break
                else:
                    print(f"The correct answer is: {sum(difficulty)}")
            
        except ValueError:
            print("Please enter a valid number.")
    print(f"You answered {score} questions right.")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Please enter 1, 2 or 3.")
        
        except ValueError:
            pass

def generate_integer(level):
    x = 0
    y = 0
    if level == 1:
        x = random.randint(1, 10)
        y = random.randint(1, 10)
    elif level == 2:
        x = random.randint(1, 100)
        y = random.randint(1, 100) 
    elif level == 3:
        x = random.randint(1, 1000)
        y = random.randint(1, 1000)
    else:
        raise ValueError("Input 1, 2 or 3")
    
    return x, y
    

if __name__ == "__main__":
    main()