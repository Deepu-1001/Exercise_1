# we have already come across the loops in previous exercise 
#passing it into a funtion was not a big deal but i came across a
#difficulty or apeaking precisely error in output i read all 
#passing by argument in python too see fault in my code but it was just 
#just and indentation error i used resources like GFG and Realpython.com
my_list = [1,2,3,4,5,5,5,5,1]
unique_list =[]
def get_unique_list(list):
    temp_list = []
    for i in list:
        if i not in temp_list:
            temp_list.append(i)
            
    return temp_list

unique_list=get_unique_list(my_list)
print(unique_list)