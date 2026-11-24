import os

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
text = "Patch 1.0.1: Fixed bug where humans need 8 hours of sleep but only get 5. Added optional snooze button to Mondays."
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(text)
