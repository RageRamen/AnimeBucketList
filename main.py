import customtkinter
import tkinter
from AnimeList import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x350")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

main_frame = customtkinter.CTkFrame(master=root, width=300)
main_frame.grid(row=0, column=1, columnspan=3, sticky="nsew")

label = customtkinter.CTkLabel(master=main_frame, text="Anime Search But Cleaner", font=("Arial", 20))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=main_frame, placeholder_text="Search Anime")
entry1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=main_frame, text="Search", command=lambda: print_anime(entry1.get()))
button.pack(pady=12, padx=10)

left_frame = customtkinter.CTkFrame(master=root, width=200, bg_color="#F0F0F0")
left_frame.grid(row=0, column=0, sticky="nsew")

label = customtkinter.CTkLabel(master=left_frame, text="Menu Options")
label.grid(row=0, column=0, pady=12, padx=10)

root.mainloop()
