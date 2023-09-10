import sys

def get_api_key():
    try:
        f = open("api_key.txt", "r")
    except OSError as e:
        print("1. Please make \"api_key.txt\" file in the backend directory.")
        print("2. Put your \"ChatGPT API KEY\" in the file.")
        sys.exit(0)
    else:
        content = f.readlines()
        f.close()
        return content[0].replace("\n", "")
