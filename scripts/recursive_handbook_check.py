import os

root = r"d:/OneDrive/00_Segundo Breno/Breno Peixoto/Doutorado/Disciplinas/Inovaçao em Servicos"
target_pattern = "Handbook of Service Innovation"

results = []
for r, d, f in os.walk(root):
    for file in f:
        if target_pattern.lower() in file.lower() and file.endswith(".pdf"):
            full_path = os.path.join(r, file)
            results.append({
                "name": file,
                "path": full_path,
                "size": os.path.getsize(full_path)
            })

print(f"Found {len(results)} matches:\n")
for item in results:
    print(f" - Name: {item['name']}")
    print(f"   Size: {item['size']} bytes")
    print(f"   Path: {item['path']}\n")

if len(results) >= 2:
    if results[0]["size"] == results[1]["size"]:
        print("IDENTICAL SIZE DETECTED. They are likely duplicates.")
    else:
        print("DIFFERENT SIZES. Possibly different versions.")
