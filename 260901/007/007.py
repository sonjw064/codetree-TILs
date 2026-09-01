secret_code, meeting_point, time = input().split()
time = int(time)

class mission:
    def __init__(self, secret_code,meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time
    
m = mission(secret_code,meeting_point, time)

print(f"secret code : {m.secret_code}")
print(f"meeting point : {m.meeting_point}")
print(f"time : {m.time}")

# Please write your code here.