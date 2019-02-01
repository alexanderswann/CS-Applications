#Alexander Swann
#Thursday, January 31, 2019
#CS Applications

#functionsPractice
x = int(input("enter a grade "))
y = int(input("enter a grade "))
z = int(input("enter a grade "))
def math2 (num1,num2):
    total = num1 + 3*num2
    return total
result = math2(x,y)
print(result)

def math3 (a,b,c):
    res1 = (-b + (b**2 - 4*a*c)**(1/2)) / (2 * a)
    res2 = (-b - (b**2 - 4*a*c)**(1/2)) / (2 * a)
    return res1, res2
result2 = math3(x,y,z)
print(result2)

def calculateGPA (g1,g2,g3):
    if (g1+g2+g3)/3 >= 90:
        gpa = 4
    elif (g1+g2+g3)/3 >= 80:
        gpa =3
    elif (g1+g2+g3)/3 >= 70:
        gpa = 2
    elif (g1+g2+g3)/3 < 70:
        gpa = 1
    return gpa

result3 = calculateGPA (x,y,z)
print(result3)
