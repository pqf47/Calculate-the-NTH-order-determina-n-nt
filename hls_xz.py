#利用行列式的性质1-4进行行列式的求解
import time
'''
|1 2 3|
|1 2 4|
|1 1 2|
'''
'''
0  3  6  9  12
'''
def HLS_XZ(list1=[],list2=[],list3=[],count1=0,sumsanjiao=0,product=1):
    n = len(list1)
    n1=n


    #如果行列式第n列全为0直接返回0
    flag1 = 0
    count3=n
    for i in range(n):
        if list1[i][count3-1]==0:
            pass
        else:
            flag1+=1
    if flag1 == 0:
        return 0

    #主分支
    else:
        while n >=2:

            # 如果行列式第n列全为0直接返回0
            flag3 = 0
            count5 = n
            for i in range(n):
                if list1[i][count5 - 1] == 0:
                    pass
                else:
                    flag3 += 1
            if flag3 == 0:
                return 0



            #对行列式进行调整，防止求list2，也就是k值时出现错误，零值错误
            #调整之后要对值进行取负
            #利用count可对（count，n）进行操作
            #flag可对是否为零，
            count1=n
            flag2=0
            count4=n
            for i in range(n):
                for j in range(count4-1):
                    if list1[i][count4-1]!=0:
                        flag2=i
            if list1[count1-1][count1-1]==0:
                    list3=list1[count4-1]
                    list1[count4-1]=list1[flag2]
                    list1[flag2]=list3
                    for i in range(n1):
                        list1[flag2][i]=-list1[flag2][i]

            #计算比例因子k
            for i in range(0,n-1):
                k1= list1[i][count1-1]/list1[count1-1][count1-1]
                list2.append(k1)
            print('list2',list2)

            #利用行列式某行（列）加上某行（列）乘以一个数在加到另一行（列）保持不变的性质
            print(list1)
            for i in range(n-1):
                for j in range(n):
                    list1[i][j]=list1[i][j]+(-1)*list2[i]*list1[count1-1][j]
            print(list1)

            #检查是否为下三角
            count2=0
            for i in range(n):
                for j in range(count2+1,n):
                    sumsanjiao+=list1[i][j]
                count2+=1
            if sumsanjiao==0 :
                break
            else:
                count2=0

            #中间变量初始化
            n-=1
            count1-=1
            list2=[]

    #计算求对角乘积，注意n已经变化，作个容器
    for i in range(n1):
        for j in range(n1):
            if i ==j:
                product*=list1[i][j]

    return product

if __name__ == '__main__':
    list1=[[1,2,3],[1,2,4],[1,1,2]]
    list2=[[0,0,0],[0,0,0],[0,0,0]]
    list3=[[1,2,0],[1,1,2],[0,0,1]]
    list4 = [[6, 2, 3, 4, 5, 9, 8],
             [0, 2, 3, 4, 5, 9, 7],
             [0, 0, 90, 4, 5, 9, 6],
             [0, 0, 1, 4, 5, 9, 5],
             [0, 0, 0, 0, 50, 9, 4],
             [1, 10, 2, 3, 4, 8, 3],
             [1, 2, 1, 5, 2, 6, 2]]
    list5 = [[6, 2, 3, 4, 5, 9, 8, 9],
             [0, 2, 3, 4, 5, 9, 7, 9],
             [0, 0, 90,4, 5, 9, 6, 8],
             [0, 0, 1, 4, 5, 9, 5, 7],
             [0, 0, 0, 0, 50,9, 4, 8],
             [1, 10,2, 3, 4, 8, 3, 9],
             [1, 2, 1, 5, 2, 6, 2, 8],
             [1, 4, 2, 7, 4, 9, 3, 0]]
    #value=HLS_XZ(list3)
    #value = HLS_XZ(list4)
    value = HLS_XZ(list5)
    print(value)
    print('time.process_time()程序运行时间：', time.process_time(),'s')
