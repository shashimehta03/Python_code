def checks(string):
    n=len(string)
    flag=0
    if n%2:
        mid=n/2
    else:
        mid= n
    start=0
    end= mid
    while(start <mid and end<n):
        if(string[start]== string[end]):
            start= start+1
            end= end+1
        else:
            flag=1
            break
    if flag==0:
        print("symmetrical")
    else:
        print("not symmetrical")

s= "abcabc"
print (s)
checks(s)
s2= "abcdab"
print(s2)
checks(s2)