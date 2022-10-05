import datetime
from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
import downloader as d

singleCount = 0
playCount = 0
advanceCount = 0
my_lst = list()


def singleShow(event):
    global singleCount
    global playCount
    global advanceCount
    advanceCount = 0
    playCount = 0
    singleCount += 1

    if singleCount == 1:
        if chkVal.get() == 1:
            chkVal.set(1)
        else:
            chkVal.set(0)
        resVal.set(720)
        extVal.set('mp4')
        isSingle.set(0)

        purlLabel.grid_remove()
        path.grid_remove()
        purlEntry.grid_remove()
        ppathEntry.grid_remove()
        chkBtn.grid_remove()
        entryFrame.grid_remove()

        entryFrame.grid(row=5, column=4, rowspan=7, columnspan=8, padx=15, pady=(5, 0), sticky='nw')
        surlLabel.grid(row=1, column=0, padx=5, pady=(18, 6), sticky='n')
        path.grid(row=2, column=0, rowspan=2, padx=5, pady=5, sticky='n')
        surlEntry.grid(row=0, column=0, columnspan=5, padx=5, pady=10, ipadx=75, sticky='n')
        spathEntry.grid(row=1, column=0, columnspan=5, padx=5, pady=(5, 10), ipadx=75, sticky='n')
        chkBtn.grid(row=3, column=0, columnspan=5, padx=5, pady=5, sticky='n')
        surlEntry.focus()


def playlistShow(event):
    global singleCount
    global playCount
    global advanceCount
    advanceCount = 0
    singleCount = 0
    playCount += 1

    if playCount == 1:
        if chkVal.get() == 1:
            chkVal.set(1)
        else:
            chkVal.set(0)
        resVal.set(720)
        extVal.set('mp4')
        isSingle.set(0)

        surlLabel.grid_remove()
        path.grid_remove()
        surlEntry.grid_remove()
        spathEntry.grid_remove()
        chkBtn.grid_remove()
        entryFrame.grid_remove()

        entryFrame.grid(row=5, column=4, rowspan=7, columnspan=8, padx=15, pady=(5, 0), sticky='nw')
        purlLabel.grid(row=1, column=0, padx=5, pady=(18, 6), sticky='n')
        path.grid(row=2, column=0, rowspan=2, padx=5, pady=5, sticky='n')
        purlEntry.grid(row=0, column=0, columnspan=5, padx=5, pady=10, ipadx=75, sticky='n')
        ppathEntry.grid(row=1, column=0, columnspan=5, padx=5, pady=(5, 10), ipadx=75, sticky='n')
        chkBtn.grid(row=3, column=0, columnspan=5, padx=5, pady=5, sticky='n')
        purlEntry.focus()


def clearURL(event):
    if urlString.get() != '':
        urlString.set('')


def clearPath(event):
    if downPath.get() != '':
        downPath.set('')


def showAdvance(event):
    global advanceCount
    advanceCount += 1
    if advanceCount == 1:
        if not bool(chkVal.get()):
            sideAdvFrame.grid(row=10, column=0, rowspan=5, columnspan=4, padx=(75, 5), pady=(25, 0), sticky='n')
            radioEXTFrame.grid(row=12, column=4, rowspan=1, columnspan=8, padx=15, pady=0, sticky='nw')
            radioRESFrame.grid(row=13, column=4, rowspan=1, columnspan=8, padx=15, pady=0, sticky='nw')

            ext.grid(row=5, column=0, padx=5, pady=(18, 5), sticky='n')
            res.grid(row=11, column=0, padx=5, pady=10, sticky='n')

            p1080.grid(row=0, column=0, padx=10, pady=5, columnspan=2, sticky='n')
            p720.grid(row=0, column=3, padx=5, pady=5, columnspan=2, sticky='n')
            p480.grid(row=0, column=6, padx=10, pady=5, columnspan=2, sticky='n')
            p360.grid(row=0, column=9, padx=10, pady=5, columnspan=2, sticky='n')

            mp4.grid(row=0, column=0, padx=5, pady=5, columnspan=3, sticky='n')
            mkv.grid(row=0, column=6, padx=10, pady=5, columnspan=3, sticky='n')

            chkSingle.grid(row=4, column=0, columnspan=5, padx=5, pady=0, sticky='n')
    else:
        advanceCount = advanceCount % 2
        if bool(chkVal.get()):
            sideAdvFrame.grid_remove()
            radioEXTFrame.grid_remove()
            radioRESFrame.grid_remove()

            ext.grid_remove()
            res.grid_remove()

            p1080.grid_remove()
            p720.grid_remove()
            p480.grid_remove()
            p360.grid_remove()
            mp4.grid_remove()
            mkv.grid_remove()

            chkSingle.grid_remove()


