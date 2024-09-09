def center_text(text:str,column_width:int) -> str:

    result = text
    length = len(text)

    if (column_width > length):
        filler_length = (column_width - length) // 2  #integer division
        result = "".ljust(filler_length) + text + "".rjust(filler_length)

    return result
