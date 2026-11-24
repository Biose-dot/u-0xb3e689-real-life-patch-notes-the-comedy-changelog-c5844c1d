import os

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
text = "v2.3: Nerfed hiccups (now last 2 minutes max), fixed bug where yawning is contagious, and Mondays now load 10% faster."
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(text)
