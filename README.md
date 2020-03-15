# Uncle Crypto Library

สวัสดีจร้าาาา นี่ลุงวิศวกรเอง ไลบรารี่นี้ใช้สำหรับการดึงราคา Crypto Currency


  - ดึงจากเว็บ https://coinmarketcap.com 
  - ดึงตามช่วงเวลาได้
  - ดึงตามวันที่ต้องการได้


### วิธีติดตั้งแสนง่าย

ไปกดไลค์เพจลุงก่อนเลย เสริมเกราะป้องกัน 555 [ลุงวิศวกร สอนคำนวณ](https://www.facebook.com/UncleEngineer)  ฮ่าาา ไม่บังคับ (กดไลค์เพจลุงหน่อยๆ 555)

เราจะติดตั้งผ่านเจ้า pip

```sh
pip install unclecrypto
```

ง่ายไหมล่ะ

วิธีใช้ก็ง่ายมาก
- เปิด Python แล้วพิพม์ตามนี้เลย

```sh
from unclecrypto import rangeprice, dayprice

LISTPRICE,DICTPRICE = rangeprice('bitcoin',start='20200105',end='20200131')
print(LISTPRICE) # ['Feb 01 2020', 9346.36, 9439.32, 9313.24, 9392.88, 25922656496, 170900662180]
print(DICTPRICE['Jan 31 2020'])

# Historical Data Day Range
L,D = rangeprice('xrp',start='20200105',end='20200131')
print(L)
print(D)

# Historical Data Day
L,D = dayprice('bitcoin','20200131')
print(L)
print(D)
print(D['date'],D['open'],D['high'],D['low'],D['close'],D['volume'],D['marketcap'])

```

### Visit

แวะเข้าไปเยี่ยมชมกันได้ แหล่งกบดานเรามีสอนหลายวิชา

| เนื้อหา | ลิ้งค์ |
| ------ | ------ |
| ลุงมีวิชาอะไรบ้าง |http://uncle-engineer.com/ |
| อ่านบทความใน Medium  | https://medium.com/@UncleEngineer |
| เพจ "ลุงวิศวกร สอนคำนวณ"  | https://www.facebook.com/UncleEngineer |
| ------ | ------ |

### ติดตามตอนต่อไป...ในเพจ "ลุงวิศวกร สอนคำนวณ"
