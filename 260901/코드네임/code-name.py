class mans:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

MAX_N = 5

users = []
for _ in range(MAX_N):
    codename, score = input().split()
    users.append(mans(codename, int(score)))

user1 = users[0]

for user in users:
    if user.score < user1.score:
        user1 = user

print(user1.codename, user1.score)
# Please write your code here.
