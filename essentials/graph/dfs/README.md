DFS(Depth-First Search, 깊이 우선 탐색)는 **그래프 탐색 알고리즘** 중 하나로, **가장 깊은 노드**까지 탐색한 후 되돌아와 다른 경로로 다시 깊이 탐색하는 방식입니다. DFS는 트리나 그래프와 같은 자료 구조에서 많이 사용되며, 주로 재귀나 스택을 이용하여 구현됩니다.

---

### DFS의 동작 방식

DFS는 다음과 같은 단계로 작동합니다:

1. **시작 노드 방문**: 탐색을 시작할 노드를 방문하고, 해당 노드를 방문했다고 표시합니다.
2. **인접 노드 방문**: 현재 노드와 인접한 노드 중 방문하지 않은 노드가 있으면 그 노드를 방문합니다.
3. **재귀 또는 스택으로 깊이 탐색**: 더 이상 방문할 인접 노드가 없으면, 이전 단계로 되돌아가서 다른 경로를 탐색합니다.
4. **반복**: 모든 노드를 방문할 때까지 반복합니다.

---

### DFS의 구현 방법

DFS는 **재귀** 또는 **스택**을 사용하여 구현할 수 있습니다. 

#### 1. 재귀를 이용한 DFS 구현

재귀 호출을 통해 DFS를 구현할 수 있습니다. 아래는 재귀를 이용한 DFS 코드입니다.

```python
def dfs_recursive(graph, node, visited):
    # 현재 노드를 방문 처리
    visited[node] = True
    print(node, end=' ')  # 방문한 노드 출력 (예시)

    # 인접한 노드를 재귀적으로 방문
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_recursive(graph, neighbor, visited)
```

- `graph`는 노드와 인접 노드를 나타내는 **인접 리스트** 형태로 표현된 그래프입니다.
- `visited`는 노드의 방문 여부를 기록하는 리스트로, 방문한 노드는 `True`로 표시합니다.
- `dfs_recursive` 함수는 현재 노드를 방문한 후, 인접 노드를 재귀적으로 호출하여 탐색을 이어나갑니다.

#### 2. 스택을 이용한 DFS 구현

스택을 사용하여 DFS를 비재귀적으로 구현할 수도 있습니다. 

```python
def dfs_stack(graph, start):
    visited = [False] * len(graph)
    stack = [start]  # 시작 노드를 스택에 넣음

    while stack:
        node = stack.pop()  # 스택에서 가장 최근 노드를 꺼냄
        if not visited[node]:
            visited[node] = True
            print(node, end=' ')  # 방문한 노드 출력 (예시)

            # 인접 노드를 스택에 추가 (역순으로 추가하여 스택에서 순서대로 탐색)
            for neighbor in reversed(graph[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)
```

- `stack`을 이용해 DFS의 후입선출(LIFO) 구조를 구현하며, 스택에서 노드를 꺼내면서 방문하지 않은 경우 방문 처리합니다.
- **역순으로 인접 노드를 스택에 추가**하면, 인접한 노드들이 원래 순서대로 탐색되도록 할 수 있습니다.

---

### DFS 예시

그래프가 다음과 같이 주어졌다고 가정해 보겠습니다:

```
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}
```

DFS 탐색 순서는 시작 노드에 따라 다르지만, 예를 들어 1번 노드에서 시작하는 경우 다음과 같은 순서로 탐색됩니다:

- **재귀 DFS**: `1 → 2 → 5 → 3 → 6 → 7 → 4`
- **스택 DFS**: `1 → 4 → 3 → 7 → 6 → 2 → 5`

---

### DFS의 시간 복잡도

- **시간 복잡도**: \(O(V + E)\)
  - \(V\)는 노드(정점)의 수, \(E\)는 간선의 수입니다.
  - DFS는 각 노드를 한 번씩 방문하고, 모든 간선을 한 번씩 탐색하므로 \(O(V + E)\)의 시간 복잡도를 가집니다.

- **공간 복잡도**: \(O(V)\)
  - 재귀 DFS는 재귀 호출 스택에 의해 공간이 추가로 사용되므로, 최악의 경우 \(O(V)\)의 스택 공간이 필요합니다.
  - 비재귀 DFS는 방문 리스트와 스택을 저장하기 위해 \(O(V)\)의 공간을 사용합니다.

---

### DFS의 활용

DFS는 다양한 문제에서 활용됩니다. 특히, 경로 탐색, 사이클 검사, 연결 요소 개수 찾기, 백트래킹 등에서 많이 사용됩니다.

- **경로 찾기**: 그래프에서 특정 노드에서 다른 노드로 가는 경로가 존재하는지 확인할 때 사용됩니다.
- **사이클 검사**: DFS를 통해 그래프 내에 사이클이 존재하는지 확인할 수 있습니다.
- **연결 요소 찾기**: DFS를 통해 연결 요소를 찾을 수 있습니다. 연결된 컴포넌트를 탐색하여 개수를 세거나, 특정 영역을 색칠하는 등의 작업에서 유용합니다.
- **백트래킹**: DFS는 백트래킹 알고리즘의 기초로 활용되며, 특히 순열, 조합, N-Queens 문제 등에서 재귀 DFS를 사용해 가능한 모든 경우의 수를 탐색할 수 있습니다.

