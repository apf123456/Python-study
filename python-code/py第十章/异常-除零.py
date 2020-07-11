print("给我2个数字，我可以相除")
print("按q退出")

while True:
    first_number=input("\nfirst number:")
    if first_number =='q':
        break
    second_number=input("\nsecond number")
    if second_number =='q':
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
            print("you can't divide by 0!")
    else:
        print(answer)