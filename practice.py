# 1번답
# a = input() #a인풋받음
# a = list(a)
# print(''.join(reversed(a))) #  a리스트를 reversed 하고 join으로 배열함


# 2번 답
# num1,num2 = input().split()
# num1,num2 = int(num1),int(num2)
# num_p = num1+num2
# num_m = num1*num2
# num_d = num1%num2
# num_minus = num1 - num2
# print(num_p)
# print(num_minus)
# print(num_m)
# print(num_d)

# 3번답
# a,b = input().split()
# if a > b:
#     print('>')
# elif a ==b:
#     print("=")
# else:
#     print('<')

#4번답

# grade = int(input())
# if 60 <= grade <= 69:
#     print('D')
# if 70<= grade <= 79:
#     print('C')
# if 80<= grade <=89:
#     print('B')
# if 90<= grade <= 100:
#     print('A')

#5번답

# num = int(input())
# for i in range(1,10):
#     print(num*i)

#6번답
# a = int(input())
# output = 0
# for i in range(a+1):
#     output += i 
# print(output) 

# 7번 답
# a= map(int,input().split())
# b= map(int,input().split())

# for i in a:
#     for g in b:
#         if i > g:
#             print(g,end=' ')
#         else:
#             pass

# 8번 답
# a = input()
# b = list(map(int,input().split()))
# print(min(b))
# print(max(b))



# 9번 답

# num_list = []
# while True:
#     num = input()
#     num_list.append(num)
#     if num == '':
#         break
# max_num = max(num_list)
# max_idx = num_list.index(max_num) + 1
# print(max_num)
# print(max_idx)

# 10번 답
# leng = int(input())+1
# leng_lst = []
# for i in range(leng):
#     leng_lst.append(i)
# leng_lst.reverse()
# for g in leng_lst:
#     if g % 2 ==1:
#         print(g)


# 11번 문제
#  3x3 행렬로 출력 (numpy library)
#     ex_input = '1 2 3 4 5 6 7 8 9'
#     ex_output = '[[1 2 3]\n[4 5 6]\n[7 8 9]]'

# 11번 답	
# import numpy as np 
# arr1 = list(map(int,input().split()))
# a = np.array(arr1)
# a_arr = a.reshape(3,3)
# print(a_arr)


# *행렬 문제 (12~13)
# \n앞 : nxn 행렬 정보 / 그 다음 + \n 기준으로 행렬의 값
# Ex) 1 4\n1 2 3 4\n5 6 7 8 = 2x4행렬 :  [1, 2, 3, 4]
#                                                     [5, 6, 7, 8]

# 12. numpy library 중 (add, subtract, multiply, floor_divide, mod, power) 함수 사용하여 출력
#     ex_input = '1 4\n1 2 3 4\n5 6 7 8'
#     ex_output = '[[ 6  8 10 12]]\n[[-4 -4 -4 -4]]\n[[ 5 12 21 32]]\n[[0 0 0 0]]\n[[1 2 3 4]]\n[[    1    64  2187 65536]]'
#mod 는 a를 b로나눈 나머지
#power는 a의 b승
#12번답
# import numpy as np

# rank =  tuple(map(int,input().split()))

# nums = list(map(int,input().split()))
# nums1 = list(map(int,input().split()))

# nums_arr = np.array(nums)
# nums1_arr = np.array(nums1)
# nums_arr = nums_arr.reshape(rank)
# nums1_arr = nums1_arr.reshape(rank)
# print(np.add(nums_arr,nums1_arr))
# print(np.subtract(nums_arr,nums1_arr))
# print(np.floor_divide(nums_arr,nums1_arr))
# print(np.multiply(nums_arr,nums1_arr))
# print(np.mod(nums_arr,nums1_arr))
# print(np.power(nums_arr,nums1_arr))


