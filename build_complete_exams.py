# -*- coding: utf-8 -*-
"""
build_complete_exams.py
10 Sinav x 40 Soru = 400 Orijinal, Kaynaklarla Birebir Uyumlu Test Sorusu.
Tum sorular ders slaytlari (DBMS_4 - DBMS_14, T-SQL, Trigger, Cursor, SP, PL/SQL, Normalizasyon),
deney foyu (DreamHome & Kutuphane semasi) ve cikmis final sorularindan derlenmistir.
"""

import json
import random

random.seed(2024)

def make_q(question_text, correct_opt, distractors, explanation):
    assert len(distractors) == 4, f"4 distractor gerekli: {question_text[:30]}"
    options = [correct_opt] + distractors
    random.shuffle(options)
    return {
        "q": question_text,
        "o": options,
        "a": options.index(correct_opt),
        "e": explanation
    }

# =========================================================================
# SINAV 1: Genel Tekrar & SQL Temelleri, Sorgu Mantığı, Operatörler
# (Kaynaklar: DBMS_6, veritabanıfinal, deney_foyu)
# =========================================================================
s1 = [
    make_q(
        "SQL komut gruplarından hangisi veritabanındaki verileri sorgulamak için kullanılan <code>SELECT</code> ifadesini kapsayan gruptur?",
        "DQL (Data Query Language)",
        ["DML (Data Manipulation Language)", "DDL (Data Definition Language)", "DCL (Data Control Language)", "TCL (Transaction Control Language)"],
        "SELECT ifadesi veri sorgulama dili olan DQL grubuna aittir; geniş anlamda DML içinde de değerlendirilir."
    ),
    make_q(
        "Aşağıdaki SQL komutlarından hangisi DDL (Veri Tanımlama Dili) kategorisinde yer alır?",
        "ALTER",
        ["INSERT", "UPDATE", "DELETE", "SELECT"],
        "CREATE, ALTER, DROP, TRUNCATE gibi nesne tanımlama komutları DDL kategorisindedir."
    ),
    make_q(
        "Bir SQL sorgusunun veritabanı motorundaki mantıksal çalışma sırası aşağıdakilerden hangisinde doğru verilmiştir?",
        "FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> DISTINCT -> ORDER BY",
        ["SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY -> DISTINCT", "FROM -> SELECT -> WHERE -> GROUP BY -> HAVING -> DISTINCT -> ORDER BY", "WHERE -> FROM -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> DISTINCT", "FROM -> GROUP BY -> HAVING -> WHERE -> SELECT -> DISTINCT -> ORDER BY"],
        "Mantıksal sırada önce kaynaklar (FROM/JOIN) belirlenir, WHERE ile filtrelenir, gruplanır, HAVING uygulanır, SELECT ile sütunlar seçilir ve en son ORDER BY ile sıralanır."
    ),
    make_q(
        "<code>SELECT</code> listesinde tanımlanan bir sütun takma adının (alias) <code>WHERE</code> yan tümcesinde doğrudan kullanılamamasının sebebi nedir?",
        "FROM ve WHERE aşamalarının mantıksal olarak SELECT aşamasından önce çalışması",
        ["WHERE yan tümcesinde yalnızca sayısal sütunların filtrelenebilmesi", "Takma adların yalnızca ORDER BY yan tümcesinde yasaklanmış olması", "Veritabanının takma adlara bellek ayırmaması ve diskte tutması", "Takma adların yalnızca toplama fonksiyonları için geçerli olması"],
        "WHERE satırları filtrelerken henüz SELECT ifadesi çalışmadığı için SELECT'te verilen takma adlar WHERE bloğunda tanınmaz."
    ),
    make_q(
        "DreamHome şemasında <code>WHERE salary BETWEEN 20000 AND 30000</code> ifadesi ile ilgili hangisi kesinlikle doğrudur?",
        "20000 ve 30000 sınır değerleri sonuç kümesine dahildir.",
        ["20000 dahil, ancak 30000 hariç olarak değerlendirilir.", "Her iki sınır değeri de (20000 ve 30000) sonuçtan hariç tutulur.", "Yalnızca 20000 ile 30000 arasındaki tek sayılar listelenir.", "Sonuç kümesi veritabanının indeksleme tipine göre değişiklik gösterir."],
        "BETWEEN...AND operatörü belirtilen sınır değerlerini (>= ve <=) her iki uçtan da dahil eder."
    ),
    make_q(
        "<code>WHERE position IN ('Manager', 'Supervisor')</code> ifadesinin mantıksal eşdeğeri hangisidir?",
        "WHERE position = 'Manager' OR position = 'Supervisor'",
        ["WHERE position = 'Manager' AND position = 'Supervisor'", "WHERE position LIKE 'Manager%' AND position LIKE '%Supervisor'", "WHERE position <> 'Manager' OR position <> 'Supervisor'", "WHERE position BETWEEN 'Manager' AND 'Supervisor'"],
        "IN operatörü parantez içindeki liste elemanlarından herhangi biriyle eşleşmeyi kontrol eder ve OR mantığıyla çalışır."
    ),
    make_q(
        "SQL Server'da <code>WHERE fName LIKE 'A___'</code> ifadesi hangi personelleri listeler?",
        "Adı A harfi ile başlayan ve toplam uzunluğu tam 4 karakter olan personeller",
        ["Adı A harfi ile başlayan ve devamında en az 3 kelime bulunan personeller", "Adı içerisinde en az 3 adet A harfi bulunan tüm personeller", "Adı A harfi ile biten ve toplam uzunluğu 3 karakter olan personeller", "Adı A harfi ile başlayan ve sınırsız uzunlukta olabilen tüm personeller"],
        "Her bir alt çizgi (_) tam bir karakteri temsil eder. A + 3 alt çizgi = 4 karakter."
    ),
    make_q(
        "<code>WHERE address LIKE '%Glasgow%'</code> ifadesi ne anlama gelir?",
        "Adres metninin herhangi bir yerinde 'Glasgow' geçen tüm kayıtları listeler.",
        ["Yalnızca adresi 'Glasgow' ile başlayan kayıtları listeler.", "Yalnızca adresi 'Glasgow' ile biten kayıtları listeler.", "Adresi tam olarak 'Glasgow' olan tek kayıtları listeler.", "Adresinde 'Glasgow' geçmeyen kayıtları listeler."],
        "% karakteri sıfır veya daha fazla karakteri temsil eder; %Glasgow% içinde Glasgow geçenleri bulur."
    ),
    make_q(
        "SQL'de <code>NULL</code> kavramı ile ilgili aşağıdaki ifadelerden hangisi DOĞRUDUR?",
        "NULL, verinin eksik veya bilinmeyen olduğunu belirtir; sıfır veya boşluk ('') değildir.",
        ["NULL, sayısal veri türlerinde otomatik olarak 0 değerine eşittir.", "NULL, karakter veri türlerinde boşluk (' ') karakterine karşılık gelir.", "İki NULL değer <code>NULL = NULL</code> ifadesiyle karşılaştırıldığında TRUE döner.", "NULL değer içeren sütunlar birincil anahtar (Primary Key) olarak tanımlanabilir."],
        "NULL bir değerin yokluğudur, bilinmeyendir. Bu nedenle 0 veya boşluk değildir; = ile değil IS NULL ile kontrol edilir."
    ),
    make_q(
        "<code>SELECT COUNT(*)</code> ile <code>SELECT COUNT(telNo)</code> arasındaki fark nedir?",
        "COUNT(*) tablodaki tüm satırları sayar; COUNT(telNo) ise telNo sütunu NULL olmayan satırları sayar.",
        ["COUNT(*) yalnızca tekil satırları sayarken, COUNT(telNo) tüm satırları sayar.", "COUNT(*) yalnızca sayısal verileri sayarken, COUNT(telNo) metinleri sayar.", "COUNT(*) boş tabloda hata verirken, COUNT(telNo) 0 döndürür.", "İki kullanım arasında mantıksal veya tanımsal hiçbir fark yoktur."],
        "COUNT(*) satırın tamamını saydığı için NULL alanları da sayar; COUNT(sütun) ise o sütunda NULL olanları atlar."
    ),
    make_q(
        "<code>SELECT staffNo, fName, salary/12 AS aylik FROM Staff</code> sorgusundaki <code>salary/12</code> nedir?",
        "Hesaplanmış (Computed) alandır ve takma ad (alias) almıştır.",
        ["Staff tablosuna fiziksel olarak eklenen yeni bir sütundur.", "Veritabanı diskinde kalıcı olarak güncellenen alandır.", "Sadece tam sayı sonuçlar üretebilen bir kısıtlamadır.", "Yalnızca yönetici pozisyonundaki personeller için çalışan bir filtredir."],
        "salary/12 sorgu anında hesaplanan dinamik bir alandır."
    ),
    make_q(
        "<code>SELECT DISTINCT propertyNo FROM Viewing</code> ifadesi ne işe yarar?",
        "Viewing tablosundaki tekrarlı propertyNo değerlerini eleyerek benzersiz listeler.",
        ["Viewing tablosundaki tüm mülk numaralarını tekrarlarıyla birlikte sıralar.", "En çok görüntülenen ilk mülk numarasını döndürür.", "Viewing tablosundan propertyNo sütununu tamamen siler.", "Yalnızca NULL olan propertyNo değerlerini listeler."],
        "DISTINCT tekrarlı satırları kaldırır, benzersiz değer kümesi üretir."
    ),
    make_q(
        "<code>ORDER BY type, rent DESC</code> ifadesi sıralamayı nasıl yapar?",
        "Önce type sütununa göre artan (ASC), aynı type içindekileri rent sütununa göre azalan (DESC)",
        ["Önce rent sütununa göre azalan, sonra type sütununa göre azalan sırada", "Hem type hem rent sütunlarına göre büyükten küçüğe doğru", "Önce type sütununa göre azalan, sonra rent sütununa göre artan sırada", "Her iki sütunun değerlerini toplayarak artan sırada"],
        "type yanında yön belirtilmediği için varsayılan ASC (artan), rent ise açıkça DESC (azalan) sıralanır."
    ),
    make_q(
        "<code>GROUP BY</code> kullanılan bir SQL sorgusunda <code>SELECT</code> listesinde aşağıdakilerden hangisi YER ALAMAZ?",
        "GROUP BY listesinde bulunmayan ve toplama fonksiyonuna alınmamış yalın sütunlar",
        ["GROUP BY yan tümcesinde açıkça belirtilmiş gruplama sütunları", "COUNT, SUM, AVG, MIN, MAX gibi toplama fonksiyonu ifadeleri", "Sabit metin veya sayısal değerler (örneğin 'Şube', 100)", "Toplama fonksiyonları üzerinde yapılan aritmetik hesaplamalar"],
        "Gruplanmış sorgularda grupta tekil olmayan yalın sütunlar SELECT listesinde bulunamaz."
    ),
    make_q(
        "<code>SELECT branchNo, COUNT(staffNo) FROM Staff GROUP BY branchNo HAVING COUNT(staffNo) > 1</code> sorgusunun amacı nedir?",
        "Personel sayısı 1'den fazla olan şubeleri ve bu şubelerdeki personel sayılarını listelemek",
        ["Personel sayısı 1 olan şubelerin numaralarını listelemek", "Tüm şubelerdeki toplam personel sayısını hesaplamak", "Maaşı en yüksek olan ilk şubenin personelini getirmek", "Hiç personeli olmayan şubeleri tespit etmek"],
        "HAVING gruplanmış verilerde grup şartı uygular; COUNT(staffNo) > 1 olan şubeleri filtreler."
    ),
    make_q(
        "SQL'de <code>UNION</code> ile <code>UNION ALL</code> arasındaki temel fark nedir?",
        "UNION tekrarlı satırları kaldırarak birleştirir; UNION ALL tekrarları korur.",
        ["UNION iki tablonun kesişimini alır; UNION ALL farkını alır.", "UNION ALL yalnızca sayısal sütunlarda çalışır; UNION metinlerde çalışır.", "UNION iki tabloyu çarpar; UNION ALL iki tabloyu böler.", "UNION sorguyu yavaşlatmazken, UNION ALL her zaman hata fırlatır."],
        "UNION DISTINCT uygulayarak tekrarları eler; UNION ALL tüm sonuç satırlarını olduğu gibi birleştirir."
    ),
    make_q(
        "<code>EXCEPT</code> (veya Oracle'da <code>MINUS</code>) küme operatörü ne döndürür?",
        "Birinci sorguda bulunup ikinci sorguda bulunmayan satırları",
        ["Her iki sorguda da ortak olarak bulunan kesişim satırlarını", "İki sorgudaki tüm satırların tekrarsız birleşimini", "İki tablonun Kartezyen çarpım sonucunu", "Yalnızca her iki tabloda da NULL olan kayıtları"],
        "EXCEPT küme farkı (A - B) işlemidir: İlk kümede olup ikincide olmayanları verir."
    ),
    make_q(
        "<code>INTERSECT</code> operatörü iki sorgu arasında uygulandığında hangi sonucu üretir?",
        "Her iki sorgu sonucunda da ortak olarak bulunan satırları (Kesişim)",
        ["Birinci sorguda olup ikinci sorguda olmayan satırları", "İki sorgudaki tüm satırların tekrarlı toplamını", "İki tablonun birincil anahtarlarının çarpımını", "Yalnızca NULL içeren satırların listesini"],
        "INTERSECT her iki SELECT sorgusunun da ürettiği ortak satırları (kesişimi) verir."
    ),
    make_q(
        "<code>UPDATE Staff SET salary = salary * 1.03</code> ifadesi <code>WHERE</code> koşulu olmadan çalıştırılırsa ne olur?",
        "Staff tablosundaki TÜM personellerin maaşı %3 oranında artırılır.",
        ["Yalnızca tablodaki ilk personelin maaşı güncellenir.", "SQL motoru WHERE olmadığı için hata verir ve çalışmaz.", "Maaşı NULL olan personellerin maaşı 1.03 yapılır.", "Staff tablosundaki tüm veriler silinir."],
        "UPDATE ifadesinde WHERE belirtilmezse tablodaki tüm satırlar güncellenir."
    ),
    make_q(
        "<code>DELETE FROM Viewing WHERE propertyNo = 'PG4'</code> ifadesi ne yapar?",
        "Viewing tablosundan propertyNo değeri 'PG4' olan tüm satırları siler; tablo yapısı kalır.",
        ["Viewing tablosunu veritabanından tamamen siler.", "propertyNo sütununu Viewing tablosundan kaldırır.", "PG4 mülkünün kirasını sıfır (0) olarak günceller.", "Yalnızca PG4 mülkünün ilk görüntüleme kaydını siler."],
        "DELETE koşula uyan satırları siler, tablo yapısına dokunmaz."
    ),
    make_q(
        "<code>INSERT INTO Staff (staffNo, fName, lName, salary) VALUES ('SL21', 'John', 'White', 30000)</code> ifadesi için hangisi doğrudur?",
        "Yalnızca belirtilen 4 sütuna değer atanır; diğer sütunlar NULL veya DEFAULT değerini alır.",
        ["Tablodaki tüm diğer sütunlara otomatik olarak sıfır (0) atanır.", "Tüm sütunlar belirtilmediği için SQL motoru mutlaka hata fırlatır.", "John White isimli mevcut tüm kayıtlar bu değerlerle güncellenir.", "Bu işlem bir görünüm (VIEW) oluşturarak sanal tablo üretir."],
        "Sütun listesi verildiğinde belirtilmeyen sütunlar (NOT NULL kısıtı yoksa) NULL veya DEFAULT değer alır."
    ),
    make_q(
        "<code>SELECT NULL + 50</code> veya <code>SELECT 'Ali' + NULL</code> ifadesinin standart SQL sonucu nedir?",
        "NULL",
        ["50 ve 'Ali'", "0 ve ''", "Sözdizimi hatası", "False"],
        "NULL bilinmeyen bir değerdir; NULL ile yapılan aritmetik veya metin birleştirme sonucu NULL'dır."
    ),
    make_q(
        "<code>COALESCE(telNo, cepTel, 'Yok')</code> ifadesi ne döndürür?",
        "Parametre listesindeki ilk NULL olmayan değeri döndürür.",
        ["Tüm telefon numaralarını aralarında tire ile birleştirir.", "Listede kaç adet telefon olduğunu sayısal olarak sayar.", "Tüm değerler NULL ise çalışma zamanında hata verir.", "Yalnızca telNo ve cepTel değerleri aynı ise 'Yok' döner."],
        "COALESCE soldan sağa ilk NULL olmayan (non-null) değeri verir."
    ),
    make_q(
        "<code>ISNULL(komisyon, 0)</code> fonksiyonu SQL Server'da ne yapar?",
        "komisyon sütunu NULL ise 0 döndürür, değilse komisyonun kendi değerini döndürür.",
        ["komisyon değerinin sıfır olup olmadığını mantıksal (TRUE/FALSE) denetler.", "komisyon sütununu tablodan tamamen siler.", "komisyon sütunundaki tüm değerleri sıfırlar.", "komisyon NULL olduğunda işlemi geri alır (ROLLBACK)."],
        "ISNULL(deger, yedek) NULL durumunda ikinci parametreyi döndürür."
    ),
    make_q(
        "SQL Server'da <code>SUBSTRING('Veritabanı', 5, 3)</code> ifadesinin çıktısı nedir?",
        "'tab'",
        ["'eri'", "'ita'", "'aba'", "'taba'"],
        "SQL Server 1 tabanlıdır. 5. karakter 't'dir. 3 karakter: 't', 'a', 'b' -> 'tab'."
    ),
    make_q(
        "SQL Server'da <code>CHARINDEX('tan', 'Veritabanı')</code> fonksiyonunun ürettiği tamsayı değer kaçtır?",
        "5",
        ["4", "6", "0", "-1"],
        "'Veritabanı' kelimesinde 't' harfi 5. sırada yer alır (1 tabanlı indeksleme)."
    ),
    make_q(
        "SQL Server'da <code>UPPER(LEFT('ali', 1)) + LOWER(SUBSTRING('ali', 2, 2))</code> ifadesinin çıktısı nedir?",
        "'Ali'",
        ["'ALİ'", "'ali'", "'A'", "'aLI'"],
        "LEFT('ali', 1) -> 'a' -> UPPER -> 'A'. SUBSTRING('ali', 2, 2) -> 'li' -> LOWER -> 'li'. Birleşimi: 'Ali'."
    ),
    make_q(
        "<code>SELECT TOP 5 * FROM Staff ORDER BY salary DESC</code> sorgusunun amacı nedir?",
        "En yüksek maaş alan ilk 5 personeli listelemek",
        ["Maaşı 5000'den yüksek olan tüm personeli listelemek", "Rastgele seçilen 5 personelin maaşını listelemek", "En düşük maaş alan ilk 5 personeli listelemek", "Personel tablosunun son 5 satırını silmek"],
        "salary DESC ile maaşlar büyükten küçüğe sıralanır, TOP 5 ile en yüksek 5 kişi alınır."
    ),
    make_q(
        "<code>SELECT clientNo, viewDate FROM Viewing WHERE propertyNo = 'PG4' AND comment IS NULL</code> sorgusu neyi arar?",
        "PG4 mülkünü görüntüleyip henüz yorum yapmamış (yorum alanı boş olan) müşterileri",
        ["PG4 mülküne 'NULL' kelimesi içeren yorum yapmış müşterileri", "Yorum alanı 0 olan tüm PG4 görüntülemelerini", "PG4 mülkünü hiç görüntülememiş olan müşterileri", "Yorum alanı dolu olan tüm müşterilerin listesini"],
        "comment IS NULL, yorum alanına herhangi bir değer girilmemiş kayıtları bulur."
    ),
    make_q(
        "İki ilişkisel cebir ifadesinin kartezyen çarpımı (R × S) sonucunda oluşan nitelik (sütun) sayısı nedir?",
        "R'nin sütun sayısı ile S'nin sütun sayısının toplamı (n + m)",
        ["R'nin sütun sayısı ile S'nin sütun sayısının çarpımı (n × m)", "R ve S'nin ortak sütunlarının sayısı", "R'nin sütun sayısı eksi S'nin sütun sayısı", "Her iki tablonun satır sayılarının toplamı"],
        "Kartezyen çarpımda sütun sayısı toplanır (derece = deg(R)+deg(S)), satır sayısı çarpılır (kardinalite = |R| × |S|)."
    ),
    make_q(
        "İlişkisel cebirde σ (sigma) sembolü hangi SQL ifadesine karşılık gelir?",
        "WHERE (Seçim / Selection)",
        ["SELECT sütunlar (Projeksiyon / Projection)", "JOIN ... ON (Birleştirme)", "GROUP BY (Gruplama)", "ORDER BY (Sıralama)"],
        "σ (sigma) satırları filtreleyen Seçim (Selection) işlemidir ve SQL'deki WHERE ile eşdeğerdir."
    ),
    make_q(
        "İlişkisel cebirde π (pi) sembolü hangi SQL ifadesine karşılık gelir?",
        "SELECT DISTINCT sütunlar (İzdüşüm / Projection)",
        ["WHERE satır_koşulu (Seçim)", "FROM tablo (Tablo tanımı)", "HAVING grup_koşulu", "ORDER BY sütun"],
        "π (pi) belirli sütunları seçen ve tekrarları kaldıran Projeksiyon (İzdüşüm) işlemidir."
    ),
    make_q(
        "<code>SELECT ad, fiyat FROM urun WHERE kategori='Elektronik'</code> sorgusunun ilişkisel cebir karşılığı hangisidir?",
        "π_ad,fiyat(σ_kategori='Elektronik'(urun))",
        ["σ_ad,fiyat(π_kategori='Elektronik'(urun))", "π_kategori(σ_ad='Elektronik'(urun))", "σ_kategori='Elektronik'(π_kategori(urun))", "π_ad,fiyat(urun) ∩ σ_kategori='Elektronik'(urun)"],
        "Önce içteki σ ile satırlar elenir, sonra dıştaki π ile istenen sütunlar izdüşürülür."
    ),
    make_q(
        "İlişkisel cebirde Doğal Birleştirme (Natural Join - ⋈) işlemi ne yapar?",
        "İki ilişkideki ortak isimli sütunlar üzerinde eşitlik kontrolü yapar ve tekrar eden sütunu teke indirir.",
        ["İki tablonun Kartezyen çarpımını koşulsuz olarak alır.", "Sadece sol tablodaki eşleşmeyen satırları NULL ile doldurur.", "İki tablodaki tüm sütunları ismine bakılmaksızın alt alta ekler.", "Birinci tablodaki satırları ikinci tablodaki satırlardan çıkarır."],
        "Doğal birleştirme, ortak isimli sütunlar üzerinden equijoin yapar ve yinelenen sütunun bir kopyasını atar."
    ),
    make_q(
        "İlişkisel cebirde Bölme (Division - /) işlemi hangi tür sorguları ifade etmek için kullanılır?",
        "'Bütün / Tüm' koşulunu içeren sorgular (Örn: Tüm dersleri alan öğrenciler)",
        ["İki sayısal sütunun birbirine aritmetik bölünmesini gerektiren sorgular", "Tablodaki verilerin iki eşit parçaya ayrılmasını sağlayan sorgular", "Yalnızca çift sayılı birincil anahtara sahip kayıtları arayan sorgular", "Sonuç kümesindeki satır sayısını yarıya indiren sorgular"],
        "Bölme (Division) işlemi 'B kümesindeki tüm elemanlarla ilişkili A elemanlarını bul' sorgularında kullanılır."
    ),
    make_q(
        "İlişkisel cebirde Semijoin (⋉) işleminin tanımı nedir?",
        "İki tablonun birleştirilmesi ve sonucun yalnızca birinci tablonun sütunları üzerine izdüşürülmesi",
        ["İki tablonun yarısının birleştirilip yarısının atılması", "Yalnızca NULL içeren satırların Kartezyen çarpımı", "İki tablonun sütun isimlerinin yer değiştirilmesi", "Dış birleştirme ile tüm NULL değerlerin temizlenmesi"],
        "Semijoin (R ⋉ S), R ⋈ S işleminin ardından sonucun yalnızca R'nin özniteliklerine izdüşürülmesidir (π_R(R ⋈ S))."
    ),
    make_q(
        "SQL'de <code>NOT EXISTS</code> alt sorgusu ne zaman <code>TRUE</code> değer üretir?",
        "Alt sorgu hiçbir satır döndürmediğinde (boş sonuç kümesi ürettiğinde)",
        ["Alt sorgu en az bir satır döndürdüğünde", "Alt sorgudaki tüm değerler NULL olduğunda", "Alt sorguda sözdizimi hatası meydana geldiğinde", "Dış sorgudaki satır sayısı alt sorgudan fazla olduğunda"],
        "NOT EXISTS alt sorgunun döndürdüğü sonuç kümesi boş ise TRUE, en az bir satır varsa FALSE döner."
    ),
    make_q(
        "<code>salary > ALL (SELECT salary FROM Staff WHERE branchNo='B003')</code> koşulu ne anlama gelir?",
        "Maaşın, B003 şubesindeki TÜM çalışanların maaşından daha büyük olması (yani en yüksek maaşından bile büyük olması)",
        ["Maaşın, B003 şubesindeki EN AZ BİR çalışanın maaşından büyük olması", "Maaşın, B003 şubesindeki çalışanların ortalama maaşına eşit olması", "Maaşın, B003 şubesindeki en düşük maaşa eşit olması", "Personelin mutlaka B003 şubesinde çalışıyor olması"],
        "> ALL alt sorgudan dönen tüm değerlerden büyük olmayı gerektirir (Maksimumdan büyük)."
    ),
    make_q(
        "<code>salary > ANY (SELECT salary FROM Staff WHERE branchNo='B003')</code> koşulu ne anlama gelir?",
        "Maaşın, B003 şubesindeki çalışanların EN AZ BİRİNİN maaşından büyük olması (yani en düşük maaşından büyük olması)",
        ["Maaşın, B003 şubesindeki tüm personellerin maaşından büyük olması", "Maaşın, B003 şubesindeki ortalama maaşa eşit olması", "Maaşın hiçbir personele eşit olmaması", "B003 şubesinde çalışan tüm personellerin listelenmesi"],
        "> ANY (veya > SOME) alt sorgudan dönen değerlerin en az birinden büyük olmayı gerektirir (Minimumdan büyük)."
    ),
    make_q(
        "ISO standardına göre <code>WHERE</code> yan tümcesinde <code><></code> işlecinin anlamı nedir?",
        "Eşit değildir (Not equal to)",
        ["Büyük veya eşittir", "Küçük veya eşittir", "Yaklaşık olarak eşittir", "Tanımsız değerdir"],
        "<> operatörü standart SQL'de eşit değildir (NOT EQUAL) anlamına gelir."
    )
]

print(f"Exam 1: {len(s1)} questions.")
