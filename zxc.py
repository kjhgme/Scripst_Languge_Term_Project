import datetime
from tkinter import *
from tkinter.ttk import *
from tkinter import font
import tkinter.messagebox
from tkinter.simpledialog import *
from xml.dom.minidom import parse, parseString  # minidom 모듈의 파싱 함수를 임포트합니다.
from xml.etree import ElementTree
import time
import urllib
import http.client
from xml.dom.minidom import parse, parseString


t = time.time()
today = int(time.strftime("%Y%m%d", time.localtime(t)))
hour = int(time.strftime('%H', time.localtime(time.time())))

today1 = datetime.datetime.now()
print(today1)

if 3 < hour <= 6:
    hour = 23
elif 6 < hour <= 9:
    hour = 2
elif 9 < hour <= 12:
    hour = 5
elif 12 < hour <= 15:
    hour = 8
elif 15 < hour <= 18:
    hour = 11
elif 18 < hour <= 21:
    hour = 14
elif 21 <= hour:
    hour = 17
elif hour <= 3:
    hour = 20
    if today % 100 - 1 == 0:
        today = today
    else:
        today = today - 1

today = str(today)

strXml = None
px = '0'
py = '0'

window = Tk()
window.title('집 밖은 위험해.')
window.geometry("400x600")
TodayImageList = []

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
    FindButton = Button(window, font=TempFont, text='검색', command=openNewWindow)
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

def openNewWindow():
    global PlaceText
    FindPlace = place.get()
    newWindow = Toplevel(window)
    newWindow.title("New Window")
    newWindow.geometry("302x400")

    placeEntry = Entry(newWindow, textvariable=place, width=20)
    placeEntry.pack()
    placeEntry.place(x=5, y=5)

    placeButton = Button(newWindow, text='검색', command=FindButtonAction)
    placeButton.pack()
    placeButton.place(x=155, y=2)

    TextScrollbar = Scrollbar(newWindow)
    TextScrollbar.pack()
    TextScrollbar.place(x=280, y=200)

    PlaceText = Text(newWindow, width=40, height=26, yscrollcommand=TextScrollbar.set)
    PlaceText.pack()
    PlaceText.place(x=0, y=30)
    PlaceText.configure(state='disabled')

    TextScrollbar.config(command=PlaceText.yview)
    TextScrollbar.pack(side=RIGHT, fill=BOTH)


    quitButton = Button(newWindow, command=newWindow.destroy, text='날씨 확인')
    quitButton.pack()
    quitButton.place(x=120, y=375)


def SearchTodayWeather():
    categorys = dict()
    categorys.clear()
    conn = http.client.HTTPConnection("apis.data.go.kr")
    conn.request("GET", "/1360000/VilageFcstInfoService/getVilageFcst?serviceKey=nFdn9jA2fHpN1RgksG1a6Gc%2FOIjJoKwMOD1Dx0J6kftuZ06MWg2mmy27TWb52n7ONuQ6%2B%2FyWmEXYjs69QPUgNg%3D%3D&pageNo=1&numOfRows=9&dataType=XML&base_date=" + today + "&base_time=0500&nx=" + px + "&ny=" + py)
    req = conn.getresponse()

    #print(req.status, req.reason)
    if req.status == 200:
        strXml = req.read().decode('utf-8')
        if strXml == None:
            print("error.")
        else:
            print("OK")         #작동하는지 확인용
            #parseData = parseString(strXml)
            tree = ElementTree.fromstring(strXml)
            print(strXml)
            itemElements = tree.iter('item')

            for item in itemElements:
                fcstDate = item.find("fcstDate")
                fcstTime = item.find("fcstTime")
                category = item.find("category")
                fcstValue = item.find("fcstValue")
                if len(category.text) > 0:
                    categorys[category.text] = fcstValue.text

    for k, v in categorys.items():
            if k == 'PTY' and v == '0':
                print('nothing')
                TodayImageList.append(PhotoImage(file='image/NB01.png'))
            elif k == 'PTY' and v == '1':
                print('비')
                TodayImageList.append(PhotoImage(file='image/NB08.png'))
            elif k == 'PTY' and v == '2':
                print('비/눈')
                TodayImageList.append(PhotoImage(file='image/NB12.png'))
            elif k == 'PTY' and v == '3':
                print('눈')
                TodayImageList.append(PhotoImage(file='image/NB11.png'))
            elif k == 'PTY' and v == '4':
                print('소나기')
                TodayImageList.append(PhotoImage(file='image/NB07.png'))
            elif k == 'PTY' and v == '5':
                print('빗방울')
                TodayImageList.append(PhotoImage(file='image/NB20.png'))
            elif k == 'PTY' and v == '6':
                print('빗방울/눈날림')
                TodayImageList.append(PhotoImage(file='image/NB22.png'))
            elif k == 'PTY' and v == '7':
                print('눈날림')
                TodayImageList.append(PhotoImage(file='image/NB21.png'))
            if k == 'SKY' and v == '1':
                print("맑음")
                TodayImageList.append(PhotoImage(file='image/NB01.png'))
            elif k == 'SKY' and v == '3':
                print("구름많음")
                TodayImageList.append(PhotoImage(file='image/NB03.png'))
            elif k == 'SKY' and v == '4':
                print("흐림")
                TodayImageList.append(PhotoImage(file='image/NB04.png'))
            if k == 'POP':
                print("강수량 : ", v, "%")
            if k == 'T3H':
                print("온도 :", v)

    TodayWeather()

bm = PhotoImage(file='image/NB01.png')
i = -1              #사진 리스트 순서 조절
def TodayWeather():
    global i
    TodayLabel = Label(window, bg='white', width=50, height=10)
    TodayLabel.pack()
    TodayLabel.place(x=20, y=80)
    i = i + 1
    if i < 0:
        TodayLabel = Label(window, image=TodayImageList, width=50, height=10)
    print(i)

def TodayDustLabel():
    DustLabel = Label(window, bg='cyan', width=50, height=10)
    DustLabel.pack()
    DustLabel.place(x=20, y=240)
    TodayDust()

def TodayDust():
    DustImageLabel = Label(window, bg='white')
    DustImageLabel.pack()
    DustImageLabel.place(x=40, y=260)


def WeekWeatherLabel():
    WeekLabel = Label(window, bg='hot pink', width=50, height=10)
    WeekLabel.pack()
    WeekLabel.place(x=20, y=400)
    WeekWeather()

def WeekWeather():
    WeekImageLabel = Label(window, bg='white')
    WeekImageLabel.pack()
    WeekImageLabel.place(x=200, y=460)

InitTopText()
Find()
FindButton()
TodayWeather()
TodayDustLabel()
WeekWeatherLabel()
window.mainloop()
