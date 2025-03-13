import os

dir_counter = 0
file_counter = 0

all_size_counter = 0

def transformation_size_file(line):
    """Преобразует строки файла в человекочитаемый формат.
    
    :params line: строка из файла
    :type line: str

    :rtype: str
    :return: преобразованная строка
    """
    line_list = [el for el in line.split(' ') if el != '']
    if int(line_list[4]) > 1024:
        line_list[4] = f'{line_list[4][0]}.{line_list[4][1]}K'
        return '  '.join(line_list)
    else:
        return '  '.join(line_list)

def counter_dir_and_file(file_code):
    """Подсчитывает количество папок и файлов в директории etc

    :params file_code: начальный символ кода строки, обозначающий тип файла
    :type file_code: str   
    """
    global dir_counter
    global file_counter
    if file_code == 'd':
        dir_counter = dir_counter + 1
    else:
        file_counter = file_counter + 1
    
def count_size_all(line):
    global all_size_counter
    size = [el for el in line.split(' ') if el != ''][4]
    all_size_counter += int(size)



with open('output.txt', 'r', encoding='utf-8') as file:
    file = file.readlines()
    for line in file:
        count_size_all(line)
        print(transformation_size_file(line), end='')
        counter_dir_and_file(line[0])
        


print(f'\nДиректорий в папке ect - {dir_counter}')
print(f'Файлов в папке ect - {file_counter}')
print(f'Размер всех файлом - {round((all_size_counter / 1024))}K')






