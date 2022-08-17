
from turtle import title
import requests
import tkinter as tk
from tkinter import *
from logging import root


def deep():
    wwww = wr2.get()
    wwww2 = wr.get()
    wwww3 = wr3.get()
    url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
    "q":"{}".format(wwww),
    "source":"{}".format(wwww2),
    "target":"{}".format(wwww3)
    }
    headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "f0eda7c17amsha10f3c793fdf668p1ba57fjsn4b46df9be184",
    "X-RapidAPI-Host": "deep-translate1.p.rapidapi.com"
    }   

    response = requests.request("POST", url, json=payload, headers=headers)

    json = response.json()

    text_translate = json['data']['translations']['translatedText']
    wr4.insert("1.0","{}".format(text_translate))

w = tk.Tk()
w.title("Перекладач")
w.geometry("800x600")
wrr = tk.Label(text="Ведіть мову для вводу")
wrr.pack()

wr = tk.Entry()
wr.pack()

wr5 = tk.Label(text="-->")
wr5.pack()

wr2 = tk.Entry()
wr2.pack()

wrr2 = Label(text="Ведіть мову для перекладу")
wrr2.pack()

wr3 = tk.Entry()
wr3.pack()

wrr3 = tk.Label(text="<--")
wrr3.pack()

wr4 = tk.Text()
wr4.pack()

wr6 = tk.Button(text="Перекласти",command=deep)
wr6.pack()

w.mainloop()

