"""
Created on Sun Nov 29 20:39:36 2020
@author: Mu-Ping
"""

import hashlib
import tkinter as tk
from os import listdir
from os.path import join
from tkinter import ttk
from tkinter.filedialog import (askopenfilename, askdirectory)
from tkinter import messagebox

def selectpath():
    if(convergence.get()==0):
        path_str = askopenfilename()
        path.set(path_str)
    elif(convergence.get()==1):
        path_str = askdirectory()
        path.set(path_str)

def encryption():
    global count
    
    if(data_combobox.current()==0):
        encryption = hashlib.md5()
    elif(data_combobox.current()==1):
        encryption = hashlib.sha1()
    
    if(convergence.get()==0):
        with open(path.get(), "rb") as f:
            buf = f.read()
            encryption.update(buf)
    elif(convergence.get()==1):
        files = listdir(path.get())
        for f in files:
            fullpath = join(path.get(), f)
            with open(fullpath, "rb") as f:
                buf = f.read()
                encryption.update(buf)

    count+=1
    if(count==1):
        record1_method.set(file[data_combobox.current()])
        record1_file.set(path.get())
        record1_hash.set(encryption.hexdigest())
    elif(count==2):
        record2_method.set(file[data_combobox.current()])
        record2_file.set(path.get())
        record2_hash.set(encryption.hexdigest())
        start['state'] = tk.DISABLED
        
def delete():
    global count
    count=0
    start['state'] = tk.NORMAL
    record1_method.set("")
    record1_file.set("")
    record1_hash.set("")
    record2_method.set("")
    record2_file.set("")
    record2_hash.set("")
def verif():
    if(record1_method.get()!=record2_method.get()):
        messagebox.showwarning("警告","請使用同個加密方法")
    elif(record1_file.get()!=record2_file.get()):
        messagebox.showwarning("警告","請使用相同檔案驗證")
    else:
        if((record1_hash.get()==record2_hash.get())):
            messagebox.showinfo("結果","完整性完好")    
        else:
            messagebox.showwarning("警告","完整性遭破壞")
window = tk.Tk()
window.geometry("650x520")
window.resizable(False, False)
window.title("MD5/SHA 檔案完整性驗證器")
count = 0

file=["MD5", "SHA"]
setting = tk.Frame(window)
setting.grid(row=0, column=0, columnspan=4, padx=10)
tk.Label(setting, font=("微軟正黑體", 12, "bold"), text="選擇加密方法").grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=4)
data_combobox = ttk.Combobox(setting, value=file, state="readonly") #readonly為只可讀狀態
data_combobox.current(0)
data_combobox.grid(row=1, column=0, columnspan=3, sticky=tk.W, pady=1)
convergence = tk.IntVar() #判斷加密條件
path = tk.StringVar()
tk.Label(setting, font=("微軟正黑體", 12, "bold"), text="選擇加密目標").grid(row=2, column=0, columnspan=3, sticky=tk.W, pady=4)
tk.Radiobutton(setting, font=("微軟正黑體", 10, "bold"), text="檔案", variable=convergence, value=0).grid(row=3, columnspan=3, sticky=tk.W)
tk.Radiobutton(setting, font=("微軟正黑體", 10, "bold"), text="資料夾", variable=convergence, value=1).grid(row=4, columnspan=3, sticky=tk.W)
tk.Label(setting, font=("微軟正黑體", 12, "bold"), text="目標路徑").grid(row=5, column=0, sticky=tk.W)
tk.Entry(setting, width=80, textvariable=path).grid(row=6, column=0, columnspan=10, sticky=tk.W)
tk.Button(setting, text='路徑選擇', command=selectpath).grid(row=6, column=10, sticky=tk.W, padx=2)
start = tk.Button(setting, text='開始加密', command=encryption)
start.grid(row=7, column=0, sticky=tk.W, padx=2)
tk.Button(setting, text='清除紀錄', command=delete).grid(row=7, column=1, sticky=tk.W, padx=2)

result_1 = tk.Frame(window)
result_1.grid(row=1, column=0, sticky=tk.NW, padx=10, pady=10)
record1_method = tk.StringVar()
record1_file = tk.StringVar()
record1_hash = tk.StringVar()

tk.Label(result_1, font=("微軟正黑體", 12, "bold"), text="紀錄一").grid(row=0, column=0, sticky=tk.W, pady=2)
tk.Label(result_1, font=("微軟正黑體", 10, "bold"), text="加密方法：").grid(row=1, column=0, sticky=tk.W, pady=1)
tk.Label(result_1, font=("微軟正黑體", 10, "bold"), textvariable=record1_method).grid(row=1, column=1, sticky=tk.W, pady=2)
tk.Label(result_1, font=("微軟正黑體", 10, "bold"), text="檔案/資料夾：").grid(row=2, column=0, sticky=tk.W, pady=1)
tk.Label(result_1, font=("微軟正黑體", 10, "bold"), textvariable=record1_file).grid(row=2, column=1, sticky=tk.W, pady=2)
tk.Label(result_1, font=("微軟正黑體", 10, "bold"), text="雜湊值：").grid(row=3, column=0, sticky=tk.W, pady=1)
tk.Label(result_1, font=("微軟正黑體", 10, "bold"), textvariable=record1_hash).grid(row=3, column=1, sticky=tk.W, pady=2)

result_2 = tk.Frame(window)
result_2.grid(row=2, column=0, sticky=tk.NW, padx=10)
record2_method = tk.StringVar()
record2_file = tk.StringVar()
record2_hash = tk.StringVar()

tk.Label(result_2, font=("微軟正黑體", 12, "bold"), text="紀錄二").grid(row=0, column=0, sticky=tk.W, pady=2)
tk.Label(result_2, font=("微軟正黑體", 10, "bold"), text="加密方法：").grid(row=1, column=0, sticky=tk.W, pady=1)
tk.Label(result_2, font=("微軟正黑體", 10, "bold"), textvariable=record2_method).grid(row=1, column=1, sticky=tk.W, pady=2)
tk.Label(result_2, font=("微軟正黑體", 10, "bold"), text="檔案/資料夾：").grid(row=2, column=0, sticky=tk.W, pady=1)
tk.Label(result_2, font=("微軟正黑體", 10, "bold"), textvariable=record2_file).grid(row=2, column=1, sticky=tk.W, pady=2)
tk.Label(result_2, font=("微軟正黑體", 10, "bold"), text="雜湊值：").grid(row=3, column=0, sticky=tk.W, pady=1)
tk.Label(result_2, font=("微軟正黑體", 10, "bold"), textvariable=record2_hash).grid(row=3, column=1, sticky=tk.W, pady=2)


verification = tk.Frame(window)
verification.grid(row=3, column=0, sticky=tk.NW, pady=10, padx=10)
tk.Button(verification, text='驗證', command=verif).grid(row=0, column=0, sticky=tk.W, padx=2)

window.mainloop()