def swapFileData():
    a=open("file1.txt", 'r')
    with open ("file1.txt", "r") as a:
        data_1 = a.read()

    b=open("file2.txt", 'r')
    with open ("file2.txt", "r") as b:
        data_2 = b.read()

    c=open("file1.txt", 'w')
    with open ("file1.txt", "r") as c:
        c.write(data_2)

    d=open("file2.txt", 'w')
    with open ("file2.txt", "r") as d:
        d.write(data_1)

swapFileData()
