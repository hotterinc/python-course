# TODO Найдите количество книг, которое можно разместить на дискете
floppy_disk_size = 1.44 * 1024 * 1024
count_of_pages = 100
count_of_lines = 50
count_of_simbols = 25
bytes_for_one_symbol = 4

print("Количество книг, помещающихся на дискету:", int(
    floppy_disk_size / (count_of_pages * count_of_lines * count_of_simbols * bytes_for_one_symbol)))
