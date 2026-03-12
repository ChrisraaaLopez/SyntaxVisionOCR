# Syntax Vision (OCR → PKM Markdown)

Syntax Vision es una herramienta de escritorio desarrollada en Python para la extracción de texto mediante OCR (Reconocimiento Óptico de Caracteres). Permite convertir notas físicas, capturas de pantalla y documentos en archivos Markdown estructurados con metadatos YAML, diseñados para sistemas de gestión de conocimiento personal (PKM).

---

## Requisitos Previos

### 1. Python

Se requiere **Python 3.10 o superior**. Puedes descargarlo desde [python.org](https://python.org). Durante la instalación, asegúrate de marcar la casilla **"Add Python to PATH"**.

### 2. Tesseract OCR

Es el motor indispensable para el reconocimiento de texto:

1. Descarga el instalador oficial: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
2. Durante la instalación, marca la casilla de **Additional script data** y **Additional language data** para incluir el paquete de lenguaje **Spanish (español)**.
3. La aplicación buscará por defecto el ejecutable en la ruta: `C:\Program Files\Tesseract-OCR\tesseract.exe`

---

## Instalación

### 1. Clonar el proyecto

```bash
git clone https://github.com/ChrisraaaLopez/SyntaxVisionOCR.git
cd SyntaxVisionOCR
```

### 2. Crear un entorno virtual (Recomendado)

Para mantener las dependencias aisladas y evitar conflictos:

```bash
python -m venv venv

# Activar en Windows:
venv\Scripts\activate

# Activar en Linux/Mac:
source venv/bin/activate
```

### 3. Instalación del paquete

Instala el proyecto y sus dependencias de forma local. Esto habilitará el comando `syntaxvision` en tu terminal:

```bash
pip install .
```

---

## Uso y Comandos

Una vez completada la instalación, lanza la aplicación desde cualquier terminal:

```bash
syntaxvision
```

Al ejecutar el comando:

1. Se mostrará un banner ASCII con el nombre del proyecto.
2. Se confirmará la conexión a la base de datos local (SQLite).
3. Se iniciará automáticamente la interfaz gráfica de usuario (GUI).

---

## Funcionalidades Principales

- **Motor Dual** — Selección entre Tesseract (rápido para texto impreso) y EasyOCR (optimizado para escritura a mano).
- **IA Multimodal** — Opción para mejorar y reconstruir el texto extraído mediante modelos avanzados (Claude, Gemini, GPT-4o).
- **Historial Persistente** — Almacenamiento automático de las notas procesadas en una base de datos local SQLite.
- **Captura Directa** — Integración con webcam para toma de fotografías en tiempo real.
- **Exportación Multiformato** — Guarda tus resultados en `.md` (con YAML frontmatter), `.pdf`, `.docx` y `.txt`.

---

## Estructura del Proyecto

```
SyntaxVision/
├── resources/               # Logos, iconos y modelos de procesamiento
├── index.py                 # Lógica principal de la interfaz y lanzador
├── setup.py                 # Configuración de empaquetado e instalación CLI
├── .gitignore               # Archivos excluidos (venv, __pycache__, etc.)
└── syntax_vision_history.db # Base de datos local para el historial
```

---

## Autor

**Christian Israel Lopez Lopez** — [@ChrisraaaLopez](https://github.com/ChrisraaaLopez)