from customtkinter import* 
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np 
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import PhotoImage
#-------------------------------------------------------------------------------------------------------------------------------------------------
def hesapla():
    renk = color_selector.get().strip().lower()  # Kullanıcının girdiği rengi al

    try:
        # 10x12 rastgele sıcaklık matrisi
        data = np.random.rand(10, 12)

      
        fig, ax = plt.subplots(figsize=(4, 3), dpi=100)
        sns.heatmap(data, cmap=renk, ax=ax, cbar=True)

      
        img_path = "heatmap.png"
        fig.savefig(img_path, bbox_inches='tight', pad_inches=0.250)
        plt.close(fig)  # Belleği temizle

        # Görüntüyü yükleyip GUI'ye ekle
        img = Image.open(img_path)
        img = img.resize((500, 350))  # Uygun boyut
        img = ImageTk.PhotoImage(img)

    
        canvas.delete("all")
        canvas.create_image(0, 0, image=background_image, anchor="nw")
        canvas.create_image(250, 599, image=img, anchor="center")  # Aşağıya konumlandır
        canvas.image = img   

    except ValueError:
        messagebox.showwarning("Uyarı", "Geçersiz renk girdiniz! Lütfen listeden bir renk seçin.")
#-------------------------------------------------------------------------------------------------------------------------------------------------
wndw=CTk()
wndw.geometry("500x760")
wndw.title("Renk-Sıcaklık Grafiği")
canvas = CTkCanvas(master=wndw, width=500, height=760)
canvas.grid(row=0, column=0)
background_image = PhotoImage(file="/Users/aliemirsertbas/Desktop/VSCO1prjct/CustomTKprjct.py/ımage/new2.png")
canvas.create_image(0, 0, image=background_image, anchor="nw")

button1=CTkButton(master=wndw, 
                  text="grafiği göster", 
                  hover_color="grey",
                  width=200, 
                  height=50,
                  corner_radius=30,
                  bg_color="#737373"
                  ,border_width=4
                  ,border_color="lightblue"
                  ,command=hesapla)
button1.place(relx=0.5, 
              rely=0.4 ,
              anchor="center")


color_options = [
    "viridis", "plasma", "inferno", "magma", "cividis", "coolwarm", 
    "cool", "rainbow"
]
color_selector = CTkComboBox(master=wndw, values=color_options, width=300, 
                  height=45,
                  bg_color="#737373"
                  ,border_width=2
                  ,border_color="lightblue")
color_selector.place(relx=0.5, rely=0.2930, anchor="center")
wndw.mainloop()