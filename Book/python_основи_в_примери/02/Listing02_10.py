# Текстова променлива:
res="Това е числото "
# Въвеждане на текст:
txt=input("Въведете име на число: ")
# Преобразуване в долен регистър:
txt=txt.lower()
# Идентификация на числото:
if txt=="едно" or txt=="единица":
    res+="1"
elif txt=="две" or txt=="двойка":
    res+="2"
elif txt=="три" or txt=="тройка":
    res+="3"
else:
    res="Числото не може да бъде идентифицирано"
# Резултат от идентификацията:
print(res)
