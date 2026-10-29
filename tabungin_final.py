import tkinter as tk
from tkinter import ttk
import json
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("400x700")
root.title("Tabungin")
root.resizable(width=False,height=False)

dark_theme = False

warna1 = "#0F52BA"
warna2 = "#E9EAEC" # putih abu
warna3 = "#979797"
warna4 = "#000000"
warna5 = "#0DAA1B"
warna6 = "#B90F0F"
warna7 = "#FFFFFF" # putih

size1 = (25, 25)
size2 = (50,50)

gambar1= Image.open("icon/edit.png")
resized_image1 = gambar1.resize(size1)
gambar1 = ImageTk.PhotoImage(resized_image1)

gambar2= Image.open("icon/trash.png")
resized_image2 = gambar2.resize(size1)
gambar2 = ImageTk.PhotoImage(resized_image2)

dark = Image.open("icon/darkmode.png")
resized_image3 = dark.resize(size2)
dark = ImageTk.PhotoImage(resized_image3)

light = Image.open("icon/lightmode.png")
resized_image4 = light.resize(size2)
light = ImageTk.PhotoImage(resized_image4)

#################
### baca data ### richard
#################

def baca_data():
    with open("json/tabungin.json", "r") as file:
        return json.load(file)
    
##################
### tulis data ### richard
#################3

def tulis_data(data):

    with open("json/tabungin.json", "w") as file:
        json.dump(data, file, indent=4)
    
#####################
### update canvas ### richard
#####################

def update_canvas():
    global canvas, tambah, scrollbar, scroll_Region,nightmode_btn,dark,light
    scroll_Region = 0

    try:
        canvas.destroy()
        
        
    except:
        pass

    canvas = tk.Canvas(bg=warna7)
    canvas.pack(fill=tk.BOTH, expand=True)

    data = baca_data()
    atas = 100
    bawah = 300

    tambah = tk.Button(
        text="+",
        width=3,
        height=1,
        command=tambah_data,
        bg=warna1,
        fg="white",
        border=0,
        font=("Arial","20"))
    
    tambah.place(x=320, y=620)

    canvas.create_rectangle(
        0, 0, 400, 80, 
        fill=warna1, 
        outline="")
    
    canvas.create_text(
        200, 40, 
        text="Tabungin", 
        font=("Arial", 20), fill="white")

    for barang in data["barang"]:
        nama = barang["barang"]
        target = barang["target"]
        tabungan = barang["tabungan"]
        tipe = barang["tipe"]
        terkumpul = barang["terkumpul"]
        persen = int((terkumpul / target) * 100)
        estimasi = (target - terkumpul) // tabungan

        if persen >= 100:
            persen = 100
        elif persen <= 0:
            persen =0 
        elif persen >=0:
            persen = persen

        if estimasi <= 0:
            estimasi =  0 
        elif estimasi >= 0:
            estimasi = estimasi
        
         


        canvas.create_rectangle(
            30, atas, 370, bawah, 
            outline="", 
            fill=warna2)
        canvas.create_text(
            50, atas + 40, 
            text=nama, 
            font=("Arial", 20), 
            fill=warna1, 
            anchor="w")
        canvas.create_text(
            50, atas + 90, 
            text=f"Rp {target}", 
            font=("Arial", 20), 
            fill=warna4, 
            anchor="w")
        canvas.create_text(
            50, atas + 130, 
            text=f"Rp {tabungan} {tipe}", 
            font=("Arial", 15), 
            fill=warna4, 
            anchor="w")
        canvas.create_text(
            200, atas + 170, 
            text=("Estimasi",estimasi,tipe), 
            font=("Arial", 15), 
            fill=warna3, 
            anchor="center")
        canvas.create_text(
            300, atas + 130, 
            text=f"{persen} %", 
            font=("Arial", 15), 
            fill=warna4, 
            anchor="w")
        canvas.create_line(
            50, atas + 150, 350, atas + 150, 
            fill=warna3)
        
        edit_btn = tk.Button(
            canvas,
            image=gambar1,  
            bg=warna2,  
            borderwidth=0,   
            highlightthickness=0,  
            command=lambda b=barang: edit_data(b['id']))
        edit_btn.image = gambar1  

        canvas.create_window(
        350, atas + 20,
        window=edit_btn,
        anchor="ne")
        
        atas = bawah + 50
        bawah += 250
        scroll_Region += 300

    scrollbar = ttk.Scrollbar(orient="vertical", command=canvas.yview)
    scrollbar.place(
        relx=1,
        rely=0, 
        relheight=1, 
        anchor="ne")
    
    if dark_theme == False:
        theme = dark
    else:
        theme = light
    
    nightmode_btn = tk.Button(
            canvas,
            image=theme,  
            bg=warna1,  
            borderwidth=0,   
            highlightthickness=0, 
            command=nightmode
            )
    canvas.create_window(
        370, 15,
        window=nightmode_btn,
        anchor="ne")
        
    
    canvas.config(yscrollcommand=scrollbar.set)
    canvas.configure(scrollregion=(0, 0, 0, scroll_Region))

