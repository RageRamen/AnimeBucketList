import customtkinter
import tkinter
from AnimeList import *
from PIL import Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("800x350")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

search_frame = customtkinter.CTkFrame(master=root, width=300)
search_frame.grid(row=0, column=1)

label = customtkinter.CTkLabel(master=search_frame, text="Anime Search But Cleaner", font=("Arial", 20),
                               anchor="center")
label.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

entry1 = customtkinter.CTkEntry(master=search_frame, placeholder_text="Search Anime")
entry1.grid(row=1, column=0, pady=10, padx=20)

button = customtkinter.CTkButton(master=search_frame, text="Search", width=10, command=lambda: update_info())
button.grid(row=1, column=1, pady=10, padx=20)

info_frame = customtkinter.CTkFrame(master=root, width=600)
info_frame.grid(row=1, column=1, pady=10, padx=10)

image = customtkinter.CTkImage()
image_button = customtkinter.CTkButton(master=info_frame)
image_button.grid(row=0, column=0, pady=10, padx=10)

title = customtkinter.CTkLabel(master=info_frame, text="Title", font=("Arial", 20), anchor="center")
title.grid(row=0, column=1, pady=10, padx=10)

score = customtkinter.CTkLabel(master=info_frame, text="Score", font=("Arial", 20), anchor="center")
score.grid(row=0, column=3, pady=10, padx=10)

# image = customtkinter.CTkImage(master=info_frame, image="anime.png")

left_frame = customtkinter.CTkFrame(master=root, width=200)
left_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

label = customtkinter.CTkLabel(master=left_frame, text="Menu Options")
label.grid(row=0, column=0, pady=12, padx=10)


def update_info():
    data = get_animedata(entry1.get())

    # Information saved
    for x in data['data']:
        str_title = x['title']
        str_score = x['score']
        str_season = x['season']
        str_year = x['year']
        str_image_url = x['images']['webp']['image_url']
        print(x['url'], x['title'], x['score'], x['season'], x['year'], x['images']['webp']['image_url'])
        title.configure(text=str_title)



root.mainloop()
