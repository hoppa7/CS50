def main():
    x = input("File name:")
    if x.endswith(".gif"):
        return "image/gif"
    elif x.endswith(".jpg"):
        return "image/jpeg"
    elif x.endswith(".jpeg"):
        return "image/jpeg"
    elif x.endswith(".png"):
        return "image/png"
    elif x.endswith(".pdf"):
        return "image/pdf"
    elif x.endswith(".txt"):
        return "text"
    elif x.endswith(".zip"):
        return "zipFile"
    else:
        return "application/octet-stream"

answer = main()
print(answer)