import tkinter as tk

# Mismo EventBroker de arriba (o importado)
class EventBroker:
    def __init__(self):
        self._listeners = {}

    def register(self, event_type, callback):
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(callback)

    def publish(self, event_type, data=None):
        if event_type in self._listeners:
            for listener in self._listeners[event_type]:
                listener(data)

class Application(tk.Tk):
    def __init__(self, broker):
        super().__init__()
        self.title("Event-Driven UI")
        self.broker = broker
        self.create_widgets()
        self.register_listeners()

    def create_widgets(self):
        # Componente de Compra (Productor de eventos)
        self.btn_comprar = tk.Button(self, text="Comprar Producto", command=self.on_buy_click)
        self.btn_comprar.pack(pady=10)

        # Componente de Estado de Inventario (Consumidor de eventos)
        self.lbl_inventario = tk.Label(self, text="Inventario: 10")
        self.lbl_inventario.pack(pady=5)

        # Componente de Historial de Compras (Consumidor de eventos)
        self.lbl_historial = tk.Label(self, text="Historial: ")
        self.lbl_historial.pack(pady=5)
    
    def on_buy_click(self):
        # El botón solo sabe que debe publicar un evento
        self.broker.publish("producto_comprado", {"producto_id": "A1", "cantidad": 1})

    def register_listeners(self):
        # Los componentes se suscriben a los eventos que les interesan
        self.broker.register("producto_comprado", self.actualizar_inventario)
        self.broker.register("producto_comprado", self.actualizar_historial)

    def actualizar_inventario(self, data):
        current_stock = int(self.lbl_inventario.cget("text").split(": ")[1])
        new_stock = current_stock - data["cantidad"]
        self.lbl_inventario.config(text=f"Inventario: {new_stock}")
        print(f"Inventario actualizado: {new_stock}")

    def actualizar_historial(self, data):
        current_history = self.lbl_historial.cget("text")
        new_history = current_history + f"Compra de {data['producto_id']}."
        self.lbl_historial.config(text=new_history)
        print(f"Historial actualizado con la compra de {data['producto_id']}")

if __name__ == "__main__":
    broker = EventBroker()
    app = Application(broker)
    app.mainloop()