text = input()
pattern = input()

def check():
    n = len(text)
    m = len(pattern)

    if m > n :
        return -1
    
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            return i
    return -1
        

        
print(check())