def checkEligibility(event):
    if radioVal.get() == 0 or urlString.get() == 'https://www.youtube.com/' or \
            urlString.get() == '' or downPath.get() == 'C:/Users/':
        btn.configure(state=DISABLED)
    else:
        if chkVal.get() == 0:
            resVal.set(720)
            extVal.set('mp4')
            isSingle.set(1)
        btn.configure(state=ACTIVE)


def init_download():
    global my_lst
    if radioVal.get() == 1:
        urlType = 'single'
        url = urlString.get()
        loc = 'C:/Users/Default/Downloads/Videos/YouTube/'
        if downPath.get() != '':
            loc = downPath.get()
        fileExt = extVal.get()
        videoRes = f"{resVal.get()}p"
        singleFile = not bool(isSingle.get())
        print(f"{urlType},\t{url},\t{loc},\t{fileExt},\t{videoRes},\t{not singleFile}")
        lst = d.download_data(url, urlType, fileExt, videoRes, singleFile, loc)
    elif radioVal.get() == 2:
        urlType = 'playlist'
        url = urlString.get()
        loc = 'C:/Users/Default/Downloads/Videos/YouTube/'
        if downPath.get() != '':
            loc = downPath.get()
        videoRes = f"{resVal.get()}p"
        fileExt = extVal.get()
        singleFile = not bool(isSingle.get())
        print(f"{urlType},\t{url},\t{loc},\t{fileExt},\t{videoRes},\t{not singleFile}")
        lst = d.download_data(url, urlType, fileExt, videoRes, singleFile, loc)
    else:
        raise WindowsError
    for items in lst:
        if type(items) is type(str()):
            items = items.strip() + ', Downloaded\n'
            my_lst.append(items)
        elif type(items) is type(list()):
            for i in items:
                i = i.strip() + ', Downloaded\n'
                my_lst.append(i)


def resetAll():
    global singleCount
    global playCount
    global advanceCount

    if radioVal.get() != 0:
        singleCount = 0
        playCount = 0
        advanceCount = 0

        radioVal.set(0)
        resVal.set(720)
        extVal.set('mp4')
        isSingle.set(1)
        chkVal.set(0)

        surlLabel.grid_remove()
        purlLabel.grid_remove()
        path.grid_remove()
        surlEntry.grid_remove()
        purlEntry.grid_remove()
        spathEntry.grid_remove()
        ppathEntry.grid_remove()
        chkBtn.grid_remove()

        entryFrame.grid_remove()
        sideAdvFrame.grid_remove()
        radioEXTFrame.grid_remove()
        radioRESFrame.grid_remove()


def showHInfo():
    showinfo('Help!', 'You can access help by filling the help form which would be included soon')


def showAInfo():
    showinfo('About', 'Created by Farzam\nAll Rights Reserved by S F M Zaidi')


def toggleList():
    sec = Tk()
    width = 300
    height = 250
    sec.geometry(f'{width}x{height}')
    lbx = Listbox(sec, width=width, height=height)

    try:
        with open("Entries.csv", 'r') as fr:
            rd_lst = fr.readlines()
            for it in my_lst:
                if it not in rd_lst:
                    with open('Entries.csv', 'a') as fa:
                        fa.writeline(it.strip() + f', {datetime.datetime.now()}\n')
                        fa.close()
            fr.close()
            for i, st in zip(range(len(rd_lst)), rd_lst):
                lbx.insert(i, st)

    except FileNotFoundError:
        with open('Entries.csv', 'w') as fw:
            fw.writelines(my_lst)
            fw.close()
    finally:
        lbx.pack(fill='both')


root = Tk()
root.geometry('600x475')
root.resizable(False, False)
root.title('PyTube Downloader')

image = Image.open('uTubeDownloader.jpg')
photo = ImageTk.PhotoImage(image)
img = Label(root, image=photo)
img.place(x=0, y=0, width=600, height=475)

# Creating Menus
mainMenu = Menu(root, tearoff=0)

fileMenu = Menu(mainMenu, tearoff=0)
fileMenu.add_command(label='Reset', command=resetAll)
fileMenu.add_command(label='Exit', command=root.destroy)

helpMenu = Menu(mainMenu, tearoff=0)
helpMenu.add_command(label='Help', command=showHInfo)
helpMenu.add_separator()
helpMenu.add_command(label='About', command=showAInfo)

mainMenu.add_cascade(label='File', menu=fileMenu)
mainMenu.add_command(label='Toggle List', command=toggleList)
mainMenu.add_cascade(label='Help', menu=helpMenu)
root.config(menu=mainMenu)

# Creating Frames
mainFrame = Frame(root)
mainFrame.pack(pady=(20, 20), padx=(20, 20), fill='both')

headingFrame = Frame(mainFrame)
headingFrame.grid(row=0, column=0, rowspan=3, columnspan=12, padx=30, pady=(20, 10))

