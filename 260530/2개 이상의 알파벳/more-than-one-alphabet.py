def check(text):
    first_text = text[0]
    for char in text:
        if char != first_text :
            return True
    return False

A = input()

if check(A):
    print("Yes")
else:
    print("No")
