# Walme Automation Script

## Overview

This script automates the process of interacting with the Walme API to fetch and complete tasks using provided tokens and proxies. It includes several features such as:
- Displaying a colorful banner animation.
- Reading tokens and proxies from files.
- Generating random headers with fake user agents.
- Fetching profile data and tasks from the Walme API.
- Completing tasks and displaying profile information.
- Handling proxies and writing used proxies to a file.
- Looping the process every 24 hours and 77 minutes.

## Features

1. **Rainbow Banner**: Displays a colorful banner animation at the start.
2. **Token and Proxy Management**: Reads tokens and proxies from `token.txt` and `proxy.txt`.
3. **Random Headers**: Generates random headers using fake user agents.
4. **Profile Data**: Fetches and displays profile data from the Walme API.
5. **Task Management**: Fetches and completes tasks from the Walme API.
6. **Proxy Handling**: Uses proxies for API requests and writes used proxies to `used_proxy.txt`.
7. **Looping**: Loops the process every 24 hours and 77 minutes.

## Requirements

- Python 3.x
- Modules listed in `requirements.txt`

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/0xsya/walme.git
   cd walme
   ```

2. Install the required modules:
   ```sh
   pip install -r requirements.txt
   ```

3. Create `token.txt` and `proxy.txt` files in the same directory as the script. Add your tokens and proxies (one per line) to these files.

## Usage

To run the script, use the following commands based on your operating system:

- **Linux/Mac**:
  ```sh
  python3 main.py
  ```

- **Windows**:
  ```sh
  python main.py
  ```

## Risks and Considerations

1. **API Rate Limits**: Be aware of API rate limits to avoid being blocked.
2. **Proxy Reliability**: Ensure your proxies are reliable to avoid connectivity issues.
3. **Data Privacy**: Handle your tokens and profile data securely to prevent unauthorized access.
4. **Script Accuracy**: Verify the accuracy and completeness of the tasks and profile data fetched by the script.

## License

This project is licensed under the MIT License.

---

# Skrip Otomatisasi Walme

## Ikhtisar

Skrip ini mengotomatisasi proses berinteraksi dengan API Walme untuk mengambil dan menyelesaikan tugas menggunakan token dan proxy yang disediakan. Ini mencakup beberapa fitur seperti:
- Menampilkan animasi banner berwarna.
- Membaca token dan proxy dari file.
- Menghasilkan header acak dengan agen pengguna palsu.
- Mengambil data profil dan tugas dari API Walme.
- Menyelesaikan tugas dan menampilkan informasi profil.
- Menangani proxy dan menulis proxy yang digunakan ke file.
- Melakukan proses looping setiap 24 jam dan 77 menit.

## Fitur

1. **Banner Pelangi**: Menampilkan animasi banner berwarna di awal.
2. **Manajemen Token dan Proxy**: Membaca token dan proxy dari `token.txt` dan `proxy.txt`.
3. **Header Acak**: Menghasilkan header acak menggunakan agen pengguna palsu.
4. **Data Profil**: Mengambil dan menampilkan data profil dari API Walme.
5. **Manajemen Tugas**: Mengambil dan menyelesaikan tugas dari API Walme.
6. **Penanganan Proxy**: Menggunakan proxy untuk permintaan API dan menulis proxy yang digunakan ke `used_proxy.txt`.
7. **Looping**: Melakukan proses looping setiap 24 jam dan 77 menit.

## Persyaratan

- Python 3.x
- Modul yang tercantum di `requirements.txt`

## Persiapan

1. Clone repositori:
   ```sh
   git clone https://github.com/0xsya/walme.git
   cd walme
   ```

2. Instal modul yang diperlukan:
   ```sh
   pip install -r requirements.txt
   ```

3. Buat file `token.txt` dan `proxy.txt` di direktori yang sama dengan skrip. Tambahkan token dan proxy Anda (satu per baris) ke file-file ini.

## Penggunaan

Untuk menjalankan skrip, gunakan perintah berikut berdasarkan sistem operasi Anda:

- **Linux/Mac**:
  ```sh
  python3 main.py
  ```

- **Windows**:
  ```sh
  python main.py
  ```

## Risiko dan Pertimbangan

1. **Batasan API**: Waspadai batasan API untuk menghindari pemblokiran.
2. **Keandalan Proxy**: Pastikan proxy Anda dapat diandalkan untuk menghindari masalah konektivitas.
3. **Privasi Data**: Tangani token dan data profil Anda dengan aman untuk mencegah akses yang tidak sah.
4. **Akurasi Skrip**: Verifikasi akurasi dan kelengkapan tugas dan data profil yang diambil oleh skrip.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT.
