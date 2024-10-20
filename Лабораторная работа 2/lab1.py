money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

month = 0
while True:
    all_spend = spend + (month * increase * spend)
    if (salary + money_capital) >= all_spend:
        spend = all_spend
        month += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", month)