sideFrame = Frame(mainFrame)
sideFrame.grid(row=4, column=0, rowspan=6, columnspan=4, padx=(75, 5), pady=(25, 10), sticky='n')

radioURLFrame = Frame(mainFrame)
radioURLFrame.grid(row=4, column=4, rowspan=1, columnspan=8, padx=15, pady=(25, 0), sticky='nw')

entryFrame = Frame(mainFrame)

sideAdvFrame = Frame(mainFrame)
radioEXTFrame = Frame(mainFrame)
radioRESFrame = Frame(mainFrame)

btnFrame = Frame(root)
btnFrame.pack(pady=(0, 20), padx=(20, 20), fill='both')

# Creating label for Heading Frame
Label(headingFrame, text='Welcome to Python YouTube Downloader', foreground='red',
      font="Arial 17 bold").pack(pady=(10, 0), padx=(5, 5), fill='both')

# Creating labels for Side Frame
Label(sideFrame, text='Type of URL', font="Tahoma 12 bold", foreground='black',
      justify='right').grid(row=0, column=0, padx=5, pady=5)
surlLabel = Label(sideFrame, text='Video URL:', font="Tahoma 12 bold", foreground='black', justify='right')
purlLabel = Label(sideFrame, text='Playlist URL:', font="Tahoma 12 bold", foreground='black', justify='right')
path = Label(sideFrame, text='Download to', font="Tahoma 12 bold", foreground='black', justify='right')
ext = Label(sideAdvFrame, text='Extension', font="Tahoma 12 bold", foreground='black', justify='right')
res = Label(sideAdvFrame, text='Quality', font="Tahoma 12 bold", foreground='black', justify='right')

# Radio Buttons for URL Label
radioVal = IntVar(radioURLFrame)
radioVal.set(0)

single = Radiobutton(radioURLFrame, text='Single', value=1, variable=radioVal, font="Stylus 10 bold")
single.grid(row=0, column=0, padx=5, pady=5, columnspan=5)
single.bind('<Button-1>', singleShow)

playlist = Radiobutton(radioURLFrame, text='Playlist', value=2, variable=radioVal, font="Stylus 10 bold")
playlist.grid(row=0, column=6, padx=10, pady=5, columnspan=5)
playlist.bind('<Button-1>', playlistShow)

# Radio Buttons for EXT Label
extVal = StringVar(radioEXTFrame)
extVal.set('mp4')

mp4 = Radiobutton(radioEXTFrame, text='MP4', value='mp4', variable=extVal, font="Stylus 10 bold")
mkv = Radiobutton(radioEXTFrame, text='MKV', value='mkv', variable=extVal, font="Stylus 10 bold")

# Radio Buttons for RES Label
resVal = IntVar(radioRESFrame)
resVal.set(720)

p1080 = Radiobutton(radioRESFrame, text='1080p', value=1080, variable=resVal, font="Stylus 10 bold")
p720 = Radiobutton(radioRESFrame, text='720p', value=720, variable=resVal, font="Stylus 10 bold")
p480 = Radiobutton(radioRESFrame, text='480p', value=480, variable=resVal, font="Stylus 10 bold")
p360 = Radiobutton(radioRESFrame, text='360p', value=360, variable=resVal, font="Stylus 10 bold")

# Creating Entries for Values
urlString = StringVar(value='https://www.youtube.com/')
surlEntry = Entry(entryFrame, textvariable=urlString, font='Stylus 11 italic underline', foreground='blue')
surlEntry.bind('<FocusIn>', clearURL)
purlEntry = Entry(entryFrame, textvariable=urlString, font='Stylus 11 italic underline', foreground='blue')
purlEntry.bind('<FocusIn>', clearURL)

downPath = StringVar(value='C:/Users/')
spathEntry = Entry(entryFrame, textvariable=downPath, font='Stylus 11 italic bold', foreground='black')
spathEntry.bind('<FocusIn>', clearPath)
ppathEntry = Entry(entryFrame, textvariable=downPath, font='Stylus 11 italic bold', foreground='black')
ppathEntry.bind('<FocusIn>', clearPath)

# Create Checkbox
chkVal = IntVar(entryFrame)
chkBtn = Checkbutton(entryFrame, text='Advance Settings', variable=chkVal)
chkBtn.bind('<ButtonRelease-1>', showAdvance)

isSingle = IntVar(entryFrame)
chkSingle = Checkbutton(entryFrame, text='Want Single AV File', variable=isSingle)

# Create Button
btn = Button(btnFrame, text='Download', command=init_download, font="Script 20 bold", padx=5, pady=5, bg='lightgreen',
             fg='white', relief=RIDGE)
btn.pack(anchor='center', pady=5)
btn.configure(state=DISABLED)
btn.bind('<Enter>', checkEligibility)

root.mainloop()
