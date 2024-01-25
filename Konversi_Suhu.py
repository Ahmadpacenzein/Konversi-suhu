

# MEMULAI PROGRAM

print("                              ==============================================")
print("                              |           Program Konversi Suhu            |")
print("                              |             by : Ahmad Zaini               |")
print("                              ==============================================")
print(" \n \n")
while True  :
#MEMINTA INPUT USER DENGAN WHILE LOOP

    while True:
        print("|======================================================================")
        print("| Pilihan suhu = \n| [1]. Celcius \n| [2]. Reamur \n| [3]. Fahrenhait \n| [4]. Kelvin")
        input_user = int(input("| Pilih salah satu jenis suhu (pilih = 1/2/3/4) = "))
        print("|======================================================================")

#HANDLING ERROR PILIHAN TIDAK TERSEDIA

        if input_user >= 5 :
            print("| Pilihan tidak tersedia ! Mohon pilih kembali")
        else:
            break

#JALANKAN PROGRAMS DAN PRINT HASIL
    if input_user==1:
        print("|======================================================================")
        suhu_celcius=int(input("| ▶ Masukan suhu Celcius = "))
        print(f"| {suhu_celcius}°C setara dengan = ")                           #pacen
        reamur_celcius= 4/5*suhu_celcius
        print(f"| ↦ Suhu Reamur = {reamur_celcius} °Re")
        kelvin_celcius = suhu_celcius + 273
        print(f"| ↦ Suhu Kelvin = {kelvin_celcius} °K")
        fahrenhait_celcius = 9/5*suhu_celcius+32
        print(f"| ↦ Suhu Fahrenhait = {fahrenhait_celcius} °F")
        print("|======================================================================")
    elif input_user==2 :
        print("|======================================================================")
        suhu_reamur=int(input("| ▶ Masukan suhu Reamur = "))
        print(f"| {suhu_reamur}°Re setara dengan = ")
        celcius_reamur = 5/4*suhu_reamur
        print(f"| ↦ Suhu Celcius = {celcius_reamur} °C")
        kelvin_reamur = celcius_reamur + 273
        print(f"| ↦ Suhu Kelvin = {kelvin_reamur} °K")
        fahrenhait_reamur = 9/4*suhu_reamur+32
        print(f"| ↦ Suhu Fahrenhait = {fahrenhait_reamur} °F")
        print("|======================================================================")
    elif input_user==3 :                                               #pacen
        print("|======================================================================")
        suhu_fahrenhait=int(input("| ▶ Masukan suhu Fahrenhait = "))
        print(f"| {suhu_fahrenhait}°F setara dengan = ")
        celcius_fahrenhait = 5/9 * (suhu_fahrenhait-32)
        print(f"| ↦ Suhu Celcius = {celcius_fahrenhait} °C")
        reamur_fahrenhait = 4/9 * (suhu_fahrenhait-32)
        print(f"| ↦ Suhu Reamur = {reamur_fahrenhait} °R")
        kelvin_fahrenhait = 5/9 * (suhu_fahrenhait-32) + 273
        print(f"| ↦ Suhu Kelvin = {kelvin_fahrenhait} °K")
        print("|======================================================================")
    elif input_user==4 :
        print("|======================================================================")
        suhu_kelvin=int(input("| ▶ Masukan suhu Kelvin = "))
        print(f"| {suhu_kelvin}°K setara dengan = ")
        celcius_kelvin = suhu_kelvin - 273
        print(f"| ↦ Suhu Celcius = {celcius_kelvin} °C")
        reamur_kelvin = 4/5 * (suhu_kelvin-273)
        print(f"| ↦ Suhu Reamur = {reamur_kelvin} °R")
        fahrenhait_kelvin = 9/5 * (suhu_kelvin - 273) + 32
        print(f"| ↦ Suhu Fahrenhait = {fahrenhait_kelvin} °F")
        print("|======================================================================")
#MEMINTA USER UNTUK MENGULANG PROGRAM KEMBALI ATAU TIDAK
    reload_program = input("Apakah anda ingin menjalankan program kembali ? (pilih y/n) = ")
    
    if reload_program == "y" or reload_program== "Y":
            print("reloading.....")
    else:
        break
 
    