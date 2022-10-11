from tanggal import *
from PIL import Image
folderNDF = ("D:/TAHUN "+thnskr+"/9. SEPTEMBER/NDF/10092022/")

yapen = Image.open(folderNDF+"yapen.png")
yapen.mode

print(yapen.mode)