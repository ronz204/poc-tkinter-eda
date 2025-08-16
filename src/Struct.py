import tkinter as tk
from tkinter import ttk

def setup_styles() -> None:
  style = ttk.Style()
  style.configure("Custom.TLabel", font=("Segoe UI", 12, "bold"), foreground="#2a4d69")
  style.configure("Custom.TEntry", foreground="#4b86b4", fieldbackground="#f5f5f5")

class LabeledEntry(ttk.Frame):
  def __init__(self, parent: tk.Widget, label: str,):
    super().__init__(parent)
    self.label = ttk.Label(self, text=label, style="Custom.TLabel")
    self.label.grid(row=0, column=0, padx=(0, 20), sticky="W")

    self.entry = ttk.Entry(self, style="Custom.TEntry")
    self.entry.grid(row=0, column=1, sticky="EW")

    self.grid_columnconfigure(1, weight=1)

  def get(self) -> str:
    return self.entry.get()

  def set(self, value: str) -> None:
    self.entry.delete(0, tk.END)
    self.entry.insert(0, value)

class FormView(ttk.Frame):
  def __init__(self, parent: tk.Widget):
    super().__init__(parent)
    self.grid_columnconfigure(0, weight=1)

    self.name_field = LabeledEntry(self, label="Nombre:")
    self.name_field.grid(row=0, column=0, padx=10, pady=10, sticky="EW")

    self.email_field = LabeledEntry(self, label="Email:")
    self.email_field.grid(row=1, column=0, padx=10, pady=10, sticky="EW")

    self.submit_btn = ttk.Button(self, text="Enviar", command=self.on_submit)
    self.submit_btn.grid(row=2, column=0, pady=20, sticky="E")

  def on_submit(self) -> None:
    name = self.name_field.get()
    email = self.email_field.get()
    print(f"Nombre: {name}, Email: {email}")


window = tk.Tk()
window.title("Grid con Views y Components")
window.geometry("600x300")

setup_styles()

form_view = FormView(window)
form_view.pack(expand=True, fill="both", padx=20, pady=20)

window.mainloop()
