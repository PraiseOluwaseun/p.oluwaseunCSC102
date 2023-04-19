print("WELCOME TO FINETECHS")



for i in range(2500):
 name = input("Enter your name: ")
 print(f"Welcome {name}")

 age  = int(input("Enter your age: "))
 eper = int(input("Enter your years of experiences: "))



 if eper > 25 and age >= 55 :
    print("Your annual tax revenue is 5600000 naira ")
 elif eper > 20 and age >= 45 :
    print("Your annual tax revenue is 4480000 naira")
 elif eper > 10 and age >= 35 :
    print("Your annual tax revenue is 1500000 naira")
 elif eper < 10 and age < 35 :
    print("Your annual tax revenue is 550000 naira")

