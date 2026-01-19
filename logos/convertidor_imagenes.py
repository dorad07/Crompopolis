import os
from PIL import Image

# Carpeta de entrada y salida
INPUT_DIR = "imagenes/input"
OUTPUT_DIR = "imagenes/output"

# Crear carpeta de salida si no existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Extensiones soportadas
EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif")

# Calidad WebP (0-100)
WEBP_QUALITY = 85  # ideal para web

for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(EXTENSIONS):
        input_path = os.path.join(INPUT_DIR, filename)
        name, _ = os.path.splitext(filename)
        output_path = os.path.join(OUTPUT_DIR, f"{name}.webp")

        try:
            with Image.open(input_path) as img:
                # Convertir a RGB si es necesario
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGBA")
                else:
                    img = img.convert("RGB")

                img.save(
                    output_path,
                    format="WEBP",
                    quality=WEBP_QUALITY,
                    method=6  # mejor compresión
                )

                print(f"✔ Convertido: {filename} → {name}.webp")

        except Exception as e:
            print(f"✖ Error con {filename}: {e}")

print("\n✅ Conversión terminada.")

