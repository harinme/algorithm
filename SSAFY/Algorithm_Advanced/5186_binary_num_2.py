import sys
sys.stdin = open('5186_input.txt')

t = int(input())
for tc in range(1, t+1):
    target_decimal_str = input().strip()
    target_len = len(target_decimal_str)
    target_decimal = int(target_decimal_str[2:]) / (10 ** (target_len-2))
    bin_str = ''
    
    count = 0  # 이진수 자리수를 셀 변수 (최대 12자리 제한)
    

    # 종료 조건과 counting을 해주지 않아서 제대로 나오지 않았음
    # 소수 부분이 0이 될 때까지, 그리고 12자리 미만일 때까지 반복
    while target_decimal != 0 and count < 12:
        target_decimal *= 2               # 소수 부분에 2를 곱함
        bit = int(target_decimal)         # 정수 부분 추출 (0 또는 1)
        bin_str += str(bit)               # 결과 문자열에 추가
        target_decimal -= bit             # 정수 부분 제거하여 남은 소수 부분 계산
        count += 1                        # 자리수 카운트 증가
    
    # 12자리 제한을 넘어서 소수 부분이 남았다면, overflow 처리
    if target_decimal != 0:
        result = "overflow"
    else:
        result = bin_str
    
    print(f'#{tc} {result}')
