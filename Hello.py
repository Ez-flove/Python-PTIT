#name = input()
#print("Hello "+ name +"!")


#print("Welcome to python.")





gpa=float(input())
if gpa<2:
    print("Yeu")
elif gpa>=2 and gpa<=2.49:
    print("Trung Binh")
elif gpa>=2.5 and gpa<=3.19:
    print("Kha")
elif gpa>=3.2 and gpa<=3.59:
    print("Gioi")
elif gpa>=3.6 and gpa<=4:
    print("Xuat sac")


person = {
    'name': 'Mai Xuan Ngoc',
    'age': 20,
    'male': True,
    'status': 'alone'        
    }

person['status'] = 'married'
print(person)