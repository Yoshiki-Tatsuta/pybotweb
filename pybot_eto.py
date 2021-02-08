def eto_command(command):
    try:
        eto, year_str = command.split()
        year = int(year_str)
        number_of_eto = (year + 8) % 12
        eto_taple = ("子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥")
        eto_name = eto_taple[number_of_eto]
        response = f"{year}年生まれの干支は「{eto_name}」です。"
    except ValueError:
        response = "生まれた年を指定してください"

    return response
