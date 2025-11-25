\# Arquitectura del Pipeline



El pipeline implementa las siguientes etapas:



1\. \*\*Checkout:\*\* Descarga el código desde GitHub.

2\. \*\*Instalación:\*\* Instala dependencias desde `requirements.txt`.

3\. \*\*Testing:\*\* Ejecuta pruebas automáticas definidas en `test\_app.py`.

4\. \*\*Documentación:\*\* Genera documentación usando Doxygen con el archivo `Doxyfile`.

5\. \*\*Archivado:\*\* Jenkins guarda los archivos generados en `html/`.



Tecnologías utilizadas:

\- Python / Flask

\- PyTest

\- Doxygen

\- Jenkins Pipeline



