# link - https://www.youtube.com/watch?v=AFYpNdN83Zg&list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs&index=40

def bubble_sort(data_list):
    for r in range(1,len(data_list)):
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]

def modified_bubble_sort(data_list):
    for r in range(1,len(data_list)):
        flag = False
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                flag = True
        if not flag:
            break


l =[23,25,31,22,11,10,5,98,68,1]
bubble_sort(l)
# modified_bubble_sort(l)
print(l)