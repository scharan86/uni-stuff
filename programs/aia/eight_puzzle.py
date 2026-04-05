import heapq

GOAL = [[1,2,3],[4,5,6],[7,8,0]]

def is_solvable(state):
    flat = [n for row in state for n in row if n != 0]
    inversions = sum(1 for i in range(len(flat)) for j in range(i+1, len(flat)) if flat[i] > flat[j])
    return inversions % 2 == 0

def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            v = state[i][j]
            if v != 0:
                dist += abs(i - (v-1)//3) + abs(j - (v-1)%3)
    return dist

def neighbors(state):
    result = []
    flat = [n for row in state for n in row]
    r, c = divmod(flat.index(0), 3)
    for dr, dc, move in [(-1,0,'Up'),(1,0,'Down'),(0,-1,'Left'),(0,1,'Right')]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            s = [row[:] for row in state]
            s[r][c], s[nr][nc] = s[nr][nc], s[r][c]
            result.append((s, move))
    return result

def solve(start):
    if not is_solvable(start):
        return 'Not solvable'
    heap = [(manhattan(start), 0, start, [])]
    visited = set()
    while heap:
        _, g, state, path = heapq.heappop(heap)
        key = tuple(n for row in state for n in row)
        if key in visited:
            continue
        visited.add(key)
        if state == GOAL:
            return path
        for s, move in neighbors(state):
            if tuple(n for row in s for n in row) not in visited:
                heapq.heappush(heap, (g+1+manhattan(s), g+1, s, path+[move]))
    return 'No solution found'

start = [[1,2,3],[4,0,6],[7,5,8]]
result = solve(start)
print('Moves:', ' -> '.join(result) if isinstance(result, list) else result)
print('Total moves:', len(result) if isinstance(result, list) else '-')
