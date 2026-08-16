// =============================================
// VTYS KONU ANLATIMLARI - Tüm Slaytlardan Derlenmiştir
// =============================================
const TOPICS = [
{
  id: "iliskisel-model",
  icon: "🔗",
  title: "İlişkisel Model (Relational Model)",
  priority: "medium",
  subtitle: "DBMS_4 - EF Codd (1970) tarafından önerilen ilişkisel veri modeli",
  content: `
<div class="topic-section">
<h3>📌 İlişkisel Model Nedir?</h3>
<p>İlişkisel Veri Tabanı Yönetim Sistemi (RDBMS), günümüzde en yaygın kullanılan veri işleme yazılımıdır. EF Codd (1970) tarafından önerilmiştir. İlişkisel modelde tüm veriler mantıksal olarak <strong>ilişkiler (tablolar)</strong> içinde yapılandırılmıştır.</p>
<ul>
<li>Her ilişkinin bir <strong>adı</strong> vardır</li>
<li>Adlandırılmış <strong>özelliklerden (sütunlar/attributes)</strong> oluşur</li>
<li>Her satır, nitelik başına <strong>bir değer</strong> içerir</li>
</ul>
<div class="info-box">
<strong>İlişkisel Modelin Hedefleri:</strong><br>
• Yüksek derecede veri bağımsızlığına izin vermek<br>
• Veri semantiği, tutarlılık ve yedeklilik problemleriyle uğraşmak için temel araçlar sağlamak
</div>
</div>

<div class="topic-section">
<h3>📐 Matematiksel İlişkiler</h3>
<p>D1 = {2, 4} ve D2 = {1, 3, 5} iki küme olsun. Kartezyen ürün:</p>
<div class="code-example">D1 × D2 = {(2,1), (2,3), (2,5), (4,1), (4,3), (4,5)}</div>
<p>Bu Kartezyen ürünün herhangi bir alt kümesi bir <strong>ilişkidir</strong>. Örneğin: R = {(2,1), (4,1)}</p>
</div>

<div class="topic-section">
<h3>🔑 İlişkilerin Özellikleri</h3>
<ul>
<li>Her ilişki <strong>benzersiz bir isme</strong> sahip olmalıdır</li>
<li>Her hücre <strong>atomik (tek) değer</strong> içermelidir</li>
<li>Her özellik <strong>kendine özgü bir ada</strong> sahiptir</li>
<li>Bir özniteliğin tüm değerleri <strong>aynı etki alanındadır</strong></li>
<li>Her satır <strong>farklıdır</strong> (yinelenen kayıt yoktur)</li>
<li>Niteliklerin ve satırların <strong>sırası önemsizdir</strong></li>
</ul>
</div>

<div class="topic-section">
<h3>🔑 İlişkisel Anahtarlar</h3>
<table class="table-styled">
<tr><th>Anahtar Türü</th><th>Açıklama</th></tr>
<tr><td><strong>Süper Anahtar (Super Key)</strong></td><td>Bir satırı benzersiz tanımlayan özellik veya özellikler kümesi</td></tr>
<tr><td><strong>Aday Anahtar (Candidate Key)</strong></td><td>Minimum süper anahtar; hiçbir alt kümesi anahtar değildir</td></tr>
<tr><td><strong>Birincil Anahtar (Primary Key)</strong></td><td>Aday anahtarlar arasından seçilen ana tanımlayıcı</td></tr>
<tr><td><strong>Yabancı Anahtar (Foreign Key)</strong></td><td>Başka bir tablonun birincil anahtarına referans veren sütun</td></tr>
</table>
</div>

<div class="topic-section">
<h3>🛡️ Bütünlük Kuralları</h3>
<h4>Varlık Bütünlüğü (Entity Integrity)</h4>
<p>Birincil anahtar <strong>NULL olamaz</strong> ve her satır için <strong>benzersiz</strong> olmalıdır.</p>

<h4>Referans Bütünlüğü (Referential Integrity)</h4>
<p>Yabancı anahtar bir değer içeriyorsa, bu değer ana tabloda <strong>mevcut ve geçerli</strong> bir satırı göstermelidir. Yabancı anahtar NULL olabilir (henüz atanmamış durumlar).</p>

<h4>NULL Kavramı</h4>
<p>NULL, eksik veya bilinmeyen değeri temsil eder. <strong>Sıfır veya boşluk değildir!</strong> NULL bir değerin yokluğudur.</p>
</div>

<div class="topic-section">
<h3>👁️ Görünümler (Views)</h3>
<p>Görünüm, sanal veya türetilmiş bir ilişkidir. Veritabanında fiziksel olarak saklanmaz, bir veya daha fazla temel ilişkiden dinamik olarak türetilir.</p>
<h4>Görünüm Amaçları:</h4>
<ul>
<li><strong>Güvenlik:</strong> Belirli kullanıcılardan veri gizleme</li>
<li><strong>Özelleştirme:</strong> Aynı verileri farklı kullanıcılara farklı şekillerde gösterme</li>
<li><strong>Basitleştirme:</strong> Karmaşık sorguları basitleştirme</li>
</ul>
<div class="info-box warning">
<strong>⚠️ Sınav notu:</strong> Birden fazla temel ilişki veya birleştirme/gruplama içeren görünümler güncellenemez!
</div>
</div>`
},
{
  id: "iliskisel-cebir",
  icon: "🧮",
  title: "İlişkisel Cebir (Relational Algebra)",
  priority: "medium",
  subtitle: "DBMS_5 - Prosedürel dil, ilişkisel işlemler",
  content: `
<div class="topic-section">
<h3>📌 İlişkisel Cebir Nedir?</h3>
<p>İlişkisel cebir, bir veya daha fazla ilişki üzerinde çalışan işlemlerle orijinal ilişkileri değiştirmeden yeni ilişki tanımlayan <strong>prosedürel bir dildir</strong>. Kapanma (closure) özelliği sayesinde bir işlemin çıktısı başka bir işlemin girdisi olabilir.</p>
</div>

<div class="topic-section">
<h3>🔧 Temel İşlemler</h3>
<table class="table-styled">
<tr><th>İşlem</th><th>Sembol</th><th>Açıklama</th><th>SQL Karşılığı</th></tr>
<tr><td><strong>Seçim (Selection)</strong></td><td>σ</td><td>Koşulu sağlayan satırları filtreler</td><td>WHERE</td></tr>
<tr><td><strong>Projeksiyon (Projection)</strong></td><td>π</td><td>Belirli sütunları seçer, tekrarları eler</td><td>SELECT DISTINCT sütunlar</td></tr>
<tr><td><strong>Birleşim (Union)</strong></td><td>∪</td><td>İki ilişkinin tüm satırlarını birleştirir</td><td>UNION</td></tr>
<tr><td><strong>Fark (Difference)</strong></td><td>−</td><td>Birinci ilişkide olup ikincide olmayan</td><td>EXCEPT</td></tr>
<tr><td><strong>Kesişim (Intersection)</strong></td><td>∩</td><td>Her iki ilişkide de olan satırlar</td><td>INTERSECT</td></tr>
<tr><td><strong>Kartezyen Çarpım</strong></td><td>×</td><td>Tüm olası çiftler</td><td>CROSS JOIN</td></tr>
</table>
</div>

<div class="topic-section">
<h3>🔗 Birleştirme (Join) Türleri</h3>
<table class="table-styled">
<tr><th>Join Türü</th><th>Açıklama</th></tr>
<tr><td><strong>Theta Join (θ)</strong></td><td>Kartezyen çarpım + koşul filtreleme (<, ≤, >, ≥, =, <>)</td></tr>
<tr><td><strong>Equijoin</strong></td><td>Theta join'in özel hali; sadece eşitlik (=) koşulu</td></tr>
<tr><td><strong>Natural Join</strong></td><td>Ortak sütunlarda equijoin + tekrar eden sütun çıkarma</td></tr>
<tr><td><strong>Outer Join (Dış Birleştirme)</strong></td><td>Eşleşmeyen satırları da dahil eder (NULL ile doldurur)</td></tr>
<tr><td><strong>Left Outer Join</strong></td><td>Sol tablodaki tüm satırları korur</td></tr>
<tr><td><strong>Right Outer Join</strong></td><td>Sağ tablodaki tüm satırları korur</td></tr>
<tr><td><strong>Full Outer Join</strong></td><td>Her iki tablodaki tüm satırları korur</td></tr>
<tr><td><strong>Semijoin</strong></td><td>Birleştirme + ilk tablonun sütunlarını projeksiyon</td></tr>
</table>
</div>

<div class="topic-section">
<h3>📊 Özetleme ve Gruplama</h3>
<p>Temel özetleme işlevleri:</p>
<ul>
<li><strong>COUNT</strong> – Değer sayısını döndürür</li>
<li><strong>SUM</strong> – Toplam</li>
<li><strong>AVG</strong> – Ortalama</li>
<li><strong>MIN</strong> – En küçük değer</li>
<li><strong>MAX</strong> – En büyük değer</li>
</ul>
<div class="info-box">
<strong>Örnek SQL → İlişkisel Cebir:</strong><br>
<code>SELECT ad, fiyat FROM urun WHERE kategori='Elektronik'</code><br>
= π<sub>ad,fiyat</sub>(σ<sub>kategori='Elektronik'</sub>(urun))
</div>
</div>`
},
{
  id: "sql-temel",
  icon: "💻",
  title: "SQL (Structured Query Language)",
  priority: "high",
  subtitle: "DBMS_6 - SELECT, WHERE, JOIN, GROUP BY, HAVING, alt sorgular",
  content: `
<div class="topic-section">
<h3>📌 SQL Komut Grupları</h3>
<table class="table-styled">
<tr><th>Grup</th><th>Amaç</th><th>Komutlar</th></tr>
<tr><td><strong>DQL</strong></td><td>Veri sorgulama</td><td>SELECT</td></tr>
<tr><td><strong>DML</strong></td><td>Veri değiştirme</td><td>INSERT, UPDATE, DELETE</td></tr>
<tr><td><strong>DDL</strong></td><td>Yapı tanımlama</td><td>CREATE, ALTER, DROP</td></tr>
<tr><td><strong>DCL</strong></td><td>Yetki yönetimi</td><td>GRANT, REVOKE</td></tr>
<tr><td><strong>TCL</strong></td><td>İşlem yönetimi</td><td>COMMIT, ROLLBACK</td></tr>
</table>
</div>

<div class="topic-section">
<h3>📝 SELECT Yazım ve Çalışma Sırası</h3>
<div class="code-example">-- Yazım sırası:
SELECT [DISTINCT] sütunlar
FROM tablo
[JOIN tablo2 ON koşul]
WHERE satır_koşulu
GROUP BY gruplama_sütunları
HAVING grup_koşulu
ORDER BY sıralama [ASC|DESC]</div>
<table class="table-styled">
<tr><th>Sıra</th><th>Mantıksal Çalışma</th><th>Açıklama</th></tr>
<tr><td>1</td><td>FROM + JOIN</td><td>Veri kaynağı oluşur</td></tr>
<tr><td>2</td><td>WHERE</td><td>Satırlar elenir</td></tr>
<tr><td>3</td><td>GROUP BY</td><td>Satırlar gruplara ayrılır</td></tr>
<tr><td>4</td><td>HAVING</td><td>Gruplar elenir</td></tr>
<tr><td>5</td><td>SELECT</td><td>Sütunlar/hesaplar seçilir</td></tr>
<tr><td>6</td><td>DISTINCT</td><td>Tekrarlı satırlar kaldırılır</td></tr>
<tr><td>7</td><td>ORDER BY</td><td>Sonuç sıralanır</td></tr>
</table>
<div class="info-box warning"><strong>⚠️ Sınav tuzağı:</strong> WHERE içinde toplama fonksiyonu (COUNT, SUM vb.) kullanılamaz! Bunun yerine HAVING kullanılır.</div>
</div>

<div class="topic-section">
<h3>🔍 WHERE Operatörleri</h3>
<table class="table-styled">
<tr><th>İşlem</th><th>Kullanım</th><th>Örnek</th></tr>
<tr><td>Karşılaştırma</td><td>=, <>, <, <=, >, >=</td><td><code>WHERE maas > 10000</code></td></tr>
<tr><td>Mantık</td><td>AND, OR, NOT</td><td><code>WHERE city='London' OR city='Glasgow'</code></td></tr>
<tr><td>Aralık</td><td>BETWEEN...AND</td><td><code>WHERE salary BETWEEN 20000 AND 30000</code></td></tr>
<tr><td>Liste</td><td>IN / NOT IN</td><td><code>WHERE position IN ('Manager','Supervisor')</code></td></tr>
<tr><td>Desen</td><td>LIKE / NOT LIKE</td><td><code>WHERE address LIKE '%Glasgow%'</code></td></tr>
<tr><td>Boşluk</td><td>IS NULL / IS NOT NULL</td><td><code>WHERE comment IS NULL</code></td></tr>
</table>
<p><strong>LIKE jokerleri:</strong> <code>%</code> = sıfır veya daha fazla karakter, <code>_</code> = tek karakter</p>
</div>

<div class="topic-section">
<h3>📊 Özetleme Fonksiyonları</h3>
<div class="code-example">SELECT COUNT(*) AS myCount FROM PropertyForRent WHERE rent > 350;
SELECT MIN(salary), MAX(salary), AVG(salary) FROM Staff;
SELECT COUNT(DISTINCT propertyNo) FROM Viewing;</div>
</div>

<div class="topic-section">
<h3>📦 GROUP BY ve HAVING</h3>
<div class="code-example">-- Her şubedeki personel sayısı ve maaş toplamı (1'den fazla personeli olan)
SELECT branchNo, COUNT(staffNo) AS sayi, SUM(salary) AS toplam
FROM Staff
GROUP BY branchNo
HAVING COUNT(staffNo) > 1
ORDER BY branchNo;</div>
<div class="info-box"><strong>WHERE vs HAVING:</strong><br>• WHERE → bireysel satırları filtreler (GROUP BY'dan ÖNCE)<br>• HAVING → grupları filtreler (GROUP BY'dan SONRA), toplama fonksiyonu içerir</div>
</div>

<div class="topic-section">
<h3>🔗 JOIN İşlemleri</h3>
<div class="code-example">-- İç birleştirme (INNER JOIN)
SELECT c.clientNo, fName, propertyNo, comment
FROM Client c, Viewing v
WHERE c.clientNo = v.clientNo;

-- Sol Dış Birleştirme (LEFT JOIN)
SELECT b.*, p.*
FROM Branch1 b LEFT JOIN PropertyForRent1 p ON b.bCity = p.pCity;

-- Sağ Dış Birleştirme (RIGHT JOIN)
SELECT b.*, p.*
FROM Branch1 b RIGHT JOIN PropertyForRent1 p ON b.bCity = p.pCity;

-- Tam Dış Birleştirme (FULL JOIN)
SELECT b.*, p.*
FROM Branch1 b FULL JOIN PropertyForRent1 p ON b.bCity = p.pCity;</div>
</div>

<div class="topic-section">
<h3>🔄 Alt Sorgular (Subqueries)</h3>
<p>Üç tür alt sorgu: <strong>Skaler</strong> (tek değer), <strong>Satır</strong> (çok sütun, tek satır), <strong>Tablo</strong> (çok satır)</p>
<div class="code-example">-- Ortalamadan yüksek maaş alanlar
SELECT staffNo, fName, salary - (SELECT AVG(salary) FROM Staff) AS salDiff
FROM Staff
WHERE salary > (SELECT AVG(salary) FROM Staff);

-- ANY / SOME kullanımı
WHERE salary > SOME (SELECT salary FROM Staff WHERE branchNo = 'B003');

-- ALL kullanımı
WHERE salary > ALL (SELECT salary FROM Staff WHERE branchNo = 'B003');

-- EXISTS kullanımı
WHERE EXISTS (SELECT * FROM Branch b WHERE s.branchNo = b.branchNo AND city='London');</div>
</div>

<div class="topic-section">
<h3>✏️ DML: INSERT, UPDATE, DELETE</h3>
<div class="code-example">-- INSERT
INSERT INTO Staff VALUES ('SG16','Alan','Brown','Assistant','M',DATE '1957-05-25',8300,'B003');

-- UPDATE
UPDATE Staff SET salary = salary * 1.05 WHERE position = 'Manager';

-- DELETE
DELETE FROM Viewing WHERE propertyNo = 'PG4';

-- Küme İşlemleri
(SELECT city FROM Branch) UNION (SELECT city FROM PropertyForRent);
(SELECT city FROM Branch) INTERSECT (SELECT city FROM PropertyForRent);
(SELECT city FROM Branch) EXCEPT (SELECT city FROM PropertyForRent);</div>
</div>`
},
{
  id: "sql-ddl",
  icon: "🏗️",
  title: "SQL Veri Tanımlama (DDL) ve Bütünlük",
  priority: "medium",
  subtitle: "DBMS_7 - CREATE, ALTER, DROP, kısıtlamalar, INDEX, VIEW, GRANT",
  content: `
<div class="topic-section">
<h3>📌 Veri Tipleri</h3>
<table class="table-styled">
<tr><th>Tip</th><th>Açıklama</th><th>Örnek</th></tr>
<tr><td>CHAR(n)</td><td>Sabit uzunluklu karakter</td><td><code>subeNo CHAR(4)</code></td></tr>
<tr><td>VARCHAR(n)</td><td>Değişken uzunluklu karakter</td><td><code>adres VARCHAR(30)</code></td></tr>
<tr><td>INTEGER/INT</td><td>Tam sayı</td><td><code>rooms SMALLINT</code></td></tr>
<tr><td>DECIMAL(p,s)</td><td>Ondalıklı sayı</td><td><code>salary DECIMAL(7,2)</code></td></tr>
<tr><td>DATE</td><td>Tarih (YIL-AY-GÜN)</td><td><code>viewDate DATE</code></td></tr>
<tr><td>BOOLEAN</td><td>TRUE / FALSE</td><td></td></tr>
<tr><td>BLOB/CLOB</td><td>Büyük nesneler</td><td></td></tr>
</table>
</div>

<div class="topic-section">
<h3>🏗️ CREATE TABLE</h3>
<div class="code-example">CREATE TABLE PropertyForRent(
  propertyNo VARCHAR(5) NOT NULL,
  street VARCHAR(25) NOT NULL,
  city VARCHAR(15) NOT NULL,
  type CHAR(1) NOT NULL DEFAULT 'F',
  rooms SMALLINT NOT NULL DEFAULT 4,
  rent DECIMAL(6,2) NOT NULL,
  ownerNo VARCHAR(5) NOT NULL,
  staffNo VARCHAR(5),
  branchNo CHAR(4) NOT NULL,
  PRIMARY KEY (propertyNo),
  FOREIGN KEY (staffNo) REFERENCES Staff ON DELETE SET NULL ON UPDATE CASCADE,
  FOREIGN KEY (ownerNo) REFERENCES PrivateOwner ON DELETE NO ACTION ON UPDATE CASCADE,
  FOREIGN KEY (branchNo) REFERENCES Branch ON DELETE NO ACTION ON UPDATE CASCADE
);</div>
</div>

<div class="topic-section">
<h3>🛡️ Bütünlük Kısıtlamaları</h3>
<table class="table-styled">
<tr><th>Kısıtlama</th><th>Açıklama</th><th>Örnek</th></tr>
<tr><td><strong>NOT NULL</strong></td><td>Boş değer kabul etmez</td><td><code>ad VARCHAR(30) NOT NULL</code></td></tr>
<tr><td><strong>UNIQUE</strong></td><td>Benzersiz değer</td><td><code>email VARCHAR(50) UNIQUE</code></td></tr>
<tr><td><strong>PRIMARY KEY</strong></td><td>Birincil anahtar</td><td><code>PRIMARY KEY (staffNo)</code></td></tr>
<tr><td><strong>FOREIGN KEY</strong></td><td>Yabancı anahtar</td><td><code>FOREIGN KEY (branchNo) REFERENCES Branch</code></td></tr>
<tr><td><strong>CHECK</strong></td><td>Değer kontrolü</td><td><code>CHECK (cinsiyet IN ('E','B'))</code></td></tr>
<tr><td><strong>DEFAULT</strong></td><td>Varsayılan değer</td><td><code>DEFAULT 'F'</code></td></tr>
</table>
<h4>Referans Bütünlüğü Aksiyonları:</h4>
<ul>
<li><strong>CASCADE:</strong> Ana tablodan silince alt tablodaki eşleşen satırları da sil</li>
<li><strong>SET NULL:</strong> Alt tablodaki yabancı anahtar değerlerini NULL yap</li>
<li><strong>SET DEFAULT:</strong> Varsayılan değere ayarla</li>
<li><strong>NO ACTION:</strong> Silme/güncelleme işlemini reddet</li>
</ul>
</div>

<div class="topic-section">
<h3>🔧 ALTER TABLE ve DROP</h3>
<div class="code-example">-- Sütun ekleme
ALTER TABLE Client ADD prefNoRooms SMALLINT;

-- Varsayılan değer ayarlama/kaldırma
ALTER TABLE Staff ALTER cinsiyet SET DEFAULT 'B';
ALTER TABLE Staff ALTER position DROP DEFAULT;

-- Kısıtlama kaldırma
ALTER TABLE PropertyForRent DROP CONSTRAINT StaffNotHandlingTooMuch;

-- Tablo silme
DROP TABLE PropertyForRent;  -- RESTRICT: bağlı nesneleri silmez, CASCADE: hepsini siler</div>
</div>

<div class="topic-section">
<h3>📇 INDEX, VIEW, GRANT/REVOKE</h3>
<div class="code-example">-- INDEX oluşturma
CREATE UNIQUE INDEX StaffNoInd ON Staff (staffNo);

-- VIEW oluşturma
CREATE VIEW Manager3Staff AS
SELECT * FROM Staff WHERE branchNo = 'B003';

-- Yetki verme
GRANT ALL PRIVILEGES ON Staff TO Manager WITH GRANT OPTION;
GRANT SELECT, UPDATE (salary) ON Staff TO Personnel, Director;

-- Yetki iptal
REVOKE ALL PRIVILEGES ON Staff FROM Director;</div>
</div>

<div class="topic-section">
<h3>💾 Transaction (İşlem Yönetimi)</h3>
<p><strong>COMMIT:</strong> İşlemi başarıyla tamamlar, değişiklikleri kalıcı kılar.<br>
<strong>ROLLBACK:</strong> İşlemi iptal eder, değişiklikleri geri alır.</p>
<div class="code-example">SET TRANSACTION READ WRITE
ISOLATION LEVEL SERIALIZABLE;</div>
</div>`
},
{
  id: "t-sql",
  icon: "⚙️",
  title: "T-SQL ile Programlama",
  priority: "high",
  subtitle: "T-SQL_1 - Değişkenler, IF/ELSE, WHILE, CASE, GO",
  content: `
<div class="topic-section">
<h3>📌 T-SQL Nedir?</h3>
<p>Transact-SQL (T-SQL), ANSI SQL'e programlama yetenekleri (değişken, döngü, koşul) ekleyen Microsoft SQL Server'a özgü bir dildir. Stored Procedure, Trigger gibi yapıları kodlarken kullanılır.</p>
</div>

<div class="topic-section">
<h3>📝 Değişken Tanımlama</h3>
<div class="code-example">-- Değişken tanımlama
DECLARE @enPahaliUrun VARCHAR(200);
DECLARE @urunKod INT, @fiyat MONEY;

-- Başlangıç değeri ile tanımlama
DECLARE @enPahaliUrun VARCHAR(200) = 'PS/2F TR KLAVYE';

-- SET ile değer atama
SET @enPahaliUrun = 'Yeni Ürün';

-- SELECT ile değer atama (sorgudan)
DECLARE @enYuksekFiyat MONEY;
SELECT @enYuksekFiyat = MAX(listeFiyat) FROM tblUrun;
SELECT @enYuksekFiyat;  -- Değeri gösterme</div>
<div class="info-box warning"><strong>⚠️ Dikkat:</strong> SELECT ile değer atarken sorgunun tek satır döndürdüğüne dikkat edin! Birden fazla satır dönerse son satırın değeri atanır.</div>
</div>

<div class="topic-section">
<h3>🔀 IF...ELSE Karar Yapısı</h3>
<div class="code-example">DECLARE @enYuksekFiyat MONEY
SELECT @enYuksekFiyat = MAX(listeFiyat) FROM tblUrun

IF (@enYuksekFiyat > 20000)
BEGIN
    PRINT 'Bu ürünlerden bazıları çok pahalıdır.'
END
ELSE IF (@enYuksekFiyat > 2000)
BEGIN
    PRINT 'Bu ürünler çok da pahalı değildir.'
END
ELSE
BEGIN
    PRINT 'Bu ürünler ucuz ürün kategorisindedir.'
END

-- EXISTS ile kontrol
IF NOT EXISTS(SELECT * FROM tblUrun)
    PRINT 'Hiç ürün kaydı yok.'</div>
</div>

<div class="topic-section">
<h3>🔄 WHILE Döngüsü</h3>
<div class="code-example">DECLARE @sayac INT = 1
WHILE (@sayac < 15)
BEGIN
    SET @sayac = @sayac + 1
    IF (@sayac = 11)
        CONTINUE  -- 11'i atla, döngü başına dön
    PRINT 'Sayaç = ' + CAST(@sayac AS VARCHAR(3))
END

-- BREAK: döngüden tamamen çık
-- CONTINUE: döngünün başına dön</div>
</div>

<div class="topic-section">
<h3>📋 CASE Kontrol Deyimi</h3>
<div class="code-example">SELECT markaKod, yildiz =
    CASE
        WHEN COUNT(urunKod) > 40 THEN '****'
        WHEN COUNT(urunKod) > 30 THEN '***'
        WHEN COUNT(urunKod) > 20 THEN '**'
        WHEN COUNT(urunKod) > 0  THEN '*'
    END,
    COUNT(*) AS toplam
FROM tblUrun
GROUP BY markaKod;</div>
</div>

<div class="topic-section">
<h3>📦 GO Bölümleyicisi ve Global Değişkenler</h3>
<p><strong>GO:</strong> T-SQL komut yığınının sonunu belirtir. SQL Server'a iletilmez, istemci tarafından yorumlanır.</p>
<p><strong>Global Değişkenler (@@):</strong></p>
<ul>
<li><code>@@VERSION</code> – SQL Server versiyon bilgisi</li>
<li><code>@@ROWCOUNT</code> – Son sorguda etkilenen satır sayısı</li>
<li><code>@@FETCH_STATUS</code> – Cursor durumu (0=başarılı, -1=hata, -2=son)</li>
<li><code>@@CONNECTIONS</code> – Bağlantı sayısı</li>
</ul>
</div>

<div class="topic-section">
<h3>🖨️ PRINT ve CAST</h3>
<div class="code-example">DECLARE @sonuc MONEY
SELECT @sonuc = SUM(listeFiyat) FROM tblUrun
PRINT CAST(@sonuc AS VARCHAR(10))  -- Sayıyı metne çevir ve yazdır</div>
</div>`
},
{
  id: "stored-procedure",
  icon: "📦",
  title: "Saklı Yordamlar (Stored Procedures)",
  priority: "high",
  subtitle: "DBMS_8_1 & saklıYordam_SP - CREATE PROCEDURE, parametreler, IN/OUT",
  content: `
<div class="topic-section">
<h3>📌 Saklı Yordam Nedir?</h3>
<p>Saklı yordam (Stored Procedure), veritabanında derlenerek saklanan, parametreler alabilen ve çağrılabilen PL/SQL veya T-SQL bloklarıdır. Modülerlik, yeniden kullanılabilirlik ve performans avantajları sağlar.</p>
</div>

<div class="topic-section">
<h3>🔧 T-SQL'de Stored Procedure</h3>
<div class="code-example">-- Basit prosedür oluşturma
CREATE PROCEDURE SelamVer
AS
BEGIN
    PRINT 'Merhaba, Dünya'
END
GO
EXEC SelamVer;

-- Parametreli prosedür
CREATE PROC sp_harfnotu_hesapla
    @ogrencino VARCHAR(5),
    @derskodu VARCHAR(6),
    @vizenotu DECIMAL,
    @finalnotu DECIMAL,
    @ortalama DECIMAL OUTPUT,
    @harfnotu VARCHAR(2) OUTPUT
AS
BEGIN
    SET @ortalama = (@vizenotu * 0.3) + (@finalnotu * 0.7)
    IF @ortalama >= 90 SET @harfnotu = 'AA'
    ELSE IF @ortalama >= 80 SET @harfnotu = 'BA'
    ELSE IF @ortalama >= 70 SET @harfnotu = 'BB'
    ELSE IF @ortalama >= 60 SET @harfnotu = 'CB'
    ELSE IF @ortalama >= 50 SET @harfnotu = 'DD'
    ELSE SET @harfnotu = 'FF'
    INSERT INTO notbilgi VALUES(@ogrencino, @derskodu, @vizenotu, @finalnotu, @ortalama, @harfnotu)
END

EXEC sp_harfnotu_hesapla '12345', 'vyt123', 79, 50, 0, 'bos';</div>
</div>

<div class="topic-section">
<h3>📋 Parametre Modları (PL/SQL)</h3>
<table class="table-styled">
<tr><th>Mod</th><th>Açıklama</th></tr>
<tr><td><strong>IN</strong></td><td>Alt programa değer iletir (salt okunur). Varsayılan moddur.</td></tr>
<tr><td><strong>OUT</strong></td><td>Çağıran programa değer döndürür</td></tr>
<tr><td><strong>IN OUT</strong></td><td>Hem giriş hem çıkış: değer alır, işler ve geri döndürür</td></tr>
</table>
<div class="code-example">-- PL/SQL'de prosedür
CREATE OR REPLACE PROCEDURE PropertiesForStaff
    (IN vStaffNo VARCHAR2) AS ...

-- IN OUT örneği
PROCEDURE squareNum(x IN OUT NUMBER) IS
BEGIN
    x := x * x;
END;</div>
</div>

<div class="topic-section">
<h3>⚡ Function (Fonksiyon) vs Procedure</h3>
<table class="table-styled">
<tr><th>Özellik</th><th>Procedure</th><th>Function</th></tr>
<tr><td>Değer Döndürme</td><td>Doğrudan değer döndürmez (OUT parametresi ile)</td><td><strong>RETURN ile tek değer döndürür</strong></td></tr>
<tr><td>Çağırma</td><td>EXEC / EXECUTE</td><td>SELECT içinde kullanılabilir</td></tr>
<tr><td>SQL İçinde</td><td>Doğrudan kullanılamaz</td><td>WHERE, SELECT içinde kullanılabilir</td></tr>
</table>
<div class="code-example">-- PL/SQL Function
CREATE OR REPLACE FUNCTION totalCustomers
RETURN NUMBER IS
    total NUMBER(2) := 0;
BEGIN
    SELECT COUNT(*) INTO total FROM customers;
    RETURN total;
END;

-- Çağırma
DECLARE c NUMBER(2);
BEGIN
    c := totalCustomers();
    dbms_output.put_line('Toplam: ' || c);
END;</div>
</div>

<div class="topic-section">
<h3>🔑 Varsayılan Parametre Değeri (T-SQL)</h3>
<div class="code-example">CREATE PROCEDURE SiparisListele
    @minTutar MONEY = 1000  -- Varsayılan değer
AS
BEGIN
    SELECT * FROM Siparis WHERE tutar >= @minTutar
END

-- Parametre gönderilmezse @minTutar = 1000 olur
EXEC SiparisListele;       -- 1000 kullanılır
EXEC SiparisListele 5000;  -- 5000 kullanılır</div>
</div>`
},
{
  id: "trigger",
  icon: "⚡",
  title: "Tetikleyiciler (Triggers)",
  priority: "high",
  subtitle: "DBMS_8_2 & trigger.pdf - AFTER, INSTEAD OF, Inserted/Deleted tabloları",
  content: `
<div class="topic-section">
<h3>📌 Trigger Nedir?</h3>
<p>Trigger, belirli bir olay (INSERT, UPDATE, DELETE) gerçekleştiğinde otomatik olarak çalışan özel bir stored procedure'dür. Dışarıdan parametre almaz, doğrudan çağrılamaz.</p>
<div class="info-box danger"><strong>🔥 SINAV İÇİN KRİTİK:</strong> Trigger'lar Inserted ve Deleted sözde tablolarını kullanır!</div>
</div>

<div class="topic-section">
<h3>📊 Inserted ve Deleted Tabloları</h3>
<table class="table-styled">
<tr><th>İşlem</th><th>INSERTED Tablosu</th><th>DELETED Tablosu</th></tr>
<tr><td><strong>INSERT</strong></td><td>✅ Yeni eklenen kayıtlar</td><td>❌ Oluşturulmaz</td></tr>
<tr><td><strong>DELETE</strong></td><td>❌ Oluşturulmaz</td><td>✅ Silinen kayıtlar</td></tr>
<tr><td><strong>UPDATE</strong></td><td>✅ Kayıtların güncellenen halleri</td><td>✅ Kayıtların eski halleri</td></tr>
</table>
<div class="info-box warning"><strong>⚠️ UPDATE = DELETE + INSERT:</strong> Bir kayıt güncellendiğinde eski hali DELETED'e, yeni hali INSERTED'e yazılır.</div>
</div>

<div class="topic-section">
<h3>🔧 Trigger Türleri</h3>
<table class="table-styled">
<tr><th>Tür</th><th>Açıklama</th><th>Nerede Tanımlanır?</th></tr>
<tr><td><strong>AFTER</strong></td><td>Olay gerçekleştikten SONRA çalışır</td><td>Sadece tablolarda</td></tr>
<tr><td><strong>INSTEAD OF</strong></td><td>Olayın YERİNE çalışır (olay gerçekleşmez)</td><td>Tablolar ve View'ler</td></tr>
<tr><td><strong>BEFORE (PL/SQL)</strong></td><td>Olay gerçekleşmeden ÖNCE çalışır</td><td>Tablolarda</td></tr>
</table>
<p><strong>FOR EACH ROW</strong> → Satır düzeyinde (her etkilenen satır için)<br>
<strong>FOR EACH STATEMENT</strong> → İfade düzeyinde (bir kez çalışır)</p>
</div>

<div class="topic-section">
<h3>💻 T-SQL Trigger Örnekleri</h3>
<div class="code-example">-- INSERT Trigger: Kayıt eklenince stoku azalt
CREATE TRIGGER stokAzalt
ON tbl_siparisDetay
AFTER INSERT
AS
SET NOCOUNT ON
UPDATE tbl_urun
SET stokDurum = stokDurum - 1
FROM tbl_urun U INNER JOIN inserted I
ON I.urunKod = U.urunKod
WHERE U.stokDurum = 1;

-- DELETE Trigger: Kontrol edilmemiş sipariş silinmesin
CREATE TRIGGER bakmadanSiparisSilme
ON tbl_siparis
AFTER DELETE
AS
IF EXISTS (SELECT * FROM DELETED D WHERE D.siparisDurumKod = 0)
BEGIN
    RAISERROR('Siparişe bakmadan silemezsiniz.', 10, 1)
    ROLLBACK
END;

-- UPDATE Trigger: Fiyat azaltılamaz
CREATE TRIGGER urunFiyatAzalmasin
ON tbl_urun
AFTER UPDATE
AS
BEGIN
    IF EXISTS (
        SELECT * FROM INSERTED I
        INNER JOIN DELETED D ON D.urunKod = I.urunKod
        WHERE D.listeFiyat > I.listeFiyat
    )
    BEGIN
        RAISERROR('Fiyat azaltılamaz!', 10, 1)
        ROLLBACK
    END
END;</div>
</div>

<div class="topic-section">
<h3>🔍 IF UPDATE() ve COLUMNS_UPDATED()</h3>
<p><strong>IF UPDATE(sütun_adı):</strong> Belirli bir sütun güncellendiğinde TRUE döner. Gereksiz tetiklemeyi önler.</p>
<div class="code-example">CREATE TRIGGER tr_fiyat_kontrol
ON tbl_urun
FOR UPDATE
AS
IF UPDATE(listeFiyat)  -- Sadece fiyat değiştiğinde çalışır
BEGIN
    -- kontrol kodları
END;</div>
</div>

<div class="topic-section">
<h3>⚡ PL/SQL Trigger Örneği</h3>
<div class="code-example">-- PL/SQL AFTER satır düzeyinde trigger
CREATE TRIGGER StaffAfterInsert
AFTER INSERT ON Staff
REFERENCING NEW AS new
FOR EACH ROW
BEGIN
    INSERT INTO StaffAudit
    VALUES (:new.staffNo, :new.fName, :new.lName,
            :new.position, :new.sex, :new.DOB,
            :new.salary, :new.branchNo);
END;

-- BEFORE/AFTER ve :NEW/:OLD referansları
-- :OLD → güncellenmeden önceki değer (UPDATE/DELETE'te)
-- :NEW → güncellendikten sonraki değer (INSERT/UPDATE'te)</div>
</div>`
},
{
  id: "cursor",
  icon: "🔄",
  title: "İmleçler (Cursors)",
  priority: "high",
  subtitle: "Cursor.pptx & DBMS_8 - DECLARE, OPEN, FETCH, CLOSE, DEALLOCATE",
  content: `
<div class="topic-section">
<h3>📌 Cursor Nedir?</h3>
<p>Cursor, bir sorgu sonucu (resultset) üzerinde <strong>satır satır</strong> dolaşmaya imkân veren yapıdır. SELECT tek seferde tüm sonucu döndürürken, Cursor ile tek tek satırlara erişilir.</p>
</div>

<div class="topic-section">
<h3>📋 T-SQL Cursor 5 Aşaması</h3>
<table class="table-styled">
<tr><th>Aşama</th><th>Komut</th><th>Açıklama</th></tr>
<tr><td>1. Tanımlama</td><td><code>DECLARE ... CURSOR FOR SELECT ...</code></td><td>Cursor değişken olarak tanımlanır</td></tr>
<tr><td>2. Açma</td><td><code>OPEN cursor_ismi</code></td><td>SELECT çalıştırılır, cursor ilk satıra ayarlanır</td></tr>
<tr><td>3. Okuma</td><td><code>FETCH ... INTO @degisken</code></td><td>Satır satır veri okunur (döngü içinde)</td></tr>
<tr><td>4. Kapatma</td><td><code>CLOSE cursor_ismi</code></td><td>Resultset boşaltılır (cursor hâlâ tanımlı)</td></tr>
<tr><td>5. Silme</td><td><code>DEALLOCATE cursor_ismi</code></td><td>Cursor hafızadan tamamen silinir</td></tr>
</table>
<div class="info-box danger"><strong>🔥 SINAV:</strong> CLOSE cursor'ı kapatır ama tanımı kalır (tekrar OPEN edilebilir). DEALLOCATE cursor'ı hafızadan tamamen siler!</div>
</div>

<div class="topic-section">
<h3>💻 T-SQL Cursor Tam Örnek</h3>
<div class="code-example">DECLARE cr_markaListesi CURSOR FOR
    SELECT markaKod, marka FROM tblMarka

OPEN cr_markaListesi
DECLARE @markaKod INTEGER, @marka VARCHAR(55)

FETCH cr_markaListesi INTO @markaKod, @marka

WHILE (@@FETCH_STATUS = 0)   -- 0 = başarılı okuma
BEGIN
    PRINT CAST(@markaKod AS VARCHAR(3))
    PRINT @marka
    FETCH cr_markaListesi INTO @markaKod, @marka
END

CLOSE cr_markaListesi
DEALLOCATE cr_markaListesi</div>
</div>

<div class="topic-section">
<h3>🌀 @@FETCH_STATUS Değerleri</h3>
<table class="table-styled">
<tr><th>Değer</th><th>Anlam</th></tr>
<tr><td><strong>0</strong></td><td>FETCH başarıyla çalıştırıldı</td></tr>
<tr><td><strong>-1</strong></td><td>FETCH sırasında hata oluştu</td></tr>
<tr><td><strong>-2</strong></td><td>Resultset'in sonuna gelindi (kayıt kalmadı)</td></tr>
</table>
</div>

<div class="topic-section">
<h3>📜 Scroll Cursor</h3>
<p>Forward-Only Cursor yalnızca ileri giderken, Scroll Cursor ileri-geri hareket edebilir:</p>
<table class="table-styled">
<tr><th>Komut</th><th>İşlev</th></tr>
<tr><td><code>FETCH FIRST</code></td><td>İlk satıra git</td></tr>
<tr><td><code>FETCH LAST</code></td><td>Son satıra git</td></tr>
<tr><td><code>FETCH NEXT</code></td><td>Bir sonraki satıra git</td></tr>
<tr><td><code>FETCH PRIOR</code></td><td>Bir önceki satıra git</td></tr>
<tr><td><code>FETCH ABSOLUTE n</code></td><td>Baştan n. kayda git</td></tr>
<tr><td><code>FETCH RELATIVE n</code></td><td>Bulunulan yerden n kayıt ilerle</td></tr>
</table>
<div class="code-example">DECLARE crScrMarka SCROLL CURSOR FOR
    SELECT markaKod, marka FROM tblMarka ORDER BY markaKod
OPEN crScrMarka
FETCH LAST FROM crScrMarka       -- Son kayıt
FETCH ABSOLUTE 2 FROM crScrMarka  -- Baştan 2. kayıt
FETCH RELATIVE 3 FROM crScrMarka  -- 3 kayıt ileri
CLOSE crScrMarka
DEALLOCATE crScrMarka</div>
</div>

<div class="topic-section">
<h3>✏️ Cursor Üzerinden Güncelleme</h3>
<div class="code-example">-- Bulunulan satırı güncelle
UPDATE tablo SET sütun = değer WHERE CURRENT OF cursor_ismi;

-- Bulunulan satırı sil
DELETE FROM tablo WHERE CURRENT OF cursor_ismi;</div>
</div>

<div class="topic-section">
<h3>🔁 PL/SQL Cursor Kullanımı</h3>
<div class="code-example">DECLARE
    c_id customers.id%type;
    c_name customers.name%type;
    CURSOR c_customers IS SELECT id, name FROM customers;
BEGIN
    OPEN c_customers;
    LOOP
        FETCH c_customers INTO c_id, c_name;
        EXIT WHEN c_customers%NOTFOUND;
        dbms_output.put_line(c_id || ' ' || c_name);
    END LOOP;
    CLOSE c_customers;
END;</div>
<h4>PL/SQL Cursor Öznitelikleri:</h4>
<ul>
<li><strong>%FOUND:</strong> Son FETCH satır döndürdüyse TRUE</li>
<li><strong>%NOTFOUND:</strong> Son FETCH satır döndürmediyse TRUE</li>
<li><strong>%ISOPEN:</strong> Cursor açıksa TRUE</li>
<li><strong>%ROWCOUNT:</strong> Şimdiye kadar döndürülen toplam satır sayısı</li>
</ul>
</div>`
},
{
  id: "plsql",
  icon: "🔮",
  title: "PL/SQL Programlama",
  priority: "high",
  subtitle: "DBMS_8 / DBMS_8_1 / DBMS_8_2 - Blok yapısı, değişkenler, kontrol, exception, paket",
  content: `
<div class="topic-section">
<h3>📌 PL/SQL Blok Yapısı</h3>
<div class="code-example">DECLARE
    -- Değişken, sabit, cursor, exception tanımları (isteğe bağlı)
BEGIN
    -- Çalıştırılabilir bölüm (zorunlu)
EXCEPTION
    -- İstisna işleme (isteğe bağlı)
END;
/</div>
</div>

<div class="topic-section">
<h3>📝 Değişken Tanımlama</h3>
<div class="code-example">vStaffNo VARCHAR2(5);
vRent NUMBER(6,2) NOT NULL := 600;
MAX_PROPERTIES CONSTANT NUMBER := 100;

-- %TYPE: Tablodaki sütunla aynı tip
vStaffNo Staff.staffNo%TYPE;

-- %ROWTYPE: Tablonun tüm sütunlarını kayıt olarak
vStaffRec Staff%ROWTYPE;

-- Atama
vStaffNo := 'SG14';

-- SELECT INTO ile atama
SELECT name, address, salary INTO c_name, c_addr, c_sal
FROM customers WHERE id = c_id;</div>
<div class="info-box"><strong>%TYPE:</strong> Bir değişkeni tablodaki sütunla aynı tipte tanımlar.<br><strong>%ROWTYPE:</strong> Bir değişkeni tablonun tüm sütunlarını içeren kayıt olarak tanımlar.</div>
</div>

<div class="topic-section">
<h3>🔀 Kontrol İfadeleri</h3>
<div class="code-example">-- IF-ELSIF-ELSE
IF (position = 'Manager') THEN
    salary := salary * 1.05;
ELSIF (position = 'Supervisor') THEN
    salary := salary * 1.04;
ELSE
    salary := salary * 1.03;
END IF;

-- LOOP
x := 1;
myLoop:
LOOP
    x := x + 1;
    EXIT myLoop WHEN (x > 3);
END LOOP myLoop;

-- FOR döngüsü
FOR i IN 1..10 LOOP
    dbms_output.put_line('i = ' || i);
END LOOP;

-- WHILE döngüsü
WHILE name IS NOT NULL LOOP
    -- işlemler
END LOOP;</div>
</div>

<div class="topic-section">
<h3>🚨 İstisna İşleme (Exception Handling)</h3>
<div class="code-example">DECLARE
    c_id customers.id%type := 8;
    c_name customers.name%type;
BEGIN
    SELECT name INTO c_name FROM customers WHERE id = c_id;
    dbms_output.put_line('Name: ' || c_name);
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        dbms_output.put_line('Müşteri kaydı yoktur!');
    WHEN TOO_MANY_ROWS THEN
        dbms_output.put_line('Birden fazla kayıt döndü!');
    WHEN OTHERS THEN
        dbms_output.put_line('Beklenmeyen hata!');
END;</div>
<table class="table-styled">
<tr><th>Önceden Tanımlı İstisna</th><th>Ne Zaman?</th></tr>
<tr><td><strong>NO_DATA_FOUND</strong></td><td>SELECT INTO satır döndürmediğinde</td></tr>
<tr><td><strong>TOO_MANY_ROWS</strong></td><td>SELECT INTO birden fazla satır döndürdüğünde</td></tr>
<tr><td><strong>CASE_NOT_FOUND</strong></td><td>CASE'de eşleşen WHEN yoksa ve ELSE yoksa</td></tr>
<tr><td><strong>ZERO_DIVIDE</strong></td><td>Sıfıra bölme</td></tr>
</table>
</div>

<div class="topic-section">
<h3>📦 Paketler (Packages)</h3>
<p>Paket, prosedürler, fonksiyonlar ve değişkenleri tek bir birim olarak gruplayan yapıdır. İki bölümden oluşur:</p>
<ul>
<li><strong>Specification (Özellik):</strong> Paketin genel (public) arayüzü</li>
<li><strong>Body (Gövde):</strong> Tüm yapıların uygulaması (public + private)</li>
</ul>
<div class="code-example">-- Paket tanımı
CREATE OR REPLACE PACKAGE cust_sal AS
    PROCEDURE find_sal(c_id customers.id%TYPE);
END cust_sal;

-- Paket gövdesi
CREATE OR REPLACE PACKAGE BODY cust_sal AS
    PROCEDURE find_sal(c_id customers.id%TYPE) IS
        c_sal customers.salary%TYPE;
    BEGIN
        SELECT salary INTO c_sal FROM customers WHERE id = c_id;
        dbms_output.put_line('Salary: ' || c_sal);
    END find_sal;
END cust_sal;

-- Kullanım
EXEC cust_sal.find_sal(5);</div>
</div>

<div class="topic-section">
<h3>📚 Kayıtlar ve Koleksiyonlar</h3>
<p><strong>3 kayıt türü:</strong> Tablo tabanlı (%ROWTYPE), Cursor tabanlı, Kullanıcı tanımlı (TYPE...IS RECORD)</p>
<p><strong>3 koleksiyon türü:</strong> İlişkisel dizi (INDEX BY), İç içe tablo (Nested Table), Varray</p>
<div class="code-example">-- VARRAY
CREATE OR REPLACE TYPE varray_names IS VARRAY(5) OF VARCHAR2(10);

-- İlişkisel dizi
TYPE salary IS TABLE OF NUMBER INDEX BY VARCHAR2(20);
salary_list salary;
salary_list('Ali') := 62000;</div>
</div>`
},
{
  id: "er-modelleme",
  icon: "📐",
  title: "Varlık-İlişki (ER) Modellemesi",
  priority: "medium",
  subtitle: "DBMS_12 - Varlıklar, İlişkiler, Nitelikler, Anahtarlar, ER Diyagramı",
  content: `
<div class="topic-section">
<h3>📌 ER Model Nedir?</h3>
<p>Varlık-İlişki (ER) modeli, veritabanı tasarımına yukarıdan aşağıya bir yaklaşımdır. Teknik olmayan bir iletişim modeli olarak kullanılır.</p>
<ul>
<li><strong>Varlıklar (Entities):</strong> Dikdörtgen ile gösterilir</li>
<li><strong>İlişkiler (Relationships):</strong> Baklava (diamond) şekli ile gösterilir</li>
<li><strong>Nitelikler (Attributes):</strong> Oval ile gösterilir</li>
</ul>
</div>

<div class="topic-section">
<h3>🏢 Varlık Türleri</h3>
<table class="table-styled">
<tr><th>Tür</th><th>Açıklama</th><th>Gösterim</th></tr>
<tr><td><strong>Güçlü Varlık</strong></td><td>Başka bir varlığın varlığına bağlı olmayan</td><td>Tek çizgili dikdörtgen</td></tr>
<tr><td><strong>Zayıf Varlık</strong></td><td>Başka bir varlığa bağlı (kendi PK'si yok)</td><td>Çift çizgili dikdörtgen</td></tr>
</table>
</div>

<div class="topic-section">
<h3>📋 Nitelik (Attribute) Türleri</h3>
<table class="table-styled">
<tr><th>Tür</th><th>Açıklama</th><th>Gösterim</th></tr>
<tr><td><strong>Basit</strong></td><td>Tek değer, bölünemez</td><td>Oval</td></tr>
<tr><td><strong>Anahtar</strong></td><td>Varlığı benzersiz tanımlar</td><td>Altı çizili oval</td></tr>
<tr><td><strong>Türetilen</strong></td><td>Başka nitelikten hesaplanan (yaş = bugün - doğum tarihi)</td><td>Kesikli çizgili oval</td></tr>
<tr><td><strong>Birleşik</strong></td><td>Birden fazla nitelikten oluşan (adres = mahalle + sokak + şehir)</td><td>Alt ovaller bağlı</td></tr>
<tr><td><strong>Çok Değerli</strong></td><td>Birden fazla değer alabilen (telefon numaraları)</td><td>Çift çizgili oval</td></tr>
</table>
</div>

<div class="topic-section">
<h3>🔗 İlişki Türleri (Cardinality)</h3>
<table class="table-styled">
<tr><th>Tür</th><th>Açıklama</th><th>Örnek</th></tr>
<tr><td><strong>1:1 (Bire-bir)</strong></td><td>Her X en fazla bir Y ile ilişkili</td><td>Başkan ↔ Bölüm</td></tr>
<tr><td><strong>1:N (Bire-çok)</strong></td><td>Her X birden fazla Y ile ilişkili olabilir</td><td>Öğretim üyesi → Sınıflar</td></tr>
<tr><td><strong>N:1 (Çoktan-bire)</strong></td><td>Birden fazla X bir Y ile ilişkili</td><td>Çocuklar → Anne</td></tr>
<tr><td><strong>M:N (Çoktan-çoğa)</strong></td><td>Her iki tarafta birden fazla</td><td>Öğrenciler ↔ Dersler</td></tr>
</table>
</div>

<div class="topic-section">
<h3>📊 Katılım Kısıtlamaları</h3>
<ul>
<li><strong>Toplam Katılım (Total):</strong> Çift çizgi — her varlık ilişkiye katılmalı</li>
<li><strong>Kısmi Katılım (Partial):</strong> Tek çizgi — bazı varlıklar katılmayabilir</li>
</ul>
<div class="info-box"><strong>Örnek:</strong> Her sınıfın bir öğretim üyesi OLMALI (toplam katılım, çift çizgi), ama bazı öğretim üyeleri ders vermeyebilir (kısmi katılım, tek çizgi).</div>
</div>`
},
{
  id: "normalizasyon",
  icon: "📊",
  title: "Normalizasyon",
  priority: "high",
  subtitle: "DBMS_14 - 1NF, 2NF, 3NF, BCNF, İşlevsel Bağımlılıklar, Anomaliler",
  content: `
<div class="topic-section">
<h3>📌 Normalizasyon Nedir?</h3>
<p>Normalizasyon, öznitelikler arasındaki ilişkileri (işlevsel bağımlılıklar) inceleyerek en uygun tablo yapısını belirleyen veritabanı tasarım tekniğidir. Amaç: <strong>veri fazlalığını azaltmak</strong> ve <strong>güncelleme anomalilerini önlemek</strong>.</p>
</div>

<div class="topic-section">
<h3>⚠️ Güncelleme Anomalileri</h3>
<table class="table-styled">
<tr><th>Anomali</th><th>Açıklama</th></tr>
<tr><td><strong>Ekleme (Insertion)</strong></td><td>Yeni veri eklemek için gereksiz bilgi girilmesi gerekir. Örn: personelsiz şube eklenemez.</td></tr>
<tr><td><strong>Silme (Deletion)</strong></td><td>Bir kaydı silmek başka bilgilerin de kaybolmasına neden olur. Örn: son personeli silince şube bilgisi kaybolur.</td></tr>
<tr><td><strong>Güncelleme (Update)</strong></td><td>Bir bilgiyi değiştirmek birden fazla kayıtta güncelleme gerektirir. Tutarsızlık riski.</td></tr>
</table>
</div>

<div class="topic-section">
<h3>🔗 İşlevsel Bağımlılık</h3>
<p>A → B: A'nın değerini biliyorsak B'nin değerini benzersiz olarak belirleyebiliriz.</p>
<ul>
<li><strong>staffNo → position</strong> (her personelin tek bir pozisyonu var)</li>
<li><strong>staffNo → branchNo</strong> (her personel tek bir şubede)</li>
<li>staffNo işlevsel bağımlılığın <strong>belirleyicisi (determinant)</strong>'dir</li>
</ul>
</div>

<div class="topic-section">
<h3>📐 Normal Formlar</h3>

<h4>1NF (İlk Normal Form)</h4>
<p>Her hücre <strong>atomik (tek) değer</strong> içermelidir. Tekrarlayan gruplar kaldırılmalıdır.</p>
<div class="info-box success"><strong>✅ 1NF olma koşulu:</strong> Her satır-sütun kesişiminde yalnızca bir değer olmalı. Çok değerli alanlar ayrı tabloya taşınmalı.</div>

<h4>2NF (İkinci Normal Form)</h4>
<p>1NF olmalı VE <strong>kısmi bağımlılık</strong> olmamalıdır. Bileşik anahtarlı tablolarda, anahtarın bir kısmına bağlı olan nitelikler ayrı tabloya taşınır.</p>
<div class="info-box"><strong>Kısmi Bağımlılık:</strong> Bileşik anahtar (A, B) varsa ve C yalnızca A'ya bağlıysa → kısmi bağımlılık var → 2NF ihlali!<br>
<strong>Not:</strong> Tek sütunlu birincil anahtarla ilişki otomatik olarak 2NF'dedir.</div>

<h4>3NF (Üçüncü Normal Form)</h4>
<p>2NF olmalı VE <strong>geçişli bağımlılık</strong> olmamalıdır.</p>
<div class="info-box"><strong>Geçişli Bağımlılık:</strong> A → B → C ise, C geçişli olarak A'ya bağlıdır. B ve C ayrı tabloya taşınır.<br>
<strong>Örnek:</strong> personel_id → departman_id → departman_adi → departman_adi geçişli bağımlıdır!</div>

<h4>BCNF (Boyce-Codd Normal Form)</h4>
<p>Her <strong>belirleyici (determinant)</strong> bir <strong>aday anahtar</strong> olmalıdır.</p>
<div class="info-box warning"><strong>⚠️ BCNF ihlali riski:</strong> İlişki iki veya daha fazla bileşik aday anahtar içeriyorsa ve aday anahtarlar üst üste biniyorsa.</div>

<h4>4NF ve 5NF</h4>
<p><strong>4NF:</strong> Çok Değerli Bağımlılık (MVD) olmamalıdır.<br>
<strong>5NF:</strong> Katılım bağımlılığı ile yönetilir. İlişki ikiden fazla parçaya ayrılmalıdır.</p>
</div>

<div class="topic-section">
<h3>🔑 Ayrıştırma Özellikleri</h3>
<ul>
<li><strong>Kayıpsız Birleştirme:</strong> Küçük tablolar birleştirildiğinde orijinal tablo elde edilmeli</li>
<li><strong>Bağımlılık Koruma:</strong> Orijinal kısıtlamalar küçük tablolarda korunmalı</li>
</ul>
</div>`
},
{
  id: "sql-functions",
  icon: "🔢",
  title: "SQL Fonksiyonları",
  priority: "medium",
  subtitle: "sql_Functions.pdf - Scalar, Table-valued, Aggregate fonksiyonlar",
  content: `
<div class="topic-section">
<h3>📌 Fonksiyon Türleri</h3>
<table class="table-styled">
<tr><th>Tür</th><th>Açıklama</th><th>Örnek</th></tr>
<tr><td><strong>Scalar Function</strong></td><td>Tek bir değer döndürür</td><td>Verilen iki sayıdan toplam hesapla</td></tr>
<tr><td><strong>Table-valued Function</strong></td><td>Tablo (sonuç kümesi) döndürür</td><td>Bir bölümdeki öğrencilerin listesini döndür</td></tr>
<tr><td><strong>Aggregate Function</strong></td><td>Bir sütundaki değerleri özetler</td><td>COUNT, SUM, AVG, MIN, MAX</td></tr>
</table>
</div>

<div class="topic-section">
<h3>💻 T-SQL'de Scalar Function</h3>
<div class="code-example">CREATE FUNCTION dbo.ToplamHesapla
(
    @sayi1 INT,
    @sayi2 INT
)
RETURNS INT
AS
BEGIN
    RETURN @sayi1 + @sayi2
END

-- Kullanım
SELECT dbo.ToplamHesapla(5, 3) AS Sonuc;  -- 8</div>
</div>

<div class="topic-section">
<h3>📋 Yaygın Yerleşik Fonksiyonlar</h3>
<table class="table-styled">
<tr><th>Kategori</th><th>Fonksiyonlar</th></tr>
<tr><td>Metin</td><td><code>LEN, UPPER, LOWER, SUBSTRING, LTRIM, RTRIM, REPLACE, CHARINDEX</code></td></tr>
<tr><td>Sayısal</td><td><code>ABS, CEILING, FLOOR, ROUND, POWER, SQRT</code></td></tr>
<tr><td>Tarih</td><td><code>GETDATE, DATEADD, DATEDIFF, DATEPART, YEAR, MONTH, DAY</code></td></tr>
<tr><td>Dönüştürme</td><td><code>CAST, CONVERT, ISNULL, COALESCE, NULLIF</code></td></tr>
</table>
</div>`
},
{
  id: "transaction",
  icon: "💾",
  title: "Transaction ve Kilitleme",
  priority: "medium",
  subtitle: "DBMS_8_2 / T-SQL - COMMIT, ROLLBACK, SAVEPOINT, izolasyon seviyeleri",
  content: `
<div class="topic-section">
<h3>📌 Transaction Nedir?</h3>
<p>Transaction, bir veya daha fazla SQL ifadesini bir bütün olarak ele alan mantıksal iş birimidir. Ya tamamı başarılır ya da tamamı geri alınır (ACID özellikleri).</p>
</div>

<div class="topic-section">
<h3>🔑 ACID Özellikleri</h3>
<table class="table-styled">
<tr><th>Özellik</th><th>Açıklama</th></tr>
<tr><td><strong>Atomicity (Bölünmezlik)</strong></td><td>İşlemin tamamı ya yapılır ya yapılmaz</td></tr>
<tr><td><strong>Consistency (Tutarlılık)</strong></td><td>İşlem öncesi ve sonrası veritabanı tutarlı kalır</td></tr>
<tr><td><strong>Isolation (Yalıtım)</strong></td><td>Eşzamanlı işlemler birbirini etkilemez</td></tr>
<tr><td><strong>Durability (Kalıcılık)</strong></td><td>Onaylanan değişiklikler kalıcıdır</td></tr>
</table>
</div>

<div class="topic-section">
<h3>💻 Transaction Komutları</h3>
<div class="code-example">BEGIN TRANSACTION;

INSERT INTO siparis VALUES (...);
UPDATE stok SET miktar = miktar - 1 WHERE ...;

SAVEPOINT sav1;  -- Kaydetme noktası

UPDATE fiyat SET tutar = tutar * 1.1;

ROLLBACK TO sav1;  -- sav1'e kadar geri al

COMMIT;  -- Tüm değişiklikleri kalıcı yap

-- Otomatik commit
SET AUTOCOMMIT ON;</div>
</div>

<div class="topic-section">
<h3>🔒 İzolasyon Seviyeleri</h3>
<table class="table-styled">
<tr><th>Seviye</th><th>Dirty Read</th><th>Non-Repeatable</th><th>Phantom</th></tr>
<tr><td>READ UNCOMMITTED</td><td>✅</td><td>✅</td><td>✅</td></tr>
<tr><td>READ COMMITTED</td><td>❌</td><td>✅</td><td>✅</td></tr>
<tr><td>REPEATABLE READ</td><td>❌</td><td>❌</td><td>✅</td></tr>
<tr><td>SERIALIZABLE</td><td>❌</td><td>❌</td><td>❌</td></tr>
</table>
</div>`
}
];
