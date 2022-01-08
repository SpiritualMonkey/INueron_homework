"""1 . you have to write a fun which will take string and return a len of
it without using a inbuilt fun len"""


def string_len(word):
    """returns the length of a string"""
    if type(word) == str:
        char = 0
        for _ in word:
            char += 1
        return char
    else:
        return "please enter a valid string"


# string_len("rohan")

"""2 . write a fun which will be able to print an index of all primitive element which you will pass """


def primitive_index(a):
    """prints all char with index of primitive elements"""
    if type(a) == bool or int or float:
        a = str(a)
        for index in range(len(a)):
            print(f"Index {index} : {a[index]}")
    else:
        for index in range(len(a)):
            print(f"Index {index} : {a[index]}")


# primitive_index(True)

"""3 . Write a fun which will take input as a dict and give me out as a list of all the values 
even in case of 2 level nesting it should work . """

dic = {
    "Info": {
        "name": "Rohan Basu",
        "course": "FSDS"
    },
    "contact no": 9876543210,
}


def dic_info(arg):
    """input as a dict and prints a list of all the values"""
    result = []
    keys = arg.keys()
    for key in keys:
        result.append(f"{key} : {arg[key]}")
        try:
            for k in arg[key].keys():
                result.append(f"{k} : {arg[key][k]}")
        except AttributeError:
            pass
    print(result)


# dic_info(dic)

"""4 . write a fun which will take another function as an input and return me an output """


def fun_op(fun):
    """will take another function as an input and return me an output"""
    return fun


# s = fun_op(string_len("rohan"))
# print(s)


"""5. write a function which will take multiple list as an input and give me concatination of all the element as 
and output"""

a = [221, 332, 312.24]
b = ["rohan", "basu", "FSDS", 788.311]
c = [3232.34, 1313.21, "inueron", ["onenueron", "DSA", "ML"]]


def list_con(*args):
    result = []
    for arg in args:
        if type(arg) == list:
            for el in arg:
                if type(el) == list:
                    result.extend(el)
                    del arg[arg.index(el)]
            result.extend(arg)
    print(result)


# list_con(a, b, c)

"""6 . write a function which will be able to take a list as an input return an index of each element 
like a inbuilt index function but even if we have repetative element it should return index """

d = [221, 332, 312.24, 1, 1, 5, 5]


def index_all(li, ch):
    """takes list and a char as an input and returns the index of the element if it is present"""
    for el in range(len(li)):
        if ch == li[el]:
            print(f"You have {li[el]} at index {el}")


# index_all(d, 5)


"""7 . Write a function which will should return list of all the file name from a directory."""


def file_list(path):
    import os

    for path, dirs, files in os.walk(path):
        print(files)


# file_list("D:/Movies/")


""" 8  . write a function which will be able to show your system configuration .  """


def system_config():
    """ prints your system config
    Link : https://www.geeksforgeeks.org/get-your-system-information-using-python-script/
    """

    import platform

    my_system = platform.uname()

    print(f"System: {my_system.system}")
    print(f"Node Name: {my_system.node}")
    print(f"Release: {my_system.release}")
    print(f"Version: {my_system.version}")
    print(f"Machine: {my_system.machine}")
    print(f"Processor: {my_system.processor}")


# system_config()


"""9 . write a function which will be able to show date and time ."""


def date_time():
    """prints the current date and time"""
    from datetime import datetime

    data = str(datetime.now())
    date = str(datetime.now().strftime("%d/%m/%Y")).split(" ")[0]
    time = data.split(" ")[1]
    print(f"Today's date : {date}")
    print(f"Time now : {time[:8]}")


# date_time()


"""10 . write a function which will be able to read a image file and show it to you."""


