# Assesement Program Magang Bersertifikat Kampus Merdeka - Studycle

## Abstrak

- Program ini menggunakan `sys.argv` sebagai metoda penerimaan input
- Input dan output dari program ini dapat ditinjau langsung dengan Terminal
- Bahasa pemograman yang digunakan adalah Python

## Cara penggunaan

- Pastikan Python versi 3.+ telah diinstal
- Pastikan Program Git telah diinstal
- Buka Terminal PC
- Arahkan directory ke tempat yang diinginkan untuk menyimpan repository ini
- Jalankan command dibawah ini:
  ```
  $ git clone https://github.com/rrahardiparta/assesement_of_studycle.git
  ```
- Arahkan dirctorynya kembali ke dalam `assesement_of_studycle`
- Jalankan program dengan perintah berikut:
  ```
  $ python main.py [Values]
  ```
  | Argumen  | Deskripsi                                           |
  | -------- | --------------------------------------------------- |
  | [Values] | Deretan angka untuk diproses dengan separator spasi |

## Contoh Penggunaan

- Pada bagian Input:

  ```
  $ python main.py 3 7 2 1 8
  ```

- Pada bagian Output

  ```
        data input:  3 7 2 1 8
        data pengurutan:  1 2 3 7 8
        rata-rata data:  4.2
        nilai tengah data:  3
        hasil kali keseluruhan data:  336

  ```

## Limitasi Program

- Program ini hanya dapat digunakan one-time-use sehingga untuk data input berikutnya harus dijalankan kembali melalui terminal
- Jika terjadi kegagalan pada saat menjalankan program, program tidak dapat mengulang ke posisi sebelum terjadi kegagalan secara otomatis
