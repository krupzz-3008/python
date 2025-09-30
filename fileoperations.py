def fileoperations():
    data=input("enter text to write in the file:")
    file=open('output.txt','w')
    file.write(data+"\n")
    file.close()
    print("data written successfully")
    file.close()

    extra=input("enter text to add in the file:")
    file=open('output.txt','a')
    file.write(extra)
    print("data added successfully")
    file.close()

    file=open('output.txt','r')
    read=file.read()
    print(read)
    file.close()

fileoperations()