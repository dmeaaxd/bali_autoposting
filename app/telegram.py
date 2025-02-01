import re

def convert_to_download_url(cell_value):
    match = re.search(r'IMAGE\("https://drive\.google\.com/uc\?export=view&id=([^"]+)"\)', cell_value)
    if match:
        file_id = match.group(1)
        return f"https://drive.google.com/uc?export=download&id={file_id}"
    return cell_value

def brease_row(row: list):
    phone = row[2]
    channels = row[3].split('\n')
    message = row[4]
    images_row = row[5:]
    images = list()

    for image in images_row:
        images.append(convert_to_download_url(image))


    return phone, channels, message, images


row = ['PF270', 'Альбина', 9518416997, 'bali_dom \nbali_arendaa', '🏝Вилла 5 спален в Нуса Дуа, красивый видом с крыши \r\n\r\n💰Стоимость 70 млн в месяц\r\nДоступна для годовой аренды 630 млн в год \r\n\r\nСобственный бассейн \r\nУборка, смена постельного белья и обслуживание бассейна включены в стоимость', '=IMAGE("https://drive.google.com/uc?export=view&id=1YpADfVbR18oO8m0pIr_KLQMUN5rqxSUX")', '=IMAGE("https://drive.google.com/uc?export=view&id=1wkwvaEEcDrFvedEim4rmeZNWV3kwdClJ")', '=IMAGE("https://drive.google.com/uc?export=view&id=1n4FKiUdf_7wqt5Ov7uj3DJtl2DM3tGIR")', '=IMAGE("https://drive.google.com/uc?export=view&id=1I39xlvEjFuIT_k5wvFenrirQIGlB2tUb")', '=IMAGE("https://drive.google.com/uc?export=view&id=1YiqBjPcB-Xaap0uH4ShSOisthFPaVIZQ")', '=IMAGE("https://drive.google.com/uc?export=view&id=1JaBqxLZXUBu94lln8Ej7zR_fpIw943Ya")']


print(brease_row(row)[0])
print(brease_row(row)[1])
print(brease_row(row)[2])
print(brease_row(row)[3])



