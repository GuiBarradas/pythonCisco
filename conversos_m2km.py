kilometers = float(input("Entre com o valor em quilômetros: "))
miles = float(input("Entre com o valor em milhas: "))

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "milhas são", round(miles_to_kilometers, 2), "quilômetros")
print(kilometers, "quilômetros são", round(kilometers_to_miles, 2), "milhas")
