import yt_dlp
# รับ URL จากผู้ใช้
url = input("กรุณาใส่ลิงก์ YouTube: ")
# ตั้งค่าการดาวน์โหลด
ydl_opts = {
    'format': 'best',  # ดาวน์โหลดคุณภาพดีที่สุด
    'outtmpl': '%(title)s.%(ext)s'  # ตั้งชื่อไฟล์ตามชื่อคลิป
}
# เริ่มดาวน์โหลด
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
print("ดาวน์โหลดเสร็จเรียบร้อย ✅")
