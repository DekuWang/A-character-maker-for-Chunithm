"""GUI, user can interact with the program here"""
# Built-in Modules
import os
import sys
import tkinter as tk
from tkinter import filedialog, Button, messagebox
from tkinter.scrolledtext import ScrolledText

# Third Party Modules
from PIL import Image, ImageTk

# Project Modules
sys.path.append("functions")
from functions.checkID import checkID
from functions.class_chara import Chara
from functions.class_work import Work

CharaList: list[Chara] = []

# will create a new window
# used to show current chara list
def view_chara_list():
    """
    for viewing the current character list
    """

    chara_list_window = tk.Toplevel()
    chara_list_window.geometry("300x350")

    # setup safe exit
    def close_window():
        chara_list_window.destroy()

    # exit when click X
    chara_list_window.protocol("WM_DELETE_WINDOW", lambda: close_window())

    # show_chara_list
    show_chara_list = tk.Label(chara_list_window, text = "Chara List:")
    show_chara_list.place(x = 50, y = 50, width=100, height=25)

    # Display all Character and their Images here
    list_area = ScrolledText(chara_list_window, width=30, height=15)
    list_area.grid(row=2, column=0, padx=10, pady=10)
    list_area.images = []
    for i in CharaList:
        temp_name_list = i.getname_str()
        temp_png_list = i.get_image()
        print(temp_png_list)
        # for j in range(len(temp_name_list)):
        #     list_area.insert(tk.END, temp_name_list[j] + "\n")
        #     temp_img = Image.open(temp_png_list[j]).resize((64, 64))
        #     temp_img = ImageTk.PhotoImage(temp_img)

        #     list_area.image_create(tk.END, padx=5, pady=5, image=temp_img)
        #     list_area.images.append(temp_img)
        #     list_area.insert(tk.END, "\n")

        for j in enumerate(temp_name_list):
            list_area.insert(tk.END, j[1] + "\n")
            temp_img = Image.open(temp_png_list[j[0]]).resize((64, 64))
            temp_img = ImageTk.PhotoImage(temp_img)

            list_area.image_create(tk.END, padx=5, pady=5, image=temp_img)
            list_area.images.append(temp_img)
            list_area.insert(tk.END, "\n")

    #exit_button
    exit_button = Button(chara_list_window, text="Exit",command = lambda: close_window())
    exit_button.place(x = 100, y = 300, width=100, height=50)

