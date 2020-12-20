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

