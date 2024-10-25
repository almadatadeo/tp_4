from array_heap_ext import ArrayHeapExt
arrHeap = ArrayHeapExt()


#### Array Heap ####
# Orden alfabético #

arrHeap.add(5, "A")
arrHeap.add(2, "B")
arrHeap.add(20, "B")
arrHeap.add(4, "C")
arrHeap.add(14, "E")
arrHeap.add(9, "F")
arrHeap.add(12, "H")
arrHeap.add(25, "J")
arrHeap.add(15, "K")
arrHeap.add(10, "L")
arrHeap.add(7, "Q")
arrHeap.add(11, "S")
arrHeap.add(8, "W")
arrHeap.add(16, "X")
arrHeap.add(6, "Z")



#### Otro Array Heap ####
##### para pruebas ######

arrHeap2 = ArrayHeapExt()
arrHeap2.add(3, "AA")
arrHeap2.add(10, "BB")
arrHeap2.add(4, "CC")
arrHeap2.add(1,"DD")
arrHeap2.add(23, "EE")
arrHeap2.add(11, "FF")
arrHeap2.add(9, "GG")
arrHeap2.add(2, "HH")

## FUSIONAR ##
arrHeap.fusionar(arrHeap2)


## ELIMINAR POR PRIORIDAD ## 
arrHeap.eliminar_por_prioridad(3)


## MODIFICAR PRIORIDAD ## 
arrHeap.cambiar_prioridad(10, 22)

## VACIAR ##
arrHeap.vaciar()









