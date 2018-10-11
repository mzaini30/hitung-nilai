jumlah_soal = int(input('Berapa soal yang mau diperiksa: '))

while True:
	salah = int(input('Berapa salahnya: '))
	nilai = (jumlah_soal - salah) / jumlah_soal * 100
	pembulatan_ke_atas = '{:.0f}'.format(nilai)
	print(pembulatan_ke_atas)