import requests
try:
    r= requests.get('https://www.google.com/')
    print(r.status_code) #bila hasilnya 200 maka berhasil
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print("ada error",e) #bila ada yang tdk sesuai e akan menjelaskan kesalahan


#berikut keterangan warna file di Pycharm
#biru = sudah disimpan di pycharm user tapi blm di github
#hijau = file baru yang belum ada di github
