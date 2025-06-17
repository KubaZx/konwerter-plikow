import tkinter as tk
from tkinter import filedialog, messagebox
from utils import json_handler, yaml_handler

def convert_json_to_yaml():
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        try:
            data = json_handler.load(file_path)
            yaml_handler.save(data, "wynik_z_gui.yaml")
            messagebox.showinfo("Sukces", "Zapisano jako wynik_z_gui.yaml")
        except Exception as e:
            messagebox.showerror("Błąd", str(e))

root = tk.Tk()
root.title("Konwerter JSON -> YAML")

btn = tk.Button(root, text="Konwertuj JSON -> YAML", command=convert_json_to_yaml)
btn.pack(pady=20, padx=20)

root.mainloop()