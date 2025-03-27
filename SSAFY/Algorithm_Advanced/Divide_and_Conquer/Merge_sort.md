## **병합 정렬 (Merge Sort)**

배열(또는 리스트)을 반으로 나누고(divide), 각각 정렬된 결과를 다시 하나로 합치는(merge) 방식을 사용하는 **분할 정복(Divide and Conquer)** 기반 정렬 알고리즘이다. 

---

## **1. 핵심 개념**

1. **분할(Divide)**
    - 주어진 배열을 **절반**으로 나눈다.
    - 나눈 뒤 각각 다시 재귀적으로 **반으로 나누는** 과정을 반복하여, **원소가 하나**가 될 때까지 진행
2. **정복(Conquer) & 병합(Merge)**
    - 더 이상 나눌 수 없는(크기 1) 배열 두 개를 **정렬된 상태**로 합친다.
    - 작은 배열들이 정렬된 상태로 합쳐짐을 재귀적으로 반복 → **전체 배열이 정렬**됨
3. **시간 복잡도**
    - `$O(NlogN)$`
    - 배열 크기가 8이라면, 분할 과정은 `$log₂8=3$`단계, 각 단계에서 병합하는 데 `$O(N)$`
4. **장점**
    - **안정적**(stable) 정렬, **큰 데이터**에 대해 균일한 `$O(NlogN)$` 보장
5. **단점**
    - 추가 메모리 공간이 필요(병합 과정에서 임시 배열 사용)

---

## **2. 정렬 과정 예시**

[Merge Sort Algorithm](https://www.youtube.com/watch?v=5Z9dn2WTg9o)

정렬 대상 배열: `[69, 10, 30, 2, 16, 8, 31, 22]`

1. **분할**
    - 전체를 2개로 나눈다: `[69, 10, 30, 2]` / `[16, 8, 31, 22]`
    - 각 부분 배열도 똑같이 분할 → 최종적으로 길이 1짜리 배열이 될 때까지
2. **병합**
    - 더 이상 나눌 수 없는 (길이1) 배열 두 개를 정렬된 상태로 합친다. 
    (이미 길이1이면 자체가 정렬된 상태)
    - 예: `[69]`와 `[10]` 병합 → `[10, 69]`
    - 이런 식으로 재귀가 끝나면서 다시 올라오면, 부분 배열들이 정렬된 상태로 계속 합쳐짐 
    → 최종적으로 전체 정렬된 배열 생성

---

## **3. 병합 정렬 구현**

아래 코드는 
병합 정렬을 진행하는(분할&병합) `merge_sort()`와, 
두 정렬된 배열을 하나로 **병합**하는 `merge()` 예시다.

추가로, 특정 로직(answer와 median 계산)을 담아서 출력하는 형태를 보여준다.

```python
def merge(left_arr, right_arr):
    """
    두 개의 정렬된 배열(left_arr, right_arr)을 병합하여
    하나의 정렬된 배열로 반환.

    * left_arr, right_arr: 이미 정렬된 상태
    * return: 병합된 새로운 배열 (오름차순 정렬)
    """
    global comparison_count  # 예: 왼쪽 배열 맨 끝 원소 vs 오른쪽 맨 끝 원소 비교 등

    # 이 로직은 기존 예시에서 사용된 "if left_arr[-1] > right_arr[-1]"를 체크하는 부분
    # 여기서는 왼쪽배열 맨 끝이 오른쪽보다 크면 comparison_count += 1
    if left_arr and right_arr:
        if left_arr[-1] > right_arr[-1]:
            comparison_count += 1

    merged_arr = []
    left_idx, right_idx = 0, 0
    left_size, right_size = len(left_arr), len(right_arr)

    # 두 배열의 원소를 비교하면서 하나씩 결과에 담는다
    while left_idx < left_size and right_idx < right_size:
        if left_arr[left_idx] <= right_arr[right_idx]:
            merged_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            merged_arr.append(right_arr[right_idx])
            right_idx += 1

    # 아직 남은 원소(둘 중 하나는 비었을 것)들을 뒤에 추가
    # left_idx가 남았으면 남은 부분, right_idx가 남았으면 그 부분
    merged_arr.extend(left_arr[left_idx:])
    merged_arr.extend(right_arr[right_idx:])

    return merged_arr

def merge_sort(arr):
    """
    병합 정렬을 재귀적으로 구현.
    1) 배열의 길이가 1 이하이면 이미 정렬된 상태
    2) 길이가 2 이상이면, 절반으로 나눈 뒤 각각을 merge_sort() 재귀
    3) 두 정렬된 부분 배열을 merge() 함수로 병합
    """
    length = len(arr)
    # 길이 1 이하 -> 이미 정렬된 상태
    if length <= 1:
        return arr 

    # 1) 분할(Divide)
    mid = length // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 왼쪽, 오른쪽을 각각 merge_sort로 정렬
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # 2) 병합(Merge)
    return merge(left_half, right_half)

# ---- 실행 예시 ----

# 전역변수: answer, comparison_count
comparison_count = 0

# 정렬할 배열
data_array = [69, 10, 30, 2, 16, 8, 31, 22]

sorted_array = merge_sort(data_array)
print("정렬 결과:", sorted_array)
# 예: [2, 8, 10, 16, 22, 30, 31, 69]

# 중앙값
n = len(sorted_array)
median_value = sorted_array[n // 2]
print("중앙값:", median_value)

print("comparison_count:", comparison_count)

```

### **3.1 코드 해설**

1. **`merge_sort(arr)`**
    - 기저 사례: 배열 길이가 1 이하이면 그대로 반환(이미 정렬)
    - 아니면 **두 부분으로 분할** → 각각 재귀적으로 정렬 → `merge()`를 통해 합침
2. **`merge(left_arr, right_arr)`**
    - 이미 정렬된 왼쪽, 오른쪽 배열을 **오름차순**으로 하나로 병합
    - 전역 변수 `comparison_count`를 증가시키는 부분이 포함(이는 문제에서 특별한 조건을 세어보고자 할 때)
    - 실제 병합(while문)은 **양쪽 배열**의 원소를 하나씩 비교하며 더 작은 쪽을 결과에 넣는다
3. **정렬 후**: `sorted_array`가 최종 결과.
    - 중앙값(median)은 길이 n인 배열에서 `n//2`번 인덱스 원소(0-based)

---

## **4. 병합 정렬 과정 (단계별)**

예) `[69, 10, 30, 2, 16, 8, 31, 22]` (길이 8)

