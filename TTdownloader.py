import re
import requests
from bs4 import BeautifulSoup

def download_tiktok(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    print("[+] Mengambil data dari TikTok...")
    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        print("Gagal mengambil halaman TikTok.")
        return

    soup = BeautifulSoup(r.text, "html.parser")

    pattern = r'https://.*?\.tiktokcdn\.com/.*?'
    matches = re.findall(pattern, str(soup))

    if not matches:
        print("Tidak ditemukan link video.")
        return

    video_url = matches[0]
    print("[+] Link Video:", video_url)

    print("[+] Mengunduh video...")
    video = requests.get(video_url, headers=headers)

    filename = "tiktok_no_watermark.mp4"
    with open(filename, "wb") as f:
        f.write(video.content)

    print(f"[✓] Berhasil! Video tersimpan: {filename}")

if __name__ == "__main__":
    link = input("Masukkan link TikTok: ")
    download_tiktok(link)
