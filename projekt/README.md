Autor: Patrycja Trojan,                    Kraków, 23.01.2022r.
---------------------------------------------------------------

---------------------------------------------------------------

Katalog projektu powinien zawierać:

1) "bst.py" - plik źródłowy klasy BinarySearchTree będącej
    reprezentacją binarnego drzewa poszukiwań

2) "node.py" - plik źródłowy klasy Node będącej reprezentacją
    pojedynczego węzła w drzewie

3) "test.py" - plik źródłowy z klasą testującą metody będące
    elementami klasy BinarySearchTree

---------------------------------------------------------------

Aby uruchomic program testujący, należy użyć w terminalu
polecenia:

python3 test.py

---------------------------------------------------------------

Klasa Node:
-----------

Atrybuty:
* left - łącze do lewego potomka
* right - łącze do prawego potomka
* parent - łącze do rodzica

---------------------------------------------------------------

Klasa BinarySearchTree:
-----------------------

Atrybuty:
* root - łącze do korzenia
* size - liczba węzłów w drzewie

Metody:
* is_empty() - zwraca True, jeśli w drzewie nie ma żadnych 
    elementów lub False, jeśli drzewo zawiera jakieś elementy
* insert(...) - metoda przyjmująca jako argument wywołania 
    wartość, która ma zostać wstawiona do drzewa i która przy
    pomocy rekurencyjnej funkcji insert_rek(...) wstawia tę
    wartość do drzewa
* inorder() - metoda, która przy pomocy rekurencyjnej funckji
    inorder_rek(...) przechodzi przez drzewo i wypisuje wartości
    w nim zawarte w kolejności inorder (lewy potomek - rodzic -
    prawy potomek)
* minValue() - metoda wyszukująca węzęł z najmniejszą wartością
    w drzewie i zwracająca łącze do niego
* delete(...) - metoda przyjmująca jako argument wartość, którą
    należy usunąć z drzewa i która robi to za pomocą funckji 
    rekurencyjnej delete_rek(...)
* search(...) - metoda, która za pomocą funckji search_rek(...)
    wyszukuje podaną jako argument wartość w drzewie i zwraca 
    łącze do węzła z tą wartościa
* dsw() - metoda, która za pomocą funckji tree_to_vine(...),
    vine_to_tree(...) oraz compress(...) dokonuje procesu
    zrównoważenia drzewa tak, by jego wysokość była rzędu
    O(log(size)). Algorytm równoważenia wykonuje się w dwóch 
    krokach:
    1) Przejście z drzewa początkowego do tzw. kręgosłupa (wszystkie
    elementy znajdują się w jednej prawej gałęzi drzewa) za
    pomocą rotacji prawych wykonywanych na lewych potomkach węzłów
    drzewa przechodzonego wzdłuż jego prawej krawędzi
    2) Przejście z kręgosłupa z powrotem do drzewa (już
    zrównoważonego) za pomocą rotacji lewych wykonywanych na co
    drugim węźle podczas wielokrotnego przechodzenia drzewa
    wzdłuż jego prawej krawędzi
* reset() - metoda, która ustawia atrybut root na None, a size
    na wartość 0 (brak węzłów w drzewie)


---------------------------------------------------------------