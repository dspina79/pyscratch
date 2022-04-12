# reading a file

with open("io/reading/sample.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)
    f.close()

