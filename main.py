"""
main.py

Aplicación de consola interactiva que resuelve un sistema de ecuaciones lineales
usando NumPy. El usuario ingresa los coeficientes y términos independientes.

Autor: [John Alejandro Ibanez Rincon]
Fecha: 16 mayo 2025
"""

import numpy as np

def resolver_sistema():
    """
    Solicita al usuario los coeficientes de un sistema 2x2 y lo resuelve.
    """

    print("Sistema de ecuaciones lineales 2x2")
    print("Forma general:")
    print("a1*x + b1*y = c1")
    print("a2*x + b2*y = c2")

    try:
        # Entrada de datos
        a1 = float(input("Ingrese a1: "))
        b1 = float(input("Ingrese b1: "))
        c1 = float(input("Ingrese c1: "))

        a2 = float(input("Ingrese a2: "))
        b2 = float(input("Ingrese b2: "))
        c2 = float(input("Ingrese c2: "))

        # Crear matrices
        A = np.array([[a1, b1],
                      [a2, b2]])
        b = np.array([c1, c2])

        # Resolver sistema
        x = np.linalg.solve(A, b)

        # Mostrar resultados
        print("\nSolución del sistema:")
        print(f"x = {x[0]:.2f}")
        print(f"y = {x[1]:.2f}")

    except ValueError:
        print("Error: debes ingresar números válidos.")
    except np.linalg.LinAlgError:
        print("Error: el sistema no tiene solución única (puede ser incompatible o indeterminado).")

if __name__ == "__main__":
    resolver_sistema()