# -*- coding: utf-8 -*-
"""
assemble_all_exams.py
Assembles all 10 exams (400 questions), audits balance and correctness,
and writes the clean examData.js.
"""

import json
from exams_part1 import e1, e2
from exams_part2 import e3, e4
from exams_part3 import e5, e6
from exams_part4 import e7, e8
from exams_part5 import e9, e10

all_exams_data = [
    {
        "id": 1,
        "title": "Sınav 1 – SQL Temelleri, Sorgu Mantığı & Operatörler",
        "desc": "DQL/DML/DDL ayrımları, WHERE, LIKE, NULL mantığı, GROUP BY/HAVING ve Küme İşlemleri",
        "topics": ["SQL", "DQL/DML/DDL", "WHERE & LIKE", "NULL Mantığı", "GROUP BY & HAVING", "UNION & EXCEPT"],
        "questions": e1
    },
    {
        "id": 2,
        "title": "Sınav 2 – Çok Tablolu Sorgular, JOIN & İlişkisel Cebir",
        "desc": "INNER/LEFT/RIGHT/FULL/CROSS JOIN, Alt Sorgular (Subqueries), ANY/ALL/EXISTS ve Cebirsel İşlemler (σ, π, ⋈, −)",
        "topics": ["JOIN Türleri", "Alt Sorgular", "ANY & ALL", "EXISTS / NOT EXISTS", "İlişkisel Cebir (σ, π, ⋈)"],
        "questions": e2
    },
    {
        "id": 3,
        "title": "Sınav 3 – DDL, Tablo Tasarımı, Kısıtlamalar & Bütünlük",
        "desc": "CREATE/ALTER/DROP, PK, FK (CASCADE/SET NULL/NO ACTION), CHECK, UNIQUE, DEFAULT, İndeksler ve Transaction (ACID)",
        "topics": ["DDL Komutları", "Kısıtlamalar (Constraints)", "Bütünlük Kuralları", "İndeksler (Clustered/Non-Clustered)", "Transaction (ACID)"],
        "questions": e3
    },
    {
        "id": 4,
        "title": "Sınav 4 – T-SQL Programlama, Değişkenler & Akış Kontrolü",
        "desc": "DECLARE, SET vs SELECT, Birleşik Operatörler, @@Global Değişkenler, IF-ELSE, CASE, WHILE (BREAK/CONTINUE)",
        "topics": ["T-SQL Temelleri", "Değişkenler & Atama", "Global Değişkenler", "IF-ELSE & CASE", "WHILE Döngüsü"],
        "questions": e4
    },
    {
        "id": 5,
        "title": "Sınav 5 – Saklı Yordamlar (Stored Procedures) & Fonksiyonlar (UDF)",
        "desc": "CREATE PROC, Parametreler, DEFAULT Değerler, OUTPUT, VIEW vs FUNCTION vs PROCEDURE, Skaler & Tablo Değerli UDF",
        "topics": ["Stored Procedure", "Parametreler & OUTPUT", "Kullanıcı Fonksiyonları (UDF)", "VIEW vs PROC vs FUNCTION", "Dinamik SQL"],
        "questions": e5
    },
    {
        "id": 6,
        "title": "Sınav 6 – Tetikleyiciler (Trigger) & Olay Tabanlı Yönetim",
        "desc": "AFTER (FOR) vs INSTEAD OF Trigger, INSERTED & DELETED Sözde Tabloları, ROLLBACK, Nested & Recursive Trigger",
        "topics": ["Trigger Temelleri", "AFTER vs INSTEAD OF", "INSERTED & DELETED", "İş Kuralı & Denetim", "Trigger Yönetimi"],
        "questions": e6
    },
    {
        "id": 7,
        "title": "Sınav 7 – İmleçler (Cursor) & Satır Satır Veri İşleme",
        "desc": "Cursor'ın 5 Adımı (DECLARE/OPEN/FETCH/CLOSE/DEALLOCATE), @@FETCH_STATUS, SCROLL Hareketleri, WHERE CURRENT OF",
        "topics": ["Cursor Yaşam Döngüsü", "FETCH & @@FETCH_STATUS", "SCROLL Cursor", "WHERE CURRENT OF", "Cursor Optimizasyonu"],
        "questions": e7
    },
    {
        "id": 8,
        "title": "Sınav 8 – Normalizasyon, Fonksiyonel Bağımlılık & ER Modelleme",
        "desc": "1NF, 2NF, 3NF, BCNF, Kısmi vs Geçişli Bağımlılık, Anomaliler, Kayıpsız Ayrıştırma, ER Varlık & İlişki Tipleri",
        "topics": ["Normalizasyon (1NF-3NF)", "BCNF & Bağımlılıklar", "Veritabanı Anomalileri", "ER Modelleme", "Zayıf Varlık & İlişkiler"],
        "questions": e8
    },
    {
        "id": 9,
        "title": "Sınav 9 – Oracle PL/SQL Mimarisi, Paketler & İleri Konular",
        "desc": "PL/SQL Blokları, %TYPE / %ROWTYPE, SELECT INTO, İstisnalar (Exceptions), Paketler (Spec/Body), Koleksiyonlar (VARRAY)",
        "topics": ["PL/SQL Blok Mimarisi", "%TYPE & %ROWTYPE", "İstisna Yönetimi", "Paketler (Package)", "Kayıtlar & Koleksiyonlar"],
        "questions": e9
    },
    {
        "id": 10,
        "title": "Sınav 10 – Kapsamlı Final Simülasyonu & Çıkmış Sorular",
        "desc": "Hocanın 15 örnek sorusu, üniversite çıkmış final soruları, kod çıktı tahminleri ve çok adımlı vaka analizleri",
        "topics": ["Çıkmış Sınav Soruları", "Kod Çıktı Analizi", "Vaka Senaryoları", "Genel Final Tekrarı", "İleri SQL"],
        "questions": e10
    }
]

