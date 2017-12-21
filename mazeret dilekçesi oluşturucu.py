metin = ("""
			        {} Müdürlüğüne
		Okulunuz öğrencisi {} numaralı velisi bulunduğum {},
		{} günü {} sebebiyle devamsızlık yapmıştır. İzinli sa-
		yılması ve gereğinin yapılmasını arz ederim. 
		""")
okul = input("Okulunuzu giriniz:")
numara = input("Numaranızı giriniz: ")
isim = input("İsminizi giriniz: ")
mazeret = input("Mazeret giriniz: ")
gün = input("Gün giriniz: ")
çıktı = metin.format(okul, numara, isim, gün, mazeret)
print(çıktı)
input()