1. **분할**
    
    ![Screenshot 2025-03-17 at 3.18.41 PM.png](attachment:fc179e88-19f3-494d-93ab-0c6841ea9e4b:Screenshot_2025-03-17_at_3.18.41_PM.png)
    
    - 8개 → 4/4로 나눔
    - 4개 → 2/2로 나눔
    - 2개 → 1/1로 나눔
2. **정렬된 1개 배열 + 정렬된 1개 배열** → 병합 → 길이2 정렬 배열
    
    ![Screenshot 2025-03-17 at 3.18.46 PM.png](attachment:d4eb8924-11a0-450d-b46b-e321eba08fe0:Screenshot_2025-03-17_at_3.18.46_PM.png)
    
3. 재귀 함수는 계속 복귀하며, 각각 병합된 길이2 → 길이4로, 마지막에 길이8 전체 병합
4. 최종 정렬 완료

---

## **5. 시간 복잡도**

- **분할**: 배열 길이가 N이면, 한 번 분할 시 2개의 배열로 쪼개진다 → `$log₂N$` 단계 분할
- **병합**: 각 단계에서 분할된 배열을 다시 합치며, 각 단계별 원소 합은 `N`
- 전체 연산량은 약 **`$O(N log N)$`**

---

## **6. 정리**

- **병합 정렬**은 분할 정복 알고리즘 중 하나로, **오름차순** 또는 **내림차순** 등 원하는 순서로 배열을 정렬할 수 있음.
- 평균, 최악 모두 **`$O(N log N)$`** 시간에 동작
- **추가 메모리**가 필요하다는 단점이 있지만, **큰 데이터**나 **안정 정렬**이 중요한 상황에서 널리 사용
- 실제 파이썬 `sorted()`나 일부 라이브러리는 비슷한 원리(Timsort 등)로 구현 
→ 분할 정복, 삽입 정렬 등을 혼합
- “재귀로 배열을 둘로 나눈 뒤, 합칠 때 정렬 상태를 유지한다”

---

## 7. [참고] 반복문 병합 정렬

<aside>
💡

**병합 정렬을 반복문(비재귀)으로 구현할 수 있나요?**

</aside>

병합 정렬은 일반적으로 **재귀**(divide → merge)로 많이 알려져 있으나, **반복문**만으로도 구현 가능하다. 

이를 흔히 **Bottom-Up Merge Sort**라고 부르며, 원리를 간단히 요약하면 다음과 같다.

