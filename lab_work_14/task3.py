import qrcode

print("Illya Vorobey, IT-31")

text = "Illya Vorobey, IT-31, vorobey@gmail.com"

image = qrcode.make(text)
image.save("contact.png")

print("saved: contact.png")