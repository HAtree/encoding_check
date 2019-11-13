import chardet
filename = "good.txt"
f = open("bad.txt", "rb")
if chardet.detect(f.read())["encoding"] != "ascii":
    print("error")
else: 
    print("success")