def show_img(path):
    """
    if you put the path as an input it will show the image
    Link : https://www.topcoder.com/thrive/articles/python-for-image-recognition-opencv
    """
    import cv2

    img = cv2.imread(path)

    cv2.imshow('image', img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()


# show_img("AI_img.jpg")


""" 11 . write a function which can read video file and play for you . """


def vid_play(path):
    """
    if you provide a path it will play the video
    Link : https://www.geeksforgeeks.org/python-play-a-video-using-opencv/
    """
    import cv2
    import numpy as np

    cap = cv2.VideoCapture(path)

    # Check if camera opened successfully
    if cap.isOpened() == False:
        print("Error opening video  file")

    # Read until video is completed
    while cap.isOpened():

        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:

            # Display the resulting frame
            cv2.imshow('Movie', frame)

            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Break the loop
        else:
            break

    # When everything done, release
    # the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()


# vid_play("D:/Movies/Girl.With.Dragon.Tattoo.2011.Multi.@Dubbedmovies.mkv")


"""12  . write a function which can move a file from one directory to another directory . """


def move_file(file_source_arg, file_destination_arg):
    import shutil
    import os

    get_files = os.listdir(file_source_arg)

    for g in get_files:
        shutil.move(file_source + g, file_destination_arg)


file_source = 'C:/Users/rohan/Desktop/TCS documentation/'
file_destination = 'C:/Users/rohan/Desktop/Nitin bhatia'

# move_file(file_source, file_destination)


"""13 . write a function which will be able to shutdown your system ."""


def sys_shut():
    """
    shuts down your system
    Link :  https://www.geeksforgeeks.org/python-script-to-shutdown-computer/
    """
    import os

    shutdown = input("Do you wish to shutdown your computer ? (yes / no): ")

    if shutdown == 'no':
        exit()
    else:
        os.system("shutdown /s /t 1")


# sys_shut()


"""14 . write a function which will be able to access your mail """

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

"""
Link : https://www.youtube.com/watch?v=6DD4IOHhNYo
Code : https://github.com/codingforentrepreneurs/30-Days-of-Python-3.6/blob/master/Day%209/day_9_end.py
"""

""" 15 . write a func by which i can send a mail to anyone """


def send_mail(domain_smtp, email_add, password, receiver_mail, mail_subject, mail_body):
    """
    domain_smtp: domain smtp add eg: for gmail use "smtp.gmail.com"
    email_add: your email
    password: your mail password
    receiver_mail: email address where you want to send the mail
    mail_subject : provide the mail subject
    mail_body: provide the mail text/body

    it send the mail once you run the function with all the parameters
    """
    import smtplib


    server = smtplib.SMTP(domain_smtp, 587)
    server.ehlo()
    server.starttls()

    my_email = email_add
    my_password = password

    server.login(my_email, my_password)

    print(server.verify(receiver_mail))

    server.sendmail(from_addr=my_email,
                    to_addrs=receiver_mail,
                    msg=f"Subject:{mail_subject}\n\n {mail_body}")

    server.quit()




# send_mail(gmail_smtp, email, password, receiver_mail, "Hello", "I am Rohan")

""" 16. write a func to read a complete PDf file .  """


def read_pdf(path):
    """ reads a pdf file"""

    import PyPDF2

    # creating a pdf file object
    pdfFileObj = open(path, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    print(pdfReader.numPages)

    # creating a page object
    pageObj = pdfReader.getPage(0)

    # extracting text from page
    print(pageObj.extractText())

    # closing the pdf file object
    pdfFileObj.close()


# read_pdf('C:/Users/rohan/Desktop/TCS documentation/LOA(pdf).pdf')

""" 17. write a function to read a word file . """


def read_word_file(path):
    """
    reads a doc/docx file
    Link : https://stackoverflow.com/questions/36001482/read-doc-file-with-python
    textract : https://textract.readthedocs.io/en/stable/
    """
    import textract

    text = textract.process("C:/Users/rohan/Desktop/Data Structure and Algorithms(MIT OCW).docx")
    print(text)


# read_word_file("C:/Users/rohan/Desktop/Data Structure and Algorithms(MIT OCW).docx")

""" 18 . write a function which can help you to filter only word file from a directory .  """


# import glob
#
# glob.glob("C:/Users/rohan/Desktop/Cognigent Docs/")


""" 19 . write a function by which you can print an ip address of your system . """


def ip_add():
    """
    prints ip address
    """
    import socket

    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    # print(f"Your Computer Name is: {hostname}")
    print(f"Your Computer IP Address is: {IPAddr}")


# ip_add()

""" 20 . write a function by which you will be able to append two PDF files . """


def pdf_merger(new_file_name_Path, *args):
    """
    :param new_file_name_Path: requires the path of the dir where it should be saved along with the filename.pdf at the end
    :param args: requires the path of the files which needs to be marged in order
    :return: the file in the mentioned path of the first argument
    """
    from PyPDF2 import PdfFileMerger

    pdfs = []

    for arg in args:
        pdfs.append(arg)

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(new_file_name_Path)
    merger.close()


# "C:/Users/rohan/Desktop/TCS documentation/result.pdf"

pdf1 = "C:/Users/rohan/Desktop/TCS documentation/Rohan Basu-Aadhar card.pdf"
pdf2 = "C:/Users/rohan/Desktop/TCS documentation/Rohan Basu-PAN.pdf"
pdf3 = "C:/Users/rohan/Desktop/TCS documentation/Rohan Basu-voter id.pdf"
# pdf_merger("C:/Users/rohan/Desktop/TCS documentation/test.pdf", pdf1, pdf2, pdf3)
