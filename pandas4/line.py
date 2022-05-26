file_url = str(input("Nhập đường dẫn file: "))

x = []

with open(file_url, 'r') as f:
    for s_line in f:
        txt =s_line.strip()
        x.append(txt)

print(x)
