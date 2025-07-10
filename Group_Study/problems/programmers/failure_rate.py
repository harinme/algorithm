'''
from collections import Counter
Counter() 배열 속 각 요소 별 빈도수 를 반환
{'1': 3, '2' : 2, '3': 0 ,,,}

get(특정 요소, 0)
=>
get(특정 요소의 키가 없다면 0으로 대체한다)
'''
from collections import Counter

def solution(N, stages):
    # 1) 각 스테이지에 머물러 있는 플레이어 수 집계
    stage_counts = Counter(stages)
    
    # 2) 남은 플레이어 수(처음엔 전체)로 초기화
    total_players = len(stages)
    
    failure_rates = []
    for stage in range(1, N+1):
        # 해당 스테이지에 도달한 플레이어 수 = total_players
        reached = total_players
        
        # 실패(도전 중) 플레이어 수
        failed = stage_counts.get(stage, 0)
        
        # 실패율 계산 (분모가 0이면 0으로 처리)
        if reached == 0:
            fail_rate = 0.0
        else:
            fail_rate = failed / reached
        
        failure_rates.append((stage, fail_rate))
        
        # 다음 스테이지로 넘어간 플레이어 수 계산
        total_players -= failed

    # 3) 실패율 내림차순, 스테이지 오름차순 정렬 후 스테이지 번호만 추출
    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    answer = [stage for stage, _ in failure_rates]
    return answer