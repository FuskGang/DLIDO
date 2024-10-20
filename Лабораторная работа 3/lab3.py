# TODO  Напишите функцию count_letters
def count_letters(text):
    storage = {}

    for letter in text:
        if (letter.isalpha()):
            l_letter = letter.lower()
            if (l_letter in storage):
                storage[l_letter] += 1
            else:
                storage[l_letter] = 1

    return storage

# TODO Напишите функцию calculate_frequency
def calculate_frequency(storage):
    new_storage = {}

    all_letters_cnt = sum(storage.values())

    for k, v in storage.items():
        new_storage[k] = round(v / all_letters_cnt, 2)

    return new_storage

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
storage = count_letters(main_str)
new_storage = calculate_frequency(storage)

for k, v in new_storage.items():
    print(f"{k}: {v:.2f}")