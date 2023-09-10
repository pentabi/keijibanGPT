import sys

def get_interval():
    try:
        f = open("interval.txt", "r")
    except OSError as e:
        print("1. Please make \"interval.txt\" file in the backend directory.")
        print("2. Type in a number in the file to indicate the interval (in seconds) ChatGPT responds.")
        sys.exit(0)
    else:
        content = f.readlines()
        f.close()
        return int(content[0].replace("\n", ""))
