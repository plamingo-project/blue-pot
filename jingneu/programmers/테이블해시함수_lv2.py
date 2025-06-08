def solution(data, col, row_begin, row_end):
    answer = 0
    
    data.sort(key=lambda x: (x[col-1], -x[0]))

    for i in range(row_begin-1, row_end):
        temp = 0
        for idx, num in enumerate(data[i]):
            temp+= num%(i+1)
            
            if (idx != len(data[i])-1):
                continue
            #temp 정해지면 xor 연산 수행
            if (i != row_begin-1):
                answer = temp^answer
            else:
                answer = temp
        
    return answer

#xor 연산 몰라서 헤맴
#xor 연산은 십진수 상태에서 연산자로 구하면 된다
#비트 연산 알아두기