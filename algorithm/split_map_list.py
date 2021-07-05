n = int(input())  #입력받은 문자열을 단순 정수int로 바꿈
#input(): 한 줄의 문자열을 입력 받음

data1 = input().split()  #split(): 공백 기준으로 문자열이 나누어짐

#map(): 리스트의 모든 원소에 각각 특정 함수를 적용할 때 사용
data2 = list(map(int, input().split()))  #list(): 그걸 다시 리스트로 만들어줌

a, b, c = map(int, input().split())
# 공백 기준으로 들어온 정수 데이터가 a, b, c에 담김
# 입력 데이터가 3개를 넘어가는 경우 패킹-언패킹 4개의 변수를 3개에 담는게 불가하므로 오류

print(n)
print(data1)
print(data2)
print(a, b, c)

"""
2
4 1 22 5
44 5 64
3 5 1

>>>

2
['4', '1', '22', '5']
[44, 5, 64]
3 5 1
"""