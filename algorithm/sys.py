import sys

#문자열 입력 받기
data = sys.stdin.readline().rstrip() #rstrip(): 엔터가 줄 바꿈 기호로 입력되는 것을 막기 위해
#print(data)

print(f"정답은 {data}입니다.") #f-string을 통해 간단히 문자열과 정수를 함께 넣을 수 있다.