# 13. 행별로 가장 작은 숫자를 뽑고 그 안에서 가장 큰 값을 출력
#     ex_input = '4 2\n2 5\n3 7\n1 3\n4 0'
#     ex_output = 3

#13번답
# import numpy as np
# a_lst = []
# while True:
    
#     a = list(map(int,input().split()))
#     if len(a) == 0:
#         break
#     a1 = np.array(a)
#     addnum = np.min(a1)
#     a_lst.append(addnum)
    
# print(max(a_lst))


# 14. 역순으로 리스트에 담기
#     ex_input = '1 2 3 4 -8 -10'
#     ex_output = '[-10  -8   4   3   2   1]'

#14번답
# ex_input = list(map(int,input().split()))
# ex_input.reverse()
# print(ex_input)

# 15. N단 트리 만들기
#     ex_input = '5'
#     ex_output = '    *\n   **\n  ***\n ****\n*****'

# # 15번 답
# ex_input = int(input())
# for i in range(1,ex_input+1):
#     print('{1}{0}\n'.format('*'*i,' '*ex_input))
#     ex_input -=1 

# 16. if) 입력 : N / 출력 : 4로 나눴을 때 나머지가 0이고 100으로 나눴을 때 나머지가 0이 아닌 경우 return '1'
#     elif) 400으로 나눴을 때 나머지가 0이면 return'1'
#     else) 모두 해당되지 않으면 '0' 출력

#     ex_input = '2000'
#     ex_output = '1'

#16번 답
# n = int(input())
# if n % 4 == 0 and n / 100 != 0:
#     a = 1 
# elif n % 400 == 0:
#     a = 1
# else:
#     print(0)
# print(a)

# 17. x,y>0 일때 '1' / x<0, y>0 일때 '2' / x<0, y<0 일때 '3' / 그렇지 않으면 4
#     ex_input = '12\n5'
#     ex_output = '1'

#17번 답
# x = int(input())
# y = int(input())
# if x and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# else:
#     print(4)


# 18. 앞에서 3개 / 나머지 2개를 list에 담고 sort 하고 맨 앞 작은 수를 골라 sum - 50
#     ex_input = '800\n700\n900\n198\n330'
#     ex_output = '848'

#18번답
# lst1 = []
# lst2 = []
# for i in range(5):
#     ex_input = int(input())
#     if i < 3:
#         lst1.append(ex_input)
#     else:
#         lst2.append(ex_input)
# lst1.sort()
# lst2.sort()
# ret = lst1[0] + lst2[0] - 50 
# print(ret)

# 19. \n 앞의 수로 \n 뒤의 숫자를 다 더한 값을 나누기 (평균)
#     ex_input = '3\n40 80 60'
#     ex_output = '60.0'

#19번 답
# ex_input = list(map(int,input().split()))
# ex_input1 = int(input())
# print(sum(ex_input)/ex_input1)


# 20.  첫번째 \n 앞에는 \n 별로 list의 개수 [5, 50, 50, 70, 80, 100], [7, 100, 95 ... 50], [9, 100, 99 ... 91]
#      \n 뒤의 숫자는 해당 list의 숫자 개수를 뜻함 [5, 50, 50, 70, 80, 100] >> 50, 50, 70, 80, 100 (5개)
#      평균 구하기 / 평균보다 큰 숫자들 count하기 / 평균보다 큰 숫자들 비율 구하기

#     ex_input = '5\n5 50 50 70 80 100\n7 100 95 90 80 70 60 50\n3 70 90 80\n3 70 90 81\n9 100 99 98 97 96 95 94 93 91'
#     ex_output = '40.000%\n57.143%\n33.333%\n66.667%\n55.556%'

# while True:
    
#     divi = int(input())
#     nums = list(map(int,input().split()))
#     nums_ave = sum(nums) / divi
#     count = 0
#     for num in nums:
        
#         if num > nums_ave:
#             count +=1
#     prt = count / len(nums) * 100 
#     print('{0}%'.format(prt))



