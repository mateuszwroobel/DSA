from zad3testy import runtests

#ttaktuje lampki jako liscie dzrzewa przedzialowego
def lamps(n, T):
    left = lambda i: 2*i + 1
    right = lambda i: 2*i + 2
    parent = lambda i: (i-1)//2

    class SegmentTree():
        def __init__(self, n):
            self.leaves = 1
            while self.leaves < n:
                self.leaves *= 2

            self.heap = [0] * (2 * self.leaves - 1)
            # liscie zaczynaja sie od self.leaves - 1
            # uzupelniam liscie tablicami [1,zielony]
            # musza byc mutowalne wiec wybieram liste a nie krotke

            for i in range(n):
                self.heap[self.leaves - 1 + i] = [0,"green"]

        def update(self,index):
            #paramtetry - index = oryginalny index z tablicy czyli u nas nr liscia
            #k - lisc odpowiednik
            k = index + self.leaves - 1
            if self.heap[k][1] == "green":
                self.heap[k][1] = "red"
                #nie musimy zmieniac sumy

            elif self.heap[k][1] == "blue":
                self.heap[k] = [0,"green"]
                k = parent(k)
                #zmienamy sume
                while k >= 0:
                    self.heap[k] -= 1
                    k = parent(k)
            else:
                #zapalamy lampke na niebieski
                self.heap[k] = [1,"blue"]
                k = parent(k)
                while k >= 0:
                    self.heap[k] += 1
                    k = parent(k)

        # def _sum(self,node, node_low, node_high, i, j):
        #     #zwracam sume w przedziale i - j
        #     #jestem w nodzie , ktory odpowiada za sume w przedziale node_low - node_high
        #
        #     #Case 1: Nie przecinaja sie
        #     if j < node_low or i > node_high:
        #         return 0
        #     #Case 2: przedzial node_low, node_high zawiera sie w calosci w i,j
        #     if i <= node_low and node_high >= j:
        #         #jesli lisc
        #         if node >= self.leaves - 1:
        #             return self.heap[node][0]
        #         else:
        #             return self.heap[node]
        #     else:
        #         #Case 3 przedzialy sie przecinaja
        #         mid = (node_low+node_high)//2
        #         left_sum = self._sum(left(node), node_low,mid,i,j)
        #         right_sum = self._sum(right(node),mid+1,node_high,i,j)
        #         return right_sum + left_sum
        #
        # def sum(self,i,j):
        #     return self._sum(0,0, self.leaves - 1, i, j)

    best = 0
    st = SegmentTree(n)
    for a,b in T:
        for lamp in range(a,b+1):
            #odpalam lampke
            st.update(lamp)

        best = max(best, st.heap[0])

    return best


runtests(lamps)
