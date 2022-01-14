def reversible(n):
    itemp_1 = str(n)    
    itemp_2 = itemp_1[::-1] 
    if (itemp_1 == itemp_2):
        print(n, "là số thuật nghịch.")
    else:
        print(n, "không phải là số thuật nghịch.")

fullName = input("Nhập họ và tên: ")
print("Họ và tên đầy đủ vừa nhập là:", fullName)

n = int(input("Nhập vào số n: "))
reversible(n)