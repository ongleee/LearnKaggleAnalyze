# LearnKaggleAnalyze

repo นี้เอาไว้หัดวิเคราะห์ข้อมูล (Data Analysis) ด้วย Python + pandas
มี 2 โปรเจกต์เล็กๆ คือ Titanic กับ Netflix อ่านโค้ดตามได้ง่ายๆ

## มีอะไรในนี้บ้าง

```
LearnKaggleAnalyze/
├── Titanic.py           # วิเคราะห์ข้อมูลผู้โดยสาร Titanic
├── train.csv            # ข้อมูล train ของ Titanic (891 แถว)
├── test.csv             # ข้อมูล test ของ Titanic (418 แถว)
├── gender_submission.csv# ไฟล์ตัวอย่าง submission ของ Kaggle
├── netflix_analysis.py  # วิเคราะห์ข้อมูล Netflix
├── netflix_titles.csv   # ข้อมูล Netflix (8807 รายการ)
└── netflix.txt          # สรุปผลวิเคราะห์ Netflix
```

## 1. Titanic Analysis

ไฟล์: `Titanic.py`

ดูว่าใครมีโอกาสรอดชีวิตมากกว่ากัน จากเพศ (`Sex`) และชั้นโดยสาร (`Pclass`)

สิ่งที่ทำในโค้ด:
- เช็กค่าว่างด้วย `isnull().sum()`
- เติมค่า `Age` ที่หายไปด้วยค่ามัธยฐาน (median)
- ดู % การรอดชีวิตโดยรวม / แยกตามเพศ / แยกตามชั้นโดยสาร
- พล็อตกราฟแท่ง 2 กราฟด้วย matplotlib

รันแบบนี้:

```bash
pip install pandas numpy matplotlib
python Titanic.py
```

> หมายเหตุ: ใน `Titanic.py` ตอนนี้ path ของ csv เป็น `C:\Projects\LearnKaggleTitanic\train.csv` ถ้ารันแล้วหาไฟล์ไม่เจอ ให้แก้เป็น `train.csv` เฉยๆ ก็พอ

## 2. Netflix Analysis

ไฟล์: `netflix_analysis.py` + สรุปผลใน `netflix.txt`

วิเคราะห์ว่ามีหนัง / ซีรีส์อะไรบ้างใน Netflix

สิ่งที่ทำในโค้ด:
- เช็กค่าว่าง + ลบแถวซ้ำ
- แปลง `date_added` เป็นวันที่ แล้วดึงปีออกมาเป็น `year_added`
- นับ Movie vs TV Show
- หา 10 ประเทศที่มีคอนเทนต์เยอะสุด
- ดูแนวโน้มจำนวนเรื่องที่เพิ่มเข้ามาแต่ละปี
- ดูการกระจายความยาวหนัง (นาที)
- ดูเรตติ้งที่เจอบ่อยสุด (เช่น TV-MA, TV-14)

รันแบบนี้:

```bash
pip install pandas matplotlib seaborn
python netflix_analysis.py
```

ผลที่เจอ (ดูฉบับเต็มใน `netflix.txt`):
- Movie เยอะกว่า TV Show: 6131 vs 2676
- ประเทศที่เจอบ่อยสุด: United States (3689 ครั้ง)
- ปีที่เพิ่มคอนเทนต์เยอะสุด: 2019 (2016 รายการ)
- ความยาวหนังมัธยฐาน: 98 นาที
- เรตติ้งที่เจอบ่อยสุด: TV-MA (3207 รายการ)

## ข้อมูลมาจากไหน

- Titanic: โจทย์ Titanic - Machine Learning from Disaster ใน Kaggle
- Netflix: ไฟล์ `netflix_titles.csv` (columns: show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description)

## มือใหม่เริ่มตรงไหน

1. ติดตั้ง Python 3 แล้วรัน `pip install pandas numpy matplotlib seaborn`
2. ลองรัน `python Titanic.py` ก่อน เพราะไฟล์สั้นสุด (40 กว่าบรรทัด)
3. แล้วค่อยไป `python netflix_analysis.py`
