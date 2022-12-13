# Examle of QR-code generetor on Python using qrcode and dateime modules
# This code result is qr-code like: 2020 12 02 Your_text


import qrcode
import datetime


dt = datetime.datetime.now()
sometext = input('Enter your text: ')
img = qrcode.make('%s %s %s %s' % (dt.year, dt.month, dt.day, sometext))
type(img)
img.save('some.png')
print('Success! Your QR-code generated!')
