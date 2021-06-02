import datetime
from tkinter import *
from tkinter.ttk import *
from tkinter import font
from tkinter.simpledialog import *
from xml.dom.minidom import parse, parseString  # minidom 모듈의 파싱 함수를 임포트합니다.
from xml.etree import ElementTree
import time
import urllib
import http.client
from xml.dom.minidom import parse, parseString


t = time.time()
today = int(time.strftime("%Y%m%d", time.localtime(t)))
hour = int(time.strftime('%H', time.localtime(t)))

weeksHour = hour
weeksToday = today

if weeksHour < 6:
    weeksHour = 18
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    yesterday = yesterday.strftime('%Y%m%d')
    weeksToday = yesterday
elif 6 <= weeksHour < 18:
    weeksHour = 6
else:
    weeksHour = 18

weeksHour = str(weeksHour)
weeksToday = str(weeksToday)
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
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    yesterday = yesterday.strftime('%Y%m%d')
    today = yesterday

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

def TodayDustLabel():
    DustLabel = Label(window, bg='cyan', width=50, height=10)
    DustLabel.pack()
    DustLabel.place(x=20, y=240)
    TodayDust()

    DustImageLabel = Label(window, bg='white')
    DustImageLabel.pack()
    DustImageLabel.place(x=40, y=260)

def WeekWeatherLabel():
    WeekLabel = Label(window, bg='hot pink', width=50, height=10)
    WeekLabel.pack()
    WeekLabel.place(x=20, y=400)
    WeekWeather()


    WeekImageLabel = Label(window, bg='white')
    WeekImageLabel.pack()
    WeekImageLabel.place(x=200, y=460)

def openNewWindow():
    global PlaceText
    FindPlace = place.get()
    newWindow = Toplevel(window)
    newWindow.title("New Window")
    newWindow.geometry("310x400")

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
    PlaceText.place(x=5, y=30)
    PlaceText.configure(state='disabled')

    TextScrollbar.config(command=PlaceText.yview)
    TextScrollbar.pack(side=RIGHT, fill=BOTH)


    quitButton = Button(newWindow, command=newWindow.destroy, text='날씨 확인')
    quitButton.pack()
    quitButton.place(x=120, y=375)

def FindButtonAction():
    FindPlace = place.get()
    global px
    global py
    global weekRain
    global weekTemperature
    if FindPlace == "서울특별시":
        px = '60'
        py = '127'
        weekRain = '11B00000'
        weekTemperature = '11B10101'
    elif FindPlace == '경기도':
        px = '60'
        py = '120'
        weekRain = '11B00000'
        weekTemperature = '11B20601'
    elif FindPlace == '강원도':
        px = '73'
        py = '134'
        weekRain = '11D10000'
        weekTemperature = '11D10401'
    elif FindPlace == '충청남도':
        px = '68'
        py = '100'
        weekRain = '11C20000'
        weekTemperature = '11C20101'
    elif FindPlace == '충청북도':
        px = '69'
        py = '107'
        weekRain = '11C10000'
        weekTemperature = '11C10301'
    elif FindPlace == '인천광역시':
        px = '55'
        py = '124'
        weekRain = '11B00000'
        weekTemperature = '11B20201'
    elif FindPlace == '경상북도':
        px = '89'
        py = '91'
        weekRain = '11H10000'
        weekTemperature = '11H10201'
    elif FindPlace == '경상남도':
        px = '91'
        py = '77'
        weekRain = '11H20000'
        weekTemperature = '11H20301'
    elif FindPlace == '전라북도':
        px = '63'
        py = '89'
        weekRain = '11F10000'
        weekTemperature = '11F10201'
    elif FindPlace == '전라남도':
        px = '51'
        py = '67'
        weekRain = '11F20000'
        weekTemperature = '21F20801'
    elif FindPlace == '부산광역시':
        px = '98'
        py = '76'
        weekRain = '11H20000'
        weekTemperature = '11H20201'
    elif FindPlace == '울산광역시':
        px = '102'
        py = '84'
        weekRain = '11H20000'
        weekTemperature = '11H20101'
    elif FindPlace == '제주특별자치도':
        px = '52'
        py = '38'
        weekRain = '11G00000'
        weekTemperature = '11G00201'
    else:
        px = '0'
        py = '0'
        weekRain = 0
        weekTemperature = 0

    SearchTodayWeather()
    SearchTodayDust()
    SearchWeakWeatherRain()
    SearchWeakWeatherTemperature()

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
            #print(strXml)
            itemElements = tree.iter('item')

            print(itemElements)

            for item in itemElements:
                fcstDate = item.find("fcstDate")
                fcstTime = item.find("fcstTime")
                category = item.find("category")
                fcstValue = item.find("fcstValue")
                if len(category.text) > 0:
                    categorys[category.text] = fcstValue.text

            print(fcstDate.text, fcstTime.text)
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

