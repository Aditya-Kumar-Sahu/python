
def insertion_sort(array):
    for i in range(1,len(array)):
        temp=array[i]
        j=i-1
        while j>-1 and temp<array[j]:
            array[j+1]=array[j]
            j-=1
        array[j+1]=temp
        print(array)
            

def delete_item(array,item):
    '''
    to delete an item from an array.
    '''
    for i in range(len(array)):
        if array[i]==item:
            loc=i
            
            for index in range(loc,len(array)-1):
                array[index]=array[index+1]
                
            array.pop()
            print(item,'deleted successfully.')
            break
    else:
        print(item,"not found.")


def  selection_sort(array):
    '''
    to sort an array by selection sort method.
    '''
    for i in range(len(array)-1):
        min_loc=i
        for j in range(i+1,len(array)):
            if array[j]<array[min_loc]:  # for ascending order
                min_loc=j
        array[i],array[min_loc]=array[min_loc],array[i]
        print(array)
    print("Array sorted successfully.")


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j+1] < array[j]:
                array[j+1],array[j]=array[j],array[j+1]
                print(array)
    print("Array sorted successfully.")


def simple_merge(a,b):
    a.extend(b)
    return a


def sort_merge(a,b):
    c=[]
    i,j=0,0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        
        else:
            c.append(b[j])
            j+=1
            
    else:
        for element in a:
            if element not in c:
                c.append(element)
                
        for element in b:
            if element not in c:
                c.append(element)
    print("Merging successful.")
    return c
            
#------------------main--------------------
# a=[1,3,7,9,11,13]
# b=[2,6,8,10]
# print(sort_merge(a, b))

# print("Orignal Array:",l)
# insertion_sort(l)
# print("Sorted Array: ",l)