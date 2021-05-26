from tkinter import *
from tkinter import font
import tkinter.messagebox
from tkinter.simpledialog import *
from xml.dom.minidom import parse, parseString # minidom 모듈의 파싱 함수를 임포트합니다.
from xml.etree import ElementTree
import time
import urllib
import http.client
from xml.dom.minidom import parse, parseString

DataList =[]        #날씨
t = time.time()
today = int(time.strftime("%Y%m%d", time.localtime(t)))
hour = int(time.strftime('%H', time.localtime(time.time())))
if hour < 5:
    today = today - 1
today = str(today)

##### global
loopFlag = 1
xmlFD = -1
BooksDoc = None
px = '0'
py = '0'

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
    global place
    TempFont = font.Font(window, size=5, weight='bold', family='Consolas')
    place = StringVar()
    FindLabel = Entry(window, textvariable=place, width=15)
    FindLabel.pack()
    FindLabel.place(x=20, y=45)

def FindButton():   #initsearchbutton
    TempFont = font.Font(window, size=10, weight='bold', family='Consolas')
    FindButton = Button(window, font=TempFont, text='검색', command=FindButtonAction)
    FindButton.pack()
    FindButton.place(x=135, y=42)

def FindButtonAction():
    FindPlace = place.get()
    global px
    global py
    if FindPlace == "서울특별시":
        px = '60'
        py = '127'
    elif FindPlace == '경기도':
        px = '60'
        py = '120'
    elif FindPlace == '강원도':
        px = '73'
        py = '134'
    elif FindPlace == '충청남도':
        px = '68'
        py = '100'
    elif FindPlace == '충청북도':
        px = '69'
        py = '107'
    elif FindPlace == '인천광역시':
        px = '55'
        py = '124'
    elif FindPlace == '경상북도':
        px = '89'
        py = '91'
    elif FindPlace == '경상남도':
        px = '91'
        py = '77'
    elif FindPlace == '전라북도':
        px = '63'
        py = '89'
    elif FindPlace == '전라남도':
        px = '51'
        py = '67'
    elif FindPlace == '부산광역시':
        px = '98'
        py = '76'
    elif FindPlace == '울산광역시':
        px = '102'
        py = '84'
    elif FindPlace == '제주특별자치도':
        px = '52'
        py = '38'
    elif FindPlace == '독도':
        px = '144'
        py = '123'
    else:
        px = '0'
        py = '0'
    SearchTodayWeather()

def SearchTodayWeather():
    global DataList
    DataList.clear()
    conn = http.client.HTTPConnection("apis.data.go.kr")
    conn.request("GET", "/1360000/VilageFcstInfoService/getVilageFcst?serviceKey=nFdn9jA2fHpN1RgksG1a6Gc%2FOIjJoKwMOD1Dx0J6kftuZ06MWg2mmy27TWb52n7ONuQ6%2B%2FyWmEXYjs69QPUgNg%3D%3D&pageNo=1&numOfRows=255&dataType=XML&base_date=" + today + "&base_time=0500&nx=" + px + "&ny=" + py)
    req = conn.getresponse()
    #print(req.status, req.reason)
    if req.status == 200:
        strXml = req.read().decode('utf-8')
        if strXml == None:
            print("error.")
        else:
            print("OK")
            parseData = parseString(strXml)
            WeatherData = parseData.childNodes
            weatheritem = WeatherData[0].childNodes
            print(weatheritem[0])

    TodayWeather()

def TodayWeather():
    global TodayWeatherLabel
    global labelList
    #x  = []
    #x.append(PhotoImage(file='image/cloudy.jpg'))
    #TodayWeatherLabel = Label(window, image=x)
    TodayWeatherLabel = Label(window, width=50, height=10, bg='green')
    TodayWeatherLabel.pack()
    TodayWeatherLabel.place(x=20, y=80)




InitTopText()
Find()
FindButton()
FindButtonAction()
TodayWeather()
window.mainloop()

#시간 고치기