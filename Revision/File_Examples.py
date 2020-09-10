def func0():
    """
    Creating file objects and looping on it
    """
    f = open("file1.txt", "r")
    for i in f:
        print(i, end='')
    f.close()
    # Demonstrating File Attributes
    print("f.closed = ", f.closed)
    print("f.encoding = ", f.encoding)
    print("f.mode = ", f.mode)
    print("f.name = ", f.name)
    print("f.newline = ", f.newlines)


def func1():
    """
    read(n) - Here 'n' is number of bytes to be read
    readline(n) - Here 'n' is number of bytes to be read
    readlines()
    """
    with open("file1.txt", "r") as f:
        print(f.read(10))  # It will print 10 bytes of data
    print()

    with open("file1.txt", "r") as f:
        print(f.read())  # It will print entire file content
    print()

    with open("file1.txt", "r") as f:
        print(f.readline(10))  # It will print 10 bytes of first line. If line overflows, it will not print the next
    print()                    # line then

    with open("file1.txt", "r") as f:
        print(f.readline())  # It will print first line and then stops
    print()

    with open("file1.txt", "r") as f:
        print(f.readlines())  # It reads all the lines and return them as each line a string element in a list


def func2():
    """
    - We will open file in write mode.
    - During write mode, we need to be very careful while writing data into the file as it overwrites the content
      present inside the file that you are writing, and all the previous data will be erased. Also, if the file is not
      available then the file will be created.
    - We have 2 methods for writing data into a file:
      - write(string) - It writes string or sequence of bytes to a file. This function returns a number which is the
                        size of data written in a single write call.
      - writelines(list) - expects an iterable as argument (an iterable object can be a tuple, a list, a string, or an
                           iterator in the most general sense). Each item contained in the iterator is expected to be a
                           string. A tuple of strings is what you provided, so things worked.
    """

    with open("file2.txt", "w") as f:
        print(f.write("This is a file2 and data is written into it via write method\n"))

    with open("file3.txt", "w") as f:
        temp_list = "This is a file2 and data is written into it via writelines method".split()
        print(f.writelines([i+' ' for i in temp_list]))
        f.write("\n")


def func3():
    """
    - We will see the example of tell() and seek() method
    - fp.seek(offset, from_what)
      where 'fp' is the file pointer you're working with; 'offset' means how many positions you will move;
      'from_what' defines your point of reference:
        - 0: means your reference point is the beginning of the file
        - 1: means your reference point is the current file position
        - 2: means your reference point is the end of the file

      if omitted, 'from_what' defaults to 0.

    - In text files (those opened without a 'b' in the mode string), only seeks relative to the beginning of the file
      are allowed (the exception being seeking to the very file end with seek(0, 2)) and the only valid offset values
      are those returned from the f.tell(), or zero. Any other offset value produces undefined behaviour.
    """

    with open("file1.txt", "rb") as f:  # See the mode. This text file is opened in the binary mode.
        print("Current Cursor Position - ", f.tell())
        print(f.read(30))

        print()

        f.seek(0, 0)  # 1st zero denotes the movement and 2nd 0 denotes cursor is at the beginning position
        print("Current Cursor Position - ", f.tell())
        print(f.read(30))

        print()

        f.seek(20, 1)  # 1st zero denotes the movement and 2nd 1 denotes cursor is at the current position
        print("Current Cursor Position - ", f.tell())
        print(f.read())

        print()

        f.seek(-10, 2)  # 1st zero denotes the movement and 2nd 2 denotes cursor position is at the end
        print("Current Cursor Position - ", f.tell())
        print(f.read(30))


if __name__ == "__main__":

    # func0()
    # func1()
    # func2()
    func3()
