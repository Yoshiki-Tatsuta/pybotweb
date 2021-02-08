import random

def choice_command(command):
    data = command.split()
    try:
        choiced = random.choice(data[1:])
        response = f"「{choiced}」が選ばれました"
    except IndexError:
        response = "選択するものを指定してください"
    return response


def dice_command(command):
    num = random.randrange(1, 7)
    response = f"「{num}」が出ました"
    return response
