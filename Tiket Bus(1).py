print ("**********Selamat Datang Di Agen Resmi Tiket Bis Antar Daerah**********")

print ("\nDaftar Pilihan Keberangkatan :")
def list ():
    print ("==========================================")
    print ('1. Jakarta - Tasik           : Rp.50000')
    print ('2. Jakarta - Bandung         : Rp.65000')
    print ('3. Jakarta - Pekalongan      : Rp.100000')
    print ('4. Jakarta - Surabaya        : Rp.125000')
    print ('5. Jakarta - Jogja           : Rp.150000')
    print ('6. Jakarta - Semarang        : Rp.200000')
    print ("==========================================")
list()

a = int (input("Silahkan Pilih Bis Keberangkatan Anda(Silahkan Ketik Nomor)"))
if a == 1:
    spec = 'Jakarta - Tasik'
    harga = 50000
elif a == 2:
    spec = 'Jakarta - Bandung'
    harga = 65000
elif a == 3:
    spec = 'Jakarta - Pekalongan'
    harga = 100000
elif a == 4:
    spec = 'Jakarta - Surabaya'
    harga = 125000
elif a == 5:
    spec = 'Jakarta - Jogja'
    harga = 150000
elif a == 6:
    spec = 'Jakarta - Semarang'
    harga = 200000
else:
    while True:
        print ("**********Tujuan Anda Tidak Tersedia, Silahkan Pilih Lagi!**********")
        a = int (input("Silahkan Pilih Bis Keberangkatan Anda(Silahkan Ketik Nomor): "))
        if a == 1 or a == 2 or a == 3 or a == 4 or a == 5 or a == 6:
            if a == 1:
                spec = 'Jakarta - Tasik'
                harga = 50000
            elif a == 2:
                spec = 'Jakarta - Bandung'
                harga = 65000
            elif a == 3:
                spec = 'Jakarta - Pekalongan'
                harga = 100000
            elif a == 4:
                spec = 'Jakarta - Surabaya'
                harga = 125000
            elif a == 5:
                spec = 'Jakarta - Jogja'
                harga = 150000
            elif a == 6:
                spec = 'Jakarta - Semarang'
                harga = 200000
            break
total = int (input("Masukan Jumlah Tiket Pembelian :"))
print('\nNota Pembelian Tiket')

print('Jurusan          :',spec)
print('Jumlah Tiket     :',total)
print('Harga            :Rp.',harga)
bayar = total * harga

print ("Anda Harus Membayar : Rp.{}".format(bayar))
ubay=int(input("Uang Bayar :"))
kembali=(ubay-bayar)
print('Uang Kembali :',kembali)
print('\nNote : Didalam Perjalanan Sudah Dapat')
bonus = ['Air Minum','Nasi Box','Selimut']
for i in range (len(bonus)):
    print("1 buah",bonus[i])
print ("===========================================================================")
print ('********Terima Kasih Atas Kepercayaannya Menggunakan Jasa Kami********')
print ("===========================================================================")
exit()