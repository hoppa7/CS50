import validators

if validators.email(input()):
    print("Valid")
else:
    print("Invalid")