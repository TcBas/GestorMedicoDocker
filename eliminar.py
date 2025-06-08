import os
import shutil

# Ruta de la carpeta que quieres procesar
carpeta = r'C:\Users\Dwight\Documents\Freddy\Pagina'
texto_a_eliminar = 'LazyCoder || sumit'
extensiones_permitidas = ['.html', '.htm', '.js', '.css', '.php']

# Carpeta para respaldos
backup_dir = os.path.join(carpeta, 'respaldos_eliminar')
os.makedirs(backup_dir, exist_ok=True)

def procesar_archivos(carpeta_base):
    for root, _, files in os.walk(carpeta_base):
        for archivo in files:
            ruta_original = os.path.join(root, archivo)
            nombre, ext = os.path.splitext(archivo)
            if ext.lower() in extensiones_permitidas:
                try:
                    with open(ruta_original, 'r', encoding='utf-8') as f:
                        contenido = f.read()
                    
                    if texto_a_eliminar in contenido:
                        # Respaldar archivo
                        ruta_relativa = os.path.relpath(ruta_original, carpeta_base)
                        ruta_backup = os.path.join(backup_dir, ruta_relativa)
                        os.makedirs(os.path.dirname(ruta_backup), exist_ok=True)
                        shutil.copy2(ruta_original, ruta_backup)

                        # Eliminar solo la coincidencia exacta
                        nuevo_contenido = contenido.replace(texto_a_eliminar, '')

                        # Guardar archivo modificado
                        with open(ruta_original, 'w', encoding='utf-8') as f:
                            f.write(nuevo_contenido)

                        print(f'✅ Modificado: {ruta_original}')
                except Exception as e:
                    print(f'❌ Error con {ruta_original}: {e}')

# Ejecutar
procesar_archivos(carpeta)
