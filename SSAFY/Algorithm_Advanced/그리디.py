# 동전 문제
coin_list = [500, 100, 50, 10] # 큰 동전부터 앞으로 작성함.
target = 1730
cnt = 0

for coin in coin_list:
    possible_cnt = target //coin # 현재 동전으로 가능한 최대 수
    cnt += possible_cnt
    target -= coin * possible_cnt
print(cnt)


# 화장실 문제
# 기숙사에는 하나의 화장실만 존재한다.
'''
A ~ D 학생은 각자의 평균 화장실 사용 시간이 다음과 같다.
A: 15/ B: 30 / C: 50/ D: 10
어떤 기준으로 접근해야 대기시간의 누적합이 최소가 될지 고민해보고 직접 구현해보자.
'''

people = [15, 30, 50, 10]
n = len(people)

# 규칙. 최소 시간인 사람부터 화장실로 들어가자.
people.sort() # 오름차순

total_time = 0 # 전체 대기 시간
remain_people = n - 1
for turn in range(n):
    time = people[turn]
    total_time += time * remain_people
    remain_people -= 1
print(total_time)

#  도둑 Knapsack
n = 3
tartget = 30
things = [(5,50), (10, 60) (20, 140)] # kg, price

# kg 당 가격으로 어떻게 정렬?
# 정렬: price/kg
# lamba: 재사용하지 않는 함수
things.sort(key=lambda x: (x[1]/x[0]), reverse=True)
