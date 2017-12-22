from io import BytesIO
f = BytesIO()
f.write('中文'.encode('UTF-8'))
print(f.getvalue())