"""Modelos relacionales para generar mock data."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date


@dataclass
class Producto:
    id_producto: int
    nombre: str
    precio: float
    categoria: str


@dataclass
class Pedido:
    id_pedido: int
    fecha_pedido: date
    productos: list[Producto]
    total: float


@dataclass
class Usuario:
    id_usuario: int
    nombre_completo: str
    correo: str
    fecha_nacimiento: date
    pedidos: list[Pedido] = field(default_factory=list)

    def agregar_pedido(self, pedido: Pedido) -> None:
        self.pedidos.append(pedido)
