#Importing Modules for Python Image Steanography
from tkinter import *
from tkinter.filedialog import *
from turtle import color
from PIL import ImageTk,Image
from stegano import exifHeader as stg
from tkinter import messagebox



#Initializing the  Main Screen
Main = Tk()
Main.title("Image Steganography")
Main.geometry("500x300")
Main.config(bg="LightSkyBlue3")



#Encryption of Image File
def Encrypt():
    Main.destroy()
    EncMain = Tk()
    EncMain.title("Encrypt")
    EncMain.geometry("500x300")
    EncMain.config(bg="LightSteelBlue4")
    
    label = Label(text="Enter the message",height="1",width="15")
    label.place(relx=0.1,rely=0.2)

    entry=Entry()
    entry.place(relx=0.5,rely=0.2)

    label1 = Label(text="Name Your File",height="1",width="15")
    label1.place(relx=0.1,rely=0.3)

    SaveEntry = Entry()
    SaveEntry.place(relx=0.5,rely=0.3)

    def OpenFile():
        global FileOpen
        FileOpen=StringVar()
        FileOpen = askopenfilename(initialdir ="/Desktop",title="SelectFile",filetypes=(("only jpeg files","*jpg"),("all type of files","*.*")))

        label2 = Label(text=FileOpen,height="2")
        label2.place(relx=0.4,rely=0.5)

    def Encrypter():
        stg.hide(FileOpen,SaveEntry.get()+".jpg",entry.get())
        messagebox.showinfo("Pop Up","Successfully Encrypted!")
        
    SelectButton = Button(text="Select Image file",bd="4",command=OpenFile,height="1",width="15")
    SelectButton.place(relx=0.1,rely=0.5)

    EncryptButton=Button(text="Encrypt",bd="5",command=Encrypter)
    EncryptButton.place(relx=0.4,rely=0.7)



#Decryption of Image File
def Decrypt():
    Main.destroy()
    DecMain=Tk()
    DecMain.title("Decrypt")
    DecMain.geometry("500x300")
    DecMain.config(bg="LightSteelBlue4")
    
    def OpenFile():
        global FileOpen
        FileOpen=StringVar()
        FileOpen=askopenfilename(initialdir="/Desktop",title="Select the File",filetypes=(("only jpeg files","*jpg"),("all type of files","*.*")))
        
        label3 = Label(text=FileOpen,height="1",width="30")
        label3.place(relx=0.4,rely=0.2)

    def Decrypter():
        Message=stg.reveal(FileOpen)
        label4=Label(text=Message,bg='lightblue1')
        label4.place(relx=0.4,rely=0.6)
        
    SelectButton=Button(text="Select the file",command=OpenFile,bd="3",height="1",width="15")
    SelectButton.place(relx=0.1,rely=0.2)

    DecryptButton=Button(text="Decrypt",command=Decrypter,bd="5")
    DecryptButton.place(relx=0.4,rely=0.4)


# creating buttons
EncryptButton=Button(text="Encrypt",command=Encrypt,bd="5",height="1")
EncryptButton.place(relx=0.3,rely=0.4)

DecryptButton=Button(text="Decrypt",command=Decrypt,bd="5",height="1")
DecryptButton.place(relx=0.6,rely=0.4)


mainloop()