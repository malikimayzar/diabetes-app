from gtts import gTTS
import pygame
import os
import time

# Inisialisasi mixer sekali di awal
pygame.mixer.init()

def speak(text):
    tts = gTTS(text=text, lang='id')
    filename = "type.mp3"
    tts.save(filename)

    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        pygame.mixer.music.unload()  # ⬅️ ini penting agar file bisa dihapus!
    except Exception as e:
        print(f"Gagal memutar suara: {e}")
    finally:
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except PermissionError:
                print("Gagal menghapus file: masih digunakan.")

def play_special_sound():
    sound_files = {
        'login': 'assets/sound_login.mp3',
        'boom': 'assets/boom.mp3'
    }

    for sound_type, file_path in sound_files.items():
        try:
            if os.path.exists(file_path):
                print(f"Memutar {sound_type}...")
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)
            else:
                print(f"File {file_path} tidak ditemukan!")
        except Exception as e:
            print(f"Gagal memutar {sound_type}: {e}")

# Database dictionary
database = {}

def tambah_data():
    speak("Masukkan nama:")
    nama = input("Masukkan nama: ").strip().lower()

    if nama.lower() == "mayzar":
        print("Developer telah terdeteksi")
        play_special_sound()
    
    speak("Masukkan umur:")
    while True:
        try:
            umur = int(input("Masukkan umur: "))
            break
        except:
            speak("Umur harus angka! Coba lagi")
    
    speak("Masukkan kota:")
    kota = input("Masukkan kota: ")
    
    database[nama] = (umur, kota)
    speak(f"Data {nama} berhasil ditambahkan!")

def lihat_statistik():
    if not database:
        speak("Database masih kosong")
        return
    
    umur_list = [data[0] for data in database.values()]
    total = sum(umur_list)
    rata_rata = total / len(umur_list)
    umur_tertinggi = max(umur_list)
    umur_terendah = min(umur_list)
    
    frekuensi = {}
    for umur in umur_list:
        frekuensi[umur] = frekuensi.get(umur, 0) + 1
    modus = [k for k, v in frekuensi.items() if v == max(frekuensi.values())]
    
    statistik = f"""
Statistik Database:
Jumlah data     : {len(database)}
Total umur      : {total}
Rata-rata umur  : {rata_rata:.1f}
Umur tertinggi  : {umur_tertinggi}
Umur terendah   : {umur_terendah}
Modus umur      : {', '.join(map(str, modus))}
"""
    print(statistik)
    speak("Ini statistik database:")
    speak(f"Total {len(database)} data")
    speak(f"Rata-rata umur {rata_rata:.1f} tahun")
    speak(f"Dari yang termuda {umur_terendah} sampai tertua {umur_tertinggi} tahun")

def tampilkan_semua_data():
    if not database:
        speak("Database masih kosong")
        return
    
    speak("Menampilkan semua data")
    print("\nDaftar Orang:")
    for idx, (nama, (umur, kota)) in enumerate(database.items(), 1):
        print(f"{idx}. {nama}: Umur {umur} tahun, dari {kota}")
    
    speak("Isi database saat ini:")
    for nama, data in database.items():
        speak(f"{nama}, berumur {data[0]} tahun, dari {data[1]}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    speak("Selamat datang di program database interaktif!")
    
    while True:
        print("\nMenu:")
        print("1. Tambah data")
        print("2. Lihat semua data")
        print("3. Lihat statistik")
        print("4. Keluar")
        
        speak("Pilih menu 1 sampai 4")
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_semua_data()
        elif pilihan == "3":
            lihat_statistik()
        elif pilihan == "4":
            speak("Terima kasih telah menggunakan program ini!")
            break
        else:
            speak("Pilihan tidak valid. Coba lagi")

if __name__ == "__main__":
    main()
