#check password strength using python


def check_password():
    password=input("Enter your password: ")

    upper= any(char.isupper() for char in password)
    digit= any(char.isdigit() for char in password)

    if upper and digit and len(password)>=8:
        return "Strong"
    else:
        return "Weak"

print(check_password())