##################
### night mode ### Abi
##################

def nightmode():
    global dark_theme,warna1,warna2,warna3,warna4,warna5,warna6,warna7
    
    if dark_theme == True:
        dark_theme = False
        warna1 = "#0F52BA"
        warna2 = "#E9EAEC" # putih abu
        warna3 = "#979797"
        warna4 = "#000000"
        warna5 = "#0DAA1B"
        warna6 = "#B90F0F"
        warna7 = "#FFFFFF" # putih
        
    elif dark_theme == False:
        dark_theme = True
        warna1 = "#408DFF"
        warna2 = "#282828" # putih abu
        warna3 = "#979797"
        warna4 = "#FFFFFF"
        warna5 = "#00FF15"
        warna6 = "#FF0000"
        warna7 = "#0D0412" # putih
       
    update_canvas()

##############
### cancle ###  Euro
##############

def cancle():
    try:
        entry_barang.destroy()
        entry_tabungan.destroy()
        entry_target.destroy()
        cb_tipe.destroy()
        label_tipe.destroy()
        button_submit.destroy()
        label_tabungan.destroy()
        label_barang.destroy()
        label_target.destroy()
        button_cancle.destroy()
        update_canvas()
    except:
        pass

    try:
        canvas.delete("all")
        scrollbar.destroy()
        canvas.yview_moveto(0)
        delete_btn.destroy()
        tambah_btn.destroy()
        kurang_btn.destroy()
        update_canvas()
    except:
        update_canvas()

###################
### tambah data ### Euro
###################

def tambah_data():
    canvas.delete("all")
    try:
        tambah.destroy()
    except:
        pass
    try:
        scrollbar.destroy()
    except:
        pass

    global entry_barang, label_barang
    global entry_target, label_target
    global cb_tipe, label_tipe
    global entry_tabungan, label_tabungan
    global button_submit, button_cancle

    canvas.yview_moveto(0)
    
    entry_barang = tk.Entry(
        width=20,
        font=("Arial", 20),
        bg=warna2)
    
    entry_barang.place(x=50, y=160)

    label_barang = tk.Label(
        text="Nama Barang",
        bg=warna7,
        fg=warna4,
        font=("Arial", 15))
    
    label_barang.place(x=50, y=125)

    entry_target = tk.Entry(
        width=20,
        font=("Arial", 20),
        bg=warna2)
    
    entry_target.place(x=50, y=260)

    label_target = tk.Label(
        text="Target",
        bg=warna7,
        fg=warna4,
        font=("Arial", 15))
    
    label_target.place(x=50, y=225)

    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground= warna2)

    cb_tipe = ttk.Combobox(
        root,
        values=["bulanan", "mingguan", "harian"],
        width=19,
        font=("Arial", 20))
    
    cb_tipe.place(x=50, y=360)

    label_tipe = tk.Label(
        text="Tipe",
        bg=warna7,
        fg=warna4,
        font=("Arial", 15))
    
    label_tipe.place(x=50, y=325)

    entry_tabungan = tk.Entry(
        width=20,
        font=("Arial", 20),
        bg=warna2)
    
    entry_tabungan.place(x=50, y=460)

    label_tabungan = tk.Label(
        text="Tabungan",
        bg=warna7,
        fg=warna4,
        font=("Arial", 15))
    
    label_tabungan.place(x=50, y=425)

    button_submit = tk.Button(
        text="Submit",
        width=20,
        font=("Arial", 15),
        fg=warna7,
        bg=warna1,
        border=0,
        command=submit)
    
    button_submit.place(x=90, y=520)

    button_cancle = tk.Button(
        text="<",
        width=3, 
        height=1, 
        fg="#FFFFFF", 
        bg=warna1,
        border=0,
        command=cancle,
        font=("Arial","30"))
    
    button_cancle.place(x=5, y=3)

    canvas.create_rectangle(
        0, 0, 400, 80, 
        outline="", 
        fill=warna1)
    
    canvas.create_text(
        200, 40, 
        text="Barang Baru", 
        font=("Arial", 20), 
        fill="#FFFFFF")

##############
### submit ### richard
##############

def submit():
    barang = entry_barang.get()
    target = int(entry_target.get())
    tabungan = int(entry_tabungan.get())
    tipe = cb_tipe.get()

    data = baca_data()

    id_terakhir = data["barang"][-1]["id"] if data["barang"] else 0
    id_baru = id_terakhir + 1

    data_baru = {
        "id": id_baru,
        "barang": barang,
        "target": target,
        "tipe": tipe,
        "tabungan": tabungan,
        "terkumpul": 0
    }

    data["barang"].append(data_baru)
    tulis_data(data)

    entry_barang.destroy()
    entry_tabungan.destroy()
    entry_target.destroy()
    cb_tipe.destroy()
    label_tipe.destroy()
    button_submit.destroy()
    label_tabungan.destroy()
    label_barang.destroy()
    label_target.destroy()
    button_cancle.destroy()

    update_canvas()

#################
### edit data ### euro
#################

