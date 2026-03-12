# Syntax Vision (OCR → PKM Markdown)

Syntax Vision es una herramienta de escritorio desarrollada en Python para la extracción de texto mediante OCR (Reconocimiento Óptico de Caracteres). Permite convertir notas físicas, capturas de pantalla y documentos en archivos Markdown estructurados con metadatos YAML, diseñados para sistemas de gestión de conocimiento personal (PKM).

---

## Requisitos Previos

### 1. Python
Se requiere Python 3.10 o superior. Puedes descargarlo desde [python.org](https://python.org). Durante la instalación, asegúrese de marcar la casilla **"Add Python to PATH"**.

### 2. Tesseract OCR
Es el motor indispensable para el reconocimiento de texto:

1. Descarga el instalador oficial: [Tesseract OCR para Windows](https://github.com/UB-Mannheim/tesseract/wiki).
2. Durante la instalación, es muy importante marcar la casilla de **Additional script data** y **Additional language data** para incluir el paquete de lenguaje **Spanish (español)**.
3. La aplicación buscará por defecto el ejecutable en la ruta: `C:\Program Files\Tesseract-OCR\tesseract.exe`.

---

## Instalación

Sigue estos comandos en tu terminal para clonar el repositorio e instalar el proyecto de forma permanente en tu sistema:

### 1. Clonar el proyecto
```bash
git clone https://github.com/ChrisraaaLopez/OCR-Project.git
cd OCR-Project
```

### 2. Instalación Global *(Recomendado para usar el comando siempre)*
Para que el comando funcione en cualquier terminal nueva sin configuraciones adicionales, instala el paquete directamente en tu Python global:
```bash
pip install .
```

---

## Uso y Comandos en Consola

Una vez completada la instalación, el programa se puede ejecutar desde cualquier carpeta o ventana de CMD simplemente escribiendo:
```bash
syntaxvision
```

Al ejecutar el comando:

1. Se mostrará un banner ASCII con el nombre del proyecto en la terminal.
2. Se confirmará la conexión a la base de datos local (SQLite).
3. Se iniciará automáticamente la interfaz gráfica del usuario (GUI).

---

## Funcionalidades Principales

- **Motor Dual:** Selección entre Tesseract (rápido para texto impreso) y EasyOCR (mejor para escritura a mano).
- **IA Multimodal:** Opción para mejorar y reconstruir el texto extraído mediante modelos avanzados (Claude, Gemini, GPT-4o).
- **Historial Persistente:** Almacenamiento automático de las últimas notas procesadas en una base de datos local SQLite.
- **Captura Directa:** Integración con webcam para toma de fotografías en tiempo real.
- **Exportación Multiformato:** Capacidad para guardar el resultado en formatos `.md`, `.pdf`, `.docx` y `.txt`.

---

## Estructura del Proyecto
```
OCR-Project/
├── resources/               # Logos, iconos y modelos de procesamiento
├── index.py                 # Lógica principal de la interfaz y lanzador del sistema
├── setup.py                 # Configuración de empaquetado e instalación CLI
└── syntax_vision_history.db # Archivo de base de datos local para el historial
```

---

## Autor

**Christian Israel Lopez Lopez** — [@ChrisraaaLopez](https://github.com/ChrisraaaLopez)