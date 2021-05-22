from tkinter import *
from tkinter import font
import tkinter.messagebox
from tkinter.simpledialog import *

window = Tk()
window.title('집 밖은 위험해.')
window.geometry("400x600")
TodayList = []
TodayList.append(PhotoImage(file='image/one.gif'))

def InitTopText():
    TempFont = font.Font(window, size=20, weight='bold', family='Consolas')
    MainText = Label(window, font=TempFont, text='집 밖은 위험해.')
    MainText.pack()

def Find(): #initsearchlistbox
    global FindLabel
    TempFont = font.Font(window, size=5, weight='bold', family='Consolas')
    FindLabel = Entry(window, width=15)
    FindLabel.pack()
    FindLabel.place(x=20, y=45)

def FindButton():   #initsearchbutton
    TempFont = font.Font(window, size=10, weight='bold', family='Consolas')
    FindButton = Button(window, font=TempFont, text='검색', command=FindButtonAction)
    FindButton.pack()
    FindButton.place(x=135, y=42)

def FindButtonAction(): #serchbuttonaction
    SearchTodayWeather()

def SearchTodayWeather():   #searchlibrary
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("apis.data.go.kr")
    conn.request("GET", "/1360000/VilageFcstInfoService/getVilageFcst?serviceKey=nFdn9jA2fHpN1RgksG1a6Gc%2FOIjJoKwMOD1Dx0J6kftuZ06MWg2mmy27TWb52n7ONuQ6%2B%2FyWmEXYjs69QPUgNg%3D%3D&pageNo=1&numOfRows=1&dataType=XML&base_date=20210520&base_time=0500&nx=60&ny=127")
    req = conn.getresponse()

    if req.status == 200:
        WeatherDoc = req.read().decode('utf-8')

    global TodayList
    TodayList.clear()

    TodayList.append(PhotoImage(file='image/one.gif'))


def TodayWeather():
    global TodayWeatherLabel

    TodayWeatherLabel = Label(window, width=50, height=10, bg='green')
    TodayWeatherLabel.pack()
    TodayWeatherLabel.place(x=20, y=80)


InitTopText()
Find()
FindButton()
FindButtonAction()
TodayWeather()
window.mainloop()