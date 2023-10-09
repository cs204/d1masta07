FILES_TYPES = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip" : "application/zip"
}

user_input = input().lower().split(".")
print(f"File name: {FILES_TYPES.get(user_input[-1], 'application/octet-stream')}")