# Audit total count
total_q = sum(len(e["questions"]) for e in all_exams_data)
print(f"Toplam Sınav: {len(all_exams_data)}, Toplam Soru: {total_q}")

# Audit option length balance and answer distribution
dist = [0, 0, 0, 0, 0]
longest_count = 0
correct_lens = []
wrong_lens = []

for e in all_exams_data:
    assert len(e["questions"]) == 40, f"Sinav {e['id']} 40 soru olmali, {len(e['questions'])} bulundu!"
    for q in e["questions"]:
        dist[q["a"]] += 1
        c_len = len(q["o"][q["a"]])
        w_lens = [len(opt) for i, opt in enumerate(q["o"]) if i != q["a"]]
        correct_lens.append(c_len)
        wrong_lens.extend(w_lens)
        if c_len >= max(w_lens):
            longest_count += 1

print("\n--- CEVAP DAĞILIMI ---")
labels = ['A', 'B', 'C', 'D', 'E']
for i in range(5):
    print(f"{labels[i]}: {dist[i]} (%{round(dist[i]/total_q*100)})")

print("\n--- ŞIK UZUNLUK ANALİZİ ---")
avg_c = round(sum(correct_lens) / len(correct_lens))
avg_w = round(sum(wrong_lens) / len(wrong_lens))
print(f"Ortalama Doğru Şık Uzunluğu: {avg_c} karakter")
print(f"Ortalama Yanlış Şık Uzunluğu: {avg_w} karakter")
print(f"Doğru Cevabın En Uzun Şık Olduğu Soru Oranı: {longest_count}/{total_q} (%{round(longest_count/total_q*100)})")

# Generate clean examData.js
def escape_js(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

output = "// =============================================\n"
output += "// VTYS 10 SINAV × 40 SORU = 400 TEST SORUSU\n"
output += "// Ders slaytları, deney föyü ve çıkmış sınavlardan derlenmiştir.\n"
output += "// =============================================\n\n"
output += "const EXAMS = [\n"

for ei, exam in enumerate(all_exams_data):
    output += f"// ==================== SINAV {exam['id']} ====================\n"
    output += "{\n"
    output += f'id:{exam["id"]}, title:"{escape_js(exam["title"])}", desc:"{escape_js(exam["desc"])}",\n'
    output += f'topics:{json.dumps(exam["topics"], ensure_ascii=False)},\n'
    output += "questions:[\n"
    
    for qi, q in enumerate(exam["questions"]):
        opts_str = ",".join([f'"{escape_js(opt)}"' for opt in q["o"]])
        output += f'{{q:"{escape_js(q["q"])}",o:[{opts_str}],a:{q["a"]},e:"{escape_js(q["e"])}"}}'
        if qi < len(exam["questions"]) - 1:
            output += ","
        output += "\n"
        
    output += "]}"
    if ei < len(all_exams_data) - 1:
        output += ","
    output += "\n\n"

output += "];\n"

with open("examData.js", "w", encoding="utf-8") as f:
    f.write(output)

print("\nexamData.js başarıyla yazıldı!")
