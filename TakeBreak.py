import webbrowser
import time

for i in range(3):
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=izGwDsrQ1eQ')
    print("The Song started on",time.ctime())