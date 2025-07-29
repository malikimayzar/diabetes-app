from gtts import gTTS
from playsound import playsound
import os
import random

def speak(text):
    tts = gTTS(text=text, lang='id')
    tts.save("type.mp3")
    playsound("type.mp3")
    os.remove("type.mp3")

responses = {
    "mayzar": ["Waduh, developer kita Turun nihhh", "Nyaa,Muhun aa nuju nyobian", "Raja Iblis Muncul Jirr"]
}

speak("Ada Pribahasa Tak Kenal Maka Tawakal Btw Nama Kamu Siapa ni?")
print("Ada Pribahasa Tak Kenal Maka Tawakal Btw Nama Kamu Siapa ni?")
nama = input("Kimi No Namaewa: ")
speak(f" halawww, {nama} Senang bertemu dengan mu")

if nama.lower() == "mayzar":
    respon = random.choice(responses["mayzar"])
    print(respon)
    speak(respon)
else:
    speak(f"Halo {nama}")

# Tampilkan Pilihan Operasi
speak(f"Ohh iya,{nama} aku ada pilihan operasi & suhu ni Silahkan Pilih Operasi bilangan di bawah ini ya....")
print("\nPilihan Operasi & suhu:")
print("1. Perjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Pekalian (x)") 
print("4. Pembagian (/)")
print("5. Pembagian Bulat (%)")
print("6. Sisa pembagian (//)")
print("7. Pangkat (xx)")
print("8. Menghitung Suhu")

while True:
    pilihan_operasi = input("Masukkan pilihan operasi (1-8): ")
    
    if not pilihan_operasi.isdigit() or int(pilihan_operasi) < 1 or int(pilihan_operasi) > 8:
        print("Masukkan angka antara 1-8!")
        speak("Masukkan angka antara 1-8!")
        continue
    
    if pilihan_operasi == "8":
        celcius = float(input("Masukkan suhu dalam Celcius: "))
        print(f"suhu adalah {celcius} Celcius")
        
        reamur = (4/5) * celcius
        teks = f"suhu dalam reamur {reamur} Reamur"
        print(teks)
        speak(teks)
        
        fahrenheit = ((9/5) * celcius) + 32
        teks = f"suhu dalam fahrenheit {fahrenheit} Fahrenheit"
        print(teks)
        speak(teks)
        
        kelvin = celcius + 273.15
        teks = f"suhu dalam kelvin {kelvin} Kelvin"
        print(teks)
        speak(teks)
        continue
    
    angka1 = input("Masukan Angka Pertama: ")
    angka2 = input("Masukan Angka Kedua: ")
    angka3 = input("Masukan Angka Ketiga: ")
    angka4 = input("Masukan Angka Keempat: ")
    
    try:
        angka1 = float(angka1)
        angka2 = float(angka2)
        angka3 = float(angka3)
        angka4 = float(angka4)
        
        # Proses Dan Hasil
        if pilihan_operasi == "1":
            hasil = angka1 + angka2 + angka3 + angka4
            teks = f"Jadi Hasil Perjumlahan nya ini ya {nama}\n {hasil}"
        elif pilihan_operasi == "2":
            hasil = angka1 - angka2 - angka3 - angka4
            teks = f"Jadi Hasil Pengurangan nya ini ya {nama}\n {hasil}"
        elif pilihan_operasi == "3":
            hasil = angka1 * angka2 * angka3 * angka4
            teks = f"Jadi Hasil Perkalian nya ini ya {nama}\n {hasil}"    
        elif pilihan_operasi == "4":
            if angka2 == 0 or angka3 == 0 or angka4 == 0:
                teks = "Tidak bisa melakukan pembagian dengan nol!"
            else:
                hasil = angka1 / angka2 / angka3 / angka4
                teks = f"Jadi Hasil Pembagian nya ini ya {nama}\n {hasil}"
        elif pilihan_operasi == "5":
            if angka2 == 0 or angka3 == 0 or angka4 == 0:
                teks = "Tidak bisa melakukan pembagian dengan nol!"
            else:
                hasil = angka1 // angka2 // angka3 // angka4
                teks = f"Jadi Hasil Pembagian Bulat nya ini ya {nama}\n {hasil}"
        elif pilihan_operasi == "6":
            if angka2 == 0 or angka3 == 0 or angka4 == 0:
                teks = "Tidak bisa melakukan pembagian dengan nol!"
            else:
                hasil = angka1 % angka2 % angka3 % angka4
                teks = f"Jadi Hasil Sisa Pembagian nya ini ya {nama}\n {hasil}"
        elif pilihan_operasi == "7":
            hasil = angka1 ** angka2 ** angka3 ** angka4
            teks = f"Jadi Hasil Pangkat nya ini ya {nama}\n {hasil}"
        
        print(teks)
        speak(teks)
        
    except ValueError:
        print("Input harus berupa angka!")
        speak("Sia.., Ngarti Angka Hungkul, Teu? Setan...,")
        print("Silakan coba lagi.\n")