## **퀵 정렬 (Quick Sort)**

퀵 정렬은 **분할 정복(Divide and Conquer)** 기법을 사용하여, 
**피벗(Pivot)을 기준**으로 원소들을 왼쪽(작은 값 그룹)과 오른쪽(큰 값 그룹)으로 분할하고, 
각각을 재귀적으로 정렬하면서 전체 배열을 정렬해 나가는 알고리즘이다.

---

## **1. 핵심 아이디어**

1. **피벗(Pivot) 선택**
    - 배열에서 임의의 원소 하나를 **피벗**으로 지정
        - 예) 가장 오른쪽 / 가장 왼쪽 / 중간 / 무작위 원소 등
    - 호어 파티션에서, 일반적으로 **배열의 첫 번째 원소**(`array[start]`)를 **피벗**으로 선정
    - 이후, 양끝에서 인덱스를 움직이며 **분할**(Partition) 진행
2. **분할(Partition)**
    - 왼쪽 인덱스(`left`)는 **피벗보다 큰** 값을 찾을 때까지 오른쪽으로 이동
    - 오른쪽 인덱스(`right`)는 **피벗보다 작은** 값을 찾을 때까지 왼쪽으로 이동
    - 만약 `left < right`라면 두 원소를 교환 후 계속 진행
    - `left >= right`가 되면 멈춤, 마지막에 **피벗**(start 위치)과 `array[right]`를 교환
    - 결과적으로 **피벗**은 정렬 시 **최종 위치**에 놓임
3. **재귀**
    - 피벗을 기준으로 왼쪽 부분 배열, 오른쪽 부분 배열 각각에 대해 **퀵 정렬**을 재귀적으로 수행
    - 부분 배열의 크기가 1 이하가 될 때까지 반복
4. **시간 복잡도**
    - 평균적으로 **`$O(N log N)$`**
    - 최악(이미 정렬된 상태에 따라) 시 **`$O(N^2)$`** 가능

---

## **2. 정렬 예시**

