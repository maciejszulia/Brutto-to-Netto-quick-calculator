import tkinter as tk
import pyperclip


root = tk.Tk()

welcome = tk.Label(root, text="Wpisz cene brutto:")
welcome.grid(row=0, column=0, columnspan=2)

get_brutto_price = tk.Entry(root)
get_brutto_price.grid(row=1, column=1)

get_brutto_price_button = tk.Button(root, text="Oblicz")
get_brutto_price_button.grid(row=1, column=2)

show_netto_price = tk.Label(root, text=f'Cena netto:')
show_netto_price.grid(row=2, column=1)

get_netto_price_copybutton = tk.Button(root, text="Kopiuj")
get_netto_price_copybutton.grid(row=4, column=2)

get_meters_in_a_pack = tk.Entry(root)
get_meters_in_a_pack.grid(row=4, column=1)

insert_meters_in_a_pack = tk.Label(root, text="Podaj metry w paczce")
insert_meters_in_a_pack.grid(row=5, column=1)

get_meters_in_a_pack = tk.Entry(root)
get_meters_in_a_pack.grid(row=6, column=1)

get_brutto_price_button = tk.Button(root, text="Oblicz")
get_brutto_price_button.grid(row=6, column=2)

show_pack_price_netto = tk.Label(root, text="Cena paczki netto: ")
show_pack_price_netto.grid(row=7, column=1)
show_pack_price_netto_copy_button = tk.Button(root, text="Kopiuj")
show_pack_price_netto_copy_button.grid(row=7, column=2)

show_pack_price_brutto = tk.Label(root, text="Cena paczki brutto: ")
show_pack_price_brutto.grid(row=8, column=1)
show_pack_price_netto_copy_button = tk.Button(root, text="Kopiuj")
show_pack_price_netto_copy_button.grid(row=8, column=2)

root.mainloop()
