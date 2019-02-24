def convert_str_to_hex(str_to_convert: str):
    string = str_to_convert.replace('#', '0x')
    return int(string, 16)
