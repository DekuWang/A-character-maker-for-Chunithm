import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, Button, messagebox
from tkinter.scrolledtext import ScrolledText
from functions.checkID import checkID
from functions.classChara import Chara

CharaList = []

# will create a new window
# used to show current chara list
def viewCharaList():
    charaListWindow = tk.Toplevel()
    charaListWindow.geometry("300x350")

    # setup safe exit
    def closeWindow():
        charaListWindow.destroy()
        
    # exit when click X
    charaListWindow.protocol("WM_DELETE_WINDOW", lambda: closeWindow())
    
    # showCharaList
    showCharaList = tk.Label(charaListWindow, text = "Chara List:")
    showCharaList.place(x = 50, y = 50, width=100, height=25)

    # Display all Character and their Images here
    listArea = ScrolledText(charaListWindow, width=30, height=15)
    listArea.grid(row=2, column=0, padx=10, pady=10)
    listArea.images = []
    for i in CharaList:
        tempNameList = i.getNameStr()
        tempPNGList = i.getPng()
        print(tempPNGList)
        for j in range(len(tempNameList)):
            listArea.insert(tk.END, tempNameList[j] + "\n")
            tempImg = Image.open(tempPNGList[j]).resize((64, 64))
            tempImg = ImageTk.PhotoImage(tempImg)

            listArea.image_create(tk.END, padx=5, pady=5, image=tempImg)
            listArea.images.append(tempImg)
            listArea.insert(tk.END, "\n")

    #exitButton
    exitButton = Button(charaListWindow, text="Exit",command = lambda: closeWindow())
    exitButton.place(x = 100, y = 300, width=100, height=50)

def createChar(win = None):
    root = tk.Toplevel()
    root.geometry("550x350")
    root.lift()

    # nameText
    nameText = tk.Label(root, text="Name:")
    nameText.place(x = 350, y = 50, width=50, height=25)
    # nameEntry
    nameEntry = tk.Entry(root)
    nameEntry.place(x = 400, y = 50, width=100, height=25)

    # idText
    idText = tk.Label(root, text="ID:")
    idText.place(x = 340, y = 100, width=50, height=25)
    # idEntry
    idEntry = tk.Entry(root)
    idEntry.place(x = 400, y = 100, width=100, height=25)   
    
    # showImg
    img = ""
    showImg = tk.Label(root, image = img)
    showImg.place(x = 23, y = 50)

    # PS
    PS = tk.Label(root, text="*preview might seems starange if input image is not square", font=("Arial", 8)).place(x = 23, y = 300)
    PS1 = tk.Label(root, text = "*but it will be croped to square in output", font=("Arial", 8)).place(x = 23, y = 317)

    # chooseImg function
    def chooseImg():
        try:
            global file_path
            file_path = filedialog.askopenfilename()
            img = Image.open(file_path)
            img = img.resize((250, 250))
            img = ImageTk.PhotoImage(img)
            showImg.configure(image = img)
            # Why image doesn't show up without this line?
            showImg.image = img
        except AttributeError:
            pass
        root.lift()
    
    # chooseImgButton
    chooseImgButton = Button(root, text="Choose Image",command = lambda: chooseImg())
    chooseImgButton.place(x = 25, y = 25, width=100, height=25)

    # setup safe exit
    def closeWindow():
        win.attributes("-disabled", 0)
        root.destroy()

    # exit when click X
    root.protocol("WM_DELETE_WINDOW", lambda: closeWindow())

    # finish function
    def appendChara(name, ID):
        if name == "" or ID == "":
            messagebox.showerror("Error", "Please enter name and ID.")
            root.lift()
            return
        elif not checkID(ID):
            messagebox.showerror("Error", "Please enter a correct character ID(ID should be exact 4 NUMBER).")
            root.lift()
            return
        elif showImg.image == "":
            messagebox.showerror("Error", "Please choose an image.")
            root.lift()
            return
        else:
            CharaList.append(Chara(name, ID, file_path))
            
    def finishChara(name, ID):
        try:
            appendChara(name, ID)
            closeWindow()
        except AttributeError:
            messagebox.showerror("Error", "Please choose an image.")
            root.lift()
            return

    # finishButton
    finishButton = Button(root, text="Done",command = lambda: finishChara(nameEntry.get(), idEntry.get()))
    finishButton.place(x = 380, y = 220, width=100, height=25)

    def addtransform(name, ID):
        appendChara(name, ID)
        transformWin()

    # addtransformButton
    addtransformButton = Button(root, text="Add Transform",command = lambda: addtransform(nameEntry.get(), idEntry.get()))
    addtransformButton.place(x = 380, y = 260, width=100, height=25)

    def transformWin():
        if len(CharaList[len(CharaList)-1].getPng()) > 3:
            addtransformButton.configure(state="disabled")
        # idText
        idText.destroy()
        # idEntry
        idEntry.destroy()  
        
        # showImg
        showImg.image = ""

        def transformFinish():
            if file_path == None:
                messagebox.showerror("Error", "Please choose an image.")
                root.lift()
                return
            CharaList[len(CharaList)-1].addPng(file_path)
            CharaList[len(CharaList)-1].addNameStr(nameEntry.get())
            closeWindow()

        finishButton.configure(command= lambda: transformFinish())

        def addMoreTransform():
            if file_path == None:
                messagebox.showerror("Error", "Please choose an image.")
                root.lift()
                return
            CharaList[len(CharaList)-1].addPng(file_path)
            CharaList[len(CharaList)-1].addNameStr(nameEntry.get())
            transformWin()
        
        addtransformButton.configure(command= lambda: addMoreTransform())

    # exitButton
    exitButton = Button(root, text="Exit",command = lambda: closeWindow())
    exitButton.place(x = 380, y = 300, width=100, height=25)

    root.mainloop()

def main():
    root = tk.Tk()
    root.geometry("300x350")
    root.attributes("-top")

    def openCreateChar(win = root):
        win.attributes("-disabled", 1)
        createChar(win)

    def generateFile():
        for i in CharaList:
            i.xmlEdit()
            i.ToDDS()
        messagebox.showinfo("Done", "Done.")
    
    createButton = Button(root, text="CreateChar",command = lambda: openCreateChar())
    createButton.place(x = 100, y = 50, width=100, height=50)

    viewButton = Button(root, text="ViewChar",command = lambda: viewCharaList())
    viewButton.place(x = 100, y = 125, width=100, height=50)

    GenerateButton = Button(root, text="Generate File",command = lambda: generateFile())
    GenerateButton.place(x = 100, y = 200, width=100, height=50)

    exitButton = Button(root, text="Exit",command = lambda: root.destroy())
    exitButton.place(x = 100, y = 275, width=100, height=50)

    root.mainloop()

if __name__ == "__main__":
    main()