[Quick Sort Algorithm](https://www.youtube.com/watch?v=WprjBK0p6rw)

---

## **3. 예시 코드 (Hoare 파티션 방식)**

- 과정 이미지
    
    ![Screenshot 2025-03-17 at 3.38.55 PM.png](attachment:f714660a-761e-41b2-abfb-b41eab256f66:Screenshot_2025-03-17_at_3.38.55_PM.png)
    
    ![Screenshot 2025-03-17 at 3.38.59 PM.png](attachment:5746dc58-ae90-4bc6-bd58-46a3fd2c5b23:Screenshot_2025-03-17_at_3.38.59_PM.png)
    
    ![Screenshot 2025-03-17 at 3.39.05 PM.png](attachment:2d9e90bb-480a-498f-8a7f-aaf282f5dca3:Screenshot_2025-03-17_at_3.39.05_PM.png)
    
    ![Screenshot 2025-03-17 at 3.39.09 PM.png](attachment:16ab918c-f721-4e31-87b6-cf2fdd970b7e:Screenshot_2025-03-17_at_3.39.09_PM.png)
    
    ![Screenshot 2025-03-17 at 3.39.13 PM.png](attachment:fb83935a-0f10-427c-9d84-f87b95777856:Screenshot_2025-03-17_at_3.39.13_PM.png)
    
    ![Screenshot 2025-03-17 at 3.39.18 PM.png](attachment:c71e59dc-902c-415a-9170-1e272332f37b:Screenshot_2025-03-17_at_3.39.18_PM.png)
    
    ![Screenshot 2025-03-17 at 3.39.23 PM.png](attachment:a227d788-f42d-41d4-9ae1-1414d275af8a:Screenshot_2025-03-17_at_3.39.23_PM.png)
    
- **피벗**은 `array[start]`
- `left = start+1`, `right = end`에서 시작
- 교차 전까지 검사하다가, 교차하면 피벗과 `array[right]` 교환
    
    ```python
    def quick_sort(array, start, end):
        """
        퀵 정렬(Quick Sort)을 호어(Hoare) 파티션 방식으로 재귀적으로 구현.
        1) partition 함수를 통해 피벗의 최종 위치를 구하고
        2) 그 왼쪽, 오른쪽 부분 배열을 각각 재귀로 정렬
        """
        if start < end:
            pivot_idx = partition(array, start, end)
            # 왼쪽 부분 정렬
            quick_sort(array, start, pivot_idx - 1)
            # 오른쪽 부분 정렬
            quick_sort(array, pivot_idx + 1, end)
    
    def partition(array, start, end):
        """
        호어(Hoare) 파티션:
        - array[start]를 피벗으로 삼고,
        - left = start + 1, right = end 에서 시작
        - left는 피벗 이상을 만날 때까지 전진
        - right는 피벗 이하를 만날 때까지 후퇴
        - left < right이면 swap 후 계속
        - left >= right이면 loop 종료, 피벗과 array[right] 교환
        - 반환값: right (피벗의 최종 위치)
        """
        pivot = array[start]
        left = start + 1
        right = end
    
        while True:
            # left가 범위 내 & pivot보다 큰 값을 찾을 때까지 증가
            # (작은 값인 경우에 계속 진행)
            while left <= right and array[left] < pivot:
                left += 1
    
            # right가 범위 내 & pivot보다 작은 값을 찾을 때까지 감소
            # (큰 값인 경우에 계속 진행)
            while right >= left and array[right] > pivot:
                right -= 1
    
            # 교차가 일어나면 반복 종료
            if left > right:
                break
            else:
                # left, right 교차 전이면 swap
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
    
        # 마지막으로 피벗을 array[right] 위치와 교환
        array[start], array[right] = array[right], array[start]
        return right
    
    data_list = [3, 2, 4, 6, 9, 1, 8, 7, 5]
    print("정렬 전:", data_list)
    
    quick_sort(data_list, 0, len(data_list) - 1)
    print("정렬 후:", data_list)
    
    """
    정렬 전: [3, 2, 4, 6, 9, 1, 8, 7, 5]
    정렬 후: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    
    ```
    
    **코드 해설**
    
    1. **피벗**: `array[start]` (가장 왼쪽 원소)
    2. **left**, **right** 인덱스 지정:
        - `left = start+1`, `right = end`
    3. **반복**
        - `left`를 오른쪽으로 이동 → **피벗보다 큰 값**(또는 같거나 큰) 만날 때 정지
        - `right`를 왼쪽으로 이동 → **피벗보다 작은 값**(또는 같거나 작은) 만날 때 정지
        - 만약 left < right이면 두 원소를 교환 후 다시 진행
        - left >= right이면 중단
    4. **피벗과 `array[right]` 교환** → `right`가 **피벗의 최종 위치**
    5. **반환**: `right`
    6. `quick_sort()`는 `start < end`이면 파티션 후 왼쪽/오른쪽 재귀

- 로무토 방식 코드
    
    아래 코드는 **가장 오른쪽** 원소를 피벗으로 선택하는 전형적인 로무토 **방식**
    
    ```python
    def quick_sort(array, start, end):
        """
        퀵 정렬(Quick Sort)을 재귀적으로 구현한 함수.
        1) partition을 통해 피벗의 올바른 위치를 찾고
        2) 해당 피벗을 기준으로 왼쪽, 오른쪽 부분 배열 각각 재귀적으로 정렬
        """
        if start < end:
            pivot_idx = partition(array, start, end)
            # 왼쪽 부분 정렬
            quick_sort(array, start, pivot_idx - 1)
            # 오른쪽 부분 정렬
            quick_sort(array, pivot_idx + 1, end)
    
    def partition(array, start, end):
        """
        partition 함수:
        - array[end]를 피벗으로 잡고
        - 피벗보다 작은 값들은 왼쪽으로, 큰 값들은 오른쪽으로 재배치
        - 최종적으로 피벗이 있을 위치를 반환
        """
        pivot = array[end]  # 마지막 원소를 피벗
        i = start - 1  # i는 피벗보다 작은 값들의 마지막 인덱스
    
        # start부터 end-1까지 순회하며, 피벗보다 작은 원소를 발견하면
        # i를 하나 증가시키고 교환(swap)함
        for j in range(start, end):
            if array[j] < pivot:
                i += 1
                # i와 j가 다를 때에만 교환
                if i != j:
                    array[i], array[j] = array[j], array[i]
    
        # 이제 i+1 위치가 피벗이 들어갈 자리
        # 피벗(end 위치)과 i+1 위치를 교환
        if (i + 1) != end:
            array[i + 1], array[end] = array[end], array[i + 1]
    
        return i + 1  # 피벗 위치 인덱스 반환
    
    data_list = [3, 2, 4, 6, 9, 1, 8, 7, 5]
    print("정렬 전:", data_list)
    
    quick_sort(data_list, 0, len(data_list) - 1)
    print("정렬 후:", data_list)
    
    """
    정렬 전: [3, 2, 4, 6, 9, 1, 8, 7, 5]
    정렬 후: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    
    ```
    
    **코드 해설**
    
    1. **`partition(array, start, end)`**
        - **피벗**: `array[end]` (가장 오른쪽 원소)
        - `i`를 `start-1`로 두고, `j`가 `start`부터 `end-1`까지 순회
        - 만약 `array[j] < pivot`, 즉 피벗보다 작으면, i를 1 증가시키고 `array[i]` ↔ `array[j]` 교환
        - 마지막에 **피벗**과 `array[i+1]`을 교환 → 피벗의 최종 위치 = `i+1`
        - 반환값: 피벗이 최종적으로 위치한 인덱스
    2. **`quick_sort(array, start, end)`**
        - 기저 조건: `start < end`일 때만 정렬 필요
        - `partition`을 통해 피벗 위치를 구하고, 그 왼쪽, 오른쪽을 재귀적 정렬
        - 병합 정렬과 달리, **병합 과정** 없이 파티션만으로 배열이 부분적으로 정렬되어 간다

---

## **4. 시간 복잡도**

- **평균**: `$O(N log N)$`
- **최악**: `$O(N^2)$` (이미 정렬된 상태에서 계속 최악의 파티션이 일어나는 경우 등)
- **장점**
    - 병합 정렬과 달리, **추가 메모리** 없이 **제자리(in-place)**로 정렬 가능
    - 평균 성능이 매우 우수
- **단점**
    - 최악의 경우 성능 저하 → 피벗 선택 기법으로 회피(무작위 피벗, 3중Median 등)

---

## **5. 정리**

1. **퀵 정렬(Quick Sort)**:
    - 분할 정복 기반, 피벗을 정해 **분할**, 부분 배열 재귀 정렬
    - 병합 과정 없이도 빠른 정렬 가능(평균 `$O(N log N)$`)
2. **코드 핵심**:
    - `partition()` 함수로 “피벗 기준 왼쪽(작은값), 오른쪽(큰값)” 분할
    - 재귀로 왼쪽/오른쪽 부분 정렬
3. **주의**: 최악 시 `$O(N^2)$` → 피벗 선택 개선, 무작위 피벗, median-of-three 등 방법 존재

퀵 정렬은 실무/실제 라이브러리에서 **널리 사용**되는 효율적 알고리즘이지만, **최악 상황** 방지를 위한 피벗 선택이 중요하다는 점을 기억하자.

---

## 6. [참고] **로무토(Lomuto) vs. 호어(Hoare)**

<aside>
💡

두 방식 모두 **퀵 정렬** 을 올바르게 구현할 수 있고,
단지 피벗 선택 및 인덱스 이동 전략이 다를 뿐이다.

효율성과 성능 측면에서 호어 방식이 로무토 방식보다 우수

</aside>

퀵 정렬에서 핵심은 **Partition(분할)** 과정으로, 피벗(Pivot)을 중심으로 배열을 나누는 로직이다. 

이 Partition 단계의 구현 방식에는 크게 **호어(Hoare) 파티션**과 **로무토(Lomuto) 파티션** 두 가지가 많이 알려져 있다.

### **6.1  로무토(Lomuto) 파티션 방식**

**특징**

- **피벗**을 보통 배열의 **마지막 원소**로 선택.
- **i** 인덱스를 `low-1`로 두고, `j`가 `low`부터 `high-1`까지 순회:
    1. 만약 `arr[j] < pivot`이면, i를 1 증가시키고 `arr[i]`↔`arr[j]`를 교환(swap).
    2. 반복이 끝나면 i+1 위치와 피벗(`arr[high]`)을 교환.
- 최종적으로 `i+1` 위치가 **피벗의 최종 위치**가 됨.

**장단점**

- **장점**
    - 구현이 **단순**하고 직관적
    - 코드가 짧고 이해하기 쉬움
- **단점**
    - 분할 과정에서 교환(swap)이 많이 발생 가능
    - 모든 원소와의 비교가 끝난 뒤, 피벗을 `i+1` 위치로 옮기기 때문에, 성능이 다소 영향을 받을 수도 있음

**간단 예시**

```python
def partition_lomuto(arr, low, high):
    pivot = arr[high]  # 마지막 원소
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # i+1에 피벗을 위치
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

```

### **6.2 호어(Hoare) 파티션 방식**

**특징**

- **피벗**을 배열의 **처음 혹은 임의 위치**(종종 첫 번째나 가운데, 무작위)로 선택.
- **left**는 `start+1`, **right**는 `end`에서 시작하여,
    1. left가 피벗보다 큰(or 같으면) 원소를 만날 때까지 이동
    2. right가 피벗보다 작은(or 같으면) 원소를 만날 때까지 이동
    3. `left < right`이면 두 원소를 교환
    4. `left >= right`이면 반복 중단, 피벗을 `right`와 교환 → 최종 피벗 위치가 `right`
- 분할 후 `right` 인덱스를 반환.

**장단점**

- **장점**
    - 평균적으로 적은 교환 횟수를 보일 수 있음(왼쪽·오른쪽에서 동시에 교환하므로)
    - 분할이 끝났을 때, 피벗이 **정확한 최종 위치**에 위치
- **단점**
    - 구현이 로무토 방식보다 약간 복잡 (left, right를 양끝에서 시작하여 교차 검사)

**간단 예시**

```python
def partition_hoare(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end

    while True:
        # left가 pivot보다 큰 원소 찾을 때까지
        while left <= end and arr[left] < pivot:
            left += 1
        # right가 pivot보다 작은 원소 찾을 때까지
        while right > start and arr[right] >= pivot:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break

    # 피벗과 arr[right] 교환
    arr[start], arr[right] = arr[right], arr[start]
    return right

```

### **6.3 비교 요약**

| 구분 | **로무토(Lomuto)** | **호어(Hoare)** |
| --- | --- | --- |
| **피벗 위치** | 배열의 **마지막 원소**(`arr[high]`) | 배열의 **첫 번째 원소**(`arr[low]`)  (또는 무작위) |
| **인덱스 이동** | `i = low-1`;  `j`가 `low→high-1` 순회 | `left = low+1`, `right = high`  양끝에서 중앙으로 |
| **파티션 방식** | `arr[j] < pivot` 이면, i↑ 후 swap i↔j | `arr[left] < pivot` → left++ / `arr[right] > pivot` → right--  교차 전이면 swap |
| **피벗 교환 시점** | 모든 j 순회 후, **피벗**과 `arr[i+1]` 교환 → i+1 | left ≥ right면 loop 종료 후, **피벗**(`arr[low]`)과 `arr[right]` 교환 → right |
| **특징** | 구현 코드가 **단순**, swap이 잦을 수 있음 | 교환 횟수 **적을** 수도, 구현이 조금 복잡 |
| **대표 의사코드** | **CLRS** 등에 흔히 소개 (pivot=arr[high]) | 퀵 정렬 고안자 Hoare가 초창기에 사용 (pivot=arr[low]) |

두 방식 모두 결과적으로 **퀵 정렬**을 구현한다.

- **로무토**
    - 비교적 **코드가 단순**해서 많이 소개됨(피벗=마지막).
- **호어**
    - 평균적으로 **swap이 적고** 효율적이라는 평가도 있으나, **인덱스 제어**가 조금 까다롭다.

**정리**

- **퀵 정렬**에서 핵심은 **피벗 선정**과 **파티션 구현**
- **로무토 방식**
    - 구현이 간단(코드 짧음), 피벗을 마지막으로 택해, `i` 인덱스 관리
- **호어 방식**
    - 양쪽에서 동시에 검사 후 교환, 교환 횟수가 적을 수 있으나 구현 복잡
    - 성능이 중요한 실제 애플리케이션에서는 호어 방식이 더 효율적이므로 권장
- 어떤 파티션 방식을 쓰든, **퀵 정렬**의 알고리즘 본질(분할 정복)은 동일하며, 최종 복잡도도 대체로 `$O(N log N$)` (최악 시 `$O(N^2)$`)이다.
- 둘 다 **올바른 퀵 정렬**을 구현할 수 있고, 실제 성능은 **입력 데이터**나 **피벗 선택** 방식에 따라 차이가 날 수 있음.

따라서 어떤 방식을 써도 퀵 정렬의 분할은 가능하지만, **코드 편의성**(로무토)과 **교환 효율**(호어) 등의 차이가 있다. 상황과 취향에 맞게 선택하여 사용하면 된다.