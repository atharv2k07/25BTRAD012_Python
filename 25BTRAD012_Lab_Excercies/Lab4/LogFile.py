try:
    with open("application.log", "r") as f:
        data = f.read().upper()

    for word in ["ERROR", "WARNING", "INFO"]:
        print(word, ":", data.count(word))

    if not data:
        print("File is empty")

except FileNotFoundError:
    print("File not found")