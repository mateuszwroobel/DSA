#wezel drzewa odpowiada za liczbe wartosci i-j w drzewie

def createSortedArray(instructions):
    left = lambda i: 2*i+1
    right = lambda i: 2*i+2
    parent = lambda i: (i-1)//2
    
    class SegmentTree():
        def __init__(self,n):
            self.leaves = 1
            while self.leaves < n:
                self.leaves*=2

            self.heap = [0] * (2 * self.leaves + 1)
            #build
            # for i in range(n):
            #     self.heap[self.leaves - 1 + A[i]] += 1

        def update(self,i):
            #parametry: i - liczba ktora dodaje do drzewa
            k = self.leaves - 1 + i
            while k >= 0:
                self.heap[k] += 1
                k = parent(k)

        def _sum(self,node,node_low,node_high,i,j):
            #node - liczba liczb w przedziale node_low - node_high
            #Szukamy ile jest liczb w przedziale z zakresu i-j
            #Case 1: Brak przeciecia
            if j < node_low or i > node_high:
                return 0
            #Case 2: Node_low i node_high w calosci sie zawieraja w i , j
            if i <= node_low and node_high <= j:
                return self.heap[node]
            #Case 3:
            mid = (node_low + node_high)//2
            sum_left = self._sum(left(node), node_low, mid, i, j)
            sum_right = self._sum(right(node), mid+1, node_high, i, j)
            return sum_left + sum_right

        def sum_query(self,i,j):
            return self._sum(0, 0, self.leaves - 1, i, j)

    n = len(instructions)
    st = SegmentTree(max(instructions)+1)
    cost = 0
    for i in range(n):
        st.update(instructions[i])
        num_of_smaller = st.sum_query(0, instructions[i]-1)
        num_of_bigger = st.sum_query(instructions[i]+1, max(instructions))
        cost += min(num_of_smaller, num_of_bigger)

    return cost


print(createSortedArray([1,5,6,2]))