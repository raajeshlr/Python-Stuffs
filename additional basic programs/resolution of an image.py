def resoltion(filename):
    image_file = open(filename,'rb')
    image_file.seek(163)
    a = image_file.read(2)
    height = (a[0]<<8) + a[1]
    a = image_file.read(2)
    width = (a[0]<<8) + a[1]
    print("the resolution is ",width,"x",height)

resoltion("image.jpg")