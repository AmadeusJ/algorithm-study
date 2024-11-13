"""
Insertion Sort
===================
=> 첫 요소는 정렬되어있다고 가정, 두번째부터 탐색하여 정렬수행
"""

# def insertion_sort1(arr):
#   n = len(arr)
#   for i in range(1, n):
#     for j in range(0, i):
#       if arr[i] > arr[j]:
#         arr[i], arr[j] = arr[j], arr[i]

#   return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # 정렬된 부분의 오른쪽 끝부터 key가 들어갈 위치를 찾음
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j] # key 가 들어갈 자리에 있는 녀석은 뒤로 민다.
            j -= 1
        arr[j + 1] = key  # 찾은 위치에 key를 삽입
    return arr


arr1 = [5, 3, 8 , 4, 2]
arr2 = [64, 34, 25, 12, 22, 11, 90]

print(insertion_sort1(arr2))

"""
삽입 정렬에서 `while`문을 사용하는 이유는 **현재 요소(`key`)가 들어갈 위치를 찾기 위해 정렬된 부분을 오른쪽 끝부터 차례로 비교하면서 이동**하기 위해서입니다. `while`문을 통해, `key`보다 큰 값들은 한 칸씩 오른쪽으로 이동하고, `key`가 들어갈 정확한 위치를 찾을 때까지 비교를 계속합니다.

### 삽입 정렬에서 `while`문이 필요한 이유

1. **적절한 삽입 위치를 찾기 위해**:
   - 삽입 정렬에서는 현재 요소를 정렬된 부분에 삽입할 때, **현재 요소(`key`)보다 큰 값들을 오른쪽으로 한 칸씩 이동**시키며 정확한 위치를 찾습니다.
   - `while`문을 사용하여, `key`가 들어갈 위치를 찾기 위해 정렬된 부분의 요소들과 반복적으로 비교할 수 있습니다.

2. **정렬된 부분에서 오른쪽으로 요소 이동**:
   - `key`가 들어갈 위치를 찾기 위해, 정렬된 부분의 끝에서부터 차례로 비교해가며 `key`보다 큰 요소들을 오른쪽으로 한 칸씩 이동시킵니다.
   - 이러한 요소 이동은 **반복적인 작업**이기 때문에 `while`문이 필요합니다.

3. **조건을 만족할 때까지 반복**:
   - `while`문에서는 `j >= 0`과 `arr[j] > key`라는 조건을 만족하는 동안 반복됩니다. 이는 `key`보다 큰 값이 계속해서 왼쪽에 있을 경우, **`key`보다 작은 값을 찾을 때까지 반복적으로 비교**하여 적절한 위치를 찾기 위해 사용됩니다.

### 예제 코드에서 `while`문의 역할

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # 정렬된 부분에서 key가 들어갈 위치를 찾음
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # 요소를 오른쪽으로 이동
            j -= 1
        arr[j + 1] = key  # 찾은 위치에 key를 삽입
    return arr
```

- **`while j >= 0 and arr[j] > key`**: `j`가 0 이상이고 `arr[j]`가 `key`보다 클 때까지 반복합니다. 즉, `key`보다 큰 값들을 오른쪽으로 이동시키면서 `key`가 들어갈 위치를 찾습니다.
- **`arr[j + 1] = arr[j]`**: 현재 `j` 위치의 값을 오른쪽으로 한 칸 이동하여 `key`가 들어갈 자리를 만듭니다.
- `j`가 `-1`이 되거나 `arr[j] <= key`가 되면 반복을 종료하고, `key`를 `arr[j + 1]`에 삽입합니다.

---

`while`문 덕분에 삽입 정렬은 각 요소를 적절한 위치에 정확히 삽입할 수 있게 되어 정렬이 올바르게 이루어집니다.
"""