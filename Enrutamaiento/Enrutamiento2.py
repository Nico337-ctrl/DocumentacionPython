#forma de importar modulos que esten en carpetas por fuera de la actual ruta
import sys
sys.path.append('E:\Programacion\Python\Doc\DocumentacionPython\Modulos')
import modulo_saludar as m_saludar

hola = m_saludar.saludar('pedro')
print(hola)