def get_inputs():
    print("🔱 SHAKUNI - The Password Mind Twister 🧠")
    print("Enter any details you remember (you can leave blank):\n")

    fields = ["name", "dob", "color", "nickname", "suffix"]
    result = {}

    for field in fields:
        value = input(f"{field.capitalize()} (optional): ").strip()
        if value:
            result[field] = value

    return result
