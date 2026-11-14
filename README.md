# Trabajo Integrador – Arquitectura y Sistemas Operativos

## Virtualización mediante Oracle VirtualBox y Ubuntu Linux ARM64

**Carrera:** Tecnicatura Universitaria en Programación  
**Materia:** Arquitectura y Sistemas Operativos  
**Alumno:** Thiago Chiappero  
**Modalidad:** Individual  
**Año:** 2026

---

## 1. Descripción del proyecto

El presente trabajo integrador tiene como objetivo estudiar y poner en práctica los conceptos de virtualización mediante la utilización de Oracle VirtualBox.

Para desarrollar el caso práctico se creó una máquina virtual sobre una computadora Mac con procesador Apple Silicon, en la cual se instaló Ubuntu 24.04.5 LTS con arquitectura ARM64.

Dentro de este entorno virtualizado se configuró Python 3.12.3 y se desarrolló un programa que permite ingresar tres notas, almacenarlas en una lista y calcular su promedio.

El proyecto permite comprender el funcionamiento de las máquinas virtuales, la asignación de recursos de hardware y la utilización de entornos aislados para realizar actividades de desarrollo y pruebas.

## 2. Objetivos

- Comprender qué es la virtualización y cuál es su utilidad.
- Conocer el funcionamiento de Oracle VirtualBox.
- Crear y configurar una máquina virtual.
- Instalar y utilizar un sistema operativo Linux.
- Configurar un entorno de programación Python.
- Desarrollar y ejecutar un programa utilizando estructuras básicas de programación.
- Documentar el procedimiento y los resultados obtenidos.

## 3. Herramientas utilizadas

| Herramienta | Utilización |
|---|---|
| Oracle VirtualBox | Creación y administración de la máquina virtual |
| Ubuntu 24.04.5 LTS | Sistema operativo virtualizado |
| Python 3.12.3 | Desarrollo del programa |
| Terminal de Ubuntu | Ejecución de comandos y del programa |
| GitHub | Organización y almacenamiento del proyecto |

## 4. Configuración de la máquina virtual

La máquina virtual creada se identifica con el nombre `Ubuntu-AYSO`.

Su configuración es la siguiente:

- Sistema operativo: Ubuntu 24.04.5 LTS.
- Arquitectura: ARM64.
- Memoria RAM: 4000 MB.
- Procesadores: 2.
- Disco virtual: aproximadamente 30 GB.
- Firmware EFI habilitado.
- Conexión de red mediante NAT.

## 5. Caso práctico: programa de cálculo de promedio

Como aplicación práctica se desarrolló un programa en Python que solicita al usuario tres notas y calcula el promedio correspondiente.

El programa utiliza listas, ciclos, entrada de datos, conversión de tipos y operaciones aritméticas.

### Código fuente

El archivo principal es `codigo/promedio.py`.

```python
# Programa para calcular el promedio de tres notas

notas = []

for i in range(3):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)

print("\n--- RESULTADOS ---")
print(f"Notas ingresadas: {notas}")
print(f"Promedio final: {promedio:.2f}")
```

### Ejecución

Para ejecutar el programa desde la terminal de Ubuntu:

```bash
python3 promedio.py
```

### Conceptos de programación aplicados

- **Listas:** permiten almacenar las tres notas ingresadas.
- **Ciclo for:** repite el ingreso de datos tres veces.
- **input():** permite recibir información del usuario.
- **float():** convierte los datos ingresados a números decimales.
- **append():** agrega cada nota a la lista.
- **sum():** realiza la suma de los valores.
- **len():** obtiene la cantidad de notas.
- **Operaciones aritméticas:** permiten calcular el promedio.

## 6. Pruebas realizadas y resultados

Se realizaron dos pruebas para comprobar el funcionamiento del programa.

**Primera prueba: números enteros**

| Nota | Valor |
|---|---:|
| Primera | 8 |
| Segunda | 9 |
| Tercera | 7 |
| Promedio | 8.00 |

**Segunda prueba: números decimales**

| Nota | Valor |
|---|---:|
| Primera | 6.5 |
| Segunda | 8.5 |
| Tercera | 9 |
| Promedio | 8.00 |

En ambas pruebas el programa funcionó correctamente y mostró los resultados esperados.

## 7. Conclusiones

La realización de este proyecto permitió comprender de manera práctica el funcionamiento de la virtualización y la importancia de los sistemas operativos en los entornos de desarrollo.

Se logró instalar y configurar Ubuntu dentro de Oracle VirtualBox, comprobar el funcionamiento de Python y desarrollar una aplicación sencilla que permitió aplicar conocimientos básicos de programación.

La experiencia también permitió conocer las ventajas de trabajar en entornos virtualizados, especialmente la posibilidad de experimentar y realizar pruebas sin modificar directamente el sistema operativo principal.

Como posibles mejoras futuras se propone incorporar validaciones de datos, ampliar la cantidad de notas y desarrollar programas con funcionalidades más complejas.

## 8. Estructura del repositorio

```text
Trabajo-Integrador-AYSO/
│
├── README.md
│
├── codigo/
│   └── promedio.py
│
├── capturas/
│   └── Evidencias del desarrollo práctico
│
├── informe/
│   └── Trabajo_Integrador.pdf
│
└── recursos/
    └── Bibliografía y documentación
```

## 9. Bibliografía y recursos

- Oracle. Documentación oficial de VirtualBox. https://www.virtualbox.org/manual/
- Ubuntu. Documentación oficial. https://documentation.ubuntu.com/
- Python Software Foundation. Documentación oficial de Python. https://docs.python.org/3/
- Material de estudio y video orientativo proporcionado por la cátedra de Arquitectura y Sistemas Operativos.

---

**Trabajo Integrador – Arquitectura y Sistemas Operativos – 2026**
