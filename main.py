import os
import requests
import time
from colorama import Fore, Style, init
from fake_useragent import UserAgent

# Inisialisasi colorama
init(autoreset=True)

# Fungsi untuk menampilkan banner animasi berwarna
def rainbow_banner():
    os.system("clear" if os.name == "posix" else "cls")
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    banner = """
  _______                          
 |     __|.--.--.---.-.-----.---.-.
 |__     ||  |  |  _  |-- __|  _  |
 |_______||___  |___._|_____|___._|
          |_____|                   
    """

    for i, char in enumerate(banner):
        print(colors[i % len(colors)] + char, end="")
        time.sleep(0.007)
    print(Fore.LIGHTYELLOW_EX + "\nPlease wait...\n")
    time.sleep(2)
    os.system("clear" if os.name == "posix" else "cls")
    for i, char in enumerate(banner):
        print(colors[i % len(colors)] + char, end="")
    print(Fore.LIGHTYELLOW_EX + "\n")

# Fungsi untuk membaca token dari file
def read_tokens(file_path):
    if not os.path.exists(file_path):
        print(Fore.RED + "File token.txt not found!")
        return []

    with open(file_path, 'r') as file:
        tokens = file.read().splitlines()

    return tokens

# Fungsi untuk membuat header acak
def generate_random_headers(token=None):
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Accept': 'application/json',
        'Accept-Language': 'id-ID,id;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': 'https://waitlist.walme.io/',
        'Origin': 'https://waitlist.walme.io',
        'Sec-Ch-Ua': '"Not(A:Brand";v="99", "Brave";v="133", "Chromium";v="133"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Gpc': '1',
        'Priority': 'u=1, i'
    }
    if token:
        headers['Authorization'] = f'Bearer {token}'
    return headers

