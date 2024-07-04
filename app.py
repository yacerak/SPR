import customtkinter as ctk

def window(title, mode="light", size="500x500", scrollbar=True):
    ctk.set_appearance_mode(mode)
    app = ctk.CTk()
    app.title(title)
    app.geometry(size)

    if scrollbar:
        canvas = ctk.CTkScrollableFrame(app, orientation="vertical")
        canvas.pack(fill='both', expand=True)
        return app, canvas

    else:
        return app

