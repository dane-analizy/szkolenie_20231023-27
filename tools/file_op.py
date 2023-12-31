def get_file_content(file_name: str, enc: str='utf-8', sep: str=';') -> list[tuple]:
    return [ tuple(line.strip().split(sep))
             for line in open(file_name, 'r', encoding=enc)
             if len(line.strip()) > 0 ]


def save_to_file(lista: list[tuple], file_name: str, enc: str = 'utf-8', sep: str = ';') -> None:
    with open(file_name, 'w', encoding=enc) as f:
        for t in lista:
            linia = sep.join([str(tt) for tt in t])+'\n'
            f.write(linia)


def save_to_file_from_dict(lista: list[dict], file_name: str, enc: str = 'utf-8', sep: str = ';') -> None:
    with open(file_name, 'w', encoding=enc) as f:
        for d in lista:
            linia = sep.join([str(dv) for dv in d.values()])+'\n'
            f.write(linia)
