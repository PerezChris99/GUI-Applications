import vlc
import tkinter as tk

class MediaPlayer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        self.create_widgets()

    def create_widgets(self):
        self.play_button = tk.Button(self)
        self.play_button["text"] = "Play"
        self.play_button["command"] = self.play
        self.play_button.pack(side="left")

        self.stop_button = tk.Button(self)
        self.stop_button["text"] = "Stop"
        self.stop_button["command"] = self.stop
        self.stop_button.pack(side="left")

        self.url_entry = tk.Entry(self)
        self.url_entry.pack(side="left")

    def play(self):
        media = self.instance.media_new(self.url_entry.get())
        self.player.set_media(media)
        self.player.play()

    def stop(self):
        self.player.stop()

root = tk.Tk()
app = MediaPlayer(master=root)
app.mainloop()
