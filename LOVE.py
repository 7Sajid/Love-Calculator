print("*************Welcome to love calculator**************")
name1= input("What Is Your Name? \n       ")
name2= input("What Is His/Her Name? \n       ")
             
combine_string = name1 + name2
lower_case_string = combine_string.lower()

t= lower_case_string.count("t")
r= lower_case_string.count("r")
u= lower_case_string.count("u")
e= lower_case_string.count("e")

true = t + r + u + e

l= lower_case_string.count("l")
o= lower_case_string.count("o")
v= lower_case_string.count("v")
e= lower_case_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

print(f"\n********** Your True Love Persentage Is {love_score }% ")


