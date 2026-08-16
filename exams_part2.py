# -*- coding: utf-8 -*-
"""
exams_part2.py: Exam 3 and Exam 4
"""
import random
random.seed(103)

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
# EXAM 3: DDL, Tablo Tasarımı, Kısıtlamalar (Constraints), Veri Tipleri & Bütünlük
# (Kaynaklar: DBMS_7, 2016 vtys final cevaplar, deney_foyu)
# =========================================================================
e3 = [
    make_q(
        "Veritabanında <code>PRIMARY KEY</code> (Birincil Anahtar) kısıtlaması ile ilgili aşağıdakilerden hangisi KESİNLİKLE DOĞRUDUR?",
        "Tabloda yalnızca bir adet Primary Key tanımlanabilir, her satırı benzersiz tanımlar ve asla NULL değer içeremez.",
        ["Bir tabloda birden fazla Primary Key sütunu bağımsız olarak tanımlanabilir.", "Primary Key sütunları varsayılan olarak NULL değer kabul edebilir.", "Primary Key kısıtlaması yalnızca tek bir sütundan oluşabilir; bileşik anahtar yapılamaz.", "Primary Key tanımlanan tabloda yabancı anahtar (Foreign Key) bulunamaz."],
        "Varlık bütünlüğü kuralı: Birincil anahtar benzersizdir, NULL olamaz ve bir tabloda tek bir PK kısıtı bulunur."
    ),
    make_q(
        "İlişkisel veritabanı bütünlük kurallarından 'Varlık Bütünlüğü' (Entity Integrity) neyi zorunlu kılar?",
        "Birincil anahtar (Primary Key) alanlarının NULL olmamasını ve her satır için benzersiz olmasını",
        ["Yabancı anahtarların daima geçerli bir kayda işaret etmesini", "Tüm sayısal alanların sıfırdan büyük olmasını", "Tabloda en az iki adet indeks bulunmasını", "Kullanıcıların yalnızca kendi kayıtlarını görebilmesini"],
        "Entity Integrity (Varlık Bütünlüğü): Temel ilişkinin birincil anahtarının hiçbir niteliği NULL olamaz."
    ),
    make_q(
        "İlişkisel veritabanlarında 'Referans Bütünlüğü' (Referential Integrity) kuralı neyi ifade eder?",
        "Yabancı anahtar (Foreign Key) değerinin, ana tablodaki geçerli bir birincil anahtar değeriyle eşleşmesini veya NULL olmasını",
        ["Tüm sütunların tekil (atomik) değer içermesini", "Birincil anahtarın en fazla 5 karakter olmasını", "Tabloların alfabetik sırayla oluşturulmasını", "Her tabloda bir tarih sütunu bulunmasını"],
        "Referans bütünlüğü: Yabancı anahtar boş (NULL) değilse, referans verdiği tablonun aday/birincil anahtarında mevcut olmalıdır."
    ),
    make_q(
        "<code>FOREIGN KEY (bolum_kod) REFERENCES Bolum(bolum_kod) ON DELETE CASCADE</code> ifadesinde ana tablodan bir bölüm silinirse ne olur?",
        "O bölüme bağlı olan alt tablodaki tüm ilgili kayıtlar da veritabanı tarafından otomatik olarak silinir.",
        ["Silme işlemi hata verir ve ana tablodaki bölümün silinmesi engellenir.", "Alt tablodaki kayıtların bolum_kod değeri otomatik olarak NULL yapılır.", "Alt tablodaki kayıtlar varsayılan (DEFAULT) bölüme atanır.", "Ana tablodaki bölüm silinir ama alt tablodaki kayıtlar aynen kalır."],
        "CASCADE silme/güncelleme eylemini ilişkili tüm alt tablolara otomatik olarak zincirleme yayar."
    ),
    make_q(
        "<code>ON DELETE SET NULL</code> referans eyleminin başarıyla çalışabilmesi için alt tablodaki yabancı anahtar sütunu hangi özelliğe sahip olmalıdır?",
        "Sütun <code>NOT NULL</code> olarak tanımlanmamış olmalı (yani NULL değer kabul edebilmelidir).",
        ["Sütun mutlaka Primary Key olarak tanımlanmış olmalıdır.", "Sütun yalnızca tam sayı (INT) veri tipinde olmalıdır.", "Sütun üzerinde UNIQUE kısıtlaması bulunmalıdır.", "Sütun üzerinde mutlaka bir CHECK kısıtlaması olmalıdır."],
        "SET NULL, ana kayıt silinince alt sütuna NULL atar; bu nedenle o sütunun NULL değer kabul etmesi şarttır."
    ),
    make_q(
        "<code>ON DELETE NO ACTION</code> (veya <code>RESTRICT</code>) kısıtlamasının davranışı nedir?",
        "Alt tabloda ilişkili kayıt varken ana tablodan o kaydın silinmesini engeller ve hata üretir.",
        ["Ana kaydı siler ve alt kayıtlardaki yabancı anahtarı sıfırlar.", "Alt tablodaki kayıtları da otomatik olarak siler.", "Ana kaydı silip alt kayıtlara varsayılan değer atar.", "Silme işlemini transaction kuyruğuna alıp bekletir."],
        "NO ACTION / RESTRICT referans bütünlüğünü korumak için bağlı kayıt varken ana kaydın silinmesine izin vermez."
    ),
    make_q(
        "<code>CREATE TABLE</code> ifadesinde <code>CHECK (vizenot >= 0 AND vizenot <= 100)</code> kısıtlamasının görevi nedir?",
        "vizenot sütununa yalnızca 0 ile 100 arasındaki değerlerin girilmesini zorunlu kılmak",
        ["vizenot sütununu birincil anahtar olarak tanımlamak", "vizenot sütunundaki NULL değerleri otomatik olarak 0 yapmak", "vizenot sütununa göre tabloyu fiziksel olarak sıralamak", "vizenot sütununu başka bir tabloyla ilişkilendirmek"],
        "CHECK kısıtlaması bir sütuna girilebilecek değerleri mantıksal bir koşulla sınırlar."
    ),
    make_q(
        "<code>CREATE TABLE</code> ifadesinde <code>harfnotu VARCHAR(2) CONSTRAINT ck_harf CHECK (harfnotu IN ('AA','BA','BB','CB','CC','DC','DD','FF'))</code> kısıtı ne sağlar?",
        "harfnotu alanına yalnızca listede belirtilen geçerli harf notlarının girilebilmesini sağlar.",
        ["harfnotu alanını otomatik olarak büyük harfe dönüştürür.", "harfnotu alanının boş (NULL) bırakılmasını zorunlu kılar.", "harfnotu alanındaki değerlerin iki karakterden uzun olmasını engeller.", "Öğrencinin ortalamasını otomatik olarak harf notuna çevirir."],
        "CHECK ... IN (...) sütun değerinin yalnızca izin verilen önceden tanımlı küme elemanlarından biri olmasını garanti eder."
    ),
    make_q(
        "SQL Server'da <code>ogrno VARCHAR(5) CONSTRAINT ck_ogrno CHECK (ogrno LIKE '[0-9][0-9][0-9][0-9][0-9]')</code> kısıtlaması neyi denetler?",
        "ogrno alanının tam olarak 5 basamaklı sayısal karakterlerden oluşmasını",
        ["ogrno alanının 0 ile 9 arasında tek bir rakam olmasını", "ogrno alanının harf veya özel karakter içerebilmesini", "ogrno alanının otomatik artan bir sayaç olmasını", "ogrno alanının 5 basamaktan küçük olmasını"],
        "Her bir [0-9] kalıbı tek bir rakamı zorunlu kılar; 5 adet [0-9] tam 5 basamaklı sayısal dizgi kontrolü yapar."
    ),
    make_q(
        "<code>UNIQUE</code> kısıtlaması ile <code>PRIMARY KEY</code> kısıtlaması arasındaki temel fark nedir?",
        "PRIMARY KEY asla NULL kabul etmezken, UNIQUE kısıtlaması standart SQL'de NULL değer kabul edebilir (SQL Server'da 1 adet NULL).",
        ["UNIQUE kısıtlaması yalnızca metin alanlarında, PRIMARY KEY ise yalnızca sayılarda kullanılır.", "Bir tabloda yalnızca 1 adet UNIQUE kısıtlaması bulunabilir.", "PRIMARY KEY yabancı anahtarla bağlanamazken UNIQUE bağlanabilir.", "UNIQUE kısıtlaması veritabanında indeks oluşturmaz."],
        "Bir tabloda birden çok UNIQUE kısıtı olabilir ve UNIQUE kuralı NULL değerlere izin verir; PK ise tektir ve NOT NULL zorunludur."
    ),
    make_q(
        "<code>DEFAULT 'Bireysel'</code> kısıtlaması ne işe yarar?",
        "INSERT sırasında o sütuna herhangi bir değer gönderilmezse varsayılan olarak 'Bireysel' değerini atar.",
        ["Sütundaki mevcut tüm değerleri 'Bireysel' olarak günceller.", "Sütunun yalnızca 'Bireysel' değerini alabilmesini zorunlu kılar.", "Sütunun NULL kabul etmesini kesin olarak engeller.", "Kullanıcının 'Bireysel' dışında değer girmesini yasaklar."],
        "DEFAULT kısıtı, veri ekleme (INSERT) anında değer belirtilmediğinde otomatik olarak atanacak başlangıç değerini belirler."
    ),
    make_q(
        "SQL Server'da <code>bolumsirano INT IDENTITY(1,1) PRIMARY KEY</code> ifadesindeki <code>IDENTITY(1,1)</code> ne anlama gelir?",
        "1 değerinden başlayıp her yeni kayıtta değeri 1'er 1'er otomatik artan sayısal kimlik sütunudur.",
        ["Yalnızca 1 ile 1 arasındaki değerleri kabul eden kısıtlamadır.", "Tabloda 1 satır ve 1 sütun bulunacağını belirtir.", "Sütunun varsayılan değerini 1.1 olarak ayarlar.", "Tabloya aynı anda yalnızca 1 kullanıcının erişebileceğini belirtir."],
        "IDENTITY(seed, increment): İlk parametre başlangıç değeri (seed=1), ikinci parametre artış miktarıdır (increment=1)."
    ),
    make_q(
        "Mevcut bir tabloya yeni bir sütun eklemek için hangi SQL komutu kullanılır?",
        "<code>ALTER TABLE TabloAdi ADD SütunAdi VeriTipi</code>",
        ["<code>CREATE COLUMN SütunAdi ON TabloAdi</code>", "<code>UPDATE TABLE TabloAdi INSERT SütunAdi</code>", "<code>MODIFY TABLE TabloAdi NEW SütunAdi</code>", "<code>INSERT INTO TabloAdi ADD SütunAdi</code>"],
        "Mevcut tabloya sütun veya kısıtlama eklemek için ALTER TABLE ... ADD komutu kullanılır."
    ),
    make_q(
        "Mevcut bir tablodan bir sütunu tamamen kaldırmak için hangi komut kullanılır?",
        "<code>ALTER TABLE TabloAdi DROP COLUMN SütunAdi</code>",
        ["<code>DELETE COLUMN SütunAdi FROM TabloAdi</code>", "<code>REMOVE SütunAdi FROM TabloAdi</code>", "<code>ALTER TABLE TabloAdi TRUNCATE COLUMN SütunAdi</code>", "<code>DROP SütunAdi ON TabloAdi</code>"],
        "Tablodan sütun silmek için ALTER TABLE ... DROP COLUMN kullanılır."
    ),
    make_q(
        "Bir tabloyu veritabanından şeması, verileri ve kısıtlamalarıyla birlikte tamamen silmek için hangi komut kullanılır?",
        "<code>DROP TABLE TabloAdi</code>",
        ["<code>DELETE TABLE TabloAdi</code>", "<code>TRUNCATE TABLE TabloAdi</code>", "<code>REMOVE TABLE TabloAdi</code>", "<code>CLEAR TABLE TabloAdi</code>"],
        "DROP TABLE tablo yapısını ve tüm verilerini fiziksel olarak tamamen siler. DELETE ise sadece satırları siler."
    ),
    make_q(
        "<code>TRUNCATE TABLE TabloAdi</code> komutu ile <code>DELETE FROM TabloAdi</code> komutu arasındaki fark nedir?",
        "TRUNCATE tüm satırları loglamayı minimum tutarak çok hızlı siler, identity sayacını sıfırlar ve WHERE almaz.",
        ["TRUNCATE tablo yapısını silerken, DELETE tablo yapısını korur.", "TRUNCATE satır satır silme yapar ve her satır için trigger tetikler.", "TRUNCATE yalnızca yabancı anahtara sahip tablolarda çalışır.", "İki komut arasında hiçbir performans veya yapısal fark yoktur."],
        "TRUNCATE DDL işlemidir: Sayfaları serbest bırakarak hızlı siler, identity'yi sıfırlar, WHERE almaz ve DML trigger tetiklemez."
    ),
    make_q(
        "<code>CHAR(10)</code> ile <code>VARCHAR(10)</code> veri tipleri arasındaki temel fark nedir?",
        "CHAR(10) girilen metin kısa olsa bile daima 10 karakterlik sabit yer kaplar; VARCHAR(10) ise metnin uzunluğu kadar değişken yer kaplar.",
        ["CHAR(10) yalnızca sayı saklayabilirken, VARCHAR(10) metin saklar.", "CHAR(10) Unicode desteklerken, VARCHAR(10) Unicode desteklemez.", "CHAR(10) maksimum 10 bayt, VARCHAR(10) ise sınırsız bayt tutar.", "CHAR(10) diskte saklanırken, VARCHAR(10) yalnızca RAM'de saklanır."],
        "CHAR sabit uzunlukludur (kısa metinlerde boşlukla tamamlar), VARCHAR ise değişken uzunlukludur (tasarrufludur)."
    ),
    make_q(
        "SQL Server'da <code>NVARCHAR(50)</code> veri tipindeki 'N' harfi neyi ifade eder?",
        "Unicode (National Character Set - UTF-16 / Çoklu dil) desteğini ve karakter başına 2 bayt yer ayrılacağını",
        ["Sütunun NULL değer kabul etmeyeceğini (Not Null)", "Sütunun yalnızca negatif sayılar tutabileceğini (Negative)", "Sütunun otomatik sayısal sayaç olduğunu (Number)", "Sütunun ağ üzerinden şifreli iletileceğini (Network)"],
        "NVARCHAR / NCHAR başındaki N harfi 'National' (Unicode) standardını temsil eder; Türkçe gibi özel karakterleri destekler."
    ),
    make_q(
        "<code>DECIMAL(10, 2)</code> (veya <code>NUMERIC(10, 2)</code>) veri tipi ne tür bir sayı saklar?",
        "Toplam 10 basamaklı ve bunun 2 basamağı virgülden sonra (ondalıklı) olan kesin sayıları (Örn: Para tutarları)",
        ["10 ile 2 arasında değişen rastgele tam sayıları", "Virgülden önce 10, virgülden sonra 2 basamak olmak üzere toplam 12 basamaklı sayıları", "Sadece 2 basamaklı negatif sayıları", "10 üzeri 2 şeklinde üslü sayıları"],
        "DECIMAL(p, s): p (precision) toplam basamak sayısı, s (scale) virgülden sonraki basamak sayısıdır."
    ),
    make_q(
        "Veritabanında çok büyük boyutlu görseller, PDF belgeleri veya ses dosyaları saklamak için hangi veri tipi uygundur?",
        "BLOB (Binary Large Object) / VARBINARY(MAX)",
        ["VARCHAR(50)", "DECIMAL(18, 4)", "DATETIME2", "SMALLINT"],
        "BLOB (Binary Large Object) ikili büyük nesneleri (resim, dosya vb.) saklamak için tasarlanmıştır."
    ),
    make_q(
        "SQL standardında <code>CREATE DOMAIN CinsiyetType AS CHAR(1) DEFAULT 'E' CHECK (VALUE IN ('E', 'K'))</code> komutu ne yapar?",
        "Veritabanında kendi kuralı ve varsayılan değeri olan yeniden kullanılabilir özel bir alan/etki alanı (Domain) tanımlar.",
        ["CinsiyetType adında yeni bir tablo oluşturur.", "Mevcut tüm tablolara CinsiyetType sütununu otomatik ekler.", "Kullanıcıların cinsiyet verilerine erişimini kısıtlar.", "Birincil anahtar kısıtlaması tanımlar."],
        "CREATE DOMAIN belirli kurallara ve kısıtlara sahip kullanıcı tanımlı bir etki alanı (domain) tipi oluşturur."
    ),
    make_q(
        "Veritabanı Görünümleri (VIEW) ile ilgili aşağıdaki ifadelerden hangisi DOĞRUDUR?",
        "Görünüm sanal/türetilmiş bir tablodur; fiziksel olarak veri saklamaz, sorgusu saklanır.",
        ["Görünümler fiziksel olarak diskte bağımsız bir tablo kopyası oluşturur.", "Görünümlere asla SELECT sorgusu yazılamaz.", "Görünüm oluşturulduktan sonra temel tablo silinse de görünüm çalışmaya devam eder.", "Görünümler parametre alarak fonksiyon gibi çağrılabilir."],
        "VIEW sanal bir tablodur, diske veri kopyalamaz; çağrıldığında arka plandaki SELECT sorgusunu çalıştırır."
    ),
    make_q(
        "Görünüm (VIEW) kullanımının temel amaçları arasında hangisi YER ALMAZ?",
        "Veritabanının disk boyutunu fiziksel olarak iki katına çıkarmak",
        ["Karmaşık ve uzun JOIN sorgularını basitleştirmek", "Kullanıcılara yalnızca görmeye yetkili oldukları sütunları/satırları sunarak güvenlik sağlamak", "Farklı kullanıcı gruplarına verileri özelleştirilmiş formatlarda göstermek", "Uygulama kodunu veritabanı şemasındaki değişikliklerden izole etmek (Mantıksal Veri Bağımsızlığı)"],
        "View disk boyutu artırmaz; güvenlik, basitleştirme ve veri bağımsızlığı için kullanılır."
    ),
    make_q(
        "Bir görünüm tanımında <code>WITH CHECK OPTION</code> ifadesi kullanıldığında ne sağlanır?",
        "Görünüm üzerinden yapılan INSERT ve UPDATE işlemlerinin, görünümün WHERE koşuluna uymasını zorunlu kılar.",
        ["Görünümün yalnızca sistem yöneticisi (sa) tarafından okunabilmesini sağlar.", "Görünümdeki tüm sütunlara otomatik NOT NULL kısıtlaması ekler.", "Görünümün her gece otomatik olarak yedeklenmesini sağlar.", "Görünümün fiziksel bir tabloya dönüştürülmesini sağlar."],
        "WITH CHECK OPTION, view üzerinden eklenen/güncellenen verilerin view filtresi dışına çıkmasını engeller."
    ),
    make_q(
        "Aşağıdaki görünümlerden (VIEW) hangisi doğrudan <code>UPDATE</code> veya <code>INSERT</code> ile GÜNCELLENEMEZ?",
        "<code>GROUP BY</code>, toplama fonksiyonu (SUM, AVG) veya <code>DISTINCT</code> içeren görünümler",
        ["Tek bir tablodan basitçe birkaç sütun seçen görünümler", "WHERE koşuluyla tek bir tablodan filtreleme yapan basit görünümler", "Tüm birincil anahtarları içeren yatay görünümler", "Sadece metin sütunlarını listeleyen görünümler"],
        "Birden çok tablodan türeyen, gruplama (GROUP BY), toplama (SUM/AVG) veya DISTINCT içeren view'ler doğrudan güncellenemez."
    ),
    make_q(
        "Veritabanında bir sütuna <code>INDEX</code> (İndeks) oluşturmanın temel amacı ve olası maliyeti nedir?",
        "Veri arama ve sorgulama işlemlerini hızlandırır; ancak INSERT/UPDATE/DELETE işlemlerinde ek maliyet oluşturur.",
        ["Tabloyu şifreleyerek güvenliğini sağlar; hiçbir performans etkisi olmaz.", "Tablodaki tüm satırları otomatik siler; disk alanını sıfırlar.", "Sorguları yavaşlatır; ancak disk alanından %50 tasarruf sağlar.", "Yalnızca Primary Key sütunlarına uygulanabilir; diğer sütunlarda hata verir."],
        "İndeks hızlı arama/erişim yapısıdır (kitap fihristi gibi); okumayı hızlandırır, yazma işlemlerinde indeks güncellendiği için ek maliyet getirir."
    ),
    make_q(
        "SQL Server'da <code>Clustered Index</code> (Kümelenmiş İndeks) ile ilgili hangisi DOĞRUDUR?",
        "Tablodaki veri satırlarını indeks anahtarına göre fiziksel olarak diskte sıralar; bu nedenle bir tabloda yalnızca 1 adet olabilir.",
        ["Bir tabloda en fazla 249 adet Clustered Index tanımlanabilir.", "Verileri diskin rastgele bloklarına yazar ve fiziksel sıraya dokunmaz.", "Clustered Index tanımlandığında Primary Key kısıtlaması geçersiz kılınır.", "Yalnızca metin (VARCHAR) veri tipindeki sütunlarda tanımlanabilir."],
        "Clustered Index tablonun diskteki fiziksel dizilişini belirler; bir tablonun diskte tek bir fiziksel sırası olabileceğinden tabloda yalnız 1 Clustered Index olur."
    ),
    make_q(
        "SQL Server'da bir tabloya <code>PRIMARY KEY</code> kısıtlaması eklendiğinde varsayılan olarak hangi indeks türü otomatik oluşturulur?",
        "Benzersiz Kümelenmiş İndeks (Unique Clustered Index)",
        ["Kümelenmemiş İndeks (Non-Clustered Index)", "Tam Metin İndeksi (Full-Text Index)", "Mekansal İndeks (Spatial Index)", "XML İndeksi"],
        "SQL Server'da Primary Key tanımlandığında varsayılan olarak o sütun/sütunlar üzerinde otomatik Unique Clustered Index oluşturulur."
    ),
    make_q(
        "<code>Non-Clustered Index</code> (Kümelenmemiş İndeks) için hangisi DOĞRUDUR?",
        "Verinin fiziksel sırasını değiştirmez; arama anahtarı ve verinin fiziksel konumuna işaret eden göstericilerden (pointer) oluşan ayrı bir yapıdır.",
        ["Bir tabloda en fazla 1 adet Non-Clustered Index tanımlanabilir.", "Tablonun disk üzerindeki tüm verilerini fiziksel olarak alfabetik sıraya dizer.", "INSERT işlemlerini hızlandırırken SELECT sorgularını yavaşlatır.", "Tanımlandığı sütunda NULL değer bulunmasını kesinlikle engeller."],
        "Non-Clustered Index kitabın arkasındaki fihrist gibidir: Ayrı bir B-Tree yapısında anahtarları ve satır adreslerini tutar; birden çok olabilir."
    ),
    make_q(
        "<code>GRANT SELECT, UPDATE(maas) ON Staff TO MuhasebeUser</code> komutunun işlevi nedir?",
        "MuhasebeUser kullanıcısına Staff tablosunda okuma ve yalnızca maas sütununu güncelleme yetkisi verir.",
        ["MuhasebeUser kullanıcısının Staff tablosundaki tüm yetkilerini iptal eder.", "MuhasebeUser adına yeni bir Staff tablosu kopyalar.", "Staff tablosundaki tüm çalışanların maaşını MuhasebeUser yapar.", "MuhasebeUser kullanıcısını veritabanından tamamen siler."],
        "GRANT DCL komutudur; belirtilen kullanıcıya belirli nesneler ve sütunlar üzerinde yetkilendirme sağlar."
    ),
    make_q(
        "<code>REVOKE SELECT ON Staff FROM PUBLIC</code> komutu ne yapar?",
        "Staff tablosunda tüm kullanıcılara (PUBLIC) daha önce verilmiş olan SELECT yetkisini geri alır.",
        ["PUBLIC adlı kullanıcıya Staff tablosunu silme yetkisi verir.", "Staff tablosunu tüm internet erişimine açar.", "PUBLIC kullanıcısının şifresini sıfırlar.", "Staff tablosundaki tüm verileri şifreler."],
        "REVOKE DCL komutudur; daha önce verilmiş ayrıcalıkları geri alır (iptal eder)."
    ),
    make_q(
        "Veritabanı işlemlerinde <code>Transaction</code> (İşlem Akışı) kavramı neyi garanti eder?",
        "Birbiriyle bağlantılı işlemler kümesinin ya tamamen başarılı olmasını (COMMIT) ya da hata durumunda tamamen geri alınmasını (ROLLBACK)",
        ["Sorguların daima tek bir satır döndürmesini", "Veritabanının yalnızca tek bir kullanıcı tarafından kullanılmasını", "Her tablonun diske şifreli olarak kaydedilmesini", "İndekslerin sorgu anında otomatik silinmesini"],
        "Transaction ACID prensibine göre mantıksal bir iş birimidir: 'Ya hep ya hiç' (Atomicity) kuralıyla çalışır."
    ),
    make_q(
        "Transaction yönetiminde <code>COMMIT</code> komutu ne işe yarar?",
        "Transaction içinde yapılan tüm ekleme, güncelleme ve silme değişikliklerini kalıcı olarak veritabanına kaydeder.",
        ["Transaction içindeki tüm işlemleri iptal edip değişiklikleri geri alır.", "Transaction'ı geçici olarak duraklatıp beklemeye alır.", "Veritabanı bağlantısını tamamen sonlandırır.", "Tablodaki tüm indeksleri yeniden derler."],
        "COMMIT işlemi onaylar ve tüm veritabanı değişikliklerini kalıcılaştırır."
    ),
    make_q(
        "Transaction yönetiminde <code>ROLLBACK</code> komutu ne işe yarar?",
        "Hata durumunda transaction başlangıcına veya belirtilen SAVEPOINT noktasına kadar olan tüm değişiklikleri geri alarak veritabanını eski haline döndürür.",
        ["Değişiklikleri diske kalıcı olarak yazar.", "Veritabanındaki tüm tabloları sıfırlar.", "Sadece SELECT sorgularını durdurur.", "Sunucuyu yeniden başlatır."],
        "ROLLBACK transaction içindeki başarısız veya iptal edilen işlemleri geri alır."
    ),
    make_q(
        "<code>SAVEPOINT Nokta1</code> (veya T-SQL'de <code>SAVE TRANSACTION Nokta1</code>) ifadesi ne sağlar?",
        "Transaction içinde bir ara kontrol noktası oluşturarak gerektiğinde tüm işlemi değil yalnızca bu noktaya kadar olan kısmı geri almayı sağlar.",
        ["Veritabanının tam bir yedek kopyasını harici diske kaydeder.", "Tablonun birincil anahtarını o noktada dondurur.", "Tüm açık transaction'ları anında COMMIT eder.", "Transaction içindeki hataları görmezden gelerek devam eder."],
        "SAVEPOINT ara kurtarma noktasıdır; ROLLBACK TO SAVEPOINT ile sadece o noktadan sonraki adımlar geri alınabilir."
    ),
    make_q(
        "ACID prensiplerinden 'A' (Atomicity - Bölünemezlik) neyi ifade eder?",
        "Transaction içindeki işlemlerin bölünemez tek bir bütün olması; bir adım başarısız olursa tüm transaction'ın iptal edilmesi",
        ["Veritabanının atomik saatle senkronize çalışmasını", "Her tabloda yalnızca tek bir atomik veri tipinin kullanılabilmesini", "Transaction'ların sırayla tek işlemci çekirdeğinde çalışmasını", "Veritabanının atomik düzeyde şifrelenmesini"],
        "Atomicity (Bölünemezlik): Ya tüm adımlar başarılı olur ya da hiçbiri gerçekleşmemiş gibi geri alınır."
    ),
    make_q(
        "ACID prensiplerinden 'I' (Isolation - Yalıtım) neyi ifade eder?",
        "Eş zamanlı çalışan transaction'ların birbirlerinin henüz onaylanmamış ara durumlarını görmemesi ve birbirlerini etkilememesi",
        ["Veritabanı sunucusunun internet bağlantısından izole edilmesini", "Tabloların disk üzerinde ayrı ayrı sektörlere yazılmasını", "Kullanıcıların yalnızca tek bir IP adresinden bağlanabilmesini", "Tüm Foreign Key bağlantılarının izole edilerek koparılmasını"],
        "Isolation (Yalıtım): Eşzamanlı işlemler birbirinden bağımsız çalışır, ara durumlar dışarıya sızmaz."
    ),
    make_q(
        "<code>ALTER TABLE Staff ADD CONSTRAINT CK_Maas CHECK (salary >= 5000)</code> komutu çalıştırıldığında tabloda halihazırda 3000 maaşlı bir kayıt varsa ne olur?",
        "Kısıtlama ekleme işlemi başarısız olur ve veritabanı motoru kural ihlali hatası verir (WITH NOCHECK kullanılmadıkça).",
        ["Mevcut 3000 maaşlı personellerin maaşı otomatik olarak 5000 yapılır.", "Mevcut 3000 maaşlı personeller tablodan otomatik olarak silinir.", "Kısıtlama sadece yeni eklenecek kayıtlara uygulanır, eskiler kontrol edilmez.", "Tablo kilitlenir ve veritabanı salt okunur moda geçer."],
        "Mevcut veriler yeni CHECK kuralına uymuyorsa ALTER TABLE işlemi hata verir ve kısıt eklenemez."
    ),
    make_q(
        "Birincil anahtarı <code>(ogrenci_no, ders_kod)</code> olan bir ilişkide <code>ogrenci_no</code> sütununa tek başına NULL atanmak istenirse ne olur?",
        "Bileşik birincil anahtarın parçası olduğu için Varlık Bütünlüğü ihlal edilir ve işlem reddedilir.",
        ["ders_kod alanı dolu olduğu sürece ogrenci_no alanına NULL atanabilir.", "NULL değer otomatik olarak 0 ile değiştirilir ve kabul edilir.", "Sistem ogrenci_no için otomatik yeni bir numara üretir.", "Tablo silinir ve yeniden oluşturulur."],
        "Bileşik birincil anahtarı oluşturan hiçbir sütun NULL değer alamaz (Varlık Bütünlüğü kuralı)."
    ),
    make_q(
        "Aşağıdakilerden hangisi bir 'Aday Anahtar'ın (Candidate Key) zorunlu özelliklerinden biri DEĞİLDİR?",
        "Mutlaka sayısal (INTEGER) bir veri tipinde tanımlanmış olması",
        ["İlişkideki her bir satırı benzersiz (unique) olarak tanımlaması", "Asla NULL değer içerememesi", "Minimum süper anahtar olması (gereksiz hiçbir sütun içermemesi)", "Kendisini oluşturan hiçbir alt kümenin tek başına anahtar özelliği taşımaması"],
        "Aday anahtar metin, sayısal veya bileşik olabilir; veri tipinin mutlaka INT olması gibi bir zorunluluk yoktur."
    )
]