def SearchTodayDust():
    pass

def SearchWeakWeatherRain():
    categorys = dict()
    categorys.clear()
    conn = http.client.HTTPConnection("apis.data.go.kr")
    conn.request("GET", "/1360000/MidFcstInfoService/getMidLandFcst?serviceKey=nFdn9jA2fHpN1RgksG1a6Gc%2FOIjJoKwMOD1Dx0J6kftuZ06MWg2mmy27TWb52n7ONuQ6%2B%2FyWmEXYjs69QPUgNg%3D%3D&pageNo=1&numOfRows=1&dataType=XML&regId=" + weekRain + "&tmFc=" + weeksToday + weeksHour + '00')
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
            # print(strXml)
            itemElements = tree.iter('item')

            for item in itemElements:
                rnSt3Am = item.find("rnSt3Am")
                wf3Am = item.find("wf3Am")
                rnSt4Am = item.find("rnSt4Am")
                wf4Am = item.find("wf4Am")
                rnSt5Am = item.find("rnSt5Am")
                wf5Am = item.find("wf5Am")
                rnSt6Am = item.find("rnSt6Am")
                wf6Am = item.find("wf6Am")
                rnSt7Am = item.find("rnSt7Am")
                wf7Am = item.find("wf7Am")
                rnSt8 = item.find("rnSt8")
                wf8 = item.find("wf8")
                rnSt9 = item.find("rnSt9")
                wf9 = item.find("wf9")
                rnSt10 = item.find("rnSt10")
                wf10 = item.find("wf10")
                rnSt3Pm = item.find("rnSt3Pm")
                wf3Pm = item.find("wf3Pm")
                rnSt4Pm = item.find("rnSt4Pm")
                wf4Pm = item.find("wf4Pm")
                rnSt5Pm = item.find("rnSt5Pm")
                wf5Pm = item.find("wf5Pm")
                rnSt6Pm = item.find("rnSt6Pm")
                wf6Pm = item.find("wf6Pm")
                rnSt7Pm = item.find("rnSt7Pm")
                wf7Pm = item.find("wf7Pm")

    print("3일 후 AM " + wf3Am.text + " 강수확률 " + rnSt3Am.text + "%")
    print("4일 후 AM " + wf4Am.text + " 강수확률 " + rnSt4Am.text + "%")
    print("5일 후 AM " + wf5Am.text + " 강수확률 " + rnSt5Am.text + "%")
    print("6일 후 AM " + wf6Am.text + " 강수확률 " + rnSt6Am.text + "%")
    print("7일 후 AM " + wf7Am.text + " 강수확률 " + rnSt7Am.text + "%")
    print("3일 후 PM " + wf3Pm.text + " 강수확률 " + rnSt3Pm.text + "%")
    print("4일 후 PM " + wf4Pm.text + " 강수확률 " + rnSt4Pm.text + "%")
    print("5일 후 pM " + wf5Pm.text + " 강수확률 " + rnSt5Pm.text + "%")
    print("6일 후 PM " + wf6Pm.text + " 강수확률 " + rnSt6Pm.text + "%")
    print("7일 후 PM " + wf7Pm.text + " 강수확률 " + rnSt7Pm.text + "%")
    print("8일 후 " + wf8.text + " 강수확률 " + rnSt8.text + "%")
    print("9일 후 " + wf9.text + " 강수확률 " + rnSt9.text + "%")
    print("10일 후 " + wf10.text + " 강수확률 " + rnSt10.text + "%")

def SearchWeakWeatherTemperature():
    pass

bm = PhotoImage(file='image/NB01.png')
i = 0              #사진 리스트 순서 조절
def TodayWeather():
    global i
    TodayLabel = Label(window, bg='white', width=50, height=10)
    TodayLabel.pack()
    TodayLabel.place(x=20, y=80)
    i = i + 1
    if i < 0:
        TodayLabel = Label(window, image=TodayImageList, width=50, height=10)
    print(i)

def TodayDust():
    pass
def WeekWeather():
    pass


InitTopText()
Find()
FindButton()
TodayWeather()
TodayDustLabel()
WeekWeatherLabel()
window.mainloop()
