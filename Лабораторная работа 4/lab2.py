# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    all_dicts = []
    with open(INPUT_FILENAME, "r", newline="") as f:
        data = csv.DictReader(f)

        for i in data:
            all_dicts.append(i)
    ...  # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4

    with open(OUTPUT_FILENAME, "w") as f:
        f.write(json.dumps(all_dicts, indent=4))

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
