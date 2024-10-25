from sorted_priority_queue import SortedPriorityQueue

############ INIT ############

PCola = SortedPriorityQueue()

############ ADD ############

PCola.add(1, "1#1") 
PCola.add(1, "1#2") 
PCola.add(2, "2#3")
PCola.add(2, "2#4")
PCola.add(3, "3#5")
PCola.add(3, "3#6")
PCola.add(4, "4#7")
PCola.add(4, "4#8")

print("############ LEN ############")
print(len(PCola))


print("############ IS_EMPTY ############")
print(PCola.is_empty())

print("############ MIN ############")
print(PCola.min())

print("############ REMOVE_MIN ############")
print(PCola.remove_min())

print("############ STR ############")
print(str(PCola))