"""
Instrucciones
Escriba un programa que interprete el índice de masa corporal (IMC) en función del peso y la altura de un usuario.

Debe decirles la interpretación de su IMC en función del valor de IMC.

Menos de 18,5 tienen bajo peso
Por encima de 18,5 pero por debajo de 25 tienen un peso normal
Por encima de los 25 pero por debajo de los 30 tienen un ligero sobrepeso
Mayores de 30 pero menores de 35 son obesos
Por encima de 35 son clínicamente obesos.
"""
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height ** 2))
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")