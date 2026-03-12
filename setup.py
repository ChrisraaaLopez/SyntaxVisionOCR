from setuptools import setup

setup(
    name='syntaxvision',
    version='1.0.0',
    py_modules=['index'], # Si tu archivo se llama index.py
    install_requires=[
        'PyQt6',
        'pytesseract',
        'opencv-python',
        'Pillow',
        'easyocr',
        'python-docx',
        'reportlab',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'syntaxvision=index:main_launcher', # Crea el comando mágico
        ],
    },
)