

class User:
    def __init__(self, user2_id, user2_level):
        User.user2_id = user2_id
        User.user2_level = user2_level

a_user = User("codetree", 10)
print(f"user {a_user.user2_id} lv {a_user.user2_level}")

user2_id, user2_level = input().split()
user2_level = int(user2_level)
b_user = User(user2_id, user2_level)


print(f"user {b_user.user2_id} lv {b_user.user2_level}")
