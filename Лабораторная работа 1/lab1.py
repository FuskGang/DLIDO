numbers = [2, -93, -2,8,None, -44, -1, -85, -14,90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

index_missing_el = 0
len_num_arr = len(numbers)
sm = 0
for num_ind in range(len_num_arr):
    if (numbers[num_ind] == None):
        index_missing_el = num_ind
        continue
    sm += numbers[num_ind]

numbers[index_missing_el] = sm / len_num_arr

print("Измененный список:", numbers)
