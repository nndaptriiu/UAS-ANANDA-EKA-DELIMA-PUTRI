### CLASS PROSES NILAI ###
class ProsesNilai:
    """Class untuk memproses perhitungan nilai"""

    @staticmethod
    def hitung_nilai_akhir(mahasiswa):
        """Menghitung nilai akhir dengan bobot: Tugas 30%, UTS 35%, UAS 35%"""
        nilai_akhir =(mahasiswa.nilai_tugas * 0.3) + \
                     (mahasiswa.nilai_uts * 0.35) + \
                     (mahasiswa.nilai_uas * 0.35)
        mahasiwa.nilai_akhir = nilai_akhir
        return nilai_akhir

    @staticmethod
    def tentukan_grade(nilai_akhir):
        """Menentukan grade berdasarkan nilai akhir"""
        if nilai_akhir >= 85:
            return "A"
        elif nilai_akhir >= 70:
            return "B"
        elif nilai_akhir >= 60:
            return "C"
        elif nilai_akhir >= 50:
            return "D"
        else:
            return "F"
