class kem:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat


n = int(input())
person = []


for _ in range(n):
    name, kor, eng, mat = input().split()
    person.append(kem(name, int(kor), int(eng), int(mat)))
    


person.sort(key=lambda x: (-x.kor, -x.eng, -x.mat))

for i in person:
    print(i.name, i.kor, i.eng, i.mat)
# Please write your code here.