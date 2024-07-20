class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def __str__(self):
        return f"Nama: {self.nama}, NIM: {self.nim}, Jurusan: {self.jurusan}"

class ManajemenMahasiswa:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.data_mahasiswa.append(mahasiswa)

    def hapus_mahasiswa(self, nim):
        self.data_mahasiswa = [mhs for mhs in self.data_mahasiswa if mhs.nim != nim]

    def tampilkan_semua_mahasiswa(self):
        for mahasiswa in self.data_mahasiswa:
            print(mahasiswa)

def main():
    manajemen = ManajemenMahasiswa()

    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Hapus Mahasiswa")
        print("3. Tampilkan Semua Mahasiswa")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan Nama: ")
            nim = input("Masukkan NIM: ")
            jurusan = input("Masukkan Jurusan: ")
            mahasiswa = Mahasiswa(nama, nim, jurusan)
            manajemen.tambah_mahasiswa(mahasiswa)
        elif pilihan == "2":
            nim = input("Masukkan NIM Mahasiswa yang akan dihapus: ")
            manajemen.hapus_mahasiswa(nim)
        elif pilihan == "3":
            manajemen.tampilkan_semua_mahasiswa()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
