import os
from PIL import Image
from rembg import remove

INPUT_DIR = "imagenes/output"
OUTPUT_DIR = "imagenes/output_nobg"

os.makedirs(OUTPUT_DIR, exist_ok=True)

EXTENSIONS = (".png", ".webp", ".jpg", ".jpeg")

WEBP_QUALITY = 90  # logos = calidad alta

for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(EXTENSIONS):
        input_path = os.path.join(INPUT_DIR, filename)
        name, _ = os.path.splitext(filename)
        output_path = os.path.join(OUTPUT_DIR, f"{name}.webp")

        try:
            with Image.open(input_path) as img:
                # Convertir a RGBA para permitir transparencia
                img = img.convert("RGBA")

                # Quitar fondo con IA
                img_no_bg = remove(img)

                # Guardar como WebP con transparencia
                img_no_bg.save(
                    output_path,
                    format="WEBP",
                    quality=WEBP_QUALITY,
                    method=6,
                    lossless=True  # ideal para logos
                )

                print(f"✔ Fondo eliminado: {filename}")

        except Exception as e:
            print(f"✖ Error con {filename}: {e}")

print("\n✅ Todos los logos procesados sin fondo.")
