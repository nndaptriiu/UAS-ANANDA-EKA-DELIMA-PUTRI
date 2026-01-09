### Main Program ###
def main():
    daftar_mahasiswa = []
    proses = "ProsesNilai()"
    tampilan = "TampilanNilai()"
    validasi = "Validasi()"

    print("=" * 90)
    print(" PROGRAM SISTEM PENILAIAN MAHASISWA ".center(90))
    print("=" * 90)

    while True:
        print("\n--- Input Data Mahasiswa ---")

        try:
            # Input data mahasiswa
            nim = input("NIM: ").strip()
            if not nim:
                print("NIM tidak boleh kosong!")
                continue

            nama = input("Nama: ").strip()
            if not nama:
                print("Nama tidak boleh kosong!")
                continue

            # Input nilai dengan validasi
            nilai_tugas = validasi.validasi_nilai(input("Nilai Tugas (0-100): "))
            nilai_uts = validasi.validasi_nilai(input("Nilai UTS (0-100): "))
            nilai_uas = validasi.validasi_nilai(input("Nilai UAS (0-100): "))

            # Proses nilai
            nilai_akhir = proses.hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
            grade = proses.tentukan_grade(nilai_akhir)

            # Simpan data
            mahasiswa = {
                'nim': nim,
                'nama': nama,
                'nilai_tugas': nilai_tugas,
                'nilai_uts': nilai_uts,
                'nilai_uas': nilai_uas,
                'nilai_akhir': nilai_akhir,
                'grade': grade
            }
            daftar_mahasiswa.append(mahasiswa)

            print(f"\nData berhasil disimpan! Nilai Akhir: {nilai_akhir:.2f}, Grade: {grade}")

        except ValueError as e:
            print(f"Error: {e}")
            continue
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan oleh user.")
            break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            continue

        # Tanya apakah ingin melanjutkan
        lanjut = input("\nTambah data lagi? (y/t): ").lower()
        if lanjut != 'y':
            break

    # Tampilkan semua data
    if daftar_mahasiswa:
        print("\n" + "=" * 90)
        print(" DATA NILAI MAHASISWA ".center(90))
        print("=" * 90)
        tampilan.tampilkan_data(daftar_mahasiswa)
    else:
        print("\nTidak ada data yang diinput.")


if __name__ == "__main__":
    main()