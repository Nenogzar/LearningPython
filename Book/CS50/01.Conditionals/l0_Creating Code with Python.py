# Деф
# Не би ли било хубаво да създадем свои собствени функции?
# Нека върнем нашия окончателен код на hello.py, като напишем код hello.py в прозореца на терминала.
# Вашият начален код трябва да изглежда по следния начин:
"""""""""
# Попитайте потребителя за неговото име, премахнете интервала от str и главна първа буква на всяка дума
name = input("What's your name? ").strip().title()

# Отпечатайте изхода
print(f"hello, {name}")

"""""""""
# Можем да подобрим нашия код, за да създадем наша собствена специална функция, която казва „hello“ за нас!
# Изтривайки целия си код в нашия текстов редактор, нека започнем от нулата:
"""""""""
name = input("What's your name? ")
hello()
print(name)

"""""""""
# При опит да изпълните този код, вашият компилатор ще изведе грешка.
# В крайна сметка няма дефинирана функция за hello.

# Можем да създадем наша собствена функция, наречена hello, както следва:
"""""""""""
def hello():
    print("hello")
name = input("What's your name? ")
hello()
print(name)

"""""
# Забележете, че всичко под def hello() е с отстъп.Python е език с отстъп.
# Той използва отстъп, за да разбере какво е частa от горната функция.
# Следователно всичко във функцията hello трябва да бъде с отстъп.
# Когато нещо не е с отстъп, то го третира така, сякаш не е във функцията hello.
# Изпълнявайки python hello.py в прозореца на терминала, ще видите, че резултатът ви не е точно такъв,
# какъвто бихте искали. Можем допълнително да подобрим нашия код:

"""""""""
# Create our own function
def hello(to):
    print("hello,", to)

# Output using our own function
name = input("What's your name? ")
hello(name)

"""""""""""
# Тук, в първите редове, вие създавате вашата функция hello.
# Този път обаче вие казвате на компилатора, че тази функция приема един параметър:извикана променлива.
# Следователно, когато извикате hello(name), компютърът предава name във функцията hello.
# Ето как предаваме стойности във функции.
# Много полезно! Стартиране на python hello.py в прозореца на терминала,
# ще видите, че резултатът е много по-близък до нашия пример, представен по-рано в тази лекция.

# Можем да променим нашия код, за да добавим стойност по подразбиране към hello:

# СЪЗДАВАНЕ НА НАША СОБСТВЕНА ФУНКЦИЯ

"""""""""
def hello(to="world"):
    print("hello,", to)


# Output using our own function
name = input("What's your name? ")
hello(name)

# Output without passing the expected arguments
hello()

"""""""""""
# Тествайте кода си сами.
# Забележете как първото здравей ще се държи, както може да очаквате,
# а второто здравей, на който не е подадена стойност, по подразбиране ще изведе hello, world.
# Не е нужно да имаме нашата функция в началото на нашата програма.
# Можем да го преместим надолу,
# но трябва да кажем на компилатора че имаме основна функция и имаме отделна функция здравей.
"""""""""
def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


# Create our own function
def hello(to="world"):
    print("hello,", to)
"""""""""
# Само това обаче ще създаде нещо като грешка. Ако стартираме python hello.py, нищо не се случва!
# Причината за това е, че нищо в този код всъщност не извиква основната функция и неоживява на нашата програма.
# Следната много малка модификация ще извика основната функция и ще възстанови нашата програма в работно състояние:

"""""""""""
def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


# Create our own function
def hello(to="world"):
    print("hello,", to)


main()
"""""""""""
# ВРЪЩАНЕ НА СТОЙНОСТ

# Можете да си представите много сценарии, при които не искате просто функция да извърши действие,
# но също и за връщане на стойност обратно към основната функция.
# Например, вместо просто да отпечатате изчислението на x + y, може да искате функция,
# която да върне стойността на това изчисление обратно към друга част от вашата програма.
# Това „връщане“ на стойност наричаме върната стойност.
# Връщане към нашия код calculator.py чрез въвеждане на код calculator.py.
# Изтрийте целия код там. Преработете кода, както следва:

"""""""""""""""
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()

"""""""""""""""
# Ефективно x се предава на квадрат. След това изчислението на x * x се връща обратно към основната функция.