import os

def save_to_file(words, path="output/passwords.txt"):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as f:
        for word in words:
            f.write(word + "\n")

    print(f"\n✅ Saved {len(words)} unique passwords to: {path}")
