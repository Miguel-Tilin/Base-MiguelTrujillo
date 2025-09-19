Escenario: Calculadora avanzada en Python (Trabajo colaborativo)

Rol: ANFITRIÓN
Miguel hara la base del proyecto con la operación POTENCIA funcionando.
El COLABORADOR  Mario hará un Pull Request para agregar RAÍZ CUADRADA.

Estructura del proyecto
proyecto-base-tu_nombre/
├─ README.txt
├─ main.py
└─ clases/
   └─ avanzadas.py

Requisitos
- Python 3.9+
- Git
- Cuenta de GitHub

Ejecución
python main.py

Flujo recomendado (ANFITRIÓN)
1) Crea el repositorio en GitHub: proyecto-base-tu_nombre
2) Sube la base (solo potencia):
   git init
   git add .
   git commit -m "Base del proyecto con potencia implementada"
   git remote add origin https://github.com/Miguel-Tilin/Base-MiguelTrujillo.git
   git push -u origin master

3) Comparte el repositorio con tu compañero (o que haga fork).
4) Crea un Issue: "Implementar raíz_cuadrada(x) en clases/avanzadas.py".
5) Espera el Pull Request de tu colaborador y haz el Merge.
6) Actualiza tu local:
   git pull origin main

Rol del COLABORADOR (instrucciones)
1) Haz Fork del repo del anfitrión.
2) Clona tu fork:
   git clone https://github.com/Miguel-Tilin/Base-MiguelTrujillo.git
   cd proyecto-base-tu_nombre
3) Crea una rama de trabajo:
   git switch -c feature/raiz-cuadrada
4) Implementa en clases/avanzadas.py:
   - Definir metodo: raiz_cuadrada(self, x: float) -> float
   - Validar x >= 0; si x < 0, levantar ValueError
   - Retornar math.sqrt(x)
5) Prueba localmente:
   python main.py
6) Guarda y sube:
   git add .
   git commit -m "Implementa raíz cuadrada"
   git push -u origin feature/raiz-cuadrada
7) Crea Pull Request hacia el repo del anfitrión:
   base: main (repo anfitrión) ← compare: feature/raiz-cuadrada (tu fork)
8) Avisar para revisión y Merge.

Criterios de aceptación
- Potencia funciona (anfitrión).
- Raíz cuadrada implementada con validación y manejo de errores (colaborador).
- main.py muestra menú y ejecuta correctamente las opciones disponibles.
- Código claro y con mensajes de error comprensibles.

Notas
- Mantener mensajes de commit descriptivos.
- No incluir librerías innecesarias.
- Si tu rama principal es "master", reemplaza "main" por "master" en los comandos.
