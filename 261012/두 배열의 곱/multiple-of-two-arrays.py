arr1 = [list(map(int, input().split())) for _ in range(3)]
a = input()  # 만약 연산 기호나 다른 입력을 받는 용도라면 유지
arr2 = [list(map(int, input().split())) for _ in range(3)]

sumss = []  # 결과를 담을 2차원 리스트

for i in range(3):
  row = []  # 한 행씩 계산하기 위한 임시 리스트
  for j in range(3):
    sums = arr1[i][j] * arr2[i][j]  # 두 수의 곱 (정수)
    row.append(sums)  # 임시 행에 추가
  sumss.append(row)  # 완성된 행을 최종 결과에 추가

for i in range(3):
    for j in range(3):
        print(sumss[i][j],end=" ")
    print()