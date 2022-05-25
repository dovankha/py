import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mssv_b_4


def initGUI():
    def save():
        if v.get() == 1:
            rs = mssv_b_4.encodeMorseFile(
                filePath.get(), "encode_morse_"+filePath.get())
            if rs == True:
                messagebox.showinfo(title="Thông tin đã được lưu",
                                    message="Tập tin mã hóa được lưu: encode_morse_" + entry1.get())
            else:
                messagebox.showerror("Kiểm tra lại dữ liệu",
                                     message="Kiểm tra lại dữ liệu")
        if v.get() == 2:
            rs = mssv_b_4.decodeMorseFile(
                filePath.get(), "decode_morse_"+filePath.get())
            if rs == True:
                messagebox.showinfo(title="Thông tin đã được lưu",
                                    message="Tập tin mã hóa được lưu: decode_morse_" + entry1.get())
            else:
                messagebox.showerror("Kiểm tra lại dữ liệu",
                                     message="Kiểm tra lại dữ liệu")

    def clear():
        filePath.set("text.txt")
        v.set(1)

    def quit():
        exit()

    main = Tk()
    main.title("MSSV - Thực hành Python - Nhóm 3")
    canvas1 = tk.Canvas(main, width=400, height=200)
    canvas1.pack()

    label1 = tk.Label(main, text='Encode/Decode Morse')
    label1.config(font=('helvetica', 14))
    canvas1.create_window(220, 25, window=label1)

    labelFilePath = tk.Label(main, text='Type Path File:')
    labelFilePath.config(font=('helvetica', 10))
    canvas1.create_window(100, 80, window=labelFilePath)

    filePath = tk.StringVar()
    filePath.set("text.txt")
    entry1 = tk.Entry(main, width=30, textvariable=filePath)
    canvas1.create_window(280, 80, window=entry1)

    v = tk.IntVar()
    v.set(1)
    radioEncode = tk.Radiobutton(
        main, width=40, text="Encode", variable=v, value=1)
    radioDecode = tk.Radiobutton(
        main, width=40, text="Decode", variable=v, value=2)
    canvas1.create_window(220, 120, window=radioEncode)
    canvas1.create_window(220, 140, window=radioDecode)

    buttonSave = tk.Button(text='Save', width=10, command=save)
    canvas1.create_window(100, 180, window=buttonSave)

    buttonClear = tk.Button(text='Clear', width=10, command=clear)
    canvas1.create_window(200, 180, window=buttonClear)

    buttonQuit = tk.Button(text='Quit', width=10, command=quit)
    canvas1.create_window(300, 180, window=buttonQuit)

    main.mainloop()


initGUI()
