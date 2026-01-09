class TampilanNilai:
    """Class untuk menampilkan output"""

    @staticmethod
    def tampilkan_header():
        """Menampilkan header tabel"""
        print("\n" + "=" * 90)
        print(f"{'NIM':<12} | {'NAMA':<20} | {'TUGAS':<6} | {'UTS':<6} | {'UAS':<6} | {'AKHIR':<7} | {'GRADE':<5}")
        print("=" * 90)

    @staticmethod
    def tampilkan_mahasiswa(mahasiswa):
        """Menampilkan data satu mahasiswa"""
        print(f"{mahasiswa.nim:<12} | {mahasiswa.nama:<20} | {mahasiswa.nilai_tugas:<6.1f} | "
              f"{mahasiswa.nilai_uts:<6.1f} | {mahasiswa.nilai_uas:<6.1f} | "
              f"{mahasiswa.nilai_akhir:<7.2f} | {mahasiswa.grade:<5}")

    @staticmethod
    def tampilkan_footer():
        """Menampilkan footer tabel"""
        print("=" * 90)