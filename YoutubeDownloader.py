from tkinter import *
from tkinter import filedialog
from pytube import YouTube

root = Tk()
root.title('Youtube Video Downloader')
root.geometry('450x80')

def set_path():
    path=filedialog.askdirectory()
    textfield2.delete(0,END)
    textfield2.insert(0,path)

def download():
    video_url = textfield1.get()
    path=textfield2.get()
    video_obj = YouTube(video_url)
    stream = video_obj.streams.get_highest_resolution( )
    stream.download(path)
    label1 = Label(root,text='Download completed :)').grid(row=2,column=0) 
    
label1 = Label(root,text='Paste url here').grid(row=0,column=0)   
button1 = Button(root,text = 'Start download',command=download,padx=5,fg='black',bg='cyan')
button2 = Button(root,text = 'set download path',padx=5,command=set_path,fg='blue',bg='white')
button1.grid(row = 2, column = 1)
button2.grid(row = 1, column = 0)
textfield1 = Entry(root,width=50)
textfield2 = Entry(root,width=50)
textfield1.grid(row=0,column=1)
textfield2.grid(row=1,column=1)

root.mainloop()
