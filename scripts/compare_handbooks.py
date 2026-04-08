import os

p1 = r"d:/OneDrive/00_Segundo Breno/Breno Peixoto/Doutorado/Disciplinas/Inovaçao em Servicos/Agarwal Selen, Roos & Gree (2015) - The handbook of service innovation.pdf"
p2 = r"d:/OneDrive/00_Segundo Breno/Breno Peixoto/Doutorado/Disciplinas/Inovaçao em Servicos/Agarwal Selen, Roos & Gree (2015) - The handbook of service innovation_ texto 1.pdf"

print(f"File 1: {os.path.exists(p1)}")
if os.path.exists(p1):
    print(f" - Size: {os.path.getsize(p1)} bytes")

print(f"File 2: {os.path.exists(p2)}")
if os.path.exists(p2):
    print(f" - Size: {os.path.getsize(p2)} bytes")

if os.path.exists(p1) and os.path.exists(p2):
    if os.path.getsize(p1) == os.path.getsize(p2):
        print("\nIDENTICAL SIZE DETECTED. Likely a duplicate.")
    else:
        print("\nDIFFERENT SIZES. Possibly different versions.")
