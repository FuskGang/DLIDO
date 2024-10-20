# TODO Найдите количество книг, которое можно разместить на дискете



all_size_mb = 1.44
page_cnt = 100
row_cnt = 50
sym_cnt = 25
one_sym_b = 4

all_size_b = 1.44 * 1024 * 1024
one_book_b = page_cnt * row_cnt * sym_cnt * one_sym_b

book_can_be = int(all_size_b // one_book_b)

print("Количество книг, помещающихся на дискету:", book_can_be)
