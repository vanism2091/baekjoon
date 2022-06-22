
problems = [1012, 1260, 1697, 2178, 2468, 2667, 7576, 10026]
not_clear = [1697, 2468, 7576]
need_to_study = [1012, 2667, 10026]


# 328 -> 80 sys.stdin.readline 
def sol_1012():
    import sys
    p=sys.stdin.readline
    sys.setrecursionlimit(10**6)
    n = int(p())
    def get_num(n, m, graph):
        def dfs(x, y):
            if x<0 or x>= n or y<0 or y>= m:
                return False
            if graph[x][y] == 0:
                return False
            graph[x][y] = 0
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        cnt = 0
        for i in range(n):
            for j in range(m):
                if dfs(i, j):
                    cnt += 1
        return cnt
        
    for _ in range(n):
        m, n, k = map(int, p().split())
        graph = [[0]*m for _ in range(n)]
        for _ in range(k):
            y, x = map(int,p().split())
            graph[x][y] = 1
        print(get_num(n, m, graph))

## TODO: 분석해보기
def other_1012():
    import sys;p=sys.stdin.readline;
    sys.setrecursionlimit(1000000)
    q=int(p())
    def T(t, o, s):
        t[s][o]=0
        if o+1 < x and t[s][o+1]==1:
            T(t,o+1,s)
        if o-1>= 0 and t[s][o-1]==1:
            T(t, o-1,s)
        if s -1 >= 0 and t[s-1][o]==1:
            T(t, o,s-1)
        if s +1 < y and t[s+1][o]==1:
            T(t,o,s+1)

    for _ in range(q):
        x, y, c = map(int, p().split())
        t = [[0] * x for _ in range(y)]
        for i in range(0,c):
            m,n=map(int,p().split());t[n][m] = 1
        v = 0
        for i in range(0,x):
            for j in range(0, y):
                if t[j][i] == 1:
                    T(t, i, j);v+=1
        print(v)




# BFS와 DFS
# input:
#   첫째 줄에 정점의 개수 N [1,1000], 간선의 개수 M [1,10,000], 탐색을 시작할 정점의 번호 V가 주어진다. 
#   다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
#   어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 내 IDEA
# list로 해도 될 것 같은데, 정점갯수 1이고 정점이 1000인 경우 메모리 낭비..
# 그래프 표현은 dictionary로 하자. {"node":[linked nodes]}
# visited도 dictionary {"node": True/False}
# 예외 케이스 :: v가 m에 없는 경우가 있었다 :)
# 34032	480 처참한 속도..:)
def sol_1260():
    n, m, v = map(int, input().split())
    graph = {}
    visited = {}

    # graph, visited 초기화
    for _ in range(m):
        i, j = map(int, input().split())
        if i not in graph:
            graph[i] = [j]
            visited[i] = False
        else : graph[i].append(j)
        if j not in graph:
            graph[j] = [i]
            visited[j] = False
        else: graph[j].append(i)

    def dfs(v):
        # if not visited[v]:
        #     return
        visited[v] = True
        print(v, end=" ")
        for i in sorted(graph[v]):
            if visited[i]:
                continue
            dfs(i)
    dfs(v)
    print()
    for k in visited:
        visited[k] = False
    from collections import deque
    def bfs(v):
        q = deque([v])
        visited[v] = True
        while q:
            # print(q)
            i = q.popleft()
            print(i, end=" ")
            for n in sorted(graph[i]):
                if not visited[n]:
                    visited[n] = True
                    q.append(n)
    bfs(v)

def sol_1260_n():
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)

    # graph, visited 초기화
    for _ in range(m):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    def dfs(v):
        visited[v] = True
        print(v, end=" ")
        for i in sorted(graph[v]):
            if visited[i]:
                continue
            dfs(i)
    dfs(v)

    visited = [False]*(n+1)
    from collections import deque
    def bfs(v):
        visited[v] = True
        q = deque([v])
        while q:
            i = q.popleft()
            print(i, end=" ")
            for n in sorted(graph[i]):
                if not visited[n]:
                    visited[n] = True
                    q.append(n)
    bfs(v)

    # 속도 차이가 너무 남...
    # 1. sys.stdin.readline().split()       :: 와... 480 -> 100 미쳤따..
    # 2. graph sort를 미리 한다 > 기존은 bfs, dfs 2번에 걸쳐서 함. :: dictionary의 경우 큰 속도 차이 없음;
    # 3. print를 계속 하지 말고 res list를 나중에 한꺼번에 프린트한다 :: 100 -> 100 ㄴㄴ

