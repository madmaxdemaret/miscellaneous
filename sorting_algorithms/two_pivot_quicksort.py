import sys
num_comp = 0
num_mov = 0


def print_array(A, start, p1, p2, end):
    
    return

    for n in range(start, p1+1):
        sys.stdout.write(str(A[n]) + ", ")

    sys.stdout.write(";")

    for n in range(p1+1, p2+1):
        sys.stdout.write(str(A[n]) + ", ")

    sys.stdout.write(";")

    for n in range(p2+1, end+1):
        sys.stdout.write(str(A[n]) + ", ")

    print(" array end")

def switch(A, source, destination):
    global num_mov
   
    num_mov += 1
    temp = A[source]
    A[source] = A[destination]
    A[destination] = temp

def partition(A,start,p1, p2):
    global num_comp
  
    if(A[p1] > A[p2]):
        switch(A, p1, p2)


    X1 = A[p1]
    X2 = A[p2]

    i1 = start-1
    i2 = i1


    for j in range(start, p1):
        num_comp += 1
        #print("comparing " + str(A[j]))
        if A[j] <= X2:
            if A[j] <= X1:
                
                #for all items in the middle, switch them starting at the end with A[j]
                for n in range(j-1, i1, -1):
                    switch(A, n, n+1)
                i1+=1
                i2+=1
            else:
                i2+=1
                switch(A,j, i2)
        #print_array(A, start, i1, i2, p2)


    for n in range(p1-1, i1, -1):
        switch(A, n, n+1)

    i2+=1

    #print(str(A) + " p2:" + str(p2) + " i2:" + str(i2))

    for n in range(p2-1, i2, -1):
        switch(A, n, n+1)

    #print_array(A, start, i1, i2, p2)

    return(i1, i2)

def qs(A, start, p1, p2):
    
    if(start<p1 and p1<p2):
        q1, q2 = partition(A,start,p1, p2)
        #print(str(q1) + " " + str(q2))
        qs(A, start, q1-1, q1)
        qs(A, q1+2, q2-1, q2)
        qs(A, q2+2, p2-1, p2)

array = [5,3,7,1,9,2,8,4,6]


print array
#print("first pivot is 4, second is 6")

qs(array, 0, 7, 8)
print array
