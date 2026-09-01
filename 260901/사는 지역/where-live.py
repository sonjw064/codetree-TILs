class value:
    def __init__(self, name_value, address_value, region_value):
        self.name_value = name_value
        self.address_value = address_value
        self.region_value = region_value

n = int(input())
people = []

for _ in range(n):
    name_value, address_value, region_value = input().split()
    people.append(value(name_value, address_value, region_value))

target = people[0]
for i in people:
    if i.name_value > target.name_value:
        target = i

print(f"name {target.name_value}")
print(f"addr {target.address_value}")
print(f"city {target.region_value}")


# Please write your code here.
