F_age, F_gender = input().split()
F_age = int(F_age)
S_age, S_gender = input().split()
S_age = int(S_age)

if (F_age >= 19 and F_gender == "M" ) or (S_age >= 19 and S_gender == "M") :
    print("1")