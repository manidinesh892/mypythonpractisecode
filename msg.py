while True:
    text=input("message")
    if(text[0]=='#'):
        continue
    if(text=="done"):
        break
    print(text) 