#Given a list of integers, check if the sum of any two integers in the list is not contained in the list.
#For example with the list [4, 5, 15, 2, 8], there is no pair of integers where their sum is in the list. The list [8, 7, 5, 3] does not satisfy the criteria since the sum of 5 and 3 is in the list.
#Write a python function which takes a list of integers and returns True if the list satisfies the criteria above, or False otherwise.
import cProfile
import timeit
def sum(numList):
    hash_table={}
    for i in range(len(numList)):    
        hash_table[numList[i]]=i

    for i in range(len(hash_table)):
        for j in range(i+1, len(hash_table)):
            if numList[i]+numList[j] in hash_table:
                return False
      
    return True

list1= [4,5,15,3,8]
print(sum(list1))

def bruteforce(numList):
    for i in range(len(numList)):
        for j in range(i+1, len(numList)):
            if numList[i] + numList[j] in numList:
                return False
        
    return True
#print(bruteforce(list1))

#cProfile.run('bruteforce(list1)', sort='time')
#cProfile.run('sum(list1)', sort='time')