# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, deli=','):
    first_split = first.split(deli)
    second_split = second.split(deli)

    first_and_second = set(first_split).intersection(set(second_split))
    return sorted(list(first_and_second))

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))
