# 이진 검색 (Binary Search)

## 1. 기본 개념

- **정의**
    - 정렬된 자료에서 **중간 지점**(mid)을 기준으로 탐색 범위를 **반씩 줄여가며** 찾는 검색 알고리즘
- **특징**
    - 시간 복잡도:`$O(log⁡n)$`(순차 검색의`$O(n)$`보다 훨씬 빠름)
    - 자료가 **정렬**되어 있어야 적용 가능
    - 삽입/삭제가 잦을 경우, 정렬 상태를 유지하는 비용이 추가로 듦

### 1.1 이진검색 과정

1. 자료의 중앙에 있는 원소를 고른다.
2. 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
3. 목표 값이 중앙 원소의 값보다 
작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 
크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
4. 찾고자 하는 값을 찾을 때까지 ①~③의 과정을 반복한다.

---

## 2. 코드 설명

### 2.1 반복문 방식

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # 검색 성공 시 인덱스 반환
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1  # 검색 실패 시 -1 반환

# 예시
numbers = [2, 4, 7, 9, 11, 19, 23]
print(binary_search(numbers, 11))  # 4 (인덱스 4)
print(binary_search(numbers, 10))  # -1 (없음)
```

**주요 로직**

1. `left`, `right`로 검색 범위를 관리
2. `mid = (left + right) // 2`
    - 현재 검색 범위의 중간 인덱스
3. 비교 후 범위 축소
    - `arr[mid] > target` → `right`를 `mid - 1`로 조정
    - `arr[mid] < target` → `left`를 `mid + 1`로 조정
4. 검색 종료 조건
    - `left > right`가 되면 검색 범위가 없으므로 실패

### 2.2 재귀 방식

```python
def binary_search_recursive(arr, left, right, target):
    '''
    재귀 함수를 이용한 이진 검색 (Binary Search)

    - arr  : 정렬된 리스트 (오름차순)
    - left : 현재 검색 범위의 시작 인덱스
    - right: 현재 검색 범위의 끝 인덱스
    - target: 찾고자 하는 값

    반환값:
    - target이 arr 안에 존재하면 해당 인덱스
    - 존재하지 않으면 -1
    '''
    # 1. 검색 범위가 유효한지 확인
    if left > right:
        return -1  # 검색 실패

    # 2. 중앙(mid) 인덱스 계산
    mid = (left + right) // 2

    # 3. 중앙 값과 target 비교
    if arr[mid] == target:
        return mid  # 검색 성공
    elif arr[mid] > target:
        # 4. target이 더 작으면 왼쪽 영역을 재귀 탐색
        return binary_search_recursive(arr, left, mid - 1, target)
    else:
        # 5. target이 더 크면 오른쪽 영역을 재귀 탐색
        return binary_search_recursive(arr, mid + 1, right, target)

# 예시
nums = [2, 4, 7, 9, 11, 19, 23]
# 배열의 전체 범위를 첫 호출 시 지정
idx_found = binary_search_recursive(nums, 0, len(nums) - 1, 4)
print("결과 인덱스:", idx_found)  # 예: 결과인덱스 1

```

**주요 로직**

```python
if arr[mid] == target:
    return mid
elif arr[mid] > target:
    return binary_search_recursive(arr, left, mid - 1, target)
else:
    return binary_search_recursive(arr, mid + 1, right, target)
```

- 같은 경우: **인덱스 mid** 반환
- 더 큰 경우: **왼쪽 구간** `[left, mid - 1]`를 재귀 탐색
- 더 작은 경우: **오른쪽 구간** `[mid + 1, right]`를 재귀 탐색

→ 학습 시, 각 단계( left, right, mid )가 어떻게 변하는지 추적해보면, 이진 검색의 작동 원리를 더 쉽게 이해할 수 있음

---

## 3. 추가 정리

- 이진 검색은 **정렬**을 필요로 한다는 점이 가장 큰 특징
    - 자료가 삽입/삭제 등으로 변경될 때마다 정렬을 다시 해야 할 수 있음
- 실제 **코딩 테스트**나 **실무**에서는
    - 한 번 정렬만 해두면 검색을 매우 빠르게 여러 번 할 수 있는 장점
    - (참고) 파이썬의 `bisect` 모듈을 사용하면 이진 검색과 비슷한 기능(인덱스 반환 등)을 간편하게 쓸 수 있음