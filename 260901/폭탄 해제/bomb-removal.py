class boom:
    def __init__(self, unlock_code, wire_color, seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds


unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

b = boom(unlock_code, wire_color, seconds)

print(f"code : {b.unlock_code}")
print(f"color : {b.wire_color}")
print(f"second : {b.seconds}")

# Please write your code here.