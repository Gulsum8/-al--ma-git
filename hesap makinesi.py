def toplama(a, b):
  return a + b
def cikarma(a, b):
  return a - b
def carpma(a, b):
  return a *b
def bolme (a, b):
  if b == 0:
    print("Tanımsız")
  else:
    return a / b
def karekok(a):
  return a ** 0.5
def us_alma(a, b):
  return a **b
def faktoriyel(a):
  if a == 0:
    return 1
  else:
    return a * faktoriyel(a - 1)


print("MENU")
print("0-Çıkış")
print("1-Toplama")
print("2-Çıkarma")
print("3-Çarpma")
print("4-Bölme")
print("5-Karekök")
print("6-Üs alma")
print("7-Faktöriyel")

bas_secim = input("Menüden bir işlem seçiniz (0-1-2-3-4-5-6-7):")



if bas_secim == "1":
  sayi_1 = float(input("Bir sayı giriniz:"))
  sayi_2 = float(input("Şimdi başka bir sayı giriniz:"))

  print("Cevabınız:", toplama(sayi_1, sayi_2))


elif bas_secim == "2":
  sayi_1 = float(input("Bir sayı giriniz:"))
  sayi_2 = float(input("Şimdi başka bir sayı giriniz:"))

  print("Cevabınız:", cikarma(sayi_1, sayi_2))


elif bas_secim == "3":
  sayi_1 = float(input("Bir sayı giriniz:"))
  sayi_2 = float(input("Şimdi başka bir sayı giriniz:"))

  print("Cevabınız:", carpma(sayi_1, sayi_2))


elif bas_secim == "4":
  sayi_1 = float(input("Bir sayı giriniz:"))
  sayi_2 = float(input("Şimdi başka bir sayı giriniz:"))

  print("Cevabınız:", bolme(sayi_1, sayi_2))


elif bas_secim == "5":
  sayi_1 = float(input("Bir sayı giriniz:"))

  print("Cevabınız:", karekok(sayi_1))


elif bas_secim == "6":
  sayi_1 = float(input("Bir sayı giriniz:"))
  sayi_2 = float(input("Şimdi başka bir sayı giriniz:"))

  print("Cevabınız:", us_alma(sayi_1, sayi_2))


elif bas_secim == "7":
  sayi_1 = float(input("Bir sayı giriniz:"))

  print("Cevabınız:", faktoriyel(sayi_1))
else:
  print("Bir Hata Gördüm Sanki!!!!!")