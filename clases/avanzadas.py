class OperacionesAvanzadas:

    def potencia(self, base: float, exponente: float) -> float:
        """
        Calcula base ** exponente.
        Ejemplos:
        - potencia(2, 3) -> 8
        - potencia(9, 0.5) -> 3
        """
        try:
            return float(base) ** float(exponente)
        except Exception:
            raise ValueError("No fue posible calcular la potencia con los valores proporcionados.")
    
    def raiz_cuadrada(self, numero: float) -> float:

        try:
            if numero < 0:
                raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
            return float(numero) ** 0.5
        except Exception:
            raise ValueError("No fue posible calcular la raíz cuadrada con el valor proporcionado.")
        