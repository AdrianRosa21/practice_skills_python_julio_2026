import json
import random
from datetime import date, timedelta
from dataclasses import asdict
from modelos_relacionales import Producto, Pedido, Usuario

def generar_mock_data() -> str:
    catalogo = [
        Producto(1, "Monitor 4K", 350.0, "Electrónica"),
        Producto(2, "Teclado Mecánico", 120.0, "Periféricos"),
        Producto(3, "Ratón Inalámbrico", 50.0, "Periféricos"),
        Producto(4, "Cable HDMI", 15.0, "Accesorios")
    ]
    
    nombres = ["Melvin Sandoval", "Carlos Barahona", "Andy Perez"]
    usuarios = []
    
    for id_usuario, nombre in enumerate(nombres, start=1):
        fecha_nacimiento = date(1980, 1, 1) + timedelta(days=random.randint(0, 5000))
        correo = f"{nombre.lower().replace(' ', '.')}@ejemplo.com"
        usuario = Usuario(id_usuario, nombre, correo, fecha_nacimiento)
        
        for i in range(random.randint(1, 3)):
            id_pedido = int(f"{id_usuario}00{i}")
            
            fecha_pedido = fecha_nacimiento + timedelta(days=random.randint(6570, 10000)) 
            
            productos_pedido = random.sample(catalogo, k=random.randint(1, 3))
            total = round(sum(p.precio for p in productos_pedido), 2)
            
            usuario.agregar_pedido(Pedido(id_pedido, fecha_pedido, productos_pedido, total))
            
        usuarios.append(usuario)

    class DateEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, date): 
                return obj.isoformat()
            return super().default(obj)
            
    return json.dumps([asdict(u) for u in usuarios], cls=DateEncoder, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    print(generar_mock_data())