def sol_1260_last_dict():
    import sys
    from collections import deque

    n, m, v = map(int, input().split())
    graph = {}
    visited = {}

    # graph, visited 초기화
    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        if i not in graph:
            graph[i] = [j]
            visited[i] = False
        else : graph[i].append(j)
        if j not in graph:
            graph[j] = [i]
            visited[j] = False
        else: graph[j].append(i)

    for k in graph:
        graph[k].sort()

    res_dfs = []
    def dfs(v):
        if v not in visited:
            res_dfs.append(v)
            return
        visited[v] = True
        res_dfs.append(v)
        for i in graph[v]:
            if visited[i]:
                continue
            dfs(i)
    dfs(v)
    print(*res_dfs)
    for k in visited:
        visited[k] = False

    res_bfs = []
    def bfs(v):
        if v not in visited:
            res_bfs.append(v)
            return
        q = deque([v])
        visited[v] = True
        while q:
            i = q.popleft()
            res_bfs.append(i)
            for n in graph[i]:
                if not visited[n]:
                    visited[n] = True
                    q.append(n)
    bfs(v)
    print(*res_bfs)



# 시간초과..:(
def sol_1697():
    from collections import deque
    
    n, k = map(int,input().split())
    res = {}
    cases = ['+1', '-1', '*2']
    while k not in res:

        pass
    def bfs(v, l):
        q1 = deque([(v, 0)])
        q2 = deque([l, 0])
        while q1 or q2:
            curr1, step1 = q1.popleft()
            curr2, step2 = q2.popleft()
            if curr1 == curr2:
                return step1 + step2
            for case in cases:
                next1 = eval(f'{curr1}{case}')
                next2 = eval(f'{curr2}{case}')
                if next1 < 0:
                    continue
                q1.append((next1, step1+1))
    print(bfs(n))




# 미로 탐색
def sol_2178():
    import sys
    from collections import deque

    n, m = map(int, input().split())
    graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
    # graph = [list(map(int, input())) for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    def dfs(x, y):
        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if nx == n-1 and ny == m-1:
                    return graph[x][y] + 1
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
    print(dfs(0, 0))
        


# 틀렸습니다 :(
def sol_2468():
    from collections import Counter

    n = int(input())
    c = Counter()
    graph = []
    for i in range(n):
        graph.append(list((map(int, input().split()))))
        c.update(graph[i])

    def dfs(x, y, h):
        if x < 0 or x >= n or y < 0 or y >= n or graph[x][y] <= h:
            return False
        graph[x][y] = 101
        dfs(x-1, y, h)
        dfs(x+1, y, h)
        dfs(x, y-1, h)
        dfs(x, y+1, h)
        return True

    def get_num(h):
        cnt = 0
        for i in range(n):
            for j in range(n):
                if dfs(i, j, h):
                    cnt += 1
        return cnt

    res = [0]
    for i in sorted(list(c)):
        curr_res = get_num(i)
        if res[-1] < curr_res:
            break
        res.append(curr_res)
    print(res[-1])



def sol_2667():
    from collections import Counter

    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    cnt = 1
    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= n or graph[x][y] != 1:
            return False
        graph[x][y] = -cnt
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    for i in range(n):
        for j in range(n):
            if dfs(i, j):
                cnt += 1
    res = [v for i, v in Counter([v for li in graph for v in li if v]).items()]
    res.sort()
    print(cnt-1)
    for i in res:
        print(i)

    # 이 유형을 bfs로 했는데 속도가 빨라서 연구할 가치가 있을듯...
def other_2667():
    def isInside(x,y):
        return (0<=x<N and 0<=y<N)

    def bfs(start):
        queue=[start]
        y, x = start
        visit[y][x]=1
        count=0
        
        while queue:
            y, x = queue.pop(0)
            count=count+1
        
            dx=[0,0,1,-1]
            dy=[-1,1,0,0]
        
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                
                if(isInside(nx,ny)):
                    if(house[ny][nx]==1 and visit[ny][nx]==0):
                        visit[ny][nx]=1
                        queue.append([ny,nx])
                    
        stack.append(count)

    N=int(input())

    house=[]
    for i in range(N):
        house.append(list(map(int, list(input()))))
        
    stack=[]
    visit=[[0]*N for i in range(N)]

    for i in range(N):
        for j in range(N):
            if(house[i][j]==1 and visit[i][j]==0):
                bfs([i,j])
                
    stack.sort()
    print(len(stack))
    for i in stack:
        print(i)

