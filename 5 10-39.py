from tkinter import *
from tkinter.simpledialog import *
import random
class MainGUI:
    def refresh(self):
        random.shuffle(self.index)
        for i in range(4):
            self.labelList[i]['image'] = self.imageList[self.index[i]]

    def verify(self):
        fourCards = []
        for i in range(4):
            fourCards.append(1+self.index[i]%13)
        fourCards.sort()
        ex = self.answer.get() #(3+5)*5-8
        ex = ex.replace('+', ' ')
        ex = ex.replace('-', ' ')
        ex = ex.replace('*', ' ')
        ex = ex.replace('/', ' ')
        ex = ex.replace('(', ' ')
        ex = ex.replace(')', ' ') #3 5 5 8
        numbers = [eval(s) for s in ex.split()] #[3,5,5,8]
        numbers.sort()
        if fourCards != numbers:
            messagebox.showinfo('틀림', '보여지는 카드를 사용해야 합니다.')
        else:
            if eval(self.answer.get()) == 24:
                messagebox.showinfo('정확', '맞았습니다.')
            else:
                messagebox.showinfo('틀림', self.answer.get()+' 은/는 24가 아닙니다.')

    def __init__(self):
        window = Tk()
        window.title('24점 게임')
        self.index = [i for i in range(52)]
        self.imageList = []
        for i in range(1,53):
            self.imageList.append(PhotoImage(file='image/card/'+str(i)+'.gif'))
        Button(text='새로고침', command=self.refresh).pack()
        frame1 = Frame(window)
        frame1.pack()
        self.labelList = []
        for i in range(4):
            self.labelList.append(Label(frame1, image=self.imageList[i]))
            self.labelList[i].pack(side=LEFT)
        self.refresh()
        frame2 = Frame(window)
        frame2.pack()
        Label(frame2, text='수식을 입력하세요: ').pack(side=LEFT)
        self.answer = StringVar()
        Entry(frame2, textvariable=self.answer, width=20).pack(side=LEFT)
        Button(frame2, text='확인', command=self.verify).pack(side=LEFT)

        window.mainloop()

MainGUI()