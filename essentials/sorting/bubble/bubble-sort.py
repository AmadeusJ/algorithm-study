"""
Bubble은 bubble 처럼 인접한 요소와 붙어먹는다. 
"""

# def bubble_1(arr):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#             print(arr)
#     return arr

# arr1 = [5, 3, 8 , 4, 2]
# arr2 = [64, 34, 25, 12, 22, 11, 90]
# print(bubble_1(arr2))

"""
==> 7번쩨 줄은 j는 i와 인접한, 요소를 두번째 차부터는 가져오지 않는다...
그러므로 정렬은 되지만, 버블정렬이라 할 수는 없다.
"""

def bubble_2(arr):
    n = len(arr)
    for i in range(n):       # ?
        for j in range(n - i - 1):  # ?
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]

    return arr

arr1 = [5, 3, 8 , 4, 2]
arr2 = [64, 34, 25, 12, 22, 11, 90]

print(bubble_2(arr2))

"""
첫 번째 반복문: for i in range(n)
이 부분은 정렬된 요소를 제외하고 나머지 요소들을 반복적으로 정렬하는 역할을 합니다.

i가 증가할수록 정렬할 범위가 줄어듦:
Bubble Sort에서는 한 번의 반복(즉, i 값의 증가)마다 가장 큰 요소가 끝으로 이동하게 됩니다.
따라서 정렬이 진행될수록 마지막 몇 개의 요소는 이미 정렬된 상태가 됩니다.
정렬된 요소를 제외하기 위해:
i가 증가할 때마다 정렬되지 않은 부분의 크기는 n - i로 줄어들기 때문에, 이 범위를 설정하기 위해 n - i - 1까지 반복을 설정하게 됩니다.
두 번째 반복문: for j in range(0, n - i - 1)
이 부분은 실제로 인접한 요소를 비교하고 교환하여 가장 큰 값을 끝으로 이동시키는 작업을 합니다.

j는 인접한 두 요소를 비교하기 위한 인덱스:
j와 j + 1 위치의 요소를 비교하여, 앞의 값이 더 크면 교환합니다. 이렇게 하면 한 번의 j 반복이 끝나면 가장 큰 요소가 현재 범위의 끝으로 "밀려"가게 됩니다.
n - i - 1인 이유:
i번째 반복이 끝날 때마다 가장 큰 요소가 리스트의 끝부터 차례로 정렬됩니다. 예를 들어 첫 번째 i 반복이 끝나면 가장 큰 값이 리스트의 끝으로 가게 됩니다.
다음 i 반복 때는 리스트의 마지막 요소를 제외하고 다시 반복합니다. 따라서 n - i - 1로 반복 범위를 좁혀줍니다.
"""