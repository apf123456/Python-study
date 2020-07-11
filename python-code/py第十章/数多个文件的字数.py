def count_words(filename):
    try:
        with open(filename,encoding="utf-8") as f_obj:
            contens=f_obj.read()
    except FileNotFoundError:
            msg="sorry,the file "+filename+" does not exit."
            print(msg)
    else:
        words=contens.split()
        num_words=len(words)
        print("The file "+filename+" has about "+str(num_words)+" words.")
filenames=["py第十章/split的作用.py","py第十章/使用json存储数据.py","py第十章/使用json存储数据2.py"]
for filename in filenames:
    count_words(filename)
