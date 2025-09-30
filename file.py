def file():
    try:
        file1 = open('k.txt', 'r')
        lines = file1.readlines()   # read all lines at once
        total = len(lines)          # count them

        for i in range(total):
            read=lines[i]
            print(f"line {i+1}: {read}")



        file1.close()  # don’t forget to close the file!

    except FileNotFoundError:
        print("File not found")

file()
