def convert_str_to_hex(str_to_convert: str):
    print(str_to_convert)
    string = str_to_convert.replace('#', '0x')
    print(string)
    return int(string, 16)