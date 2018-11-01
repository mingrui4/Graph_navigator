def yes_or_no():
    x = input("Need disabled accessibility? Y/N (press Enter to continue): ")
    if x == "Y" :
        disabled = True
    elif x == "N" :
        disabled = False
    else:
        x = None
        yes_or_no()
    return disabled
disabel = yes_or_no()
print(disabel)

