from tabulate import tabulate

data = [
    ["Alice", 24, "Engineer"],
    ["Bob", 30, "Data Scientist"],
    ["Charlie", 28, "Teacher"]
]

print (tabulate(data, 
               headers=["Name", "Age", "profession"], 
               tablefmt="grid"
               ))
