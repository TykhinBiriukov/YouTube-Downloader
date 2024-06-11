from pytube import YouTube 
from tkinter import *
import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.geometry("960x500")
app.title("YouTube Downloader")
app.minsize(960, 500)
app.maxsize(960, 500)
             
Grid.rowconfigure(app,0,weight=1)
Grid.rowconfigure(app,1,weight=1)
Grid.rowconfigure(app,2,weight=1)
Grid.rowconfigure(app,3,weight=1)
Grid.rowconfigure(app,4,weight=1)
Grid.rowconfigure(app,5,weight=1)

Grid.columnconfigure(app,0,weight=1)
Grid.columnconfigure(app,1,weight=1)
Grid.columnconfigure(app,2,weight=1)
Grid.columnconfigure(app,3,weight=1)
Grid.columnconfigure(app,4,weight=1)
Grid.columnconfigure(app,5,weight=1)
Grid.columnconfigure(app,6,weight=1)

def State1Button():
    button1state = customtkinter.CTkButton(master=app, width=720, height=240, corner_radius=15, font=("", 65), text="Download Video", command=lambda: State2Actions(button1state, button1state))
    button1state.grid(row=3, pady = 100, padx = 120) 


def State2Actions(widget, widget1): 
    widget.grid_forget()
    widget1.grid_forget() 
    
    downloadFromInputButton = customtkinter.CTkButton(master=app, width=720, height=200, border_width=0, corner_radius=15, font=("", 40), text="Download From Manual Input", command=lambda: ManualLinksInput(downloadFromInputButton, downloadFromTxtButton))
    downloadFromInputButton.grid(row=1, column = 3, pady = 30)
    
    downloadFromTxtButton = customtkinter.CTkButton(master=app, width=720, height=200, border_width=0, corner_radius=15, font=("", 40), text="Read & Download From .txt File", command=lambda: TxtUrlInput(downloadFromInputButton, downloadFromTxtButton))
    downloadFromTxtButton.grid(row=4, column = 3, pady = 30)

    
def ManualLinksInput(downloadFromInputButton, downloadFromTxtButton):
    downloadFromInputButton.grid_forget()
    downloadFromTxtButton.grid_forget()
    
    labeToDownloadlLink = customtkinter.CTkLabel(master=app, text="Enter downloading link: ", font=("", 30))
    labeToDownloadlLink.grid(row=1, column=1, columnspan=2)
    
    linkInput=customtkinter.StringVar()
    linkEntry = tkinter.Entry(master=app,textvariable = linkInput, font=("",25), width=20)
    linkEntry.grid(row=2, column=1, columnspan=2)
    
    labeWhereToDownload = customtkinter.CTkLabel(master=app, text="Enter downloading path: ", font=("", 30))
    labeWhereToDownload.grid(row=1, column=4, columnspan=2)
    
    passInput=customtkinter.StringVar()
    passEntery = tkinter.Entry(master=app,textvariable = passInput, font=("",25), width=20)
    passEntery.grid(row=2, column=4, columnspan=2)
    
    submitButton = customtkinter.CTkButton(app, height= 120, width= 350, border_width=0, corner_radius=15, font=("",40), text = "Submit", command=lambda: ManualInputDownloadComplete(labeToDownloadlLink, linkEntry, labeWhereToDownload, passEntery, submitButton, passInput, linkInput, errorMassage))  
    submitButton.grid(row=3, rowspan=3, column=1, columnspan=5)
    
    errorMassage = customtkinter.CTkLabel(master=app, text="Please enter valid link and path", font=("", 25))


def ManualInputDownloadComplete(labeToDownloadlLink, linkEntry, labeWhereToDownload, passEntery, submitButton, passInput, linkInput, errorMassage):
    try:
        Downloding(passInput, linkInput)
        
        labeToDownloadlLink.grid_forget()
        linkEntry.grid_forget()
        labeWhereToDownload.grid_forget()
        passEntery.grid_forget()
        submitButton.grid_forget()
        errorMassage.grid_forget()

        dowloadFinishedlabel = customtkinter.CTkLabel(master=app, text="Video is succesfully downloaded!", font=("", 40))
        dowloadFinishedlabel.grid(row=2, column=1, columnspan=5)
        
        askForAnotherDownload = customtkinter.CTkButton(master=app, height= 200, width= 700, border_width=0, corner_radius=15, font=("",40), text = "Download Another Video", command=lambda: State2Actions(dowloadFinishedlabel, askForAnotherDownload))
        askForAnotherDownload.grid(row=3, rowspan=3, column=1, columnspan=5)

    except:
        submitButton.grid(row=4, rowspan=2, column=1, columnspan=5)
        
        errorMassage.grid(row=3, column=1, columnspan=5)


