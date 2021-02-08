from pybot_wareki import wareki_command
from pybot_eto import eto_command
from pybot_random import choice_command, dice_command
from pybot_datetime import today_command, now_command, weekday_command
from pybot_sqrt import sqrt_command
from pybot_event import event_command
from pybot_wiki import wikipedia_command


command_file = open("pybot.txt", encoding="utf-8")
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines()

bot_dict = {}
for line in lines:
    word_list = line.split(",")
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response

def pybot(command):
    # command = input("pybot> ")
    response = ""
    try:

        for messege in bot_dict:
            if messege in command:
                response = bot_dict[messege]
                break

        if "和暦" in command:
            response = wareki_command(command)

        if "干支" in command:
            response = eto_command(command)

        if "選ぶ" in command:
            response = choice_command(command)

        if "さいころ" in command:
            response = dice_command(command)

        if "今日" in command:
            response = today_command()

        if "現在" in command:
            response = now_command()

        if "曜日" in command:
            response = weekday_command(command)

        if "平方根" in command:
            response = sqrt_command(command)

        if "イベント" in command:
            response = event_command(command)

        if "辞典" in command:
            response = wikipedia_command(command)

        if not response:
            response = "ナニヲイッテイルカワカラナイ"
        return response

        # if "さようなら" in command:
        #    break
    except Exception as e:
        print("予期せぬエラーが発生しました")
