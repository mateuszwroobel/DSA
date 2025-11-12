import heapq
#871
def minRefuelStops(target, startFuel, stations):
    # Ide po kolei po nastepnych stacjach dodajac, ilosc paliwa do kopca max,
    # gdy zabraknie mi paliwa to zdejmuje z kopca i dotankowuje je maksymalna wartoscia,
    # Zlozonosci:
    # push - O(log(n))
    # pop - O(1)
    # naprawienie struktury kopca - O(log(n))
    # W najgorszym wypadku wykonam "n" tych operacji, wiec zlozonosc calego algorytmu - O(nlogn)
    heap = []
    fuel = startFuel

    #mozna dojechac bez tankowania
    if fuel >= target: return 0

    #pomocnicza tablica
    station = [[0,startFuel]]
    for pos, f in stations:
        station.append([pos,f])
    station.append([target,0])
    n = len(station)
    cnt = 0

    for i in range(1,n):
        dist_tween_stations = station[i][0] - station[i-1][0]
        fuel_in_station = station[i][1]
        fuel -= dist_tween_stations

        while fuel < 0 and heap:
            get_fuel = heapq.heappop(heap)
            cnt+=1
            fuel += (-get_fuel)

        if fuel < 0:
            return -1

        heapq.heappush(heap,-fuel_in_station)

    return cnt


# target = 100
# stations = [[10,100]]
# startFuel = 1
# print(minRefuelStops(target,startFuel,stations))

def nextGreaterElement(nums1, nums2):
    # Do rozwiazania stosuje stos, Bede tworzyl stos malejacy(najwieksze wartosci na dole stosu) i szedl od konca tablicy.
    # Jesli stos bedzie pusty oznacza ze nie ma nastepnego wiekszego elementu na prawo.
    # Jesli jest element na stosie to oznacza ze bedzie to dokladnie elementu u gory
    # Gdy bede dodawal do stosu element "a", to bede zdejmowal ze stosu elementy az element
    # naprawie monotonicznosc stosu. Dopiero wtedy spisuje odpowiedź do tablicy arr
    # Na koncu przypisanie dla elementow z nums1 odpowiedzi

    m = len(nums2)
    n = len(nums1)
    arr = [-1] * m
    stack = []
    for i in range(m - 1, -1, -1):

        while stack and stack[-1] <= nums2[i]:
            last_element = stack[-1]
            if last_element <= nums2[i]:
                # zdejmuje se stosy aby naprawic monotonicznosc
                stack.pop()
        if stack:
            arr[i] = stack[-1]
            stack.append(nums2[i])
        if not stack:
            stack.append(nums2[i])

    ind = {}  # klucz - element z nums2, value = next greater element
    for i in range(m):
        ind[nums2[i]] = arr[i]

    ans = [-1] * n
    for i in range(n):
        ans[i] = ind[nums1[i]]
    return ans

# nums1= [4,1,2]
# nums2 = [1,3,4,2]
# print(nextGreaterElement(nums1,nums2))

#LC 503
def nextGreaterElements(self, nums):
    n = len(nums)

    # dlugosc nowej tablicy
    m = n + n - 1
    nums1 = [None] * m

    # ustawianie cyklicznej tablicy
    for i in range(n):
        nums1[i] = nums[i]
    for i in range(n, m):
        nums1[i] = nums[i - n]

    arr = [-1] * n
    stack = []
    for i in range(m - 1, -1, -1):

        while stack and stack[-1] <= nums1[i]:
            # zdejmuje se stosy aby naprawic monotonicznosc
            stack.pop()

        if stack and i < n:
            arr[i] = stack[-1]
        stack.append(nums1[i])

    return arr