def Downloding(passInput, linkInput):
    videoUrl=linkInput.get()
    pathToDownload=passInput.get()
#https://www.youtube.com/watch?v=dQw4w9WgXcQ
#D:\Programming\Projects\YouTube_Downloader\Download Test
    youtube = YouTube(videoUrl)
    video = youtube.streams.get_highest_resolution()
    video.download(pathToDownload)
    
    
def TxtUrlInput(downloadFromInputButton, downloadFromTxtButton):
    downloadFromInputButton.grid_forget()
    downloadFromTxtButton.grid_forget()
    
    labeToDownloadlTxt = customtkinter.CTkLabel(master=app, text="Enter path to txt file: ", font=("", 30))
    labeToDownloadlTxt.grid(row=1, column=1, columnspan=2)
    
    txtInput=customtkinter.StringVar()
    txtLinkEntry = tkinter.Entry(master=app,textvariable = txtInput, font=("",25), width=20)
    txtLinkEntry.grid(row=2, column=1, columnspan=2)
    
    labeWhereToDownload = customtkinter.CTkLabel(master=app, text="Enter downloading path: ", font=("", 30))
    labeWhereToDownload.grid(row=1, column=4, columnspan=2)
    
    passInput=customtkinter.StringVar()
    passEntery = tkinter.Entry(master=app,textvariable = passInput, font=("",25), width=20)
    passEntery.grid(row=2, column=4, columnspan=2)
    
    submitButton = customtkinter.CTkButton(app, height= 120, width= 350, border_width=0, corner_radius=15, font=("",40), text = "Submit", command=lambda: TxtInputDownloadComplete(labeToDownloadlTxt, txtLinkEntry, labeWhereToDownload, passEntery, submitButton, passInput, txtInput, errorMassage))  
    submitButton.grid(row=3, rowspan=3, column=1, columnspan=5)
    
    errorMassage = customtkinter.CTkLabel(master=app, text="Please make sure that every link is written from new line and path is valid", font=("", 23))


def TxtInputDownloadComplete(labeToDownloadlTxt, txtLinkEntry, labeWhereToDownload, passEntery, submitButton, passInput, txtInput, errorMassage):
    try:
        DownlodingFromTxt(passInput, txtInput)
        
        labeToDownloadlTxt.grid_forget()
        txtLinkEntry.grid_forget()
        labeWhereToDownload.grid_forget()
        passEntery.grid_forget()
        submitButton.grid_forget()
        errorMassage.grid_forget()

        dowloadFinishedlabel = customtkinter.CTkLabel(master=app, text="Video is succesfully downloaded!", font=("", 40))
        dowloadFinishedlabel.grid(row=2, column=1, columnspan=5)
        
        askForAnotherDownload = customtkinter.CTkButton(master=app, height= 200, width= 700, border_width=0, corner_radius=15, font=("",40), text = "Download Another Video", command=lambda: State2Actions(dowloadFinishedlabel, askForAnotherDownload))
        askForAnotherDownload.grid(row=3, rowspan=3, column=1, columnspan=5)

    except:
        submitButton.grid(row=4, rowspan=2, column=1, columnspan=5)
        
        errorMassage.grid(row=3, column=0, columnspan=7)


def DownlodingFromTxt(passInput, txtInput):
    txtPass=txtInput.get()
    pathToDownload=passInput.get()
    
    txtFile = open(txtPass, "r")
    for i in txtFile:      
        youtube = YouTube(i)
        video = youtube.streams.get_highest_resolution()
        video.download(pathToDownload) 


State1Button()
app.mainloop()