# -*- coding: utf-8 -*-
"""
exams_part1.py: Exam 1 and Exam 2
"""
import random
random.seed(101)

def make_q(question_text, correct_opt, distractors, explanation):
    assert len(distractors) == 4, f"4 distractor required: {question_text[:30]}"
    options = [correct_opt] + distractors
    random.shuffle(options)
    return {
        "q": question_text,
        "o": options,
        "a": options.index(correct_opt),
        "e": explanation
    }

# =========================================================================
# EXAM 1: Temel SQL, Mantıksal Çalışma Sırası, Filtreleme & Operatörler
# =========================================================================
e1 = [
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

# =========================================================================
# EXAM 2: Çok Tablolu Sorgular, JOIN Çeşitleri, Alt Sorgular & İlişkisel Cebir
# (Kaynaklar: DBMS_5, DBMS_6, deney_foyu)
# =========================================================================
random.seed(102)
e2 = [
    make_q(
        "SQL'de <code>INNER JOIN</code> uygulandığında sonuç kümesinde hangi satırlar yer alır?",
        "Yalnızca her iki tabloda da birleştirme koşulunu sağlayan (eşleşen) satırlar",
        ["Sol tablodaki tüm satırlar ve sağdaki eşleşen satırlar", "Sağ tablodaki tüm satırlar ve soldaki eşleşen satırlar", "Her iki tablodaki eşleşmeyen tüm satırlar NULL ile", "İki tablodaki satırların koşulsuz tüm olası kombinasyonları"],
        "INNER JOIN (iç birleştirme) her iki tabloda da ON koşuluyla eşleşen satırları döndürür."
    ),
    make_q(
        "<code>LEFT JOIN</code> (veya <code>LEFT OUTER JOIN</code>) işlemi ile ilgili aşağıdakilerden hangisi DOĞRUDUR?",
        "Sol tablodaki tüm satırlar gelir; sağ tabloda eşleşme yoksa o sütunlar NULL ile dolar.",
        ["Yalnızca sağ tabloda eşleşen satırlar sonuç kümesine eklenir.", "Sol tablodaki eşleşmeyen satırlar sonuçtan tamamen atılır.", "Sol ve sağ tablonun kesişim kümesini tekrarsız döndürür.", "Eşleşme olmayan satırlar için veritabanı motoru hata fırlatır."],
        "LEFT JOIN sol tablodaki tüm verileri korur, sağ tarafta eşleşmeyen kısımları NULL ile doldurur."
    ),
    make_q(
        "<code>RIGHT JOIN</code> (veya <code>RIGHT OUTER JOIN</code>) mantığı aşağıdakilerden hangisidir?",
        "Sağ tablodaki tüm satırlar korunur; sol tabloda eşleşme yoksa NULL ile listelenir.",
        ["Sol tablodaki tüm satırlar korunur; sağ taraf NULL ile listelenir.", "Yalnızca sol tablonun birincil anahtarına sahip satırlar listelenir.", "Her iki tablodaki satırlar çarpılarak yeni satırlar üretilir.", "İki tablonun fark kümesi hesaplanarak sağ tarafa aktarılır."],
        "RIGHT JOIN sağ tablodaki tüm kayıtları garanti eder, sol taraftaki eksikleri NULL yapar."
    ),
    make_q(
        "SQL'de <code>FULL JOIN</code> (veya <code>FULL OUTER JOIN</code>) ne sonuç üretir?",
        "Her iki tablodaki tüm satırları getirir; eşleşmeyen tarafların sütunlarını NULL ile doldurur.",
        ["Yalnızca iki tabloda da tam eşleşen satırları tekilleştirerek listeler.", "Sol tablodaki kayıtları silip sağ tablodaki kayıtları korur.", "İki tablonun birincil anahtarlarını toplayarak tek sütun yapar.", "Yalnızca her iki tarafta da NULL olan satırları filtreler."],
        "FULL JOIN hem sol hem sağ tablodaki tüm satırları korur, eşleşmeyen tarafları NULL ile tamamlar."
    ),
    make_q(
        "10 satırlı bir TabloA ile 5 satırlı bir TabloB arasında <code>CROSS JOIN</code> yapıldığında sonuç kümesinde kaç satır oluşur?",
        "50 satır (10 × 5)",
        ["15 satır (10 + 5)", "5 satır (MIN(10, 5))", "2 satır (10 / 5)", "0 satır (Eşleşme koşulu olmadığı için)"],
        "CROSS JOIN (Kartezyen çarpım) iki tablodaki satır sayılarının çarpımı kadar (|A| × |B|) satır üretir."
    ),
    make_q(
        "<code>SELECT c.clientNo, fName, propertyNo FROM Client c, Viewing v WHERE c.clientNo = v.clientNo</code> sorgusu hangi JOIN türünün eski sözdizimidir?",
        "INNER JOIN (Eski SQL-89 sözdizimi)",
        ["LEFT OUTER JOIN", "FULL OUTER JOIN", "CROSS JOIN", "NATURAL JOIN"],
        "FROM tablosu virgülle ayrılıp WHERE'de eşitlik yazılması ANSI öncesi klasik INNER JOIN sözdizimidir."
    ),
    make_q(
        "Aşağıdaki sorguda hangi iki temel ilişkisel işlem birlikte kullanılmıştır?\n<code>SELECT m.ad, d.bolum_adi FROM Personel m JOIN Bolum d ON m.bolum_id = d.bolum_id</code>",
        "Birleştirme (Join) ve İzdüşüm (Projection)",
        ["Seçim (Selection) ve Fark (Difference)", "Birleşim (Union) ve Kesişim (Intersection)", "Bölme (Division) ve Seçim (Selection)", "Yalnızca İzdüşüm (Projection)"],
        "JOIN işlemi tabloları birleştirir (Join), SELECT m.ad, d.bolum_adi ise belirli sütunları seçer (Projection)."
    ),
    make_q(
        "<code>SELECT * FROM Staff WHERE salary > (SELECT AVG(salary) FROM Staff)</code> sorgusundaki alt sorgu ne tür bir alt sorgudur?",
        "Skaler Alt Sorgu (Tek bir sayısal değer döndürür)",
        ["Tablo Alt Sorgusu (Çok satır ve çok sütun döndürür)", "Satır Alt Sorgusu (Tek satır, birden çok sütun döndürür)", "Korele Olmayan Görünüm Sorgusu", "Özyinelemeli (Recursive) Alt Sorgu"],
        "AVG(salary) tek bir skaler sayısal değer döndürdüğü için bu bir skaler alt sorgudur (scalar subquery)."
    ),
    make_q(
        "Bir alt sorgu (Subquery) SQL standardına göre aşağıdaki yan tümcelerin hangisinde KULLANILAMAZ?",
        "ORDER BY yan tümcesinde (doğrudan sıralama ifadesi olarak genel alt sorgu)",
        ["WHERE yan tümcesinde", "HAVING yan tümcesinde", "FROM yan tümcesinde (Türetilmiş tablo olarak)", "SELECT listesinde (Skaler alan olarak)"],
        "Alt sorgular SELECT, FROM, WHERE ve HAVING bloklarında kullanılır; doğrudan genel alt sorgular ORDER BY içinde desteklenmez."
    ),
    make_q(
        "<code>SELECT b.branchNo, b.city, s.fName FROM Branch b LEFT JOIN Staff s ON b.branchNo = s.branchNo WHERE s.staffNo IS NULL</code> sorgusunun amacı nedir?",
        "Hiç personeli bulunmayan (boş olan) şubeleri listelemek",
        ["Tüm personellerin çalıştığı şubeleri listelemek", "Personel sayısı en fazla olan şubeyi bulmak", "Personelinin adı 'NULL' olan şubeleri listelemek", "Personeli olan ama şehri olmayan şubeleri getirmek"],
        "LEFT JOIN sonrası sağ tablonun birincil anahtarının IS NULL olması, sol tabloda olup sağda eşleşmesi olmayanları bulur."
    ),
    make_q(
        "Alt sorgularda kullanılan <code>EXISTS</code> operatörü ile ilgili hangisi DOĞRUDUR?",
        "Alt sorgu en az 1 satır döndürdüğü anda arama tamamlanır ve TRUE üretilir; performanslıdır.",
        ["Alt sorgunun tüm satırlarını belleğe çekip tek tek sayarak satır sayısını kontrol eder.", "EXISTS ile birlikte yalnızca <code>SELECT COUNT(*)</code> kullanılmak zorundadır.", "Alt sorguda NULL değer varsa EXISTS her zaman FALSE döndürür.", "EXISTS yalnızca sayısal sütunlar içeren alt sorgularda çalışır."],
        "EXISTS varlık kontrolü yapar; ilk eşleşen satırı bulduğu anda TRUE döner ve taramayı bitirir."
    ),
    make_q(
        "<code>SELECT p.ad, p.maas FROM Personel p WHERE p.maas > (SELECT AVG(m.maas) FROM Personel m WHERE m.bolum_id = p.bolum_id)</code> sorgusu ne tür bir alt sorgudur?",
        "İlişkili (Correlated) Alt Sorgu",
        ["Bağımsız (Uncorrelated) Alt Sorgu", "Statik Skaler Sorgu", "Dış Birleştirme Sorgusu", "Kartezyen Alt Sorgu"],
        "İç sorguda dış sorgunun tablosuna (p.bolum_id) referans verildiği için her satır için tekrar çalışır; buna Correlated Subquery denir."
    ),
    make_q(
        "DreamHome şemasında <code>(SELECT city FROM Branch) INTERSECT (SELECT city FROM PropertyForRent)</code> sorgusu ne döndürür?",
        "Hem şube hem de kiralık mülk bulunan ortak şehirlerin listesini",
        ["Yalnızca şubesi olup mülkü olmayan şehirleri", "Tüm şube ve mülk şehirlerinin tekrarlı birleşimini", "Hiç şubesi ve mülkü bulunmayan şehirleri", "Mülk sayısı şube sayısından fazla olan şehirleri"],
        "INTERSECT kesişim kümesini alır: Her iki tabloda da ortak bulunan şehirleri tekilleştirerek getirir."
    ),
    make_q(
        "<code>(SELECT city FROM Branch) EXCEPT (SELECT city FROM PropertyForRent)</code> sorgusu ne döndürür?",
        "Şubesi bulunan ancak hiç kiralık mülkü olmayan şehirlerin listesini",
        ["Kiralık mülkü olan ancak hiç şubesi olmayan şehirleri", "Hem şubesi hem de kiralık mülkü olan ortak şehirleri", "Tüm şehirlerin alfabetik sıralı listesini", "Şube sayısı ile mülk sayısı eşit olan şehirleri"],
        "EXCEPT (A - B): Branch'te olup PropertyForRent'te olmayan şehirleri bulur."
    ),
    make_q(
        "İlişkisel cebirde <code>R ∪ S</code> (Birleşim) işlemi yapılabilmesi için temel ön koşul nedir?",
        "R ve S ilişkilerinin birleşim uyumlu (Union-compatible: aynı sayıda ve eşleşen tiplerde sütunlara sahip) olması",
        ["R ve S ilişkilerinin aynı sayıda satıra sahip olması", "R ve S ilişkilerinin aynı birincil anahtarı paylaşması", "R ilişkisinin S ilişkisinin bir alt kümesi olması", "Her iki tablonun da aynı veritabanı şemasında bulunması"],
        "Birleşim uyumluluğu (Union compatibility): Her iki ilişkinin de derece (öznitelik sayısı) ve karşılıklı etki alanlarının (tiplerinin) aynı olmasıdır."
    ),
    make_q(
        "İlişkisel cebirde <code>R − S</code> (Fark) işlemi için hangisi DOĞRUDUR?",
        "R ilişkisinde bulunan fakat S ilişkisinde bulunmayan kayıtları içerir.",
        ["S ilişkisinde bulunan fakat R ilişkisinde bulunmayan kayıtları içerir.", "R ve S ilişkilerinin ortak elemanlarını içerir.", "R ve S ilişkilerinin Kartezyen çarpımından farkını alır.", "Her iki ilişkideki tüm satırların toplamını verir."],
        "Küme farkı R - S, R'de olup S'de olmayan satırları verir."
    ),
    make_q(
        "İlişkisel cebirde <code>ρ (rho)</code> sembolü hangi işlevi temsil eder?",
        "Yeniden adlandırma (Rename - Tabloya veya sütunlara yeni isim/takma ad verme)",
        ["Kayıt silme (Remove)", "Sonuçları sıralama (Reorder)", "Referans bütünlüğü kontrolü (Reference)", "İlişkileri sıfırlama (Reset)"],
        "ρ (rho) ilişkisel cebirde ilişkileri veya öznitelikleri yeniden adlandırmak (alias/rename) için kullanılır."
    ),
    make_q(
        "İlişkisel cebirde Teta Birleştirme (Theta Join - ⋈_θ) nedir?",
        "Kartezyen çarpımın ardından belirli bir genel karşılaştırma koşulunun (θ: =, <, >, <= vb.) uygulanması",
        ["Yalnızca eşitlik durumunda yapılan doğal birleştirme", "İki tablonun farkının alınıp karekökünün hesaplanması", "Sadece NULL değer içeren satırların çarpılması", "İki ilişkinin sütunlarının alfabetik olarak dizilmesi"],
        "Theta Join: R ⋈_θ S = σ_θ (R × S). Kartezyen çarpım üzerine teta koşullu seçim uygulanmasıdır."
    ),
    make_q(
        "Eşit Birleştirme (Equijoin) ile Doğal Birleştirme (Natural Join) arasındaki en belirgin fark nedir?",
        "Equijoin eşleşen ortak sütunların her ikisini de korurken, Natural Join yinelenen sütunun bir kopyasını eler.",
        ["Equijoin yalnızca büyüktür (>) kullanırken, Natural Join eşittir (=) kullanır.", "Equijoin tablodaki satırları silerken, Natural Join yeni sütun ekler.", "Natural Join yalnızca tek satırlık tablolarda çalışır.", "İkisi arasında hiçbir mantıksal veya tanımsal fark yoktur."],
        "Equijoin'de her iki tablonun ortak sütunları sonuçta ayrı ayrı kalır; Natural Join'de ortak sütun teke indirilir."
    ),
    make_q(
        "<code>SELECT s.fName, p.propertyNo FROM Staff s CROSS JOIN PropertyForRent p</code> sorgusu ne üretir?",
        "Her bir personelin her bir mülkle eşleştiği tüm olası ikili kombinasyonları (Kartezyen çarpım)",
        ["Yalnızca personelin sorumlu olduğu mülklerin listesini", "Hiçbir personelin yönetmediği boş mülkleri", "Yalnızca aynı şehirde bulunan personel ve mülkleri", "Personel sayısı ile mülk sayısı eşit olan kayıtları"],
        "CROSS JOIN koşulsuz kartezyen çarpımdır; sol tablodaki her satır sağ tablodaki her satırla eşleşir."
    ),
    make_q(
        "<code>WHERE salary >= (SELECT MAX(salary) FROM Staff WHERE branchNo = 'B003')</code> ifadesi aşağıdakilerden hangisiyle tamamen aynı sonucu verir?",
        "<code>WHERE salary >= ALL (SELECT salary FROM Staff WHERE branchNo = 'B003')</code>",
        ["<code>WHERE salary >= ANY (SELECT salary FROM Staff WHERE branchNo = 'B003')</code>", "<code>WHERE salary >= SOME (SELECT salary FROM Staff WHERE branchNo = 'B003')</code>", "<code>WHERE salary IN (SELECT salary FROM Staff WHERE branchNo = 'B003')</code>", "<code>WHERE salary = (SELECT MIN(salary) FROM Staff WHERE branchNo = 'B003')</code>"],
        "Bir kümedeki MAX değerden büyük/eşit olmak, o kümedeki ALL (tüm) değerlerden büyük/eşit olmakla eşdeğerdir."
    ),
    make_q(
        "<code>WHERE salary > (SELECT MIN(salary) FROM Staff WHERE branchNo = 'B003')</code> ifadesi aşağıdakilerden hangisiyle tamamen aynı sonucu verir?",
        "<code>WHERE salary > ANY (SELECT salary FROM Staff WHERE branchNo = 'B003')</code>",
        ["<code>WHERE salary > ALL (SELECT salary FROM Staff WHERE branchNo = 'B003')</code>", "<code>WHERE salary = ALL (SELECT salary FROM Staff WHERE branchNo = 'B003')</code>", "<code>WHERE salary NOT IN (SELECT salary FROM Staff WHERE branchNo = 'B003')</code>", "<code>WHERE salary < ANY (SELECT salary FROM Staff WHERE branchNo = 'B003')</code>"],
        "Bir kümedeki MIN değerden büyük olmak, o kümedeki ANY (en az bir) değerden büyük olmakla eşdeğerdir."
    ),
    make_q(
        "<code>SELECT b.branchNo, COUNT(p.propertyNo) FROM Branch b LEFT JOIN PropertyForRent p ON b.branchNo = p.branchNo GROUP BY b.branchNo</code> sorgusunda hiç mülkü olmayan bir şube için COUNT değeri kaç çıkar?",
        "0 (Sıfır)",
        ["NULL", "1", "Hata verir", "-1"],
        "COUNT(p.propertyNo) NULL değerleri saymadığı için, eşleşmeyen şube için mülk sütunu NULL gelir ve COUNT sonucu 0 olur."
    ),
    make_q(
        "Yukarıdaki sorguda <code>COUNT(p.propertyNo)</code> yerine <code>COUNT(*)</code> kullanılsaydı hiç mülkü olmayan şube için sonuç kaç çıkardı?",
        "1 (Çünkü LEFT JOIN sonucu şube bilgisiyle oluşan 1 adet satır vardır ve COUNT(*) satırı sayar)",
        ["0 (Sıfır)", "NULL", "Hata verir", "Sonsuz"],
        "Tuzak soru: COUNT(*) satırın tamamını saydığından LEFT JOIN ile oluşan [Sube1, NULL, NULL...] satırını 1 olarak sayar!"
    ),
    make_q(
        "SQL'de <code>NATURAL JOIN</code> kullanılırken karşılaşılabilecek en büyük risk/tehlike nedir?",
        "Tablolara sonradan aynı isimde fakat farklı amaçlı bir sütun eklendiğinde birleştirme mantığının bozulması",
        ["Sorgunun derlenememesi ve her zaman sözdizimi hatası fırlatması", "Tablodaki tüm birincil anahtarların otomatik olarak silinmesi", "Veritabanı indekslerinin diskten kalıcı olarak kaldırılması", "Yalnızca tek bir satır döndürmeye zorlanması"],
        "Natural Join aynı isimli tüm sütunları otomatik eşleştirdiğinden, tablolara aynı isimli alakasız kolon eklenince sorgu bozulur."
    ),
    make_q(
        "<code>SELECT * FROM Ogrenci WHERE bolum_kod NOT IN (SELECT bolum_kod FROM Bolum WHERE aktif = 1)</code> sorgusunda alt sorgu <code>NULL</code> bir değer döndürürse ne olur?",
        "Dış sorgu hiçbir satır döndürmez (Boş küme döner; çünkü NOT IN içinde NULL varsa sonuç UNKNOWN olur).",
        ["Dış sorgu tüm öğrencileri eksiksiz listeler.", "Yalnızca bolum_kod değeri NULL olan öğrenciler listelenir.", "Veritabanı derleyicisi kritik hata fırlatıp bağlantıyı keser.", "Alt sorgudaki NULL değer otomatik olarak 0 yapılır."],
        "Kritik SQL tuzağı: NOT IN (değerler..., NULL) karşılaştırması her satır için UNKNOWN ürettiğinden sonuç boş küme döner."
    ),
    make_q(
        "<code>NOT IN</code> kullanımındaki NULL tehlikesinden kaçınmak için hangi alternatif yapı tavsiye edilir?",
        "<code>NOT EXISTS</code> veya <code>LEFT JOIN ... WHERE sag_tablo.id IS NULL</code>",
        ["<code>OR</code> operatörüyle zincirleme karşılaştırma", "<code>IN ALL</code> bileşik operatörü", "<code>BETWEEN NULL AND 100</code> ifadesi", "<code>UNION ALL</code> ile tabloları birleştirme"],
        "NOT EXISTS üç değerli mantıktaki (Three-Valued Logic) NULL tuzaklarından etkilenmez ve daha güvenlidir."
    ),
    make_q(
        "İki tablonun birleştirilmesinde <code>ON</code> yan tümcesi ile <code>WHERE</code> yan tümcesi arasındaki fark (özellikle OUTER JOIN'de) nedir?",
        "ON koşulu birleştirmenin nasıl yapılacağını belirler; WHERE ise birleştirmeden sonra oluşan satırları eler.",
        ["ON yalnızca sayısal alanlarda, WHERE metin alanlarında kullanılır.", "ON koşulu gruplamadan sonra çalışır; WHERE gruplamadan önce çalışır.", "İkisi tamamen aynıdır ve OUTER JOIN'de hiçbir fark yaratmaz.", "ON sorguyu yavaşlatırken WHERE indeks kullanımını zorunlu kılar."],
        "OUTER JOIN'de ON sağ tablonun eşleşmesini kontrol eder; WHERE ise birleşmiş nihai satırları filtrelediği için LEFT JOIN'i fiilen INNER JOIN'e çevirebilir."
    ),
    make_q(
        "<code>SELECT a.*, b.* FROM TabloA a LEFT JOIN TabloB b ON a.id = b.id WHERE b.durum = 'Aktif'</code> sorgusunun fiili sonucu nedir?",
        "WHERE koşulu eşleşmeyen satırlardaki NULL durumları elediği için sorgu fiilen INNER JOIN gibi çalışır.",
        ["TabloA'daki tüm satırlar durumuna bakılmaksızın eksiksiz gelir.", "TabloB'deki tüm kayıtlar silinerek TabloA güncellenir.", "Sorgu derleme hatası vererek çalışmayı durdurur.", "TabloA'nın yalnızca pasif kayıtları listelenir."],
        "LEFT JOIN yapılmasına rağmen WHERE b.durum = 'Aktif' yazılırsa, b.durum'un NULL olduğu satırlar elenir ve sorgu INNER JOIN'e dönüşür."
    ),
    make_q(
        "Yukarıdaki sorguda TabloA'daki tüm satırların korunması ve sadece 'Aktif' olan TabloB kayıtlarının eşleşmesi için 'Aktif' şartı nereye yazılmalıdır?",
        "<code>ON a.id = b.id AND b.durum = 'Aktif'</code> (ON yan tümcesine)",
        ["<code>HAVING b.durum = 'Aktif'</code> yan tümcesine", "<code>GROUP BY b.durum</code> yan tümcesine", "<code>ORDER BY b.durum = 'Aktif'</code> yan tümcesine", "<code>WHERE a.id IS NOT NULL</code> yan tümcesine"],
        "OUTER JOIN filtreleme koşulları ON içine yazılırsa, eşleşmeyen sol satırlar elenmez, sağ tarafı NULL olarak korunur."
    ),
    make_q(
        "SQL'de <code>SELF JOIN</code> (Özyinelemeli / Kendi Kendine Birleştirme) ne zaman kullanılır?",
        "Bir tablodaki satırların yine aynı tablodaki diğer satırlarla ilişkisi olduğunda (Örn: Personel tablosunda mudur_id)",
        ["Tablodaki verilerin iki katına çıkarılması gerektiğinde", "Tabloya yeni bir sütun eklendiğinde", "Veritabanında yalnızca tek bir tablo tanımlı olduğunda", "Tablonun yedeği diske yazılırken"],
        "Personel ve yöneticisinin aynı tabloda tutulduğu hiyerarşik yapılarda tablo kendisine JOIN edilir (Self Join)."
    ),
    make_q(
        "<code>SELECT e.fName AS Calisan, m.fName AS Mudur FROM Staff e LEFT JOIN Staff m ON e.managerNo = m.staffNo</code> sorgusunda müdürü olmayan en üst düzey yöneticinin Mudur sütununda ne yazar?",
        "NULL",
        ["'Müdür Yok'", "'0'", "Kendi adı", "Hata"],
        "En üst yöneticinin managerNo alanı NULL olduğundan, LEFT JOIN sonucunda m.fName alanı NULL gelecektir."
    ),
    make_q(
        "İlişkisel cebirde <code>π_staffNo(Staff) − π_staffNo(PropertyForRent)</code> ifadesi neyi bulur?",
        "Hiç kiralık mülk yönetmeyen (üzerinde mülk kaydı olmayan) personellerin numaralarını",
        ["Tüm personellerin ve yönettikleri mülklerin listesini", "Kiralık mülklerin bulunduğu tüm personelleri", "Personeli olmayan kiralık mülklerin numaralarını", "En çok mülk yöneten personelin numarasını"],
        "Tüm personellerden mülk yöneten personeller çıkarılırsa (küme farkı), geriye hiç mülk yönetmeyenler kalır."
    ),
    make_q(
        "<code>SELECT DISTINCT branchNo FROM Branch WHERE branchNo IN (SELECT branchNo FROM PropertyForRent)</code> sorgusunun ilişkisel cebir karşılığı nedir?",
        "<code>π_branchNo(Branch) ∩ π_branchNo(PropertyForRent)</code>",
        ["<code>π_branchNo(Branch) ∪ π_branchNo(PropertyForRent)</code>", "<code>π_branchNo(Branch) − π_branchNo(PropertyForRent)</code>", "<code>Branch × PropertyForRent</code>", "<code>σ_branchNo(Branch)</code>"],
        "PropertyForRent tablosunda bulunan şubelerin Branch tablosuyla kesişimi π(Branch) ∩ π(PropertyForRent) ifadesidir."
    ),
    make_q(
        "İlişkisel cebirde birleştirme işleminin kapanma (closure) özelliği ne anlama gelir?",
        "İlişkisel işlemlerin sonucunun daima yeni bir 'ilişki' (tablo) olması ve başka işlemlere girdi olabilmesi",
        ["Birleştirme yapıldıktan sonra tablonun veritabanına kilitlenmesi", "Tablodaki tüm foreign key bağlantılarının otomatik kapatılması", "Sorgunun tamamlanmasının ardından belleğin serbest bırakılması", "İşlemin yalnızca kapalı ağlarda çalışabilmesi"],
        "Kapanma özelliği: Bir ilişkisel işlemin çıktısı da bir ilişkidir, bu sayede iç içe sorgular/işlemler zincirlenebilir."
    ),
    make_q(
        "<code>SELECT * FROM Viewing v WHERE NOT EXISTS (SELECT * FROM Client c WHERE c.clientNo = v.clientNo)</code> sorgusu neyi tespit etmek için kullanılır?",
        "Referans bütünlüğü bozulmuş (Client tablosunda kaydı olmayan 'yetim' görüntüleme satırlarını)",
        ["En çok mülk görüntüleyen müşterileri", "Hiçbir mülkü görüntülememiş aktif müşterileri", "Yorum alanı dolu olan tüm müşterileri", "Sistemdeki tüm kayıtlı kullanıcıları"],
        "Viewing tablosunda clientNo var ama Client tablosunda karşılığı yoksa bu referans bütünlüğü hatasını (orphan record) gösterir."
    ),
    make_q(
        "SQL Server'da <code>FULL OUTER JOIN</code> kullanırken her iki tarafta da eşleşmeyen satırları filtrelemek için WHERE yan tümcesinde ne kullanılır?",
        "<code>WHERE a.id IS NULL OR b.id IS NULL</code>",
        ["<code>WHERE a.id = b.id</code>", "<code>WHERE a.id IS NOT NULL AND b.id IS NOT NULL</code>", "<code>WHERE a.id <> b.id</code>", "<code>WHERE a.id IN (b.id)</code>"],
        "FULL JOIN sonrası a.id IS NULL OR b.id IS NULL yazılırsa yalnız eşleşmeyen (simetrik fark) satırlar listelenir."
    ),
    make_q(
        "Aşağıdaki küme operatörlerinden hangisi standart SQL'de varsayılan olarak yinelenen (duplicate) satırları korur?",
        "UNION ALL",
        ["UNION", "INTERSECT", "EXCEPT", "MINUS"],
        "UNION, INTERSECT ve EXCEPT varsayılan olarak DISTINCT çalışırken, yalnızca UNION ALL tekrarları korur."
    ),
    make_q(
        "<code>SELECT branchNo, city FROM Branch UNION SELECT branchNo, street FROM PropertyForRent</code> sorgusunda dönen sütun başlıkları hangi sorgudan alınır?",
        "İlk (üstteki) SELECT sorgusundaki sütun adlarından (branchNo, city)",
        ["İkinci (alttaki) SELECT sorgusundaki sütun adlarından (branchNo, street)", "Her iki sütunun adının birleşiminden (city_street)", "Veritabanı motorunun ürettiği Col1, Col2 varsayılan adlarından", "Sorgu derleme hatası verir ve sütun başlığı oluşmaz"],
        "Küme işlemlerinde sonuç kümesinin sütun isimleri daima ilk (en üstteki) SELECT ifadesinden türetilir."
    ),
    make_q(
        "SQL'de <code>WHERE NOT (salary > 10000 AND branchNo = 'B003')</code> ifadesi ile aşağıdakilerden hangisi mantıksal olarak eşdeğerdir?",
        "<code>WHERE salary <= 10000 OR branchNo <> 'B003' OR salary IS NULL OR branchNo IS NULL</code>",
        ["<code>WHERE salary <= 10000 AND branchNo <> 'B003'</code>", "<code>WHERE salary > 10000 OR branchNo = 'B003'</code>", "<code>WHERE salary = 10000 AND branchNo = 'B003'</code>", "<code>WHERE salary < 10000 AND branchNo = 'B003'</code>"],
        "De Morgan kuralı: NOT (A AND B) = (NOT A) OR (NOT B). salary > 10000'in tersi salary <= 10000, branchNo = 'B003'ün tersi branchNo <> 'B003'tür."
    )
]

print(f"Exam 1: {len(e1)}, Exam 2: {len(e2)}")
