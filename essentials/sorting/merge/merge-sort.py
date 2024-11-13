
def merge_sort1(arr):
    
    # 리스트의 크기가 1 이하이면 이미 정렬된 상태이므로 그대로 반환
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

     # 각 절반에 대해 병합 정렬을 재귀적으로 호출
    left = merge_sort1(arr[:mid])
    right = merge_sort1(arr[mid:])

    # 두 정렬된 리스트를 병합하여 반환
    return merge(left, right)


def merge(left, right):
    sorted_list = []
    i = j = 0
    # 두 리스트를 병합하면서 정렬
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # 남은 요소들을 추가
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

arr1 = [5, 3, 8 , 4, 2]
arr2 = [64, 34, 25, 12, 22, 11, 90]

print(merge_sort1(arr2))