# =========================================================================
# EXAM 4: T-SQL Programlama, Değişkenler, Karar Yapıları, Döngüler & Global Değişkenler
# (Kaynaklar: T-SQL_1, veritabanıfinal, saklıYordam_SP)
# =========================================================================
random.seed(104)
e4 = [
    make_q(
        "T-SQL'de değişken tanımlamak için hangi anahtar kelime kullanılır ve değişken adları hangi sembolle başlar?",
        "<code>DECLARE</code> anahtar kelimesi kullanılır ve değişken adları <code>@</code> sembolü ile başlar.",
        ["<code>DIM</code> kullanılır ve değişken adları <code>$</code> sembolü ile başlar.", "<code>VAR</code> kullanılır ve değişken adları <code>#</code> sembolü ile başlar.", "<code>LET</code> kullanılır ve değişken adları <code>%</code> sembolü ile başlar.", "<code>NEW</code> kullanılır ve değişken adları <code>&</code> sembolü ile başlar."],
        "T-SQL'de yerel değişkenler DECLARE @degiskenAdi VeriTipi şeklinde tanımlanır."
    ),
    make_q(
        "Aşağıdaki T-SQL değişken tanımlamalarından hangisi sözdizimi açısından GEÇERLİDİR?",
        "<code>DECLARE @enPahaliUrun VARCHAR(200) = 'Klavye', @enYuksekFiyat MONEY = 500</code>",
        ["<code>DECLARE @enPahaliUrun AS VARCHAR(200) := 'Klavye'</code>", "<code>SET @enPahaliUrun VARCHAR(200) = 'Klavye'</code>", "<code>DIM @enPahaliUrun VARCHAR(200) = 'Klavye'</code>", "<code>DECLARE VARIABLE enPahaliUrun = 'Klavye'</code>"],
        "T-SQL'de tek bir DECLARE altında virgülle ayrılarak birden çok değişken tanımlanabilir ve başlangıç değeri atanabilir."
    ),
    make_q(
        "T-SQL'de <code>SET @degisken = deger</code> ile <code>SELECT @degisken = deger</code> arasındaki temel fark nedir?",
        "SET standart olarak tek değişkene değer atar; SELECT ise sorgu sonucundaki birden fazla sütun değerini aynı anda birden fazla değişkene atayabilir.",
        ["SET yalnızca sayılarda, SELECT ise metinlerde değer atar.", "SET değişkeni silerken, SELECT değişkeni oluşturur.", "SET disk üzerinde atama yapar, SELECT RAM'de atama yapar.", "İkisi arasında hiçbir davranış veya sözdizimi farkı yoktur."],
        "SELECT @a = col1, @b = col2 FROM Tablo ile tek sorguda birden çok değişkene atama yapılabilir; SET tek değişkene atama yapar."
    ),
    make_q(
        "T-SQL'de <code>SELECT @fiyat = listeFiyat FROM Urun</code> ifadesi çok sayıda satır döndürürse <code>@fiyat</code> değişkeninin son değeri ne olur?",
        "Sorgunun işlediği en son satırdaki listeFiyat değerini tutar.",
        ["Sorgudaki tüm listeFiyat değerlerinin toplamını tutar.", "Değişken otomatik olarak NULL değerine döner.", "T-SQL motoru derleme zamanında hata verir ve çalışmayı durdurur.", "İlk satırdaki listeFiyat değerini sabit olarak korur."],
        "SELECT atamasında sorgu çok satır dönerse hata vermez; değişken üzerinde her satır için atama tekrarlanır ve son satırın değeri kalır."
    ),
    make_q(
        "Aşağıdaki T-SQL kodunun ekran çıktısı nedir?\n<code>DECLARE @x INT = 5;\nSET @x += 7;\nSET @x -= 2;\nSELECT @x;</code>",
        "10",
        ["12", "14", "5", "8"],
        "@x = 5 -> += 7 ile 12 -> -= 2 ile 10 olur."
    ),
    make_q(
        "T-SQL'de <code>DECLARE @sayac INT = 20; SET @sayac /= 4; SET @sayac %= 3; SELECT @sayac;</code> kodunun sonucu kaçtır?",
        "2",
        ["5", "0", "1", "3"],
        "@sayac = 20 -> /= 4 ile 5 -> %= 3 (5 mod 3) ile 2 olur."
    ),
    make_q(
        "T-SQL'de <code>@@</code> (çift et) işaretiyle başlayan değişkenler neyi ifade eder?",
        "Sistem (Global) durum değişkenlerini (Örn: @@VERSION, @@ROWCOUNT, @@ERROR)",
        ["Kullanıcı tanımlı geçici tabloları", "Yalnızca şifrelenmiş özel değişkenleri", "Başka sunucudan çağrılan uzak fonksiyonları", "Transaction log dosyası işaretçilerini"],
        "@@ ile başlayan değişkenler SQL Server sisteminin sağladığı global/sistem durum değişkenleridir."
    ),
    make_q(
        "T-SQL'de <code>@@ROWCOUNT</code> global değişkeni neyi döndürür?",
        "En son çalıştırılan SQL ifadesinden etkilenen veya okunan satır sayısını",
        ["Veritabanındaki toplam tablo sayısını", "Mevcut tablodaki toplam sütun sayısını", "Cursor içinde kalan okunmamış kayıt sayısını", "Veritabanına o an bağlı olan aktif kullanıcı sayısını"],
        "@@ROWCOUNT son ifadenin etkilediği (satır sayısı) bilgisini verir."
    ),
    make_q(
        "T-SQL'de <code>@@FETCH_STATUS</code> değişkeninin <code>0</code> değerini üretmesi ne anlama gelir?",
        "Son FETCH komutunun başarıyla bir satır okuduğunu",
        ["Cursor'ın sonuna gelindiğini ve okunacak satır kalmadığını", "Cursor okuması sırasında kritik bir hata oluştuğunu", "Cursor'ın henüz OPEN edilmediğini", "Okunan satırın tüm sütunlarının NULL olduğunu"],
        "@@FETCH_STATUS: 0 = başarılı, -1 = bitti/başarısız, -2 = satır kayıp/yok."
    ),
    make_q(
        "SQL Server'da <code>GO</code> komutu ile ilgili aşağıdakilerden hangisi DOĞRUDUR?",
        "Bir T-SQL komutu değildir; Management Studio gibi istemci araçların sorgu yığınını (batch) sunucuya gönderme ayırıcısıdır.",
        ["T-SQL dilinin standart bir döngü başlatma komutudur.", "Veritabanını hemen kapatıp yeniden başlatan sunucu komutudur.", "Yalnızca SELECT sorgularını hızlandırmak için kullanılan bir ipucudur (hint).", "Transaction'ları otomatik olarak COMMIT eden bir DDL komutudur."],
        "GO bir T-SQL komutu değil, istemci araçları (SSMS, sqlcmd) tarafından yorumlanan batch ayırıcısıdır."
    ),
    make_q(
        "Bir sorgu yığınında (batch) <code>CREATE PROCEDURE</code>, <code>CREATE VIEW</code> veya <code>CREATE TRIGGER</code> ifadeleri kullanılırken kural nedir?",
        "Bu ifadelerin her biri kendi yığınının (batch) ilk komutu olmalıdır; aralarında <code>GO</code> kullanılmalıdır.",
        ["Aynı yığın içinde sınırsız sayıda CREATE VIEW ve PROCEDURE alt alta yazılabilir.", "Bu ifadeler asla GO kullanılmadan tek satırda yazılmalıdır.", "CREATE PROCEDURE ifadesinden önce mutlaka bir SELECT sorgusu bulunmalıdır.", "Bu ifadeler yalnızca transaction blokları içinde çalıştırılabilir."],
        "CREATE PROC/VIEW/TRIGGER yığındaki (batch) ilk ifade olmak zorundadır; bu nedenle öncelerinde ve sonralarında GO kullanılır."
    ),
    make_q(
        "T-SQL'de <code>PRINT</code> komutunun temel amacı nedir?",
        "İstemciye (Messages sekmesine) metin tabanlı bilgilendirme veya hata ayıklama mesajı yazdırmak",
        ["Veritabanındaki tabloyu fiziksel kağıt yazıcısına göndermek", "Tabloya otomatik olarak yeni bir satır eklemek", "Değişkenin değerini kalıcı olarak diske kaydetmek", "Sorgu sonucunu Grid görünümünde tablo olarak listelemek"],
        "PRINT komutu hata ayıklama (debug) ve kullanıcıya metin mesajı iletme amacıyla kullanılır."
    ),
    make_q(
        "Aşağıdaki T-SQL kod bloğu çalıştırıldığında ne yazdırılır?\n<code>DECLARE @x INT = 15;\nIF @x > 20\n    PRINT 'A';\nELSE IF @x > 10\n    PRINT 'B';\nELSE\n    PRINT 'C';</code>",
        "'B'",
        ["'A'", "'C'", "'A' ve 'B'", "Hiçbir şey yazdırmaz"],
        "@x = 15. İlk koşul (@x > 20) yanlış. İkinci koşul (@x > 10) doğru olduğu için 'B' yazdırılır."
    ),
    make_q(
        "T-SQL'de <code>IF</code> veya <code>ELSE</code> bloğunun altında birden fazla kod satırı çalıştırılmak isteniyorsa hangi yapı zorunludur?",
        "<code>BEGIN ... END</code> blok yapısı",
        ["<code>{ ... }</code> küme parantezleri", "<code>( ... )</code> normal parantezler", "<code>START ... FINISH</code> yapısı", "<code>DO ... LOOP</code> yapısı"],
        "T-SQL'de çok satırlı bloklar BEGIN ... END arasına alınmak zorundadır (C/Java'daki { } gibi)."
    ),
    make_q(
        "Aşağıdaki T-SQL kodunun çıktısı nedir?\n<code>IF NOT EXISTS (SELECT * FROM Staff WHERE salary > 100000)\n    PRINT 'Çok yüksek maaşlı yok';\nELSE\n    PRINT 'Var';</code> (Not: Staff tablosunda maksimum maaş 30000'dir)",
        "'Çok yüksek maaşlı yok'",
        ["'Var'", "NULL", "Sözdizimi hatası", "0"],
        "100000'den yüksek maaşlı personel olmadığı için alt sorgu boş döner; NOT EXISTS doğru olur ve 'Çok yüksek maaşlı yok' yazar."
    ),
    make_q(
        "T-SQL'de <code>CASE</code> ifadesi ile ilgili aşağıdakilerden hangisi DOĞRUDUR?",
        "SELECT listesinde, WHERE yan tümcesinde, ORDER BY'da ve GROUP BY'da koşullu değer üretmek için kullanılabilen bir ifadedir.",
        ["Yalnızca stored procedure'lerin içinde kullanılabilir; normal SELECT'te kullanılamaz.", "Tablodan satır silmek için kullanılan bir DML komutudur.", "Mutlaka en az 5 adet WHEN şartı içermek zorundadır.", "CASE bloğunun sonunda END anahtar kelimesi opsiyoneldir."],
        "CASE SQL ifadelerinde koşula göre değer dönüştüren çok esnek bir yapıdır ve END ile kapatılır."
    ),
    make_q(
        "Aşağıdaki sorguda <code>CASE</code> ifadesinin görevi nedir?\n<code>SELECT fName, salary, CASE WHEN salary >= 20000 THEN 'Yüksek' ELSE 'Normal' END AS Seviye FROM Staff</code>",
        "Maaşı 20000 ve üzeri olanlara 'Yüksek', diğerlerine 'Normal' etiketli Seviye sütunu üretmek",
        ["Maaşı 20000'den az olan personelleri tablodan silmek", "Maaşları 20000 TL olarak güncellemek", "Personelleri Seviye isimli iki farklı tabloya paylaştırmak", "Yalnızca maaşı yüksek olan personelleri filtrelemek"],
        "CASE ifadesi her satır için maaşa bakarak 'Seviye' adında hesaplanmış sütun değeri üretir."
    ),
    make_q(
        "Aşağıdaki <code>WHILE</code> döngüsü kaç kez çalışır ve ekrana ne yazar?\n<code>DECLARE @i INT = 1;\nWHILE @i <= 3\nBEGIN\n    PRINT @i;\n    SET @i += 1;\nEND;</code>",
        "3 kez çalışır ve sırasıyla 1, 2, 3 yazdırır.",
        ["Sonsuz döngüye girer.", "4 kez çalışır ve 1, 2, 3, 4 yazdırır.", "Hiç çalışmaz.", "Yalnızca 3 yazdırır."],
        "@i=1 (yazar, @i=2), @i=2 (yazar, @i=3), @i=3 (yazar, @i=4), @i=4 olunca döngü biter. Çıktı: 1, 2, 3."
    ),
    make_q(
        "T-SQL'de <code>WHILE</code> döngüsünde <code>BREAK</code> komutunun görevi nedir?",
        "Döngü koşuluna bakılmaksızın döngüyü anında sonlandırır ve <code>END</code>'den sonraki satıra geçer.",
        ["Döngünün bir sonraki adımına (başına) atlar.", "Sunucu oturumunu tamamen kapatır.", "Transaction'ı geri alarak (ROLLBACK) sistemi durdurur.", "Değişkenin değerini sıfırlar."],
        "BREAK döngüyü tamamen kırar ve döngü dışına çıkar."
    ),
    make_q(
        "T-SQL'de <code>WHILE</code> döngüsünde <code>CONTINUE</code> komutunun görevi nedir?",
        "Döngü gövdesinde kendisinden sonraki satırları atlayarak doğrudan döngü başına (şart kontrolüne) döner.",
        ["Döngüden tamamen çıkar ve işlemi bitirir.", "Döngüyü duraklatıp kullanıcıdan girdi bekler.", "Döngüdeki değişkeni 1 artırır.", "Tüm transaction loglarını diske yazar."],
        "CONTINUE döngünün o anki iterasyonunu sonlandırıp bir sonraki iterasyon için döngü başına atlar."
    ),
    make_q(
        "Aşağıdaki T-SQL kodunun ekran çıktısı nedir?\n<code>DECLARE @s INT = 0;\nWHILE @s < 5\nBEGIN\n    SET @s += 1;\n    IF @s = 3 CONTINUE;\n    PRINT @s;\nEND;</code>",
        "1, 2, 4, 5 (3 atlanır)",
        ["1, 2 (3'te durur)", "1, 2, 3, 4, 5", "3, 4, 5", "Yalnızca 5"],
        "@s=3 olduğunda CONTINUE çalıştığı için PRINT @s çalıştırılmadan döngü başına dönülür; 3 hariç hepsi basılır."
    ),
    make_q(
        "Aşağıdaki T-SQL kodunun ekran çıktısı nedir?\n<code>DECLARE @s INT = 0;\nWHILE @s < 10\nBEGIN\n    SET @s += 1;\n    IF @s = 4 BREAK;\n    PRINT @s;\nEND;</code>",
        "1, 2, 3",
        ["1, 2, 3, 4", "4, 5, 6, 7, 8, 9, 10", "1, 2, 3, 5, 6, 7, 8, 9, 10", "Hiçbir şey"],
        "@s=1,2,3 yazdırılır. @s=4 olduğunda BREAK komutu döngüyü sonlandırır. Çıktı: 1, 2, 3."
    ),
    make_q(
        "T-SQL'de <code>CAST(123.45 AS INT)</code> ifadesinin ürettiği sonuç nedir?",
        "123 (Ondalık kısmı atarak tam sayıya dönüştürür)",
        ["124 (Yukarı yuvarlar)", "123.45", "Sözdizimi hatası", "NULL"],
        "CAST(... AS INT) ondalık kısmı budayarak (truncate) tam sayı değerini (123) verir."
    ),
    make_q(
        "T-SQL'de <code>CONVERT(VARCHAR(10), GETDATE(), 104)</code> ifadesindeki '104' stil parametresi tarihi hangi formatta üretir?",
        "dd.mm.yyyy (Alman / Türkiye standardı nokta ile ayrılmış tarih formatı)",
        ["yyyy-mm-dd (ISO standardı)", "mm/dd/yyyy (ABD standardı)", "dd/mm/yyyy (İngiliz standardı)", "yyyy.mm.dd"],
        "SQL Server'da CONVERT ile 104 stil kodu dd.mm.yyyy formatını üretir."
    ),
    make_q(
        "T-SQL'de bit düzeyinde <code>NOT</code> operatörü olarak hangi sembol kullanılır?",
        "<code>~</code> (Tilde sembolü)",
        ["<code>!</code> (Ünlem)", "<code>NOT</code>", "<code>^</code>", "<code>#</code>"],
        "T-SQL bit düzeyinde operatörler: ~ (Bitwise NOT), & (Bitwise AND), | (Bitwise OR), ^ (Bitwise XOR)."
    ),
    make_q(
        "Aşağıdaki kodun çıktısı nedir?\n<code>DECLARE @a BIT = 1;\nSELECT ~@a;</code>",
        "0 (1'in bit düzeyinde değili)",
        ["1", "NULL", "-1", "Hata"],
        "Bit seviyesinde 1 değerinin tersi (~1) 0'dır."
    ),
    make_q(
        "T-SQL'de <code>SET NOCOUNT ON</code> komutunun görevi nedir?",
        "Çalıştırılan SQL ifadelerinden sonra dönen '(1 satır etkilendi)' mesajlarının istemciye iletilmesini engelleyerek performansı artırmak",
        ["Tablodaki satır sayısının sıfırlanmasını sağlamak", "COUNT(*) fonksiyonunun çalışmasını engellemek", "Tüm SELECT sorgularını durdurmak", "Veritabanına yeni kayıt eklenmesini yasaklamak"],
        "SET NOCOUNT ON mesaj trafiğini azaltarak stored procedure ve trigger'larda ağ ve CPU performansını optimize eder."
    ),
    make_q(
        "T-SQL'de <code>WAITFOR DELAY '00:00:05'</code> ifadesi ne yapar?",
        "Kodun yürütülmesini 5 saniye boyunca duraklatır (bekletir).",
        ["5 saniye içinde cevap vermeyen sorguyu iptal eder.", "5 saniye sonra veritabanını kapatır.", "Tüm tabloları 5 saniyeliğine kilitler.", "Sorguyu 5 kez üst üste çalıştırır."],
        "WAITFOR DELAY belirtilen süre kadar (hh:mm:ss) işletimi bekletir."
    ),
    make_q(
        "T-SQL'de <code>TRY...CATCH</code> hata yakalama bloğu ile ilgili hangisi DOĞRUDUR?",
        "BEGIN TRY içinde bir hata oluştuğunda akış anında BEGIN CATCH bloğuna geçer ve ERROR_MESSAGE() ile hata okunabilir.",
        ["CATCH bloğu çalıştıktan sonra kod TRY bloğunun kaldığı satırdan devam eder.", "TRY...CATCH blokları yalnızca SELECT ifadelerinde çalışır.", "CATCH bloğu zorunlu değildir, sadece TRY yazılabilir.", "Tüm hatalar otomatik olarak COMMIT edilir."],
        "TRY bloğunda hata olduğunda yürütme CATCH bloğuna atlar; ERROR_MESSAGE(), ERROR_NUMBER() gibi fonksiyonlarla hata yönetilir."
    ),
    make_q(
        "T-SQL'de <code>@@ERROR</code> global değişkeni ne zaman <code>0</code> değerini döndürür?",
        "En son çalıştırılan T-SQL ifadesi hatasız ve başarılı bir şekilde tamamlandığında",
        ["Veritabanında hiçbir tablo bulunmadığında", "Kullanıcı sistem yöneticisi olduğunda", "Son sorgu boş küme döndürdüğünde", "Sunucu yeniden başlatıldığında"],
        "@@ERROR = 0 işlemin hatasız bittiğini gösterir; 0'dan farklıysa oluşan son hatanın numarasını tutar."
    ),
    make_q(
        "T-SQL'de <code>@@IDENTITY</code> global değişkeni neyi döndürür?",
        "Mevcut oturumda herhangi bir tabloda en son üretilen otomatik artan IDENTITY değerini",
        ["O an oturum açmış olan kullanıcının ID numarasını", "Sunucunun benzersiz lisans numarasını", "Veritabanındaki toplam kullanıcı sayısını", "En son açılan transaction'ın ID numarasını"],
        "@@IDENTITY o oturumda en son üretilen identity değerini verir."
    ),
    make_q(
        "T-SQL'de <code>SCOPE_IDENTITY()</code> ile <code>@@IDENTITY</code> arasındaki fark nedir?",
        "SCOPE_IDENTITY() yalnızca mevcut kod kapsamında (scope) üretilen identity'yi döndürürken, @@IDENTITY trigger'ların ürettiği identity'leri de kapsar.",
        ["SCOPE_IDENTITY() yalnızca Oracle'da, @@IDENTITY ise SQL Server'da çalışır.", "SCOPE_IDENTITY() metin kimliklerini, @@IDENTITY sayısal kimlikleri döndürür.", "@@IDENTITY geriye hiçbir zaman değer döndürmez.", "İkisi arasında hiçbir fark yoktur."],
        "Trigger tetiklenirse @@IDENTITY trigger'ın eklediği tablonun identity'sini dönebilir; bu yüzden güvenli olan SCOPE_IDENTITY()'dir."
    ),
    make_q(
        "Aşağıdaki T-SQL kodunun çıktısı nedir?\n<code>DECLARE @ad VARCHAR(20) = 'Fatih';\nDECLARE @sonuc VARCHAR(30);\nSET @sonuc = 'Merhaba ' + ISNULL(@ad, 'Misafir');\nSELECT @sonuc;</code>",
        "'Merhaba Fatih'",
        ["'Merhaba Misafir'", "'Merhaba NULL'", "'Fatih'", "Hata verir"],
        "@ad = 'Fatih' olduğu için ISNULL(@ad, 'Misafir') -> 'Fatih' döner. Sonuç 'Merhaba Fatih' olur."
    ),
    make_q(
        "Yukarıdaki kodda <code>@ad</code> değişkenine <code>NULL</code> değeri atansaydı çıktı ne olurdu?",
        "'Merhaba Misafir'",
        ["'Merhaba '", "'NULL'", "NULL", "Hata verir"],
        "@ad NULL olursa ISNULL(@ad, 'Misafir') ikinci parametre olan 'Misafir'i döner; sonuç 'Merhaba Misafir' olur."
    ),
    make_q(
        "T-SQL'de <code>RAISERROR('Hatalı işlem yapıldı.', 16, 1);</code> komutunun işlevi nedir?",
        "Kullanıcı tanımlı bir hata mesajı fırlatır ve hata seviyesi 16 olduğu için CATCH bloğunu tetikler.",
        ["Sistem loglarını temizleyerek ekrana uyarı basar.", "Veritabanını güvenli modda yeniden başlatır.", "Tablodaki hatalı satırları otomatik olarak düzeltir.", "Sadece bilgilendirme mesajı basar, akışı etkilemez."],
        "RAISERROR kullanıcı tanımlı hata üretir; 11-19 arası severity seviyeleri TRY/CATCH'te CATCH bloğuna yönlendirir."
    ),
    make_q(
        "Aşağıdaki T-SQL ifadesinde hangi durum gerçekleşir?\n<code>DECLARE @x INT = 10, @y INT = 0;\nBEGIN TRY\n    SELECT @x / @y;\nEND TRY\nBEGIN CATCH\n    PRINT 'Sıfıra bölme hatası yakalandı';\nEND CATCH</code>",
        "Sıfıra bölme hatası TRY içinde oluşur, akış CATCH bloğuna atlar ve 'Sıfıra bölme hatası yakalandı' yazdırılır.",
        ["Sorgu 0 sonucunu ekrana yazdırır ve CATCH bloğu çalışmaz.", "SQL Server çöker ve oturum kapanır.", "Sorgu NULL döner ve hata oluşmaz.", "CATCH bloğu sözdizimi hatası verir."],
        "10 / 0 sıfıra bölme hatası (Divide by zero) üretir; TRY bloğu kesilip CATCH bloğu çalışır."
    ),
    make_q(
        "T-SQL'de geçici tablo (Temporary Table) tanımlamak için isim ön eki olarak ne kullanılır?",
        "Yerel geçici tablolar için <code>#TabloAdi</code>, genel (global) geçici tablolar için <code>##TabloAdi</code>",
        ["Yerel için <code>@TabloAdi</code>, genel için <code>$TabloAdi</code>", "Yerel için <code>_TabloAdi</code>, genel için <code>__TabloAdi</code>", "Yerel için <code>%TabloAdi</code>, genel için <code>%%TabloAdi</code>", "Yerel için <code>temp.TabloAdi</code>"],
        "#Tablo tek oturuma özel temp table, ##Tablo tüm oturumların görebildiği global temp table'dır."
    ),
    make_q(
        "T-SQL'de Tablo Değişkeni (Table Variable) nasıl tanımlanır?",
        "<code>DECLARE @TabloAdi TABLE (id INT, ad VARCHAR(50))</code>",
        ["<code>CREATE TABLE VARIABLE @TabloAdi (id INT)</code>", "<code>SET @TabloAdi = TABLE (id INT)</code>", "<code>NEW TABLE @TabloAdi (id INT)</code>", "<code>DIM @TabloAdi AS TABLE (id INT)</code>"],
        "Tablo değişkenleri DECLARE @degisken TABLE (kolon tanımları) şeklinde tanımlanır."
    ),
    make_q(
        "T-SQL'de tek satırlık açıklama (yorum) eklemek için hangi karakterler kullanılır?",
        "<code>--</code> (İki tire işareti)",
        ["<code>//</code> (İki eğik çizgi)", "<code>#</code> (Kare)", "<code>/*</code> (Yıldız)", "<code>REM</code> (Kelime)"],
        "T-SQL'de tek satırlık yorumlar -- ile, çok satırlı yorumlar /* ... */ ile yapılır."
    ),
    make_q(
        "Aşağıdaki T-SQL kodunun çıktısı nedir?\n<code>DECLARE @sayi INT = 100;\nIF @sayi BETWEEN 50 AND 150\n    PRINT 'Aralıkta';\nELSE\n    PRINT 'Dışında';</code>",
        "'Aralıkta'",
        ["'Dışında'", "'NULL'", "Sözdizimi hatası", "Hiçbir şey"],
        "100 sayısı 50 ile 150 arasında olduğu için IF koşulu doğrudur ve 'Aralıkta' yazar."
    )
]

print(f"Exam 3: {len(e3)}, Exam 4: {len(e4)}")
