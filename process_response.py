def separate(text):
    parts = text.split(":")
    initial_text = parts[0].strip()
    list_points = parts[1].strip().split("\n")
    return initial_text, list_points