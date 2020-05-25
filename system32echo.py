try:
	import tkinter
except ImportError:
	import Tkinter as tkinter
import os

mainWindow = tkinter.Tk()
mainWindow.title("System 32 files ")
mainWindow.geometry('680x480-8-200')
label = tkinter.Label(mainWindow, text='tkinter test demo')
label.grid(column=0, row=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

filesList = tkinter.Listbox(mainWindow)
filesList.grid(column=0, row=1, sticky='nsew', rowspan='2')
filesList.config(border=2, relief='sunken')
for zone in os.listdir('/Windows/System32'):
	filesList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=filesList.yview)
listScroll.grid(column=1, row=1, sticky='nsw', rowspan=2)
filesList['yscrollcommand'] = listScroll.set

optionFrame = tkinter.LabelFrame(mainWindow, text="file details")
optionFrame.grid(column=3, row=1, sticky='ne')
rbValue = tkinter.IntVar()
rbValue.set(3)

radio1 = tkinter.Radiobutton(optionFrame, text='filename', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text='timestamp', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text='path', value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

timeFrame = tkinter.LabelFrame(mainWindow, text='time')
timeFrame.grid(row='3', column='0', sticky='new')
hourSpinner = tkinter.Spinbox(timeFrame, width='2', values=tuple(range(0, 24)))
minutesSpinner = tkinter.Spinbox(timeFrame, width='2', from_=0, to=59)
secondsSpinner = tkinter.Spinbox(timeFrame, width='2', from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minutesSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondsSpinner.grid(row=0, column=4)
timeFrame['padx']=36

resultLabel = tkinter.Label(mainWindow, text='result')
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='nwe')
yearLabel = tkinter.Label(dateFrame, text='years')
monthLabel = tkinter.Label(dateFrame, text='months')
daysLabel = tkinter.Label(dateFrame, text='days')
yearLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
daysLabel.grid(row=0, column=2, sticky='w')
yearSpin = tkinter.Spinbox(dateFrame, width=4, from_=2000, to=2099)
monthSpin = tkinter.Spinbox(dateFrame, width=4,values=('jan', 'feb', 'mar', 'apr', 'mai', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'))
daySpin = tkinter.Spinbox(dateFrame, width=4, from_=1, to=31)
yearSpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
daySpin.grid(row=1, column=2)
dateFrame['padx']=36
okButton=tkinter.Button(mainWindow,text='OK')
okButton.grid(row=4,column=3,sticky='e')
cancelButton=tkinter.Button(mainWindow,text='Cancel',command=mainWindow.quit)
cancelButton.grid(row=4,column=4,sticky='w')

mainWindow.mainloop()
