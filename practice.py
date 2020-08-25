def stringunquie(string):
    uchars =set()
    for c in string:
        if c in uchars:
            return False
        uchars.add(c)
    return print("yes")
    
def repalceWhiteSpace(str1):
    b=str1.replace(" ","%20")
    return b

def isPaldrome(a):
    return a == a[::-1]

def checkPremutations(a,b):
    list1= len(a)
    list2=len(b)

    if(list1 != list2):
        return False
    
    sortList1=sorted(a)
    a= " ".join(sortList1)
    sortList2=sorted(b)
    b= " ".join(sortList2)

    for i in range(0, list1, 1): 
        if (a[i] != b[i]): 
            return False
  
    return True

def oneEdit(a,b):
    l1=len(a)
    l2=len(b)
    if l1 - l2 >1 or  l2 - l1 >1:
        return False
    i=0
    j=0
    diff = False
    while(i<l1 and j<l2):
        if i != j:
            if diff == False:
                diff = True
            if l1 == l2:
                i+=1
        else:
            j+=1
        j+=1
    return True

def compressin(string1):
    count=0
    res= ""
    res+=string1[0]

    for i in range(len(string1)-1):
        if string1[i] == string1[i+1]:
            count+=1
        else:
            if count >1:
                res += str(count)
            res+= string1[i+1]
            count =1
    if count >1:
        res += str(count)
    return res 

def rotation(s1,s2):
    for c in s1:
        if c.find(s2):
            return True
        else:
            return False
    
        
print(rotation("waterbottle","melon"))



#print(compressin("aaadddrree"))
# str1="pale"
# str2="bales"
# if oneEdit(str1,str2):
#     print("yes")

# else:
#     print("no")

#stringunquie("abccde")

# st1="abc"
# str2="cba"
# if(checkPremutations(st1,str2)):
#     print("yes")
# else:
#     print("no")

#print(repalceWhiteSpace("mr john smith")) 


# if(isPaldrome(st1)):
#     print("yes")
# else:
#     print("no")

