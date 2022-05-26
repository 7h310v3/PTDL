file_url = str(input("Nhập đường dẫn file: "))

x = []

with open(file_url, 'r') as f:
    for s_line in f:
        txt =s_line.strip()
        tmp = "#Vẽ biểu đồ boxplot cho " + txt + ".\n" + "df_dl.boxplot(['" + txt + "'])"
        x.append(tmp)

for i in x:
    print(i)