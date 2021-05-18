from tkinter import *

class MainGUI:
    def today(self):    #오늘의 날씨
        pass
        '''category = 
if category == POP -> 강수확률 fcstValue %
POP	강수확률	%
PTY	강수형태	코드값
R06	6시간 강수량	범주 (1 mm)
REH	습도	%
S06	6시간 신적설	범주(1 cm)
SKY	하늘상태	코드값
T3H	3시간 기온	℃
TMN	아침 최저기온	℃
TMX	낮 최고기온	℃
UUU	풍속(동서성분)	m/s
VVV	풍속(남북성분)	m/s
WAV	파고	M
VEC	풍향	deg
WSD	풍속	m/s
'''
    def dust(self):     #미세먼지 농도
        pass
    def week(self):     #중기예보
        pass
    def find(self):     #주소찾기
        pass
    def gmail(self):    #gmail로 송신
        pass
    def tel(self):      #텔레그램으로 송신
        pass
    def __init__(self):
        window = Tk()
        window.title('집 밖은 위험해.')
        frame = Frame(window)
        frame.pack()
        frame2 = Frame(window)
        frame2.pack()
        frame3 = Frame(window)
        frame3.pack()
        frame4 = Frame(window)
        frame4.pack()

        #image1 = PhotoImage(file='one.gif')

        self.place = StringVar()
        Entry(frame, textvariable=self.place, width=20).pack(side=LEFT)
        Button(frame, text='검색', command=self.find).pack(side=LEFT)     #커맨드 xml 가져오게 만들기
        Button(frame, text='telegram', command=self.tel).pack(side=RIGHT)    #텔레그램 이미지로 변경할 것
        Button(frame, text='gmail', command=self.gmail).pack(side=RIGHT)    #gmail 이미지로 변경할 것
        self.canvas1 = Canvas(frame2, width=300, height=100, bg='white')
        self.canvas1.pack()
        self.canvas2 = Canvas(frame3, width=300, height=100, bg='red')
        self.canvas2.pack()
        self.canvas3 = Canvas(frame4, width=300, height=100, bg='green')
        self.canvas3.pack()

        window.mainloop()

MainGUI()

