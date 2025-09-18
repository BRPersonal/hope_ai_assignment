from itertools import product

def center_text(text:str,column_width:int) -> str:

    result = text
    length = len(text)

    if (column_width > length):
        filler_length = (column_width - length) // 2  #integer division
        filler_spaces = (" " * filler_length)
        result = filler_spaces + text + filler_spaces

    return result

def generate_parameter_combinations(param_dict:dict) -> [dict] :
    return [dict(zip(param_dict.keys(),combo)) for combo in product(*param_dict.values())]