def create_character(win = None):
    """
    function for creating a new character
    """
    root = tk.Toplevel()
    root.geometry("550x350")
    root.lift()

    # name_text
    name_text = tk.Label(root, text="Name:")
    name_text.place(x = 350, y = 50, width=50, height=25)
    # name_entry
    name_entry = tk.Entry(root)
    name_entry.place(x = 400, y = 50, width=100, height=25)

    # id_text
    id_text = tk.Label(root, text="ID:")
    id_text.place(x = 340, y = 100, width=50, height=25)
    # id_entry
    id_entry = tk.Entry(root)
    id_entry.place(x = 400, y = 100, width=100, height=25)

    # show_img
    img = ""
    show_img = tk.Label(root, image = img)
    show_img.place(x = 23, y = 50)

    # PS
    tk.Label(root,
             text="*preview might seems starange if input image is not square",
             font=("Arial", 8)).place(x = 23, y = 300)
    tk.Label(root,
             text = "*but it will be croped to square in output",
             font=("Arial", 8)).place(x = 23, y = 317)

    # choose_img function
    def choose_img():
        try:
            global file_path
            file_path = filedialog.askopenfilename()
            img = Image.open(file_path)
            img = img.resize((250, 250))
            img = ImageTk.PhotoImage(img)
            show_img.configure(image = img)
            # Why image doesn't show up without this line?
            show_img.image = img
        except AttributeError:
            pass
        root.lift()

    # choose_img_button
    choose_img_button = Button(root, text="Choose Image",command = lambda: choose_img())
    choose_img_button.place(x = 25, y = 25, width=100, height=25)

    # setup safe exit
    def close_window():
        win.attributes("-disabled", 0)
        root.destroy()

    # exit when click X
    root.protocol("WM_DELETE_WINDOW", lambda: close_window())

    # finish function
    def append_chara(name, ID):
        if name == "" or ID == "":
            messagebox.showerror("Error", "Please enter name and ID.")
            root.lift()
            return
        elif not checkID(ID):
            messagebox.showerror("Error",
                                 "Please enter a correct character ID(ID should be exact 4 NUMBER).")
            root.lift()
            return
        elif show_img.image == "":
            messagebox.showerror("Error", "Please choose an image.")
            root.lift()
            return
        else:
            CharaList.append(Chara(name, ID, file_path))
       
    def finish_chara(name, ID):
        try:
            append_chara(name, ID)
            close_window()
        except AttributeError:
            messagebox.showerror("Error", "Please choose an image.")
            root.lift()
            return

    # finish_button
    finish_button = Button(root, text="Done",
                           command = lambda: finish_chara(name_entry.get(),
                                                          id_entry.get()))
    finish_button.place(x = 380, y = 220, width=100, height=25)

    def addtransform(name, ID):
        append_chara(name, ID)
        transform_win()

    # add_transform_button
    add_transform_button = Button(root,
                                  text="Add Transform",
                                  command = lambda: addtransform(name_entry.get(), id_entry.get()))
    add_transform_button.place(x = 380, y = 260, width=100, height=25)

    def transform_win():
        if len(CharaList[len(CharaList)-1].get_image()) > 8:
            add_transform_button.configure(state="disabled")
        # id_text
        id_text.destroy()
        # id_entry
        id_entry.destroy()

        # ranl_text
        rank_text = tk.Label(root, text="Transfer Rank:")
        rank_text.place(x = 305, y = 100, width=100, height=25)
        # rank_entry
        rank_entry = tk.Entry(root)
        rank_entry.place(x = 400, y = 100, width=100, height=25)

        # show_img
        show_img.image = ""

        def entry_processing():
            """
            Function for chjecking the user input,
            There should be an image and the numeric rank
            If requirements meet, the entry will be added to the current character
            """
            if file_path is None:
                messagebox.showerror("Error", "Please choose an image.")
                root.lift()
                return
            elif rank_entry.get() == "" or not rank_entry.get().isnumeric():
                messagebox.showerror("Error", "Please enter a correct rank.")
                root.lift()
                return
            CharaList[len(CharaList)-1].add_image(file_path)
            CharaList[len(CharaList)-1].addname_str(name_entry.get())
            print(rank_entry.get())
            CharaList[len(CharaList)-1].transfer_rank.append(rank_entry.get())


        def transform_finish():
            """
            finish the transform
            """
            entry_processing()
            close_window()

        finish_button.configure(command= lambda: transform_finish())

        def add_more_transform():
            """
            add more transform
            """
            entry_processing()
            transform_win()

        add_transform_button.configure(command= lambda: add_more_transform())

    # exit_button
    exit_button = Button(root, text="Exit",command = lambda: close_window())
    exit_button.place(x = 380, y = 300, width=100, height=25)

    root.mainloop()

def main():
    """
    The main function for the GUI
    """
    root = tk.Tk()
    root.geometry("300x350")
    root.attributes("-top")

    def open_create_character(win = root):
        win.attributes("-disabled", 1)
        create_character(win)

    def generate_file():
        for i in CharaList:
            i.xml_edit()
            i.to_dds()
        Work(514, "自製").edit_xml()
        messagebox.showinfo("Done", "Done.")

    create_button = Button(root, text="CreateChar",command = lambda: open_create_character())
    create_button.place(x = 100, y = 50, width=100, height=50)

    view_button = Button(root, text="ViewChar",command = lambda: view_chara_list())
    view_button.place(x = 100, y = 125, width=100, height=50)

    generate_button = Button(root, text="Generate File",command = lambda: generate_file())
    generate_button.place(x = 100, y = 200, width=100, height=50)

    exit_button = Button(root, text="Exit",command = lambda: root.destroy())
    exit_button.place(x = 100, y = 275, width=100, height=50)

    root.mainloop()

if __name__ == "__main__":
    main()
    os.system('pause')
