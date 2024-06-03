'''
KELOMPOK 5

Arasy Hemasthiar
Bulan Dewi Gulita
Hilmi Tito Shalahudin
M. Fajar Latiful Habib
'''


# Data penampung sementara ketika melakukan registrasi 
data_user = {}

def cek_Alphanumeric(string): #memeriksa apakah string hanya mengandung huruf dan angka menggunakan method.is_alphanumeric
    return all(char.isalnum() for char in string) #mengembalikan "True" jika 'char' adalah huruf atau angka  

def cek_Huruf(string): #memeriksa apakah string hanya mengandung huruf 
    return all(char.isalpha() for char in string)

def cek_Digit(string): #memeriksa apakah string hanya mengandung angka
    return string.isdigit()

def validasi_Userid(userid): #function memeriksa validitas userid berdasarkan ketentuan
    if not (6 <= len(userid) <= 20): #jika panjang elemen userid tidak masuk range 6-20
        return False 
    if not any(cek_Huruf(char) for char in userid): # jika tidak ada huruf di dalam userid
        return False
    if not any(cek_Digit(char) for char in userid): # jika tidak ada string yang hanya mengandung angka
        return False
    if not cek_Alphanumeric(userid): # jika tidak ada huruf dan angka  di dalam userid
        return False
    if userid in data_user:
        return False
    return True

def validasi_Password(password):
    special_char = "/.,@#$%"
    if len(password) < 8:
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in special_char for char in password):
        return False
    return True

def validasi_Email(email):
    parts = email.split('@')
    
    if len(parts) != 2:
        return "Email Tidak Valid, Format Email Salah (Hanya boleh satu @)"
    
    username, rest = parts
    
    if '.' not in rest:
        return "Email Tidak Valid, Alasan: Format Email Salah (Tidak ada .ekstensi)"
    
    domain, ext = rest.split('.')
    
    if len(ext.split('.')) > 2:
        return "Email Tidak Valid, Alasan: Format Ekstensi yg anda masukkan Salah (Maksimal dot(.) untuk ekstensi 2)"
    
    if len(ext) > 5:
        return "Email Tidak Valid, Alasan: Format Ekstensi yg anda masukkan Salah (Maksimal 5 Karakter)"
    
    if not username.replace('_', '').replace('.', '').isalnum():
        return "Email Tidak Valid, Alasan: Format Username yg anda masukkan salah"
    
    if not username[0].isalnum():
        return "Email Tidak Valid, Alasan: Format Username yg anda masukkan salah"
    
    if not domain.isalnum():
        return "Email Tidak Valid, Alasan: Format Hosting yg anda masukkan Salah"
    
    if any(char in "!\"#$%&'()*+,/:;<=>?@[\\]^`{|}~" for char in email):
        return "Email Tidak Valid, Alasan: Format Email Salah (Simbol Karakter Khusus Tidak bisa diterima)"
    
    valid_extensions = ["com", "net", "org", "id", "my", "sg"]
    if ext not in valid_extensions:
        return "Email Tidak Valid, Alasan: Format Ekstensi yg anda masukkan Salah"
    
    return email, "Alamat Email yg anda Masukkan Valid"

def validasi_Gender(gender):
    return gender.lower() in ["male", "female", "pria", "wanita"]

def validasi_Umur(umur):
    if cek_Digit(umur):
        umur = int(umur)
        if 17 <= umur <= 80:
            return True
    return False

def validasi_Kodepos(kodepos):
    return cek_Digit(kodepos) and len(kodepos) == 5

def validasi_Nomerhp(nomerhp):
    return cek_Digit(nomerhp) and 11 <= len(nomerhp) <= 13

