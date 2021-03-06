import random
import time

#求解一个二行列式的值，例如
'''
|1 1 1|
|0 3 3| = 27
|0 0 9|
'''
#_______________辅助函数____________________
#求阶乘
def jiec(self):
    if self==0 or self==1:
        jienum=1
    else:
        jienum=self*jiec(self-1)
    return jienum
#————————————————阶乘求逆，谁的阶乘是这个数—————
#一个数，找到这个数是谁的阶乘
def jiecn(jiec,a=1,i=0):
    if jiec==0 or jiec==1:
        return i+1
    if jiec==2:
        return jiec

    for i in range(1,jiec):

        a*=i
        if (a==jiec):
             break
    if a==jiec:
        return i
    else:
        print('这个数是哪家的阶乘出来的，我找不到啊！')
#________________判断逆序数__________________
#判断一个序列的逆序数
def pdnxs(listp=[],count=0):
    for i in range(len(listp)):
        for j in range(i,len(listp)):
            if listp[i]>listp[j]:
                count+=1
    return count

#________把两个二级级嵌套列表，对列个列表里边的，次级列表进行匹配____________________
###________________________做成索引________________________________________
####______________这两个列表具有n！个次级列表，每个次级列表具有n个元素______________
def jiehe(list1=[],list2=[],list3=[],list4=[],n=0):
    nj = len(list1)  # 具有n！个次级列表的，列表的的阶数
    n =jiecn(nj)
    for i in range(nj):
        for j in range(n):
            list3.append(list1[i][j])
            list3.append(list2[i][j])
    a = 0
    b = 2*n
    for i in range(0, 2*nj*n, 2*n): #切几刀需要nj刀，在哪里切，切多长
        list4.append(list3[a:b])
        a += 2*n
        b += 2*n
    return list4
#_______________把一个1~n的列表全排列，并给出所有结果,结果其实是0~n-1的,不影响_________________________
###########————————————————此技术可结合字典产生大自然的馈赠——————————————#####################_____
def sjlb(n=5,list3=[],list3_1=[],list4=[],count1=0):
    print('执行函数：sjlb')
    nj =jiec(n)
    for i3 in range(n):
        list3_1.append(i3)

    while count1!=nj:
        random.shuffle(list3_1)
        list3=list3_1[:]
        if (list3 not in list4):
            list4.append(list3)
            count1 += 1
            print('第{0}种可能{1}'.format(count1, list3))
            print('进度{0}/{1},{2:.4f}%'.format(count1, nj, ((count1 / nj) * 100)))
        #print(list4)

    print('sjlb执行完毕！')
    print('全排列共有n！次中可能，本次共有{0}个元素，所以有{1}种结果'.format(n,count1))
    return list4
#_______________n！种全排列前提函数和输出函数详情见sjlb_________________________________
######——————————————————结合字典，来一起感谢大自然的馈赠————————————————————#########___
def plhs(list1=[],list2=[]):
    ##需要把hlsvalu里面的list2传进来,，为list1，这是一,1~n的列表长度为n
    # ##____构建一个未来为了存储每一种结果的空容器list2
    n = len(list1)
    # for i2 in range(jiec(n)):
    #     list2.append([])
    ##__在一个range里面的任意一个数，并把每n组数变成列表sjlb.list3,把n！组sjlb.list3存到一个列表中list3
        #####产生一个列表sjlb.list3,要求里面的元素不能重复，可用哈希算法检索，判断哈希列表中没有0，0标志有一个没有,即有重复
           #第二个要求，sjlb.list3,数量要
            #第三个要求list3里面元素不能重复
    #调用sjlb函数
    list2=sjlb(n)
    return list2


