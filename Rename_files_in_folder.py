import os

def List_photos():
    File_list = os.listdir("/home/ayman/Desktop/Algorithms/Python_Udacity_Course/Take_aBreak/Photos/prank")
    Photos_name = "File"
    Origins=os.getcwd()
    os.chdir("/home/ayman/Desktop/Algorithms/Python_Udacity_Course/Take_aBreak/Photos/prank")
    for i in range(len(File_list)):
        translator = File_list[i].maketrans('', '', "0123456789")
        Photos_name = File_list[i].translate(translator)
        print("The File will be renamed from",File_list[i],"To",Photos_name)
        os.rename(File_list[i],Photos_name)
    os.chdir(Origins)

List_photos()








