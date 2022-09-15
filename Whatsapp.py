import pywhatkit
from tanggal import thnskr, bulanangka, bulan, skr, tanggalsekarang

folder = ("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/RRI/")
#pywhatkit.sendwhatmsg_instantly("+6282248864335", "Informasi prakiraan cuaca Kabupaten Provinsi Papua serta prakiraan cuaca pelayaran dan tinggi gelombang Perairan Papua - Papua Barat, "+tanggalsekarang+" berlaku 24 jam mulai pukul 09.00 WIT", )
pywhatkit.sendwhats_image("+6285244365190", folder+skr+".png", "Mohon izin menyampaikan update prakiraan cuaca wilayah Papua tanggal "+tanggalsekarang+". Terima kasih")