"""
토마토
- 1이 몇 개인지, 어디에 있는지 알아야 하고 (시작 지점)
- bfs를 하면서 상하좌우는 이전 step의 +1
- 그런데 다른 토마토도 있을 테니 만약 0이 아니면 min(step+1, value)
- 만약 min이후 step+1이 아니라 value라면, 그 방향으로는 그만 append
- 전체 상자 내에서 최댓값을 프린트
- 끝났는데 0이 있으면 -1을 출력

- 시간초과 :(
    5% index마다 bfs 쭉..
    45% 1 있는 만큼 q 리스트를 만들어서 depth마다 q를..
"""
def sol_7576_1():
    import sys
    from collections import deque

    p = sys.stdin.readline
    m, n = map(int, p().split())
    idxs = []
    graph = []

    # 그래프 초기화
    for i in range(n):
        l = list(map(int,p().split()))
        graph.append(l)
        if 1 not in l:
            continue
        for j, v in enumerate(l):
            if v == 1: idxs.append((i, j))
    cnt = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # BFS 정의
    def bfs(i, j, cnt):
        q = deque([(i, j)])
        while q:
            print(cnt, q)
            cnt += 1
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                c = graph[nx][ny]; b = graph[x][y]+1
                if c == 0 or c > b:
                    graph[nx][ny] = b
                    q.append((nx, ny))
                elif c <= b:
                    continue
    for x, y in idxs:
        bfs(x, y, cnt)
    res = [v for l in graph for v in l]
    if 0 in res:
        print(-1)
    else:
        print(max(res)-1)


def sol_7576_2():
    import sys
    from collections import deque

    p = sys.stdin.readline
    m, n = map(int, p().split())
    idxs = []
    graph = []

    # 그래프 초기화
    for i in range(n):
        l = list(map(int,p().split()))
        graph.append(l)
        if 1 not in l:
            continue
        for j, v in enumerate(l):
            if v == 1: idxs.append((i, j))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # BFS 정의
    def bfs(idxs):
        qs = [deque([(x, y)]) for x, y in idxs]
        while qs:
            for q in qs:
                if not q:
                    qs.remove(q)
                    continue
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    c = graph[nx][ny]; b = graph[x][y]+1
                    if c == 0 or c > b:
                        graph[nx][ny] = b
                        q.append((nx, ny))
                    elif c <= b:
                        continue
    bfs(idxs)
    res = [v for l in graph for v in l]
    if 0 in res:
        print(-1)
    else:
        print(max(res)-1)
    


# 적록 색약
def sol_10026():
    n = int(input())
    graph = []
    dic = {"R": -1, "G": 1, "B": 0}
    for _ in range(n):
        graph.append([dic[i] for i in input()])

    def get_num(is_abs):
        def dfs(x, y, curr):
            if x<0 or x>= n or y<0 or y>= n:
                return
            if is_abs:
                if abs(graph[x][y]) != curr: return
            else:
                if graph[x][y] != curr: return
            if visited[x][y]:
                return
            visited[x][y] = 1
            dfs(x-1, y, curr)
            dfs(x+1, y, curr)
            dfs(x, y-1, curr)
            dfs(x, y+1, curr)
            pass

        visited = [[0]*n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0:
                    dfs(i, j, graph[i][j])
                    cnt += 1
        return cnt
    print(get_num(False))
    print(get_num(True))
    
    # R : 114
    # G : 103
    # B : 98
    
## 내 속도 90쯤, 이분은 72
def other_10026():
    import sys
    sys.setrecursionlimit(10**6)
    n=int(input())
    a=[[" "]*(n+2)]+[list(" "+input()+" ")for i in[0]*n]+[[" "]*(n+2)]
    b=[i.copy()for i in a]
    def cnt(s,x,y,c):
        s[x][y]=" "
        if s[x-1][y]==c:cnt(s,x-1,y,c)
        if s[x+1][y]==c:cnt(s,x+1,y,c)
        if s[x][y-1]==c:cnt(s,x,y-1,c)
        if s[x][y+1]==c:cnt(s,x,y+1,c)
    c=d=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if a[i][j]!=" ":
                cnt(a,i,j,a[i][j]);c+=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if b[i][j]=="G":b[i][j]="R"
    for i in range(1,n+1):
        for j in range(1,n+1):
            if b[i][j]!=" ":
                cnt(b,i,j,b[i][j]);d+=1
    print(c,d)