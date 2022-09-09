from datetime import date, datetime,timedelta
import calendar
import os
import locale
locale.setlocale(locale.LC_TIME, 'id_ID')

today = date.today()
yesterday = date.today() - timedelta(days=1)
yesterday2 = date.today() - timedelta(days=2)
tomorrow = date.today() + timedelta(days=1)
datetoday = today.day
bulan = calendar.month_name[today.month]
bulanangka = datetime.now().month

# date
tglkmrn = yesterday.strftime("%d")
tglskr = today.strftime("%d")
tglbsk = tomorrow.strftime("%d")
blnskr = today.strftime("%m")
thnskr = today.strftime("%Y")

# dd/mm/YY
kmrn = yesterday.strftime("%d%m%Y")
bsk = tomorrow.strftime("%d%m%Y")
skr = today.strftime("%d%m%Y")

# .strftime("%d %B, %Y")
tanggalkemarin = yesterday.strftime("%d %B %Y")
tanggalsekarang = today.strftime("%d %B %Y")
#print(tanggalkemarin2)
