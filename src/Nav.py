
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App con Navegación Dinámica")
        self.geometry("900x600")
        self.configure(bg="#f4f4f4")

        # Estilos ttk
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame", background="#f4f4f4")
        style.configure("Nav.TFrame", background="#181c22")
        style.configure(
            "Nav.TButton",
            font=("Segoe UI", 11, "bold"),
            background="#181c22",
            foreground="#e0e6ed",
            borderwidth=0,
            focusthickness=0,
            padding=(0, 0),
            anchor="center"
        )
        style.map(
            "Nav.TButton",
            background=[("active", "#2d8cf0"), ("pressed", "#2d8cf0")],
            foreground=[("active", "#fff"), ("pressed", "#fff")]
        )
        style.configure("Title.TLabel", font=("Segoe UI", 22, "bold"), background="#f4f4f4", foreground="#181c22")
        style.configure("Content.TFrame", background="#f4f4f4")
        style.configure("Content.TLabel", font=("Segoe UI", 15), background="#f4f4f4", foreground="#23272f")

        # Layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Barra de navegación
        nav_width = 140
        self.nav_frame = ttk.Frame(self, style="Nav.TFrame", width=nav_width)
        self.nav_frame.grid(row=0, column=0, sticky="ns")
        self.nav_frame.grid_propagate(False)
        for i in range(5):
            self.nav_frame.grid_rowconfigure(i, weight=1)

        # Contenido dinámico
        self.content_frame = ttk.Frame(self, style="Content.TFrame")
        self.content_frame.grid(row=0, column=1, sticky="nsew")
        self.content_frame.grid_propagate(True)

        # Crear páginas
        self.pages = {
            "Inicio": self.create_home_page(),
            "Perfil": self.create_profile_page(),
            "Configuración": self.create_settings_page()
        }

        # Botones de navegación
        for i, (name, _) in enumerate(self.pages.items()):
            btn = ttk.Button(
                self.nav_frame,
                text=name,
                style="Nav.TButton",
                command=lambda n=name: self.show_page(n)
            )
            btn.grid(row=i, column=0, sticky="nsew", padx=0, pady=(18 if i == 0 else 8, 8))
            self.nav_frame.grid_rowconfigure(i, weight=1)
        self.nav_frame.grid_columnconfigure(0, weight=1)

        # Mostrar página inicial
        self.show_page("Inicio")

    def create_home_page(self):
        frame = ttk.Frame(self.content_frame, style="Content.TFrame")
        label = ttk.Label(frame, text="Página de Inicio", style="Title.TLabel")
        label.pack(pady=40)
        desc = ttk.Label(frame, text="Bienvenido a la aplicación. Usa la barra lateral para navegar.", style="Content.TLabel")
        desc.pack(pady=10)
        return frame

    def create_profile_page(self):
        frame = ttk.Frame(self.content_frame, style="Content.TFrame")
        label = ttk.Label(frame, text="Perfil del Usuario", style="Title.TLabel")
        label.pack(pady=40)
        desc = ttk.Label(frame, text="Aquí puedes ver y editar tu información personal.", style="Content.TLabel")
        desc.pack(pady=10)
        return frame

    def create_settings_page(self):
        frame = ttk.Frame(self.content_frame, style="Content.TFrame")
        label = ttk.Label(frame, text="Configuraciones", style="Title.TLabel")
        label.pack(pady=40)
        desc = ttk.Label(frame, text="Ajusta las preferencias de la aplicación aquí.", style="Content.TLabel")
        desc.pack(pady=10)
        return frame

    def show_page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()
        self.pages[page_name].pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()