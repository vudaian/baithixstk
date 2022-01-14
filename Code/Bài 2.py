def find_sum(n):
    totalVariable = 0
    tempNumber = n
    while (n > 0):
        totalVariable = totalVariable + n % 10
        n = int(n / 10)
    print("Tổng các chữ số của số", tempNumber, "là:", totalVariable)
 
middleName = input("Nhập tên đệm: ")
print("Tên đệm vừa nhập vào là:", middleName)
 
n = int(input("Nhập vào số n: "))
find_sum(n)