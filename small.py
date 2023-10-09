num_1=int(input("Enter First number:"))
num_2=int(input("Enter Second number:"))
num_3=int(input("Enter Third number:"))
if num_1<num_2 and num_1<num_3:
    print("Smallest Number:",num_1)
elif num_2<num_3 and num_2<num_1:
    print("Smallest Number:",num_2)
else:
    print("Smallest Number:",num_3)