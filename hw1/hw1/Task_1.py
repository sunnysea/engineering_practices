# title Задача 1
# description Дан файлик .py, нужно привести к формату, в котором будет можно загружать на GitHub в формате .md
# ---end----

# https://codeshare.io/RbDOML
import codecs
import os
import numpy as np



INPUT_CODE_DELIMITER = '# ---end----'
MD_CODE_DELIMITER = '<!---split here-->'
def read_file(file_name, what_to_do='r', encoder="utf-8"):
    with open(file_name, what_to_do, encoding=encoder) as decision:
        if what_to_do == 'r':
            data = decision.read()
        else:
            data = decision.write('')
    return data

def get_info_from_md_file(data, MD_CODE_DELIMITER):
    titles, old_code = data.split(MD_CODE_DELIMITER)
    #print(titles, old_code)
    return titles, old_code

def write_data(file_name, new_title, new_data, old_title, old_data, MD_CODE_DELIMITER):
    with open(file_name, 'w', encoding='utf-8') as f:
        content = '\n'.join([old_title, new_title, MD_CODE_DELIMITER, old_data, new_data])
        #print(old_title, new_title, MD_CODE_DELIMITER, old_data, new_data, sep='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        f.write(content)

def prepare_md_titles(first):
    if len(first) != 0:
        first = first.split('#')
        if first[1].startswith(' title '):
            title = first[1][7:].strip()
        if first[2].startswith(' description '):
            description = first[2][13:].strip()
        return title, description
    else:
        return None, None

def prepare_md_code(title, description, sourse_code):
    title_data = '+ [{}](#{})\n\n'.format(title, '-'.join(list(map(lambda x: x.lower(), title.split()))))
    data = '## {}\n\n{} \n\n```python{}```'.format(title, description, sourse_code[2:-3])
    return title_data, data

def converter(decision, INPUT_CODE_DELIMITER):
    first, last = decision.split(INPUT_CODE_DELIMITER)
    title, description = prepare_md_titles(first)
    title_data, data = prepare_md_code(title, description, last)
    return title_data, data

def main():
    content = read_file('my_file.py')
    new_title, new_data = converter(content, INPUT_CODE_DELIMITER)
    if os.path.exists('README.md') and os.path.getsize('README.md') > 0:
        md_content = read_file('README.md')
        old_title, old_data = get_info_from_md_file(md_content, MD_CODE_DELIMITER)
    else:
        md_content = read_file('README.md', what_to_do='w')
        old_title, old_data = None, None
    write_data('README.md', new_title, new_data, old_title, old_data, MD_CODE_DELIMITER)


if __name__ == "__main__":
    main()