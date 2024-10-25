from array_heap_ext_abstract import ArrayHeapExtAbstract
from data_structures import ArrayHeap
from typing import Any

class ArrayHeapExt(ArrayHeapExtAbstract, ArrayHeap):
    def fusionar(self, otro: ArrayHeap) -> None:

        ## En este caso borra todos los elementos del otro heap pasado por parámetro
        ## Si se quisiera utilizar el otro heap se podría hacer de la siguiente manera

        #otro2 = ArrayHeapExt()
        #for e in range(0, len(otro)):
        #    otro2.add(e)

        ## y debajo utilizar otro2 en vez de otro.

        if not otro.is_empty() and not self.is_empty():
            for _ in range(len(otro._data)):
                item = otro.remove_min()
                self.add(item[0], item[1])
        else:
            raise Exception("Uno o ambos heaps vacíos.")

    def vaciar(self) -> None:
        """ Una vez invocado el Heap queda sin elementos. """
        if not self.is_empty():
            for _ in range(len(self._data)):
                self.remove_min()
        else:
            raise Exception("Heap vacío.")
        
    def eliminar_por_prioridad(self, k: Any) -> None:
        """ Elimina el elemento con prioridad igual al parámetro k.
        Luego de ser invocado la estructura debe preservar la condición de orden
        Args:
        k (Any): prioridad del elemento a eliminar.
        """

        for i in range(len(self._data)):
            if self._data[i]._key == k:
                index = i
                break
        if index is None:
            raise Exception("No existe elemento que desea eliminar.")
        else:
            self._swap(index, len(self._data) - 1)
            self._data.pop()

            self._upheap(index)
            self._downheap(index)


    def cambiar_prioridad(self, k_actual: Any, k_nueva: Any) -> None:
        """ Cambia la prioridad de los nodos con prioridad igual k_actual y establece como nueva prioridad k_nueva.
        Args:
        k_actual (Any): prioridad actual del elemento a modificar
        k_nueva (Any): nueva prioridad que debe ser asignada.
        """
        for i in range(len(self._data)):
            if self._data[i]._key == k_actual:
                index = i
                break
        self._data[index]._key = k_nueva
        self._upheap(index)
        self._downheap(index)