def edit_data(id_data):
    global delete_btn, tambah_btn, kurang_btn
    try:
        canvas.delete("all")
        scrollbar.destroy()
        canvas.yview_moveto(0)
        delete_btn.destroy()
        tambah_btn.destroy()
        kurang_btn.destroy()
    except:
        pass

    
   
    data = baca_data()
    atas = 100
    bawah = 300

    for barang in data["barang"]:
        if barang["id"] == id_data:
            nama = (barang["barang"])
            target = (barang["target"])
            tabungan = (barang["tabungan"])
            tipe = (barang["tipe"])
            terkumpul = (barang["terkumpul"])
            persen = int((terkumpul / target) * 100)
            estimasi = ((target - terkumpul) // tabungan)
            kurang = (target-terkumpul)

            if persen >= 100:
                persen = 100
            elif persen <= 0:
                persen =0 
            elif persen >=0:
                persen = persen

            if estimasi <= 0:
                estimasi = 0 
            elif estimasi >= 0:
                estimasi = estimasi
        
         
            canvas.create_rectangle(
                0, 0, 400, 80, 
               fill=warna1, 
                outline="")
    

            canvas.create_rectangle(
                30, atas, 370, bawah, 
                outline="", 
                fill=warna2)
            button_cancle = tk.Button(
                text="<",
                width=3, 
                height=1, 
                fg="#FFFFFF", 
                bg=warna1,
                border=0,
                command=cancle,
                font=("Arial","30"))
    
            button_cancle.place(x=5, y=3)

            canvas.create_text(
                50, 140, 
                text=nama, 
                font=("Arial", 20), 
                fill=warna1, 
                anchor="w")
            canvas.create_text(
                50, 190, 
                text=f"Rp {target}", 
                font=("Arial", 20), 
                fill=warna4, 
                anchor="w")
            canvas.create_text(
                50, 230, 
                text=f"Rp {tabungan} {tipe}", 
                font=("Arial", 15), 
                fill=warna4, 
                anchor="w")
            canvas.create_text(
                200, 270, 
                text=("Estimasi",estimasi,tipe),
                font=("Arial", 15), 
                fill=warna3, 
                anchor="center")
            canvas.create_text(
                300, 230, 
                text=f"{persen} %", 
                font=("Arial", 15), 
                fill=warna4, 
                anchor="w")
            canvas.create_line(
                50, 250, 350, 250, 
                fill=warna3)
            
            canvas.create_rectangle(
                30, 350, 370, 500, 
                outline="", 
                fill=warna2)
            canvas.create_line(
                200, 360, 200, 450 ,
                fill=warna3)
            
            canvas.create_text(
                110, 370, 
                text="terkumpul", 
                font=("Arial", 15), 
                fill=warna4, 
                anchor="center")
            
            canvas.create_text(
                110, 400, 
                text=("Rp",terkumpul), 
                font=("Arial", 15), 
                fill=warna5, 
                anchor="center")
            
            canvas.create_text(
                290, 370, 
                text="kurang", 
                font=("Arial", 15), 
                fill=warna4, 
                anchor="center")
            
            canvas.create_text(
                290, 400, 
                text=("Rp",kurang), 
                font=("Arial", 15), 
                fill=warna6, 
                anchor="center")
            
            tambah_btn = tk.Button(
            text="+",
            width=5,
            height=1,
            bg=warna5,
            fg=warna7,
            border=0,
            font=("Arial","20"),
            command=lambda id=barang['id']: menabung(id,tabungan))
            tambah_btn.place(x=300, y=550)

            kurang_btn = tk.Button(
            text="-",
            width=5,
            height=1,
            bg=warna6,
            fg=warna7,
            border=0,
            font=("Arial","20"),
            command=lambda id=barang['id']: ambil_tabungan(id,tabungan))
            kurang_btn.place(x=300, y=620)

            
            delete_btn = tk.Button(
                text="-",
                image=gambar2,
                width=75,
                height=75,
                bg=warna1,
                fg=warna7,
                border=0,
                font=("Arial","20"),
                command=lambda id=barang['id']: delete_data(id))
            delete_btn.place(x=320, y=3)

################
### menabung ### richard
################

def menabung(id_data,jumlah):
    global canvas
    
    data = baca_data()
    
    for item in data['barang']:
        if item['id'] == id_data:
            item['terkumpul'] += jumlah
            break

    tulis_data(data)
    
    canvas.delete(menabung)

    edit_data(id_data)

######################
### ambil tabungan ### richard
######################

def ambil_tabungan(id_data,jumlah):
    data = baca_data()
    for item in data['barang']:
        if item['id'] == id_data:
            item['terkumpul'] -= jumlah
            break
        
    tulis_data(data)

    edit_data(id_data)

###################
### delete data ### euro
###################

def delete_data(id_data):
    data = baca_data()

    data['barang'] = [item for item in data['barang'] if item['id'] != id_data]

    for index, item in enumerate(data['barang'], start=1):
        item['id'] = index

    tulis_data(data)

    update_canvas()


update_canvas()
root.mainloop()
