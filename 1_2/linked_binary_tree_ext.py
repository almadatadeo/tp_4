from linked_binary_tree_abstract import LinkedBinaryTreeExtAbstract
from data_structures import BinaryTreeNode, LinkedBinaryTree
from typing import Iterable, Any, List, Optional
from data_structures import LinkedQueue

class LinkedBinaryTreeExt(LinkedBinaryTreeExtAbstract, LinkedBinaryTree):

    def __iter__(self) -> Iterable[Any]:
        queue = LinkedQueue()
        queue.enqueue(self._root)

        while not queue.is_empty():
            current = queue.first()

            yield current

            if current.left_child:
                queue.enqueue(current.left_child)

            if current.right_child:
                queue.enqueue(current.right_child)

            queue.dequeue()

    def __eq__(self, other):
        return self.element == other.element


    def ancestro_mas_inmediato(self, nodo1: BinaryTreeNode, nodo2: BinaryTreeNode) -> BinaryTreeNode:
        pass

    def hojas(self) -> List[Any]:
        lista: List[Any] = []
        for e in self:
            if not e.left_child and not e.right_child:
                lista.append(e)
        return lista


    def nivel(self, nodo: BinaryTreeNode) -> int:
        """Busca el nodo pasado por parámetro en el árbol y si lo encuentra
        Retorna su nivel. El nivel del nodo raíz es 0 el nivel de los hijos
        de la raíz es 1 y así sucesivamente.
        Args:
        nodo (BinaryTreeNode): nodo del que se quiere conocer su nivel.
        Returns:
        List[Any]: lista formada por los elementos de los nodos hoja.
        """
        pass
        


    def diametro(self) -> int:
        """Indica el diámetro o ancho máximo de un árbol.
        El ancho máximo es la cantidad máxima de nodos que hay en un mismo nivel del árbol.
        Returns:
        int: devuelve la máxima cantidad de nodos entre todos los niveles que conforman el árbol.
        """
        pass

    def es_balanceado(self) -> bool:
        actual = self._root
        izq = 0
        while actual:
            if actual.left_child:
                izq = izq + 1
            actual = actual.left_child

        actual = self._root
        der = 0
        while actual:
            if actual.right_child:
                der = der + 1
            actual = actual.right_child
        
        if( 1 > (izq - der) > -1 ):
            return True
        else:
            return False


