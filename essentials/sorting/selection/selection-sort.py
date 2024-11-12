"""
Selection Sort
==================
Selection은 하나의 요소를 나머지 요소에 대해 모두 비교하며 조건이 맞을 때마다 자리를 교체한다.
"""

# def selection_sort1(arr):
#   n = len(arr)
#   for i in range(n):
#     _min = arr[i]
#     for j in range(n):
#       if arr[j] < _min:
#         _min = arr[j]
#         arr[i], arr[j] = arr[j], arr[i]

#   return arr
"""
=> 위 코드는 
"""


def selection_sort2(arr):
  n = len(arr)
  for i in range(n):
    min_index = i   # 현재 위치를 최소값 위치로 가정
    for j in range(i + 1, n):     # ?
      if arr[j] < arr[min_index]:
        min_index = j
      arr[i], arr[min_index] = arr[min_index], arr[i]  # 최소값을 현재 위치로 교환

  return arr


arr1 = [5, 3, 8 , 4, 2]
arr2 = [64, 34, 25, 12, 22, 11, 90]

print(selection_sort1(arr2))

"""
`for j in range(i + 1, n):`에서 `i + 1`로 설정한 이유는 **현재 인덱스 `i` 이후의 요소들만 탐색하여, 그 중에서 가장 작은 값을 찾기 위해서**입니다. 

Selection Sort는 **정렬되지 않은 부분에서 가장 작은 값을 찾아 현재 위치 `i`와 교환**하는 방식으로 동작합니다. 이를 위해 `i` 이후의 요소들만 비교해도 충분합니다.

### 구체적인 이유

1. **정렬된 부분을 제외하고 비교**:
   - `i` 이전까지는 이미 정렬이 완료된 상태입니다. 따라서 `i` 위치 이후부터만 탐색하면 됩니다.
   
2. **불필요한 비교 방지**:
   - `for j in range(i + 1, n):`로 설정하면, 현재 위치 `i`를 기준으로 나머지 요소들과만 비교하므로, 불필요한 비교를 줄일 수 있습니다.
   - 만약 `j`가 `i + 1`이 아닌 `i`부터 시작하면, `i`와 `i` 위치의 요소를 비교하는 불필요한 비교가 발생할 수 있습니다.

### Selection Sort의 동작 과정 예시

간단한 리스트 `[5, 3, 8, 4, 2]`로 이 반복 구조가 어떻게 작동하는지 설명하겠습니다.

1. 첫 번째 반복 (`i = 0`):
   - `i = 0`에서 `j`는 `1`부터 시작합니다.
   - `arr[0]` 이후의 요소 `[3, 8, 4, 2]` 중에서 최소값을 찾습니다.
   - 최소값은 `2`이므로, `arr[0]`과 교환하여 `[2, 3, 8, 4, 5]`로 만듭니다.

2. 두 번째 반복 (`i = 1`):
   - `i = 1`에서 `j`는 `2`부터 시작합니다.
   - `arr[1]` 이후의 요소 `[8, 4, 5]` 중에서 최소값 `3`을 확인합니다 (위치 변경 없음).

이런 식으로 `i` 이후의 요소들만 탐색하여 가장 작은 값을 `i` 위치에 교환하는 것이 Selection Sort의 기본 원리입니다.
"""
