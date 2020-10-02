# cook your dish here
#minimum number of operation required to convert one tuple to another
def calculate():
    oper = []
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    e = []
    d = []
    count = 0
    for i in range(3):
        e.append(a[i])
        d.append(b[i])
    m = 0
    c = 0
    op = 0
    flag = 0

    for i in range(3):
        if(a[i]!=b[i]):
            if(a[i]>b[i]):
                c = a[i]-b[i]
                b[i] = b[i] + c
                flag = flag + 1
                for i in range(3):
                    if(a[i]!=b[i]):
                        flag = flag + 1
                if(flag>0):
                    op = op + 1
                    flag = 0
            else:
                c = b[i]-a[i]
                a[i] = a[i] + c
                flag = flag + 1
                for i in range(3):
                    if(a[i]!=b[i]):
                        flag = flag + 1
                if(flag>0):
                    op = op + 1
    for i in range(3):
        if(a[i]==b[i]):
            count = count + 1
    if(count==3):
        oper.append(op)

    m = 0
    c = 0
    op = 0
    flag = 0
    count = 0
    a = []
    b = []
    for i in range(3):
        a.append(e[i])
        b.append(d[i])
    for i in range(3):
        if(a[i]!=b[i]):
            if(a[i]>b[i]):
                if(a[i]%b[i]==0):
                    m = a[i]//b[i]
                    b[i] = b[i]*m
                    flag = flag + 1
                    for i in range(3):
                        if(a[i]!=b[i]):
                            if(b[i]*m==a[i]):
                                b[i]= b[i]*m
                                flag = flag + 1
                if(flag>0):
                    op = op + 1
                    flag = 0
            else:
                if(b[i]%a[i]==0):
                    m = b[i]//a[i]
                    a[i] = a[i]*m
                    flag = flag + 1
                    for i in range(3):
                        if(a[i]!=b[i]):
                            if(a[i]*m==b[i]):
                                a[i]= a[i]*m
                                flag = flag + 1
                if(flag>0):
                    op = op + 1
                    flag = 0
    for i in range(3):
        if(a[i]==b[i]):
            count = count + 1
    if(count==3):
        oper.append(op)


    m = 0
    c = 0
    op = 0
    flag = 0
    count = 0
    a = []
    b = []
    for i in range(3):
        a.append(e[i])
        b.append(d[i])
    for i in range(3):
        if(a[i]!=b[i]):
            if(a[i]>b[i]):
                if(a[i]%b[i]==0):
                    m = a[i]//b[i]
                    b[i] = b[i]*m
                    flag = flag + 1
                    for i in range(3):
                        if(a[i]!=b[i]):
                            if(b[i]*m==a[i]):
                                b[i]= b[i]*m
                                flag = flag + 1
                    if(flag>0):
                        op = op + 1
                        flag = 0
                else:
                    c = a[i]-b[i]
                    b[i] = b[i] + c
                    flag = flag + 1
                    for i in range(3):
                        if(a[i]!=b[i]):
                            if(b[i]+c==a[i]):
                                b[i]= b[i] + c
                                flag = flag + 1
                    if(flag>0):
                        op = op + 1
                        flag = 0
            else:
                if(b[i]%a[i]==0):
                    m = b[i]//a[i]
                    a[i] = a[i]*m
                    flag = flag + 1
                    for i in range(3):
                        if(a[i]!=b[i]):
                            if(a[i]*m==b[i]):
                                a[i]= a[i]*m
                                flag = flag + 1
                    if(flag>0):
                        op = op + 1
                        flag = 0
                else:
                    c = b[i]-a[i]
                    a[i] = a[i] + c
                    flag = flag + 1
                    for i in range(3):
                        if(a[i]!=b[i]):
                            if(a[i]+c==b[i]):
                                a[i]= a[i] + c
                                flag = flag + 1
                    if(flag>0):
                        op = op + 1
                        flag = 0
    
    for i in range(3):
        if(a[i]==b[i]):
            count = count + 1
    if(count==3):
        oper.append(op)               

    
    return min(oper)             
                


T = int(input())
listf= []
for i in range(T):
    p = calculate()
    listf.append(p)
for ele in listf:
    print(ele)
    
