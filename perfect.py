import random
import string
import time
from datetime import datetime
from tabulate import tabulate

def main():
    nomor_urut = 1
    hasil_data = []

    while True:
        # Buat angka random dengan panjang 64 karakter
        angka_random = ''.join(random.choice(string.hexdigits + string.ascii_letters) for _ in range(64))

        # Pilih kode warna secara acak untuk pesan "Sukses"
        kode_warna_sukses = random.choice(['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m'])

        # Pilih kode warna secara acak untuk angka_random
        kode_warna_angka = random.choice(['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m'])
        while kode_warna_angka == kode_warna_sukses:
            kode_warna_angka = random.choice(['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m'])

        # Format data yang akan dicetak
        data = [f"{nomor_urut}.", f"{kode_warna_sukses}Sukses{chr(27)}[0m", f"{kode_warna_angka}{angka_random}{chr(27)}[0m"]
        print(tabulate([data], headers=["Nomor", "Pesan", "Private-key"], tablefmt="grid"))

        # Simpan angka_random dan waktu ke dalam list hasil_data
        waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hasil_data.append([nomor_urut, waktu_sekarang, angka_random, "Sukses"])

        # Tunda eksekusi berikutnya selama 1 detik
        time.sleep(1)

        nomor_urut += 1

        # Tampilkan data yang telah terkumpul setiap kali mencetak 10 baris
        if nomor_urut % 10 == 1 and nomor_urut > 1:
            cow_msg = ""
            for data in hasil_data:
                cow_msg += f"{data[0]}. {data[1]} - {data[2]}\n"
                cow_msg += f"{data[3]}\n"

            print(cow_msg)

            # Simpan hasil_data ke dalam file privatekey.txt dan hapus data yang sudah tercetak
            with open('privatekey.txt', 'a') as file:
                for data in hasil_data:
                    file.write(f"{data[0]}. {data[1]} - {data[2]}\n")
                    file.write(f"{data[3]}\n")

            hasil_data = []

if __name__ == "__main__":
    main()


