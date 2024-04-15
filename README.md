# Zadania programistyczne nr 6

> Można korzystać z funkcji pomocniczych!

Węzeł drzewa binarnego jest zdefiniowany w następujący sposób:

```python
class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

W węzłach drzew znajdują się liczny całkowite z przedziału [-1000, 1000].

Zaimplementuj zadania 1-4 korzystając z zamieszczonego kodu i uzupełniając brakujące jego fragmenty oznaczone komentarzem `#TODO`. Pobierz plik dotyczący danego zadania, uzupełnij brakujące fragmenty kodu i prześlij ten plik na UPEL tak jak do tej pory.

### Zad.1. (15pkt)

Mając dane 2 korzenie drzew binarnych `root1` i `root2`, zwróć scalone drzewo. W tym celu zaimplementuj metodę `merge_trees(root1: Optional[Node], root2: Optional[Node])-> Optional[Node]`, która przyjmuje dwa korzenie i zwraca korzeń scalonego drzewa.

**Przebieg procesu scalania:**

Wyobraź sobie, że umieszczasz drzewa `root1` i `root2` jedno na drugim. Niektóre węzły obu drzew się pokryją, podczas gdy inne nie. Zadanie polega na scaleniu obu drzew w nowe drzewo binarne. Zasada scalania jest taka, że jeśli dwa węzły się pokrywają, to wartości węzłów się sumują jako nowa wartość scalonego węzła. W przeciwnym razie zostanie użyty niepusty węzeł jako węzeł nowego drzewa. Proces scalania musi się rozpocząć od korzeni obu drzew.

Dodatkowo zaimplementuj funkcję `display_preorder(root: Optional[Node])` do wyświetlania przechodzenia drzewa metodą pre-order. Metoda ta przyjmuje korzeń drzewa root i odwiedza wszystkie jego węzły metodą pre-order, wyświetlając ich wartości oddzielone od siebie spacjami.

**Przykład 1:**

```
Drzewo 1      Drzewo 2      Scalone Drzewo
    1             2              3
   / \           / \            / \
  3   2         1   3          4   5
 /               \   \        / \   \
5                 4   7      5   4   7

```

**Przykład 2:**

```
Drzewo 1      Drzewo 2      Scalone Drzewo
    0             2              2
   /             / \            / \
  3            -3   3          0   3
 /                            /
5                            5

```

### Zad.2. (15pkt)

Dane jest drzewo binarne z korzeniem `root`. Zadanie polega na przejściu drzewa poziomami od korzenia w dół, od lewej do prawej i zapisać proces przechodzenia drzewa

W tym celu zaimplementuj metodę `get_level_order(root: Optional[Node]) -> List[List[int]]`, która przyjmuje korzeń drzewa i zwraca listę list (`List[List[int]]`), która reprezentuje proces przechodzenia drzewa. Zewnętrzna lista reprezentuje kolejne poziomy, a wewnętrzne listy reprezentują kolejne wartości węzłów na danym poziomie.

**Przykład 1:**

```
root:
    3
   / \
  9  20
    /  \
   15   7

Output: [[3],[9,20],[15,7]]
```

**Przykład 2:**

```
root:
    1
   / \
  2   3
     / \
    4   5

Output: [[1],[2,3],[4,5]]

```

### Zad.3. (20pkt)

Dany jest korzeń drzewa BST `root` oraz wartości dwóch węzłów znajdujących się w tym drzewie (`p` i `q`). Znajdź najniższego wspólnego przodka węzłów `p` i `q`.

W tym celu zaimplementuj metodę `get_lowest_common_ancestor(root: Optional[Node], p: int, q: int) -> int`, która zwróci wartość najniższego wspólnego przodka dla węzłów o wartościach `p` i `q.`

Najniższy wspólny przodek między dwoma węzłami p i q jest najniższym węzłem w drzewie, który ma zarówno p, jak i q jako potomków. Zakładamy, że węzeł może być potomkiem samego siebie.

Przyjmij, że następujące założenia są spełnione:

- wszystkie wartości węzłów w drzewie `root` są unikatowe
- drzewo `root` zawiera wartości `p` i `q`
- p ≠ q

Przykład 1:

```
p = 2, q = 8
root:
         6
      /    \
     2      8
    / \    / \
   0   4  7   9
      / \
     3   5

Output: 6
Najniższy wspólny przodek węzłów 2 i 8 to węzeł 6.
```

**Przykład 2:**

```
p = 1, q = 6
root:
         5
      /    \
     3      8
    / \    / \
   2   4  7   9
      / \
     1   6

Output: 4
Najniższy wspólny przodek węzłów 1 i 6 to węzeł 4.
```

**Przykład 3:**

```
p = 1, q = 4
root:
         5
      /    \
     3      8
    / \    / \
   2   4  7   9
      / \
     1   6

Output: 4
Explanation: Najniższy wspólny przodek węzłów 1 i 4 to węzeł 4.

```

### Zad.4. (25pkt)

Dane jest drzewo binarne o korzeniu `root` oraz liczba całkowita `target`. Zwróć `true`, jeśli istnieje taka ścieżka w tym drzewie od korzenia do liścia, taka że suma wszystkich wartości wzdłuż tej ścieżki jest równa `target`. W tym celu zaimplementuj metodę `has_path_sum(root: Optional[Node], target: int) -> bool`, która dla danych `root` oraz `target` zwróci `true` jeżeli taka ścieżka istnieje oraz `false` w przeciwnym wypadku.

**Przykład 1:**

```
target = 22
root:

       5
      / \
     4   8
    /   / \
   11  13  4
  /  \      \
 7    2      1

Output: true

Ścieżka: 5 -> 4 -> 11 -> 2
Suma wartości na tej ścieżce wynosi 22, co odpowiada wartości target.
```

**Przykład 2:**

```
target = 5
root:
    1
   / \
  2   3

Output: false
W drzewie nie ma żadnej ścieżki od korzenia do liścia, której suma wartości wynosiłaby 5.
```

**Przykład 3:**

```
target = 38
root:
     3
    / \
   9  20
     /  \
    15   7

Output: true
Ścieżka: 3 -> 20 -> 15
Suma wartości na tej ścieżce wynosi 38, co odpowiada target.

```
