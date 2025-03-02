**The Ultra Mega Files Tool - Утилита для работы с файлами**

**Инструкция по запуску:**

Для запуска утилиты из командной строки можно использовать файл tool.cmd

**Формат запуска:**

tool < command > [parametrs]

**Запуск графического интерфейса**

Запусть gui.py

**Доступные команды:**

copy - копирует файл

tool copy < filename > < destination>

пример использования

    tool copy c:\file1.txt c:\directory

del - удаляет файл < filename >

tool del < filename >

пример использования

    tool del c:\file1.txt

count - подсчитывает количество файлов в папке

-r, --recursive - делает подсчет рекурсивно во всех подпапках

tool count < directory> [-r]

пример использования

    tool count c:\directory -r

search - поиск файлов в папке и подпапках по регулярному выражению

tool search < directory> < regexp >

пример использования


    tool search c:\directory file123

add_date - добавляет дату создания файла в имя файла ко всем файлам в папке

-r, --recursive - включать файлы в подпапках

tool add_date < directory> [-r]

пример использования

    tool add_date c:\directory -r

analyse - выводит размер папки и размер файлов и папок в этой папке

tool analyse < directory>

пример использования

    tool analyse c:\directory

gentest - генерирует тестовую структуру папок и фалов указанного количества

tool gentest < directory>

пример использования

    tool analyse c:\directory

