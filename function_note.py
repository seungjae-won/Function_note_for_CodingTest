'''
    @brief : 자연수의 전체 자릿수 합 구하기

    @date : 2020/12/20 업데이트

    @return : sum (int)

    @param : n (int)
'''
def digit_sum(n):
    return sum(int(i) for i in str(n))


'''
    @brief : matrix 내 column 추출하기

    @date : 2020/12/20 업데이트

    @return : sum (int)

    @param : column (int), matrix (list)
'''
def column_extract(column, matrix):
    return list(map(lambda x: x[column] , matrix))


'''
    @brief : 다음 조건에 맞는 list 내 가장 가까운 index value
             list.index() 함수와 같이 이용시 해당 index 추출 가능 

    @date : 2020/12/20 업데이트

    @return : sum (int)

    @param : list (list)
'''
def following_value(list):
    # if 문에 원하는 조건 input
    return next(value for value in list if value != 0)
    # list.index()를 통해 해당 value의 index 추출 가능
    return list.index(next(value for value in list if value != 0))


'''
    @brief : list 내 모든 value가 0(False)인지 True인지 판단, 
             하나라도 0(False)가 존재하는지 판단 

    @date : 2020/12/20 업데이트

    @return : bool (True or False)

    @param : list (list)
'''
def any_all_list(list):
    # list 내 value가 모두 0(False)이면 True, 하나라도 0이 아니면 False
    return any(list)
    # list 내 value가 하나라도 0(False)이면 False, 모두 True이면 True
    return all(list)



# 출처 : https://brownbears.tistory.com/468 
'''
    @brief : 10진법의 숫자와 변환하고자 하는 n진법(base)을 input으로 주면 변환 결과 return

    @date : 2020/12/21 업데이트

    @return : result (int)

    @param : number (int), base (int)
'''
def numeral_system(number, base):
    NOTATION = '0123456789ABCDEF'
    q,r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base)+n if q else n

    # 위 경우와 반대로 n진수를 10진수로 변환하기 위해서 사용하는 함수
    int(str('n진법 수 - str type input'), int('base - int type의 현재 진법 input'))
    


'''
    @brief : graph와 start가 주어졌을 때 dfs 수행

    @date : 2020/12/23 업데이트

    @return : visited (list)

    @param : graph (dict), start (int)
'''
def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
                
    return visited

'''
    @brief : graph와 start가 주어졌을 때 bfs 수행

    @date : 2020/12/23 업데이트

    @return : visited (list)

    @param : graph (dict), start (int)
'''
from collections import deque

def bfs(graph, start):

    visited = [start]
    
    queue = deque([start])
    
    while queue:
        v = queue.popleft()
    
        for i in graph[v]:
            if not i in visited:
                queue.append(i)
                visited.append(i)
                
    return visited

'''
    @brief : 주어진 num에 대해서 소수판별 수행 - 시간복잡도 sqrt(N)

    @date : 2020/12/31 업데이트

    @return : bool

    @param : num (int)
'''
def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True
                
'''
    @brief : 주어진 num에 이하에 대해서 소수판별 수행

    @date : 2020/12/31 업데이트

    @return : eratos (list)

    @param : num (int)
'''
import math
def eratos_Prime(num):

    eratos = [1] * (2 * num + 1)
    eratos[0] = 0
    eratos[1] = 0

    for i in range(2, int(math.sqrt(len(eratos)))):
        if eratos[i]:
            for j in range(i + i, len(eratos), i):
                eratos[j] = 0
    return eratos


# 출처 : https://roseline124.github.io/algorithm/2019/03/22/Algorithm-baekjoon-2108.html
'''
    @brief : 주어진 num_list에 대해서 최빈값을 return

    @date : 2021/1/1 업데이트

    @return : mod (int)

    @param : num_list (list)
'''

from collections import Counter

def mode(num_list):
    mode_dict = Counter(num_list)
    modes = mode_dict.most_common()    
    
    if len(num_list) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]

    return mod

'''
    @brief : graph와 출발점 start가 주어질 때 dijkstra 알고리즘 구현

    @date : 2021/1/6 업데이트

    @return : dp (list)

    @param : grpah (dict), start (int)
'''

import heapq
import sys

def dijkstra(graph, start):
    inf = sys.maxsize
    dp = [inf]*len(graph)
    dp[start] = 0
    heap = []
    heapq.heappush(heap, (0,start))
    
    while heap:
        weight, current = heapq.heappop(heap)
        
        if dp[current] < weight:
            continue
        
        for w, next_n in graph[current]:
            next_w = w+weight
            
            if next_w < dp[next_n]:
                dp[next_n] = next_w
                heapq.heappush(heap, (next_w,next_n))
    
    return dp