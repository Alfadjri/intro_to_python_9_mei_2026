import datetime

tanggal = datetime.datetime.now()
perintal = "Surat Sakit"
jumlah_lampiran = 2
nama_atasan = "Jokowi Dodo"

# posisional argumen
print("============")
print("{0}\nPerihal:{1}\nJumlah Lampiran : {2}\nKepada Yth {3}".format(tanggal,perintal,nama_atasan,jumlah_lampiran))
#keyword
print("============")
print("{tanggal}\nPerihal:{hal}\nJumlah Lampiran : {lampiran}\nKepada Yth {atasan}".format(tanggal = tanggal,hal = perintal,atasan =nama_atasan,lampiran = jumlah_lampiran))
print("============")
print(f"{tanggal}\nPerihal:{perintal}\nJumlah Lampiran : {jumlah_lampiran}\nKepada Yth {nama_atasan}")