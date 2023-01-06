import customtkinter
from AnimeList import *
from PIL import Image
from io import BytesIO

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("Anime List")
        self.geometry(f"{800}x{400}")

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.search_frame = customtkinter.CTkFrame(self, corner_radius=10, width=600, height=200, border_width=2, border_color="gray")
        self.search_frame.grid(row=0, column=1, pady=10, padx=10)

        self.menu_title = customtkinter.CTkLabel(self.search_frame, text="Anime Search But Clean",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"),
                                                 anchor="center")
        self.menu_title.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

        self.entry1 = customtkinter.CTkEntry(self.search_frame, placeholder_text="Search Anime")
        self.entry1.grid(row=1, column=0, pady=10, padx=20)

        self.button = customtkinter.CTkButton(self.search_frame, text="Search", width=10,
                                              command=lambda: self.update_info())
        self.button.grid(row=1, column=1, pady=10, padx=20)

        self.info_frame = customtkinter.CTkFrame(self, corner_radius=10, width=600, height=300)
        self.info_frame.grid(row=1, column=1, rowspan=3, pady=10, padx=10, sticky="nsew")

        self.info_frame.rowconfigure(0, weight=1)
        self.info_frame.columnconfigure(1, weight=1)

        self.info_pic_frame = customtkinter.CTkFrame(self.info_frame, corner_radius=10)
        self.info_pic_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.image = customtkinter.CTkImage(light_image=Image.open("Ramen.jpg"))
        self.image.configure(size=(150, 220))
        self.image_label = customtkinter.CTkLabel(self.info_pic_frame, image=self.image, text="")
        self.image_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.info_mid_frame = customtkinter.CTkFrame(self.info_frame, corner_radius=10)
        self.info_mid_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.title = customtkinter.CTkLabel(self.info_mid_frame, text="Title", font=("Arial", 20))
        self.title.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.score = customtkinter.CTkLabel(self.info_mid_frame, text="Score", font=("Arial", 20))
        self.score.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")

        self.season = customtkinter.CTkLabel(self.info_mid_frame, text="Season", font=("Arial", 20))
        self.season.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")

        self.year = customtkinter.CTkLabel(self.info_mid_frame, text="Year", font=("Arial", 20))
        self.year.grid(row=1, column=1, pady=10, padx=10, sticky="nsew")

        # image = customtkinter.CTkImage(master=info_frame, image="anime.png")

        self.left_frame = customtkinter.CTkFrame(self, width=200)
        self.left_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.menu_title = customtkinter.CTkLabel(self.left_frame, text="Menu Options",
                                                 font=customtkinter.CTkFont(size=15, weight="bold"))
        self.menu_title.grid(row=0, column=0, pady=12, padx=10)

        self.theme_optionmenu_label = customtkinter.CTkLabel(self.left_frame, text="Change Theme:")
        self.theme_optionmenu_label.grid(row=1, column=0, padx=10, pady=(10, 0))

        self.theme_optionmenu = customtkinter.CTkOptionMenu(self.left_frame, values=["System", "Light", "Dark"],
                                                            command=self.change_theme_mode)
        self.theme_optionmenu.grid(row=2, column=0, padx=10, pady=(10,0))

        self.random_anime_button = customtkinter.CTkButton(self.left_frame, text="Random Anime", command=self.random_anime_event)
        self.random_anime_button.grid(row=3, column=0, padx=10, pady=(10, 0))
    def update_info(self):
        data = get_animedata(self.entry1.get())

        # Information saved
        for x in data['data']:
            str_title = x['title']
            str_score = x['score']
            str_season = x['season']
            str_year = x['year']
            self.update_image_content(x['images']['webp']['image_url'])
            self.title.configure(text=str_title)
            self.score.configure(text=str_score)
            self.season.configure(text=str_season)
            self.year.configure(text=str_year)
            print(x['url'], x['title'], x['score'], x['season'], x['year'], x['images']['webp']['image_url'])

    def update_image_content(self, url):
        response = requests.get(url)
        image_data = response.content
        self.image.configure(light_image=Image.open(BytesIO(image_data)))

    def random_anime_event(self):
        data = get_random_animedata()
        x = data['data']

        str_title = x['title']
        str_score = x['score']
        str_season = x['season']
        str_year = x['year']
        self.update_image_content(x['images']['webp']['image_url'])
        self.title.configure(text=str_title)
        self.score.configure(text=str_score)
        self.season.configure(text=str_season)
        self.year.configure(text=str_year)
        print(x['url'], x['title'], x['score'], x['season'], x['year'], x['images']['webp']['image_url'])

    def change_theme_mode(self, appearance_mode):
        customtkinter.set_appearance_mode(appearance_mode)



if __name__ == "__main__":
    app = App()
    app.mainloop()
