import java.util.*;

public class Main {
    public static void main(final String[] args) {

        testExercicio1();
        // testExercicio2();
        // testExercicio3();

    }

    public static void testExercicio1() {

        SinglyLinkedList<Integer> list = new SinglyLinkedList<Integer>();

        list.addLast(4);
        list.addLast(47);
        list.addLast(0);
        list.addLast(47);
        list.addLast(3);

        System.out.println(list);

        list.posicion();
        // list.deleteDuplicates();

        System.out.println(list);
    }
}

class SinglyLinkedList<T extends Comparable> {
    private Node<T> first; // Primero nodo de la lista
    private int size; // Tamano de la lista

    // Constructor (crea lista vacia)
    SinglyLinkedList() {
        first = null;
        size = 0;
    }

    // Retorna el tamano de la lista
    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return (size == 0);
    }

    public void addLast(T v) {
        Node<T> newNode = new Node<T>(v, null);
        if (isEmpty()) {
            first = newNode;
        } else {
            Node<T> cur = first;
            while (cur.getNext() != null)
                cur = cur.getNext();
            cur.setNext(newNode);
        }
        size++;
    }

    public String toString() {
        String str = "{";
        Node<T> cur = first;
        while (cur != null) {
            str += cur.getValue();
            cur = cur.getNext();
            if (cur != null)
                str += ",";
        }
        str += "}";
        return str;
    }

    // Encontrar posicion
    /*
     * list.addLast(47);
     * list.addLast(89);
     * list.addLast(47);
     * list.addLast(56);
     * list.addLast(56);
     */
    public void posicion() {
        int cont = 1;
        int cont2 = 0;
        Node<T> auxiliar = first;
        Node<T> auxiliar2 = first;

        while (auxiliar.getNext() != null) {
            while (auxiliar2.getNext() != null) {
                System.out
                        .println("fuera: " + auxiliar.getValue() + "//" + auxiliar2.getNext().getValue() + "//" + cont);

                if (auxiliar.getValue().compareTo(auxiliar2.getNext().getValue()) == 0) {
                    System.out.println(auxiliar.getValue() + "//" + auxiliar2.getNext().getValue() + "//" + cont);
                    cont2++;
                    size--;
                    System.out.println("valor de aux2: " + auxiliar2.getValue());
                    auxiliar2.setNext(auxiliar2.getNext().getNext());
                    // auxiliar2 = auxiliar2.getNext().getNext();
                    System.out.println("valor de aux2: " + auxiliar2.getValue());
                    break;
                }
                if (cont2 != 0)
                    break;

                auxiliar2 = auxiliar2.getNext();// recorre segundo while
                cont++;
            }
            cont = 1;
            auxiliar2 = auxiliar.getNext();

            auxiliar = auxiliar.getNext();// recorre segundo while

        }

    }
    // Elimina aquellos nodos de la lista que esten duplicados
    /*
     * public void deleteDuplicates() {
     * Node<T> auxiliar = null;
     * }
     */
}

class Node<T> {
    private T value; // Valor guardado en el nodo
    private Node<T> next; // Referencia para el proximo nodo de la lista

    // Constructor
    Node(T v, Node<T> n) {
        value = v;
        next = n;
    }

    // Getters e Setters
    public T getValue() {
        return value;
    }

    public Node<T> getNext() {
        return next;
    }

    public void setValue(T v) {
        value = v;
    }

    public void setNext(Node<T> n) {
        next = n;
    }
}