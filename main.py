import customtkinter
import tkinter
from AnimeList import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("800x350")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

search_frame = customtkinter.CTkFrame(master=root, width=300)
search_frame.grid(row=0, column=1)

label = customtkinter.CTkLabel(master=search_frame, text="Anime Search But Cleaner", font=("Arial", 20), anchor="center")
label.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

entry1 = customtkinter.CTkEntry(master=search_frame, placeholder_text="Search Anime")
entry1.grid(row=1, column=0, pady=10, padx=20)

button = customtkinter.CTkButton(master=search_frame, text="Search", width=10, command=lambda: update_info())
button.grid(row=1, column=1, pady=10, padx=20)

info_frame = customtkinter.CTkFrame(master=root, width=600)
info_frame.grid(row=1, column=1, pady=10, padx=10)

title = customtkinter.CTkLabel(master=info_frame, text=entry1.get(), font=("Arial", 20), anchor="center")
title.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

left_frame = customtkinter.CTkFrame(master=root, width=200)
left_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

label = customtkinter.CTkLabel(master=left_frame, text="Menu Options")
label.grid(row=0, column=0, pady=12, padx=10)

def update_info():
    print_anime(entry1.get())
    title.configure(text=entry1.get())


root.mainloop()