# Fungsi untuk mengambil data profil
def fetch_profile(token, headers):
    url = "https://api.walme.io/user/profile"
    headers['Authorization'] = f'Bearer {token}'

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            print(Fore.GREEN + "✔ Successfully fetched profile data!")
            return response.json()
        else:
            print(Fore.RED + f"❌ Failed to fetch profile data. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"❌ Error fetching profile data: {e}")
        return None

# Fungsi untuk menampilkan data profil dalam format yang diinginkan
def display_profile(profile_data):
    print(Fore.GREEN + f"✔ Name: {profile_data.get('name')}")
    print(Fore.GREEN + f"✔ Username: {profile_data.get('display_name')}")
    print(Fore.GREEN + f"✔ Email: {profile_data.get('email')}")
    print(Fore.GREEN + f"✔ Matrix User: {profile_data.get('matrix_user')}")
    print(Fore.GREEN + f"✔ Referral Code: {profile_data.get('referral_code')}")
    print(Fore.GREEN + f"✔ Total XP: {profile_data.get('reward')}")
    print(Fore.GREEN + f"✔ Referral Reward: {profile_data.get('reward_ref')}")
    print(Fore.GREEN + f"✔ Total Referral: {profile_data.get('total_ref')}")

    # Extract Telegram, Discord, and Twitter from identities
    identities = profile_data.get('identities', [])
    telegram = next((identity.get('auth_name') for identity in identities if identity.get('auth_provider') == 'telegram'), 'N/A')
    discord = next((identity.get('auth_name') for identity in identities if identity.get('auth_provider') == 'discord'), 'N/A')
    twitter = next((identity.get('auth_name') for identity in identities if identity.get('auth_provider') == 'twitter'), 'N/A')

    print(Fore.GREEN + f"✔ Telegram: {telegram}")
    print(Fore.GREEN + f"✔ Discord: {discord}")
    print(Fore.GREEN + f"✔ Twitter: {twitter}")
    print(Fore.GREEN + f"✔ Last Login: {profile_data.get('last_login')}")
    print(Fore.GREEN + f"✔ Created: {profile_data.get('created_at')}")

# Fungsi untuk mengambil semua task (termasuk nested tasks)
def fetch_all_tasks(token, headers):
    url = "https://api.walme.io/waitlist/tasks"
    headers['Authorization'] = f'Bearer {token}'

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            print(Fore.GREEN + "✔ Successfully fetched tasks!")
            return response.json()
        else:
            print(Fore.RED + f"❌ Failed to fetch tasks. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"❌ Error fetching tasks: {e}")
        return None

# Fungsi rekursif untuk mengekstrak semua task (termasuk child tasks)
def extract_all_tasks(tasks):
    all_tasks = []
    for task in tasks:
        # Tambahkan task saat ini ke daftar
        all_tasks.append(task)
        # Jika task memiliki child, ekstrak child tasks secara rekursif
        if 'child' in task and task['child']:
            all_tasks.extend(extract_all_tasks(task['child']))
    return all_tasks

# Fungsi untuk menyelesaikan task
def complete_task(task_id, token, headers):
    url = f"https://api.walme.io/waitlist/tasks/{task_id}"
    headers['Authorization'] = f'Bearer {token}'

    # Data yang dikirim (kosong karena hanya PATCH)
    data = {}

    try:
        response = requests.patch(url, headers=headers, json=data, timeout=10)

        if response.status_code == 200:
            print(Fore.GREEN + f"✅ Successfully completed task {task_id}!")
            return response.json()
        else:
            print(Fore.RED + f"❌ Failed to complete task {task_id}. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"❌ Error completing task: {e}")
        return None

# Fungsi untuk menampilkan waktu mundur
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        timer = f"{hours:02d}:{mins:02d}:{secs:02d}"
        print(Fore.YELLOW + f"⏳ Waiting for the next loop: {timer}", end="\r")
        time.sleep(1)
        seconds -= 1
    print()

# Fungsi utama
def main():
    # Tampilkan banner animasi berwarna
    rainbow_banner()

    tokens = read_tokens('token.txt')

    if not tokens:
        return

    # Simpan header untuk setiap akun
    account_headers = {}

    # Looping setiap 10 jam
    loop_duration = 10 * 3600  # 10 jam dalam detik

    while True:
        for idx, token in enumerate(tokens):
            print(Fore.CYAN + f"🔍 Processing account {idx + 1}...")

            # Buat header untuk akun ini jika belum ada
            if token not in account_headers:
                account_headers[token] = generate_random_headers(token)

            headers = account_headers[token]

            # Mengambil data profil
            profile_data = fetch_profile(token, headers)

            if profile_data:
                display_profile(profile_data)

                # Mengambil semua task
                tasks = fetch_all_tasks(token, headers)

                if tasks:
                    # Ekstrak semua task (termasuk nested tasks)
                    all_tasks = extract_all_tasks(tasks)

                    # Cek dan selesaikan task "7-DAY Challenge: Boost Your XP"
                    for task in all_tasks:
                        if task.get('title') == "7-DAY Challenge: Boost Your XP" and task.get('status') in ['new', 'started']:
                            task_id = task.get('id')
                            print(Fore.CYAN + f"🔄 Found and processing task: 7-DAY Challenge: Boost Your XP (ID: {task_id})")
                            task_response = complete_task(task_id, token, headers)

                            if task_response:
                                print(Fore.BLUE + "📝 Task Response:")
                                print(f"Task ID: {task_response.get('id')}")
                                print(f"Title: {task_response.get('title')}")
                                print(f"Status: {task_response.get('status')}")
                                print(f"Reward: {task_response.get('reward')} XP")
                                print(f"Started At: {task_response.get('started_at')}")
                                print(f"Completed At: {task_response.get('completed_at')}")

                            # Delay 30 detik setelah setiap task selesai
                            print(Fore.YELLOW + "⏳ Waiting for 30 seconds before processing the next task...")
                            time.sleep(30)
                            break  # Keluar dari loop setelah menyelesaikan task
                        elif task.get('title') == "7-DAY Challenge: Boost Your XP":
                            print(Fore.YELLOW + "⏭️ 7-DAY Challenge: Boost Your XP already completed or not available.")

                    # Filter task yang belum selesai (status: new atau started), KECUALI "7-DAY Challenge: Boost Your XP"
                    incomplete_tasks = [task for task in all_tasks
                                          if task.get('title') != "7-DAY Challenge: Boost Your XP" and task.get('status') in ['new', 'started']]

                    # Menyelesaikan task yang belum selesai
                    for task in incomplete_tasks:
                        task_id = task.get('id')
                        task_title = task.get('title')
                        task_status = task.get('status')

                        print(Fore.CYAN + f"🔄 Processing task: {task_title} (ID: {task_id}, Status: {task_status})")

                        if task_status in ['new', 'started']:
                            task_response = complete_task(task_id, token, headers)

                            if task_response:
                                print(Fore.BLUE + "📝 Task Response:")
                                print(f"Task ID: {task_response.get('id')}")
                                print(f"Title: {task_response.get('title')}")
                                print(f"Status: {task_response.get('status')}")
                                print(f"Reward: {task_response.get('reward')} XP")
                                print(f"Started At: {task_response.get('started_at')}")
                                print(f"Completed At: {task_response.get('completed_at')}")

                            # Delay 30 detik setelah setiap task selesai
                            print(Fore.YELLOW + "⏳ Waiting for 30 seconds before processing the next task...")
                            time.sleep(30)
                        else:
                            print(Fore.YELLOW + "⏭️ Task already completed. Skipping...")
                else:
                    print(Fore.RED + "❌ Failed to fetch tasks.")
            else:
                print(Fore.RED + "❌ Failed to fetch profile data.")

            # Pemisah antara akun
            print(Fore.MAGENTA + "━" * 50 + "\n")

        # Hitung mundur untuk loop berikutnya
        countdown_timer(loop_duration)

        # Tampilkan banner animasi berwarna sebelum loop berikutnya
        rainbow_banner()

if __name__ == "__main__":
    main()
