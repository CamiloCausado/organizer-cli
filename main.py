import os
import shutil
from datetime import datetime

# Definición de categorías por extensión
EXTENSIONES = {
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pp', '.csv'],
    'Imágenes': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
    'Código': ['.py', '.cpp', '.c', '.java', '.html', '.css', '.js', '.sql'],
    'Archivos': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Ejecutables': ['.exe', '.msi', '.deb', '.rpm', '.AppImage']
}

def organizar_directorio(ruta_objetivo):
    if not os.path.exists(ruta_objetivo):
        print(f"❌ La ruta '{ruta_objetivo}' no existe.")
        return

    archivos_movidos = 0
    print(f"\n📂 Iniciando organización en: {ruta_objetivo}\n" + "-"*40)

    for item in os.listdir(ruta_objetivo):
        ruta_item = os.path.join(ruta_objetivo, item)
        
        # Ignorar carpetas
        if os.path.isdir(ruta_item):
            continue

        ext = os.path.splitext(item)[1].lower()
        categoria_destino = 'Otros'

        for categoria, exts in EXTENSIONES.items():
            if ext in exts:
                categoria_destino = categoria
                break

        # Crear carpeta destino si no existe
        carpeta_destino = os.path.join(ruta_objetivo, categoria_destino)
        os.makedirs(carpeta_destino, exist_ok=True)

        # Mover archivo
        shutil.move(ruta_item, os.path.join(carpeta_destino, item))
        print(f"✔ Movido: {item} ➔ {categoria_destino}/")
        archivos_movidos += 1

    print("-" * 40)
    print(f"🎉 Proceso completado. Archivos organizados: {archivos_movidos}")

if __name__ == "__main__":
    print("=== AUTOMATIZADOR DE ARCHIVOS ===")
    ruta = input("Ingresa la ruta de la carpeta a organizar: ").strip()
    if ruta:
        organizar_directorio(ruta)
    else:
        print("⚠ Debe ingresar una ruta válida.")