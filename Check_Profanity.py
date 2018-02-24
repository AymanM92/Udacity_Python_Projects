import urllib.request
from urllib.parse import quote

def ReadTxt():
    filo = open("file.txt")
    words = filo.read()
    filo.close()
    CheckProfanity(words)

def CheckProfanity(IntendedText):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+quote(IntendedText))
    Text_Status = connection.read()
    connection.close()
    if "b\'false\'" == str(Text_Status):   '''This will do the same functionality''' #if "false" in str(Text_Status):
        print("No Profanity found Clean text")
    else:
        print("Profanity found you'd better change it !!")

ReadTxt()