def register():
    while True:
        print("----------- Register -------")
        userid = input("Masukkan UserId: ")
        if not validasi_Userid(userid):
            print("UserId tidak valid atau sudah ada. Harus Kombinasi Huruf dan Angka, tidak boleh ada karakter lain, dan panjang 6-20 karakter.")
            continue

        password = input("Masukkan Password: ")
        if not validasi_Password(password):
            print("Password tidak valid. Harus Kombinasi Huruf Kapital, Huruf Kecil, Angka dan Karakter Khusus (/.,@#$%), minimal 8 karakter.")
            continue

        email = input("Masukkan Email: ")
        if not validasi_Email(email):
            print("Email tidak valid.")
            continue

        nama = input("Masukkan Nama: ")
        if not cek_Huruf(nama):
            print("Nama hanya boleh mengandung huruf alfabet.")
            continue

        gender = input("Masukkan Gender (Male/Female atau Pria/Wanita): ")
        if not validasi_Gender(gender):
            print("Gender tidak valid. Harus 'Male' atau 'Female', 'Pria' atau 'Wanita'.")
            continue

        umur = input("Masukkan Usia: ")
        if not validasi_Umur(umur):
            print("Usia tidak valid. Harus Integer antara 17 dan 80 tahun.")
            continue

        pekerjaan = input("Masukkan Pekerjaan: ")
        if not cek_Huruf(pekerjaan):
            print("Pekerjaan hanya boleh mengandung huruf alfabet.")
            continue

        hobbies = input("Masukkan Hobi (pisahkan dengan koma jika lebih dari satu): ").split(",")
        if not all(cek_Huruf(hobi.strip()) for hobi in hobbies):
            print("Hobi hanya boleh mengandung huruf alfabet dan lebih dari satu.")
            continue

        kota = input("Masukkan Nama Kota: ")
        if not cek_Huruf(kota):
            print("Nama Kota hanya boleh mengandung huruf alfabet.")
            continue

        rt = input("Masukkan RT: ")
        if not cek_Digit(rt):
            print("RT harus berupa angka.")
            continue

        rw = input("Masukkan RW: ")
        if not cek_Digit(rw):
            print("RW harus berupa angka.")
            continue

        kodepos = input("Masukkan Zip Code: ")
        if not validasi_Kodepos(kodepos):
            print("Zip Code tidak valid. Harus berupa angka dan terdiri dari 5 digit.")
            continue

        lat = input("Masukkan Latitude: ")
        try:
            lat = float(lat)
        except ValueError:
            print("Latitude harus berupa angka desimal.")
            continue

        lon = input("Masukkan Longitude: ")
        try:
            lon = float(lon)
        except ValueError:
            print("Longitude harus berupa angka desimal.")
            continue

        nomerhp = input("Masukkan No HP: ")
        if not validasi_Nomerhp(nomerhp):
            print("No HP tidak valid. Harus berupa angka dan panjangnya antara 11 hingga 13 karakter.")
            continue

        print("Simpan Data (Y/N):")
        save = input().lower()
        if save == 'y':
            data_user[userid] = {
                'password': password,
                'email': email,
                'nama': nama,
                'gender': gender,
                'umur': int(umur),
                'pekerjaan': pekerjaan,
                'hobbies': hobbies,
                'alamat': {
                    'kota': kota,
                    'rt': rt,
                    'rw': rw,
                    'kodepos': kodepos,
                    'geo': {
                        'lat': lat,
                        'lon': lon
                    }
                },
                'nomerhp': int(nomerhp)
            }
            print("Data tersimpan.")
        else:
            print("Data tidak tersimpan.")
        
        break

def show_profile(user_data):
    print("Data Anda")
    print(f"Nama      : {user_data['nama']}")
    print(f"Email     : {user_data['email']}")
    print(f"Gender    : {user_data['gender']}")
    print(f"Umur      : {user_data['umur']}")
    print(f"Pekerjaan : {user_data['pekerjaan']}")
    print(f"Hobi      : {user_data['hobbies']}")
    print(f"Alamat       :")
    print(f"Nama Kota : {user_data['alamat']['kota']}")
    print(f"RT        : {user_data['alamat']['rt']}")
    print(f"RW        : {user_data['alamat']['rw']}")
    print(f"Kode Pos  : {user_data['alamat']['kodepos']}")
    print(f"Geo       :")
    print(f"  Lat      : {user_data['alamat']['geo']['lat']}")
    print(f"  Longitude: {user_data['alamat']['geo']['lon']}")
    print(f"No Hp     : {user_data['nomerhp']}")   
    print("Anda Berhasil Login")


def login():
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        print("----------- Login -----------")
        id_login = input("Masukkan ID: ")
        password_login = input("Masukkan Password: ")  

        if id_login in data_user or password_login in data_user:
            if id_login in data_user:
                if data_user[id_login]['password']==password_login:
                    show_profile(data_user[id_login])
                    return True
                else:
                    print("Password Salah")              
            else:
                print("ID Tidak Terdaftar ")
        else:
            print('ID & Password Salah')

        attempts += 1
        if attempts < max_attempts:
            print(f"Gagal melakukan login. Kesempatan tersisa: {max_attempts - attempts}")
        else:
            print("Gagal melakukan login 5 kali. Kembali ke menu utama.")

        print("Anda telah mencapai batas maksimal percobaan login.")


def main():
    while True:
        print("\n--- Selamat datang di Tim 5 Apps ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Masukkan pilihan: ")

        if choice == '1':
            register()
        elif choice == '2':
            if login():
                break
        elif choice == '3':
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

#Tes input error 
'''
userid = arasy67
password = arasy67 ==> error karena, Password tidak valid. Harus Kombinasi Huruf Kapital, Huruf Kecil, Angka dan Karakter Khusus (/.,@#$%), minimal 8 karakter.
=========
userid = arasy67
password = Ar@sy6789O
email = arasy21@gmail.com
nama = Arasy
gender = pria 
umur = 22
pekerjaan = mahasiswa
hobbies = bengong
alamat = jl. in dulu aja 01
kota = Bandung
rt = 001
rw = 001
kodepos = 40294
geo:
    lat = -6.19312
    lon = 106.821810
nomerhp = 08123456789
'''