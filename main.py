import os
import json
import time
from settings import Settings
from element import Element
class PeriodikTabel:

    def __init__ (self):
        self.settings = Settings()
        
    
    def load_data(self):
        try:
            with open (self.settings.elements_location, 'r') as file:
                self.settings.elements = json.load(file)
        except: 
            self.settings.elements = {}

        try:
            with open (self.settings.users_location, 'r') as file:
                self.settings.users = json.load(file)
        except:
            self.settings.users = {}

    def save_data(self):
        with open(self.settings.elements_location, 'w') as file:
            json.dump(self.settings.elements, file)
    
    def clear_screen(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def show_menus(self):
        self.clear_screen()
        print(self.settings.menu)

    def cari_element(self, simbol):
        elements  = self.settings.elements
        if simbol in elements:
            print("Element ditemukan")
            print(f"Nama Element: {elements[simbol]['nama'].title()}")
            print(f"Simbol Element: {simbol}\t")
            print(f"Nomor Atom: {elements[simbol]['nomoratom']}")
            print(f"Periode: {elements[simbol]['periode']}")
            print(f"Golongan: {elements[simbol]['golongan']}")
            return True
            
        else:
            print("Element tidak ditemukan!")
            
            
    def cek_simbol(self, simbol):
        elemen = self.settings.elements
        if simbol in elemen:
            return True

    def check_option_user(self, pilihan):
        if pilihan == "q":
            pilihan = input("Apakah anda yakin ingin keluar? (y/n)")
            if len(pilihan) == 1:
                if pilihan.lower() == "y":
                    print("Program akan otomatis mati dalam 3 detik.")
                    time.sleep(3)
                    self.settings.active = False
                    self.clear_screen()
                elif pilihan.lower() == "n":
                    input("Tekan Enter Untuk Coba Kembali")
            else:
                print("Tidak Boleh Kosong")
                input("Tekan Enter Untuk Coba Kembali")
        elif pilihan == "1":
            self.clear_screen()
            a = "lihat nama element"
            print(a.upper())
            elements = self.settings.elements
            print(f"Simbol:\t\tNama Element:")

            for simbol, element in elements.items():
                print(f"{simbol}\t\t{element['nama'].title()}")
            input("Press Enter To Return")
        elif pilihan == "2":
            self.clear_screen()
            a = "Informasi lebih detail mengenai element"
            print(a.upper())
            simbol = input("Masukkan Simbol Element : ")
            if len(simbol) < 1:
                print("Tidak Boleh Kosong")
                input("Tekan Enter Untuk Coba Kembali")
            else:
                self.cari_element(simbol)
                input("Tekan Enter Untuk Coba Kembali")
        elif pilihan == "3":
            self.clear_screen()
            a = "Menambahkan element baru"
            print(a.upper())
            simbol = input("Simbol : ")
            if len(simbol) <1 :
                print("Tidak Boleh Kosong")
                input("Tekan Enter Untuk Coba Kembali")
            else:
                if self.cek_simbol(simbol):
                    print("Simbol sudah dipakai\nHarap memasukkan simbol yang lain")
                    input("Tekan Enter Untuk Coba Kembali")
                else:
                    nama = input("Nama Element : ")
                    nomoratom = input("Nomor Atom : ")
                    periode = input("Periode : ")
                    golongan = input("Golongan : ")
                    if len(nama) < 1:
                        print("Gagal menambahkan; Ada yang kosong")
                        
                    elif len(nomoratom) < 1:
                        print("Gagal menambahkan; Ada yang kosong")
                        
                    elif len(periode) < 1:
                        print("Gagal menambahkan; Ada yang kosong")
                        
                    elif len(golongan) <1 :
                        print("Gagal menambahkan; Ada yang kosong")
                    
                    else:
                        element = Element(simbol, nama, nomoratom, periode, golongan)
                        self.settings.elements[element.simbol] = {
                            "nama" : element.nama,
                            "nomoratom" : element.nomoratom,
                            "periode" : element.periode,
                            "golongan" : element.golongan
                        }

                        with open(self.settings.elements_location, 'w') as file:
                            json.dump(self.settings.elements, file)
                        print("Element telah berhasil disimpan")
                    input("Tekan Enter Untuk Kembali")

        elif pilihan == "4":
            self.clear_screen()
            a = "Memperbarui element"
            print(a.upper())
            simbol = input("Simbol Element : ")
            if len(simbol) < 1:
                print("Tidak Boleh Kosong")
                input("Tekan Enter Untuk Coba Kembali")
            else:
                if self.cari_element(simbol):
                    print()
                    print("1. Simbol Element\n2. Nama Element\n3. Nomor Atom\n4. Periode\n5. Golongan\nC. Batal")
                    option = input("Apa yang ingin anda perbarui? (1/2/3/4/5/C)")
                    if len(option) < 1:
                        print("Tidak Boleh Kosong")
                        input("Tekan Enter Untuk Coba Kembali")
                    else:
                        if option == "1":
                            self.clear_screen()
                            print(f"Simbol Element: {simbol}\t")
                            simbol_lama = self.settings.elements[simbol]
                            simbol_baru = input("Masukkan simbol baru : ")
                            if len(simbol_baru) < 1:
                                print("Tidak Boleh Kosong!")
                                input("Tekan Enter Untuk Coba Kembali")
                            else:
                                if self.cek_simbol(simbol_baru):
                                    print("Simbol sama/sudah terpakai\nHarap memasukkan simbol yang baru!")
                                    input("Tekan Enter Untuk Coba Kembali")
                                else:
                                    self.settings.elements[simbol_baru] = {
                                        "nama" : simbol_lama['nama'],
                                        "nomoratom" : simbol_lama['nomoratom'],
                                        "periode" : simbol_lama['periode'],
                                        "golongan" : simbol_lama['golongan']
                                    }

                                    del self.settings.elements[simbol]
                                    self.save_data()
                                    print("Simbol Baru Telah Berhasil Disimpan!")
                                    input("Tekan Enter Untuk Coba Kembali")

                        elif option == "2":
                            self.clear_screen()
                            element= self.settings.elements
                            print(f"Nama Element: {element[simbol]['nama'].title()}")
                            nama_baru = input("Masukkan Nama Baru : ")
                            if len(nama_baru) < 1:
                                print("Tidak Boleh Kosong!")
                            else:
                                self.settings.elements[simbol]['nama'] = nama_baru
                                self.save_data()
                                print("Nama Baru Telah Berhasil Disimpan!")
                            input("Tekan Enter Untuk Coba Kembali")

                        elif option == "3":
                            self.clear_screen()
                            element = self.settings.elements
                            print(f"Nomor Atom: {element[simbol]['nomoratom']}")
                            nomoratom_baru = input("Masukkan Nomor Atom Yang Baru : ")
                            if len(nomoratom_baru) < 1:
                                print("Tidak Boleh Kosong!")
                            else:
                                self.settings.elements[simbol]['nomoratom'] = nomoratom_baru
                                self.save_data()
                                print("Nomor Atom Yang Baru Berhasil Tersimpan!")
                            input("Tekan Enter Untuk Coba Kembali")
                        elif option == "4":
                            self.clear_screen()
                            element = self.settings.elements
                            print(f"Periode: {element[simbol]['periode']}")
                            periode_baru = input("Masukkan Periode Baru : ")
                            if len(periode_baru) < 1:
                                print("Tidak Boleh Kosong!")
                            else:
                                self.settings.elements[simbol]['periode'] = periode_baru
                                self.save_data()
                                print("Periode Yang Baru Berhasil Tersimpan!")
                            input("Tekan Enter Untuk Coba Kembali")
                        elif option == "5":
                            self.clear_screen()
                            element = self.settings.elements
                            print(f"Golongan: {element[simbol]['golongan']}")
                            golongan_baru = input("Masukkan Golongan Baru : ")
                            if len(golongan_baru) < 1:
                                print("Tidak Boleh Kosong!")
                            else:
                                self.settings.elements[simbol]['golongan'] = golongan_baru
                                self.save_data()
                                print("Golongan Yang Baru Berhasil Tersimpan")
                            input("Tekan Enter Untuk Coba Kembali")
                        elif option.upper() == "C":
                            self.clear_screen()
                            input("Tekan Enter Untuk Coba Kembali")
                        else:
                            print("Harap memasukkan pilihan yang ada di menu!")
                            True
                            input("Tekan Enter Untuk Kembali")
                else:
                    input("Tekan Enter Untuk Coba Kembali")
        elif pilihan == "5":
            self.clear_screen()
            a = "Menghapus element"
            print(a.upper())
            simbol = input("Masukkan Simbol Element : ")
            if len(simbol) < 1:
                print("Tidak Boleh Kosong")
                input("Tekan Enter Untuk Coba Kembali")
            else:
                if self.cari_element(simbol):
                    hapus = input("Apakah anda yakin ingin menghapus element ini ? (y/n)")
                    if len(hapus) < 1:
                        print("Tidak Boleh Kosong")
                        input("Tekan Enter Untuk Coba Kembali")
                    else:
                        if hapus.lower() == "y":
                            del self.settings.elements[simbol]
                            self.save_data()
                            print("Element Telah Dihapus")
                            input("Tekan Enter Untuk Coba Kembali")
                        elif hapus.lower() == "n":
                            input("Tekan Enter Untuk Coba Kembali")
                        else:
                            print("Harap Masukkan pilihan yang ada di menu")
                else:
                    input("Tekan Enter Untuk Coba Kembali")
        elif len(pilihan) < 1:
            print("Tidak Boleh Kosong!")
            input("Tekan Enter Untuk Coba Kembali")
        else:
            print("Harap memasukkan nomor yang ada di menu")
            True
            input("Tekan Enter Untuk Coba Kembali")
    def run(self):
        self.load_data()
        self.settings.active = True

        while self.settings.active:
            self.show_menus()
            self.check_option_user(input("Masukkan Pilihan : ").lower())

            
if __name__ == '__main__':
    app = PeriodikTabel()
    app.run()