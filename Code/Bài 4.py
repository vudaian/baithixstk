string = ', '
information = input("Nhập vào họ tên và mã sinh viên: ")
value = string.join(information)
list = value.split(",")
tuple = tuple(list)

print ("Danh sách là: ", end=" ")
print(list)   
print ("Tuple là: ", end=" ")
print(tuple)