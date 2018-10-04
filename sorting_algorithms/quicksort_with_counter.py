num_comp = 0
num_mov = 0


def switch(A, s, d):
    global num_mov
   
    num_mov += 1
    temp = A[s]
    A[s] = A[d]
    A[d] = temp

def partition(A,p,r):
    global num_comp
    
    X = A[r]
    i = p-1
    for j in range(p, r):
        num_comp += 1
        if A[j] <= X:
            i += 1
            switch(A, i, j)
    switch(A, i+1, r)
    return i+1
            
def qs(A, p, r):
    if p<r:
        q = partition(A,p,r)
        qs(A,p,q-1)
        qs(A,q+1,r)

qs([50, 30, 70, 10, 90, 20, 80, 40, 60], 0, 8)
print(str(num_comp) + " + " + str(num_mov))
