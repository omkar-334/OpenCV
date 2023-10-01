import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('image.png')
for detection in result:
    text = detection[1]
    print(text)