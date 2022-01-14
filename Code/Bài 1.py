def dictionary(d):
    d = dict()
    for i in range(1, n + 1, 1):
        d[i] = i * i
    print (d)
    
name = input("Nhập tên: ")
print("Tên vừa nhập là:", name)
 
n = int(input("Nhập vào số n: "))
print("Dictionary:", end=" ")
dictionary(n)