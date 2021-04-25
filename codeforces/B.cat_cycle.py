"""
Suppose you are living with two cats: A and B. 
There are n napping spots where both cats usually sleep.

Your cats like to sleep and also like all these spots, 
so they change napping spot each hour cyclically:

Cat A changes its napping place in order: n,n−1,n−2,…,3,2,1,n,n−1,… 
In other words, at the first hour it's on the spot n and then goes in decreasing order cyclically;
Cat B changes its napping place in order: 1,2,3,…,n−1,n,1,2,… 
In other words, at the first hour it's on the spot 1 and then goes in increasing order cyclically.
The cat B is much younger, so they have a strict hierarchy:
A and B don't lie together. In other words, 
if both cats'd like to go in spot x then the A takes this place 
and B moves to the next place in its order 
(if x<n then to x+1, but if x=n then to 1). 
Cat B follows his order, so it won't return to the skipped spot x after A frees it,
but will move to the spot x+2 and so on.

Calculate, where cat B will be at hour k?
"""


# n = no. of spots, k = hours
def cat_cycle():
    t = int(input())
    for tests in range(t):
        n = 0
        k = 0
        inp = list(map(int,input().split()))
        n = inp[0]
        k = inp[1]

        arr = []
        for i in range(n+1):
            arr.append(i)
        cat_a = arr[-1]
        cat_b = arr[1]
        cat_a_place = -1
        cat_b_place = 1
        for places in range(2, k+1):
            cat_a_place -= 1
            cat_b_place += 1
            if cat_b_place > n:
                cat_b_place = 1
            if cat_a_place < -n:
                cat_a_place = -1


            if arr[cat_a_place] == arr[cat_b_place]:
                if cat_b_place >= n:
                    cat_b_place = 1
                else:
                    cat_a = arr[cat_a_place]
                    cat_b = arr[cat_b_place+1]
                    cat_b_place = cat_b_place + 1
            else:
                cat_a = arr[cat_a_place]
                cat_b = arr[cat_b_place]
            

        print(cat_b)


cat_cycle()




    