1. 처음에는 배열을 길이 1짜리 구간(이미 정렬된 상태)으로 간주한다.
2. 길이 1짜리 구간들을 **2개씩 병합**해 길이 2짜리 구간을 정렬 상태로 만든다.
3. 다시 길이 2짜리 구간들을 2개씩 병합해 길이 4짜리 구간을 만든다.
4. 이런 식으로 subarray(부분 구간) 크기가 1, 2, 4, 8, ... 로 **2배씩 증가**하며 전체 배열을 정렬해나간다.

이 과정을 모두 **반복문**을 통해 구현하면, **재귀 호출 없이**도 병합 정렬의 원리와 동일한 **`$O(N log N)$`** 정렬이 가능하다.

### **7.1 반복문 기반 병합 정렬 템플릿 코드**

아래 코드는 **“반복적 병합 정렬(Iterative Merge Sort)”** 예시이다.

```python
def merge_two_subarrays(arr, start, mid, end):
    """
    arr[start..mid]와 arr[mid+1..end]라는 두 정렬된 부분 배열을
    하나로 정렬해 병합하는 함수.
    """
    merged = []
    left_idx = start
    right_idx = mid + 1

    while left_idx <= mid and right_idx <= end:
        if arr[left_idx] <= arr[right_idx]:
            merged.append(arr[left_idx])
            left_idx += 1
        else:
            merged.append(arr[right_idx])
            right_idx += 1

    # 남은 요소 붙이기
    while left_idx <= mid:
        merged.append(arr[left_idx])
        left_idx += 1

    while right_idx <= end:
        merged.append(arr[right_idx])
        right_idx += 1

    # 실제 arr에 병합 결과 반영
    for i, val in enumerate(merged):
        arr[start + i] = val

def iterative_merge_sort(arr):
    """
    반복문(비재귀)으로 병합 정렬을 구현한 함수.
    Bottom-Up 방식:
    1) 길이 1씩 구간을 2개씩 합쳐 길이2 정렬
    2) 길이2씩 구간을 2개씩 합쳐 길이4 정렬
    3) ...
    """
    n = len(arr)
    size = 1  # 부분 배열의 크기(1,2,4,8,..)

    while size < n:
        # step 단위로 subarray를 병합
        for start in range(0, n, 2 * size):
            mid = start + size - 1
            end = min(start + 2 * size - 1, n - 1)

            # 만약 mid(왼쪽 구간 끝)가 배열 범위 내라면 병합 수행
            if mid < end < n:
                merge_two_subarrays(arr, start, mid, end)

        size *= 2

# ---- 실행 예시 ----
data_array = [69, 10, 30, 2, 16, 8, 31, 22]
print("정렬 전:", data_array)
iterative_merge_sort(data_array)
print("정렬 후:", data_array)

"""
정렬 전: [69, 10, 30, 2, 16, 8, 31, 22]
정렬 후: [2, 8, 10, 16, 22, 30, 31, 69]
"""

```

**코드 해설**

1. **`merge_two_subarrays(arr, start, mid, end)`**
    - `arr[start..mid]`와 `arr[mid+1..end]`는 이미 정렬되어 있다고 가정
    - 두 부분 배열을 **오름차순**으로 병합해, `arr[start..end]` 구간을 정렬 상태로 만듦
2. **`iterative_merge_sort(arr)`**
    - `size`는 병합할 부분 구간의 길이. 처음엔 1로 시작(길이1 배열은 이미 정렬)
    - `size`가 1→2→4→8... 이렇게 2배씩 증가하며, 구간들을 **병합**
    - `range(0, n, 2*size)`로 `start`를 잡고, `mid = start+size-1`, `end = start+2*size-1`로 나눈 뒤 `merge_two_subarrays` 실행
    - `end`가 배열 끝을 넘지 않도록 `min(...)` 처리
    - `size`가 배열 길이를 넘으면(또는 같으면) 모든 병합 완료

**정리**

- **병합 정렬**은 보통 **재귀 방식**(Divide and Conquer)으로 많이 구현되지만,
- **반복문**(Bottom-Up)으로도 **동일한 로직**을 구현 가능 → **Iterative Merge Sort**
- 두 구현 모두 **시간 복잡도는 `$O(N log N)$`**, 안정 정렬이며, 추가 메모리가 필요하다는 점도 동일
- 상황과 취향에 따라 **재귀**(더 직관적) 또는 **반복**(스택 없이도 구현 가능)으로 선택해 사용하면 된다.