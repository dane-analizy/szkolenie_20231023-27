def get_file_content(file_name: str, enc: str='utf-8', sep: str=';') -> list[tuple]:
    return [ tuple(line.strip().split(sep))
             for line in open(file_name, 'r', encoding=enc)
             if len(line.strip()) > 0 ]


def save_to_file(lista: list[tuple], file_name: str, enc: str='utf-8', sep: str=';'):
    with open(file_name, 'w', encoding=enc) as f:
        for t in lista:
            linia = sep.join(t)+'\n'
            f.write(linia)
