from tkinter import *
from tkinter import messagebox
from tkinter_widgets import TkinterWidgets
import json

FONT = ("Arial", 8, "bold")
LOCATION_INFO_PATH = "location_info.json"


class EnterLocation:
    def __init__(self):
        # inform user that their account is being created
        messagebox.showinfo(title="Create Account", message="Could not find location_info.json. Enter your location.")

        # create window
        self.window = Tk()
        self.window.title("Add Account")
        self.window.config(padx=15, pady=15)

        # create widgets and widget data struct
        self.widgets = TkinterWidgets()
        self.create_labels()
        self.create_entries()
        self.create_buttons()

        # main loop for window
        self.window.mainloop()

    def create_labels(self) -> None:
        """
        Creates labels and stores them in widgets
        :return: None
        """

        # 3 labels
        label_1 = Label(text="latitude: ", font=FONT)
        label_2 = Label(text="Longitude: ", font=FONT)

        # set label alignment
        label_1.grid(row=0, column=0, pady=5)
        label_2.grid(row=1, column=0, pady=5)

        # store in dict
        label_dict = {
            "lat": label_1,
            "lon": label_2,
        }

        # store in widgets
        self.widgets.add_label_dict(label_dict)

    def create_entries(self) -> None:
        """
        Creates entries and stores them in widgets
        :return: None
        """

        # create entries
        entry_1 = Entry(width=20)
        entry_2 = Entry(width=20)

        # align entries
        entry_1.grid(row=0, column=1, columnspan=2, pady=5)
        entry_2.grid(row=1, column=1, columnspan=2, pady=5)

        # store in dict
        entry_dict = {
            "lat": entry_1,
            "lon": entry_2,
        }

        # store in widgets
        self.widgets.add_entry_dict(entry_dict)

    def create_buttons(self) -> None:
        """
        creates a button, stores it in widgets
        :return: None
        """

        # create and align button
        button = Button(text="Create", font=FONT, command=self.save_account)
        button.grid(row=3, column=2)

        # store in widgets
        self.widgets.add_button(key="create", button=button)

    def save_account(self) -> None:
        """
        takes information input by user and stores it in json files
        :return: None
        """

        # gets user info
        lat = self.widgets.get_entries("lat").get()
        long = self.widgets.get_entries("lon").get()

        # creates dict
        location_info = {
            "lat": lat,
            "lon": long,
        }

        # stores dict in json file
        with open (LOCATION_INFO_PATH, 'w') as file:
            json.dump(location_info, file, indent=4)

        # informs user
        messagebox.showinfo(title="Location stored", message="Location stored, close the pop ups")
