import math

def sqrt_command(command):
    try:
        sqrt, number_str = command.split()
        x = int(number_str)
        sqrt_x = math.sqrt(x)
        response = f"{x} の平方根は {sqrt_x} です"
    except ValueError:
        response = "数字を指定してください"
    return response