#————————————————————主函数————————————————————————
def hlsvalue(list1=[],list2=[],list2_1=[],list3=[],list4=[],list5=[],list5_1=[],list6=[],
             list7=[],list7_1=[],list8=[],value11=0
            ,hlssumx=1,i8nixshu=0,n=0,nj=0):

    #第一步__对传入的行列式list1进行特征提取，不要在循环里面各算一次，浪费时间
    n=len(list1)#行列式的阶数
    nj=jiec(n)

    #第二步__产生一个1~n的列表list2,用这个列表为母体，产生出n！个不同的全排列
    for i2 in range(n):
        list2.append(i2)

    #第三步__利用上1~n的列表list2,产生1~n之间排列的所有可能共有n!个，每种可能为list3的次级列表，放入list3
    ###_____本部分较为复杂写plhs(list2),返回list3___###
    #调用plhs，plhs调用sjlb函数
    list3=plhs(list2)

    #第四步__计算出所有排列的逆序数,共n！个，放入列表list4
    for i4 in range(nj):
        list4.append(pdnxs(list3[i4]))

    #第五步__产生一个嵌套列表里面有n！个1~n的的次级列表，这个列表为list5
    for i5 in range(nj):
        for j5 in range(n):
            list5_1.append(j5)
        list5.append(list5_1)
        list5_1=[]

    #第六步__把list3的次级列表和list5的次级列表结合,做成list1的索引，放入list6中
    ### 调用结合函数
    list6=jiehe(list5,list3)

    #第七步__通过索引list6找出list1中的值的n!种组合，以列表的形式放入list7,list7包含n！个次级列表
    for i7 in range(nj):
        for j7 in range(n):
            list7_1.append(list1[list6[i7][2 * j7]][list6[i7][2 * j7 + 1]])
        list7.append(list7_1)
        list7_1 = []

    #第八步__把每种组合里面的数相乘后,乘以这个组合的逆序数放入列表list8中
    for i8 in range(nj):
        i8nixshu=list4[i8]
        for j8 in range(n):
            hlssumx *= list7[i8][j8]
        hlssumx*=(-1)**i8nixshu
        list8.append(hlssumx)
        hlssumx=1
    #第九步__对list8中的数求和为value11
    value11=sum(list8)

    return value11



if __name__=='__main__':
    #程序开始时间定点
    startime = time.perf_counter()
    list1=[[1,2,1],
           [0,1,1],
           [200,0,1]]
    list2=[[6,2,3,4,5],
           [0,2,3,4,5],
           [0,0,90,4,5],
           [0,0,1,4,5],
           [0,0,0,0,50]]
    list3=[[6,2,3,4,5,9],
           [0,2,3,4,5,9],
           [0,0,90,4,5,9],
           [0,0,1,4,5,9],
           [0,0,0,0,50,9],
           [1,10,2,3,4,8]]
    list4 = [[6, 2, 3, 4, 5, 9, 8],
             [0, 2, 3, 4, 5, 9, 7],
             [0, 0, 90,4, 5, 9, 6],
             [0, 0, 1, 4, 5, 9, 5],
             [0, 0, 0, 0, 50,9, 4],
             [1, 10,2, 3, 4, 8, 3],
             [1, 2, 1, 5, 2, 6, 2]]
    list5 = [[6, 2, 3, 4, 5, 9, 8, 9],
             [0, 2, 3, 4, 5, 9, 7, 9],
             [0, 0, 90, 4, 5, 9, 6, 8],
             [0, 0, 1, 4, 5, 9, 5, 7],
             [0, 0, 0, 0, 50, 9, 4, 8],
             [1, 10, 2, 3, 4, 8, 3, 9],
             [1, 2, 1, 5, 2, 6, 2, 8],
             [1, 4, 2, 7, 4, 9, 3, 7]]
    #print('行列式：{}.行列式值：'.format(list1),hlsvalue(list1))
    #print('行列式：{}.行列式值：'.format(list2),hlsvalue(list2))
    #print('行列式：{}\n行列式值：'.format(list3), hlsvalue(list3))
    #print('行列式：{}\n行列式值：'.format(list4), hlsvalue(list4))
    print('行列式：{}\n行列式值：'.format(list5), hlsvalue(list5))
    #程序结束时间定点
    endtime = time.perf_counter()
    dur = endtime - startime
    print('程序运行时间：', dur,'s')
    #另一种计时方式
    print('time.process_time()程序运行时间：', time.process_time(),'s')
    #枚举的方法对7阶行列式还是可以的，用时80s，对8以上就耗时表较多，时间复杂度O(2**n)以上

    # list6 = [[1, 2, 3], [1, 2, 4], [1, 1, 2]]
    # print('行列式：{}\n行列式值：'.format(list6), hlsvalue(list6))