DFS는 깊이 우선으로 탐색하는 특징 때문에, **모든 경로를 탐색해야 하는 문제**나 **최대 깊이로 탐색해야 하는 문제**에서 자주 사용되는 알고리즘입니다.


DFS(Depth-First Search)를 구현할 때 **재귀**와 **스택** 중 어느 것을 사용하는 것이 더 최적인지는 문제의 특성과 요구 사항에 따라 다릅니다. 두 방식의 장단점을 비교해보고, 어떤 경우에 더 적합한지 살펴보겠습니다.

---

### 1. **재귀를 사용한 DFS**

#### 장점
1. **구현이 간단**:
   - 재귀 함수는 자연스럽게 호출 스택을 사용하므로 코드가 간결하고 직관적입니다.
   - 작은 규모의 문제나 깊이가 적당히 제한된 문제에서 빠르게 작성할 수 있습니다.

2. **가독성**:
   - 그래프 탐색의 논리가 명확하게 드러나며, 수학적인 알고리즘을 그대로 구현하기 쉽습니다.

#### 단점
1. **스택 오버플로우 위험**:
   - 재귀 호출이 깊어지면 호출 스택이 넘쳐 **스택 오버플로우**가 발생할 수 있습니다.
   - 일반적인 파이썬의 재귀 호출 한도는 약 1000번 정도이므로, 그래프의 깊이가 깊으면 적합하지 않습니다.

2. **디버깅 어려움**:
   - 재귀 호출의 흐름을 따라가면서 디버깅하기가 스택 기반 방식보다 어려울 수 있습니다.

#### 적합한 경우
- 그래프의 깊이가 비교적 얕고, 정점 개수도 적어서 재귀 호출 한도 내에 들어오는 경우.
- 간결한 코드가 중요하거나, 문제의 논리를 빠르게 구현해야 하는 경우.
- 재귀 구조가 문제의 본질과 잘 맞는 경우(예: 트리 탐색).

---

### 2. **스택을 사용한 DFS**

#### 장점
1. **스택 오버플로우 없음**:
   - 재귀 대신 명시적으로 스택을 사용하기 때문에 호출 스택 제한을 피할 수 있습니다.
   - 깊이가 매우 깊거나 정점 수가 많은 그래프에서 안전하게 작동합니다.

2. **유연성**:
   - 스택을 명시적으로 사용하므로, 탐색 순서나 방식(예: 반복 순서를 뒤집는 등)을 쉽게 제어할 수 있습니다.
   - 방문 여부를 명시적으로 처리하므로, 복잡한 그래프에서도 안정적입니다.

#### 단점
1. **코드가 복잡**:
   - 스택을 명시적으로 관리해야 하므로 코드가 길어질 수 있습니다.
   - 논리가 명확히 보이지 않을 수 있습니다.

2. **가독성 낮음**:
   - 재귀에 비해 코드가 직관적이지 않을 수 있으며, 추가적인 구현이 필요합니다.

#### 적합한 경우
- 그래프의 깊이가 매우 깊거나, 노드의 개수가 재귀 호출 한도를 초과할 가능성이 있는 경우.
- 명시적으로 스택을 관리하거나 탐색 순서를 세밀히 제어해야 하는 경우.
- 대규모 그래프를 탐색해야 하는 문제(특히 깊이가 불균형한 그래프).

---

### 3. **재귀와 스택의 비교 표**

| **구분**         | **재귀**                              | **스택**                              |
|-------------------|---------------------------------------|---------------------------------------|
| **구현 난이도**   | 간단하고 직관적                       | 다소 복잡                             |
| **스택 오버플로우** | 발생 가능                            | 발생하지 않음                         |
| **탐색 제어**     | 제한적                                | 유연하게 제어 가능                    |
| **사용 메모리**   | 호출 스택 사용                       | 명시적 스택 사용 (메모리 효율 비슷)    |
| **적합한 상황**   | 깊이가 제한적인 소규모 그래프          | 깊이가 깊거나 큰 규모의 그래프         |

---

### 4. **결론: 언제 어떤 방식을 선택할까?**

1. **작은 그래프**:
   - 재귀를 사용하는 것이 간결하고 빠르게 구현할 수 있어 적합합니다.

2. **깊이가 깊거나 대규모 그래프**:
   - 스택 기반 DFS를 사용하는 것이 더 안전하고 확장성 있습니다.

3. **특정 탐색 순서가 중요한 경우**:
   - 스택 기반 DFS를 사용하면 명시적으로 탐색 순서를 제어할 수 있어 적합합니다.

4. **디버깅이나 안정성**:
   - 스택 방식이 호출 스택에 의존하지 않으므로 더 안정적이고 디버깅하기 쉽습니다.

---

### 실제 구현에서의 선택

- **트리 탐색이나 백트래킹 문제**: 재귀 방식이 더 직관적이며 간단하게 구현 가능합니다.
- **그래프 탐색 문제(특히 불균형한 그래프)**: 스택 기반 DFS가 적합하며, 복잡한 그래프에서도 안정적으로 작동합니다.

일반적으로 **재귀 방식은 간결하고 직관적이며, 스택 방식은 유연하고 안정적**입니다. 문제의 특성과 그래프 크기에 따라 적절한 방식을 선택하세요.