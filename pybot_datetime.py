from datetime import date, datetime

def today_command():
    today = date.today()
    response = f"今日の日付は {today} です"
    return response

def now_command():
    now = datetime.now()
    response = f"現在の日時は {now} です"
    return response

def weekday_command(command):
    try:

        data = command.split()
        year = int(data[1])
        month = int(data[2])
        day = int(data[3])
        one_day = date(year, month, day)

        weekday_str = "月火水木金土日"
        weekday = weekday_str[one_day.weekday()]

        response = f"{one_day} は {weekday} 曜日です"
    except IndexError:
        response = "3つの値（年月日）を指定してください"
    except ValueError:
        response = "正しい日付を指定してください"

    return response
