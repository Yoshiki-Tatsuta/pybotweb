def wareki_command(command):
    wareki, year_str = command.split()
    if year_str.isdigit():
        year = int(year_str)
        if year >= 2019:
            reiwa = year - 2018
            response = f"西暦{year}年は、令和{reiwa}年です"
        elif year >= 1989:
            heisei = year - 1988
            response = f"西暦{year}年は、平成{heisei}年です"
        else:
            response = f"西暦{year}年は、平成より前です"
    else:
        response = "数値を指定してください"

    return response
