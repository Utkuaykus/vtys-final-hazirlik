# -*- coding: utf-8 -*-
"""
generate_perfect_topics.py
Generates the comprehensive, all-inclusive, 100-guarantee topic explanation guide (topics.js)
covering every single concept, formula, code example, exam trap, and comparison matrix
from all lecture slides (DBMS_4 to DBMS_14, T-SQL, Trigger, Cursor, SP, PL/SQL, Normalizasyon),
lab manual (DreamHome & Kütüphane), and university past exams.
"""

import json

TOPICS_DATA = [
    {
        "id": "iliskisel-model",
        "icon": "🔗",
        "title": "İlişkisel Model (Relational Model)",
        "priority": "medium",
        "subtitle": "DBMS_4 - E.F. Codd (1970) İlişkisel Veri Modeli, Bütünlük Kuralları & Anahtar Hiyerarşisi",
        "content": """
<div class="topic-section">
    <h3>📌 İlişkisel Modelin Doğuşu ve Temel Kavramlar</h3>
    <p>İlişkisel Veri Tabanı Yönetim Sistemi (RDBMS), 1970 yılında <strong>E.F. Codd</strong> tarafından IBM laboratuvarlarında matematiksel küme teorisine dayalı olarak geliştirilmiştir. İlişkisel modelde tüm veriler mantıksal olarak <strong>ilişkiler (tablolar / relations)</strong> şeklinde temsil edilir.</p>
    <ul>
        <li><strong>İlişki (Relation / Tablo):</strong> Satır ve sütunlardan oluşan iki boyutlu matematiksel veri yapısıdır.</li>
        <li><strong>Demet (Tuple / Satır / Record):</strong> İlişkideki tek bir varlığa ait bilgileri içeren yatay kayıttır.</li>
        <li><strong>Nitelik (Attribute / Sütun / Field):</strong> Bir varlığın adlandırılmış özelliğidir (Örn: <code>ad</code>, <code>maas</code>).</li>
        <li><strong>Etki Alanı (Domain):</strong> Bir niteliğin alabileceği geçerli atomik değerler kümesidir (Örn: Not alanı için 0-100 aralığı).</li>
        <li><strong>Derece (Degree / Arity):</strong> Bir tablodaki toplam nitelik (sütun) sayısıdır.</li>
        <li><strong>Kardinalite (Cardinality):</strong> Bir tablodaki toplam demet (satır) sayısıdır.</li>
    </ul>
</div>

<div class="topic-section">
    <h3>📐 Matematiksel İlişki Tanımı</h3>
    <p>D<sub>1</sub>, D<sub>2</sub>, ..., D<sub>n</sub> etki alanları olsun. Kartezyen Çarpım: D<sub>1</sub> × D<sub>2</sub> × ... × D<sub>n</sub> kümesidir.</p>
    <p>Bir <strong>İlişki (R)</strong>, bu Kartezyen çarpım kümesinin herhangi bir alt kümesidir: <code>R ⊆ (D₁ × D₂ × ... × Dₙ)</code>.</p>
</div>

<div class="topic-section">
    <h3>🔑 Anahtar (Key) Türleri ve Hiyerarşisi</h3>
    <table class="table-styled">
        <tr><th>Anahtar Türü</th><th>Tanım ve Özellikleri</th><th>Sınav Örneği</th></tr>
        <tr><td><strong>Süper Anahtar (Super Key)</strong></td><td>Tablodaki her bir satırı benzersiz (unique) olarak tanımlayabilen herhangi bir sütun veya sütunlar kümesidir. Fazladan gereksiz sütun içerebilir.</td><td><code>(TCKimlik, Ad, Soyad)</code></td></tr>
        <tr><td><strong>Aday Anahtar (Candidate Key)</strong></td><td>Gereksiz hiçbir sütun içermeyen <strong>minimum süper anahtardır</strong>. Kendisini oluşturan hiçbir alt küme tek başına anahtar olamaz. Asla NULL içeremez.</td><td><code>TCKimlik</code>, <code>OgrenciNo</code></td></tr>
        <tr><td><strong>Birincil Anahtar (Primary Key - PK)</strong></td><td>Aday anahtarlar arasından veritabanı tasarımcısı tarafından tablonun ana tanımlayıcısı olarak seçilen tekil anahtardır. <strong>Asla NULL olamaz!</strong></td><td><code>OgrenciNo</code></td></tr>
        <tr><td><strong>Alternatif / İkincil Anahtar (Alternate Key)</strong></td><td>Aday anahtarlar arasından birincil anahtar olarak seçilmeyen diğer aday anahtarlardır (UNIQUE kısıtı verilir).</td><td><code>TCKimlik</code></td></tr>
        <tr><td><strong>Yabancı Anahtar (Foreign Key - FK)</strong></td><td>Bir tablodaki satırı başka bir tablonun birincil (veya aday) anahtarına bağlayan referans sütunudur. Referans bütünlüğünü sağlar. NULL değer kabul edebilir.</td><td><code>BolumKod</code> (Ogrenci tablosunda)</td></tr>
        <tr><td><strong>Bileşik Anahtar (Composite Key)</strong></td><td>Birden fazla sütunun bir araya gelerek oluşturduğu tek bir birincil anahtardır.</td><td><code>(OgrenciNo, DersKod)</code></td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🛡️ İlişkisel Bütünlük Kuralları (Integrity Rules)</h3>
    <div class="info-box">
        <strong>1. Varlık Bütünlüğü (Entity Integrity):</strong><br>
        Temel bir ilişkinin Birincil Anahtarını (PK) oluşturan hiçbir sütun <strong>NULL (boş/bilinmeyen) DEĞER ALAMAZ</strong> ve her satırda benzersiz olmalıdır.
    </div>
    <div class="info-box">
        <strong>2. Referans Bütünlüğü (Referential Integrity):</strong><br>
        Bir yabancı anahtar (FK) değeri boş (NULL) değilse, mutlaka hedef tablodaki geçerli ve mevcut bir birincil anahtar değerine işaret etmelidir. 'Yetim kayıt' (orphan record) oluşamaz!
    </div>
    <div class="info-box warning">
        <strong>3. Etki Alanı Bütünlüğü (Domain Integrity):</strong><br>
        Her sütun yalnızca kendi etki alanında tanımlanan veri tipine ve CHECK kısıtlarına uygun atomik değerler alabilir.
    </div>
    <div class="info-box warning">
        <strong>4. İş / Kullanıcı Tanımlı Bütünlük (Enterprise / Business Integrity):</strong><br>
        Kurumun özel iş kurallarını zorunlu kılan kısıtlamalardır (Örn: Maaş asgari ücretten az olamaz, final notu 0-100 arası olmalıdır). Trigger ve CHECK kısıtları ile sağlanır.
    </div>
</div>
"""
    },
    {
        "id": "iliskisel-cebir",
        "icon": "🧮",
        "title": "İlişkisel Cebir (Relational Algebra)",
        "priority": "high",
        "subtitle": "DBMS_5 - Prosedürel İlişkisel İşlemler, Semboller (σ, π, ⋈, ×, ÷, ⋉) & SQL Dönüşümleri",
        "content": """
<div class="topic-section">
    <h3>📌 İlişkisel Cebir Nedir?</h3>
    <p>İlişkisel cebir, bir veya daha fazla ilişkiyi girdi alarak orijinal ilişkileri değiştirmeden sonuçta <strong>yeni bir ilişki (tablo)</strong> üreten <strong>prosedürel sorgu dilidir</strong>.</p>
    <p><strong>Kapanma (Closure) Özelliği:</strong> Her işlemin çıktısı yine bir ilişkisel tablo olduğundan, işlemler iç içe (nested) ve zincirleme olarak birleştirilebilir.</p>
</div>

<div class="topic-section">
    <h3>📐 Temel ve Türetilmiş İşlemler Tablosu</h3>
    <table class="table-styled">
        <tr><th>İşlem Adı</th><th>Sembol</th><th>Matematiksel Gösterim</th><th>SQL Eşdeğeri</th><th>Açıklama</th></tr>
        <tr><td><strong>Seçim (Selection)</strong></td><td>σ (sigma)</td><td>σ<sub>koşul</sub>(R)</td><td><code>WHERE</code></td><td>Koşulu sağlayan satırları (yatay alt küme) filtreler.</td></tr>
        <tr><td><strong>İzdüşüm (Projection)</strong></td><td>π (pi)</td><td>π<sub>sütun1, sütun2</sub>(R)</td><td><code>SELECT DISTINCT</code></td><td>Belirtilen sütunları (dikey alt küme) seçer, tekrarlı satırları eler.</td></tr>
        <tr><td><strong>Birleşim (Union)</strong></td><td>∪</td><td>R ∪ S</td><td><code>UNION</code></td><td>İki birleşim uyumlu tablonun tüm satırlarını tekrarsız birleştirir.</td></tr>
        <tr><td><strong>Küme Farkı (Difference)</strong></td><td>−</td><td>R − S</td><td><code>EXCEPT / MINUS</code></td><td>R ilişkisinde bulunup S ilişkisinde bulunmayan kayıtları verir.</td></tr>
        <tr><td><strong>Kesişim (Intersection)</strong></td><td>∩</td><td>R ∩ S = R − (R − S)</td><td><code>INTERSECT</code></td><td>Her iki ilişkide de ortak bulunan satırları verir.</td></tr>
        <tr><td><strong>Kartezyen Çarpım</strong></td><td>×</td><td>R × S</td><td><code>CROSS JOIN</code></td><td>Tüm olası satır çiftlerini üretir. Derece = n+m, Kardinalite = |R| × |S|.</td></tr>
        <tr><td><strong>Teta Birleştirme</strong></td><td>⋈<sub>θ</sub></td><td>R ⋈<sub>θ</sub> S = σ<sub>θ</sub>(R × S)</td><td><code>JOIN ... ON koşul</code></td><td>Kartezyen çarpım üzerine teta karşılaştırma koşulu (<, ≤, =, >, ≥, <>) uygular.</td></tr>
        <tr><td><strong>Doğal Birleştirme</strong></td><td>⋈</td><td>R ⋈ S</td><td><code>NATURAL JOIN</code></td><td>Ortak isimli sütunlarda eşitlik kontrolü yapar ve yinelenen sütunu teke indirir.</td></tr>
        <tr><td><strong>Bölme (Division)</strong></td><td>÷ veya /</td><td>R ÷ S</td><td>'Tümünü içeren' sorgular</td><td>S'deki tüm elemanlarla ilişkili olan R elemanlarını bulur (Örn: Tüm dersleri alan öğrenciler).</td></tr>
        <tr><td><strong>Yeniden Adlandırma</strong></td><td>ρ (rho)</td><td>ρ<sub>S</sub>(R) veya ρ<sub>(A1,A2)</sub>(R)</td><td><code>AS alias</code></td><td>İlişkiye veya niteliklerine yeni isim/takma ad verir.</td></tr>
        <tr><td><strong>Semijoin (Yarı Birleşim)</strong></td><td>⋉</td><td>R ⋉ S = π<sub>R</sub>(R ⋈ S)</td><td><code>WHERE EXISTS</code></td><td>R ve S birleştirilir ancak yalnızca R'nin sütunları sonuçta döndürülür.</td></tr>
        <tr><td><strong>Sol Dış Birleştirme</strong></td><td>⟕</td><td>R ⟕ S</td><td><code>LEFT JOIN</code></td><td>R'deki tüm kayıtlar gelir, S'de eşleşmeyenler NULL ile dolar.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>💡 Sınavda Çıkan SQL ↔ İlişkisel Cebir Dönüşüm Örnekleri</h3>
    <div class="code-example">-- Örnek 1: Yazılım bölümündeki personellerin ad ve maaşları
-- SQL: SELECT ad, maas FROM Personel WHERE bolum = 'Yazilim';
CEBİR: π_ad, maas ( σ_bolum='Yazilim' (Personel) )

-- Örnek 2: '163 Main St' adresindeki şubede çalışan personellerin bilgileri
CEBİR: Staff ⋈_Staff.branchNo=Branch.branchNo ( σ_street='163 Main St' (Branch) )

-- Örnek 3: Hiç kiralık mülk yönetmeyen personeller
CEBİR: π_staffNo(Staff) − π_staffNo(PropertyForRent)

-- Örnek 4: Tüm dersleri alan öğrenciler (Bölme / Division)
CEBİR: π_ogrNo, dersKod(Notlar) ÷ π_dersKod(Dersler)</div>
</div>
"""
    },
    {
        "id": "sql-temel",
        "icon": "💻",
        "title": "SQL (Structured Query Language) ve JOIN İşlemleri",
        "priority": "high",
        "subtitle": "DBMS_6 - Sorgulama Sırası, Filtreleme, JOIN Türleri, Alt Sorgular & Küme Mantığı",
        "content": """
<div class="topic-section">
    <h3>📌 SQL Komut Aileleri</h3>
    <table class="table-styled">
        <tr><th>Grup</th><th>Açılımı</th><th>Temel Komutlar</th><th>Görevi</th></tr>
        <tr><td><strong>DQL</strong></td><td>Data Query Language</td><td><code>SELECT</code></td><td>Verileri filtreleyip sorgulamak</td></tr>
        <tr><td><strong>DML</strong></td><td>Data Manipulation Language</td><td><code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code></td><td>Tablodaki verileri eklemek, güncellemek ve silmek</td></tr>
        <tr><td><strong>DDL</strong></td><td>Data Definition Language</td><td><code>CREATE</code>, <code>ALTER</code>, <code>DROP</code>, <code>TRUNCATE</code></td><td>Veritabanı nesnelerini oluşturmak ve değiştirmek</td></tr>
        <tr><td><strong>DCL</strong></td><td>Data Control Language</td><td><code>GRANT</code>, <code>REVOKE</code></td><td>Kullanıcı yetkilerini tanımlamak ve geri almak</td></tr>
        <tr><td><strong>TCL</strong></td><td>Transaction Control Language</td><td><code>COMMIT</code>, <code>ROLLBACK</code>, <code>SAVEPOINT</code></td><td>İşlem akışını onaylamak ve geri almak</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>⚙️ SQL Motorunun Mantıksal Çalışma Sırası (Logical Query Processing)</h3>
    <p>Bir SQL sorgusu yazıldığı sırada değil, aşağıdaki <strong>kesin mantıksal sırada</strong> çalıştırılır:</p>
    <div class="code-example">1. FROM & JOIN     → Kaynak tablolar belirlenir ve birleştirilir.
2. WHERE           → Bireysel satırlar filtrelenir (Toplama fonksiyonu KULLANILAMAZ).
3. GROUP BY        → Kalan satırlar belirtilen sütunlara göre gruplanır.
4. HAVING          → Oluşan grup özetleri filtrelenir (Toplama fonksiyonu İÇERİR).
5. SELECT          → İstenen sütunlar ve hesaplanmış alanlar hesaplanır.
6. DISTINCT        → Tekrarlayan satırlar sonuç kümesinden elenir.
7. ORDER BY        → Sonuç kümesi sıralanır (ASC / DESC).
8. TOP / LIMIT     → İstenen satır adedi sınırlandırılır.</div>
    <div class="info-box warning">
        <strong>⚠️ Kritik Sınav Tuzağı:</strong> SELECT'te tanımlanan bir takma ad (alias) <code>WHERE</code> içinde KULLANILAMAZ! Çünkü WHERE, SELECT'ten önce çalışır. Ancak <code>ORDER BY</code> içinde kullanılabilir çünkü ORDER BY en son çalışır!
    </div>
</div>

<div class="topic-section">
    <h3>🔗 JOIN (Tablo Birleştirme) Çeşitleri</h3>
    <table class="table-styled">
        <tr><th>Join Çeşidi</th><th>Sözdizimi</th><th>Sonuç Mantığı</th></tr>
        <tr><td><strong>INNER JOIN</strong></td><td><code>FROM A INNER JOIN B ON A.id = B.id</code></td><td>Yalnızca her iki tabloda da birleştirme koşulunu sağlayan (eşleşen) satırları getirir.</td></tr>
        <tr><td><strong>LEFT (OUTER) JOIN</strong></td><td><code>FROM A LEFT JOIN B ON A.id = B.id</code></td><td>Sol tablodaki (A) TÜM satırları korur; sağ tabloda (B) eşleşmeyen sütunlar <code>NULL</code> olur.</td></tr>
        <tr><td><strong>RIGHT (OUTER) JOIN</strong></td><td><code>FROM A RIGHT JOIN B ON A.id = B.id</code></td><td>Sağ tablodaki (B) TÜM satırları korur; sol tabloda (A) eşleşmeyen sütunlar <code>NULL</code> olur.</td></tr>
        <tr><td><strong>FULL (OUTER) JOIN</strong></td><td><code>FROM A FULL JOIN B ON A.id = B.id</code></td><td>Her iki tablodaki tüm satırları getirir; eşleşmeyen taraflar <code>NULL</code> ile doldurulur.</td></tr>
        <tr><td><strong>CROSS JOIN</strong></td><td><code>FROM A CROSS JOIN B</code></td><td>Koşulsuz Kartezyen Çarpımdır. A'nın her satırını B'nin her satırıyla eşler (Satır sayısı = |A| × |B|).</td></tr>
        <tr><td><strong>SELF JOIN</strong></td><td><code>FROM Staff e LEFT JOIN Staff m ON e.mgrId = m.id</code></td><td>Tablonun hiyerarşik ilişkiler için kendisine JOIN edilmesidir.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🔄 Alt Sorgular (Subqueries) & Özel Yüklemler</h3>
    <ul>
        <li><strong>Skaler Alt Sorgu:</strong> Tek bir satır ve tek bir sütun (tek bir değer) döner. <code>WHERE maas > (SELECT AVG(maas) FROM Personel)</code></li>
        <li><strong>Tablo Alt Sorgusu:</strong> Çok satır döner. <code>WHERE bolum_id IN (SELECT bolum_id FROM Bolum WHERE sehir='Ankara')</code></li>
        <li><strong>ANY / SOME:</strong> Alt sorgudan dönen değerlerin <strong>EN AZ BİRİNDEN</strong> büyük/küçük olmayı arar (Minimumdan büyük).</li>
        <li><strong>ALL:</strong> Alt sorgudan dönen değerlerin <strong>TAMAMINDAN</strong> büyük/küçük olmayı arar (Maksimumdan büyük).</li>
        <li><strong>EXISTS / NOT EXISTS:</strong> Alt sorgunun en az 1 satır üretip üretmediğini kontrol eder; ilk kayıtta TRUE döner (Hızlı ve NULL güvenlidir).</li>
    </ul>
</div>
"""
    },
    {
        "id": "sql-ddl",
        "icon": "🏗️",
        "title": "SQL Veri Tanımlama (DDL), Kısıtlar & İndeksler",
        "priority": "high",
        "subtitle": "DBMS_7 - CREATE/ALTER/DROP, Kısıtlamalar, İndeks Stratejileri, Domain & DCL",
        "content": """
<div class="topic-section">
    <h3>📌 DDL Komutları & Tablo Yönetimi</h3>
    <div class="code-example">-- Tablo Oluşturma
CREATE TABLE Ogrenci (
    ogrno VARCHAR(5) NOT NULL,
    tckimlik VARCHAR(11) NOT NULL,
    ad NVARCHAR(30) NOT NULL,
    soyad NVARCHAR(50) NOT NULL,
    bolumkod VARCHAR(3),
    kayittarih DATE DEFAULT GETDATE(),
    CONSTRAINT pk_ogrenci PRIMARY KEY (ogrno),
    CONSTRAINT uq_tc UNIQUE (tckimlik),
    CONSTRAINT fk_bolum FOREIGN KEY (bolumkod) REFERENCES Bolum(bolumkod)
        ON DELETE SET NULL ON UPDATE CASCADE,
    CONSTRAINT ck_tc CHECK (LEN(tckimlik) = 11 AND tckimlik NOT LIKE '%[^0-9]%')
);

-- Tabloyu Değiştirme (ALTER TABLE)
ALTER TABLE Ogrenci ADD eposta VARCHAR(100);
ALTER TABLE Ogrenci DROP COLUMN eposta;
ALTER TABLE Ogrenci ADD CONSTRAINT ck_ad_uzunluk CHECK (LEN(ad) >= 2);

-- Tabloyu Silme (DROP vs TRUNCATE vs DELETE)
DROP TABLE Ogrenci;        -- Tabloyu şeması ve verileriyle tamamen siler.
TRUNCATE TABLE Ogrenci;    -- Tüm satırları hızlıca siler, identity sıfırlar, DDL'dir, WHERE almaz.
DELETE FROM Ogrenci;       -- Satır satır siler, log tutar, identity sıfırlamaz, DML'dir.</div>
</div>

<div class="topic-section">
    <h3>🛡️ Yabancı Anahtar Silme/Güncelleme Eylemleri (Referential Actions)</h3>
    <table class="table-styled">
        <tr><th>Seçenek</th><th>Ana Tablodan Kayıt Silindiğinde Alt Tablo Ne Yapar?</th></tr>
        <tr><td><strong>CASCADE</strong></td><td>Ana kayda bağlı olan tüm alt kayıtları veritabanı <strong>otomatik olarak zincirleme siler</strong> (veya günceller).</td></tr>
        <tr><td><strong>SET NULL</strong></td><td>Alt tablodaki yabancı anahtar sütununu <code>NULL</code> yapar (Sütunun NULL kabul etmesi şarttır).</td></tr>
        <tr><td><strong>SET DEFAULT</strong></td><td>Alt tablodaki yabancı anahtar sütununu sütunun varsayılan (DEFAULT) değerine atar.</td></tr>
        <tr><td><strong>NO ACTION / RESTRICT</strong></td><td>Bağlı alt kayıt varsa ana kaydın silinmesini <strong>engeller ve hata fırlatır</strong> (Varsayılan davranış).</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>⚡ İndeks Türleri ve Mimari Farkları</h3>
    <table class="table-styled">
        <tr><th>Özellik</th><th>Kümelenmiş İndeks (Clustered Index)</th><th>Kümelenmemiş İndeks (Non-Clustered Index)</th></tr>
        <tr><td><strong>Fiziksel Sıralama</strong></td><td>Tablodaki veri satırlarını diskte fiziksel olarak indeks sırasına göre dizer (Sözlük gibi).</td><td>Verilerin fiziksel sırasını değiştirmez; ayrı bir B-Tree fihristi oluşturur (Kitap arkası indeksi gibi).</td></tr>
        <tr><td><strong>Tablo Başına Adet</strong></td><td><strong>Yalnızca 1 adet</strong> olabilir (Tablonun diskte tek bir fiziksel sırası vardır).</td><td>Bir tabloda <strong>birden çok (999'a kadar)</strong> tanımlanabilir.</td></tr>
        <tr><td><strong>Varsayılan Durum</strong></td><td>Tabloda <code>PRIMARY KEY</code> tanımlandığında otomatik oluşturulur.</td><td><code>UNIQUE</code> kısıtı tanımlandığında veya manuel <code>CREATE INDEX</code> ile oluşturulur.</td></tr>
        <tr><td><strong>Performans Etkisi</strong></td><td>Aralık sorgularında (BETWEEN, <, >) ve sıralamada (ORDER BY) maksimum hız sağlar.</td><td>Noktasal aramalarda (WHERE id = 5) arama anahtarını satır işaretçisine (RID/PK) eşler.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🔐 Veri Kontrol Dili (DCL)</h3>
    <div class="code-example">-- Yetki Verme (GRANT)
GRANT SELECT, INSERT ON Ogrenci TO User1;
GRANT UPDATE (maas) ON Staff TO MuhasebeUser;

-- Yetki Geri Alma (REVOKE)
REVOKE INSERT ON Ogrenci FROM User1;</div>
</div>
"""
    },
    {
        "id": "t-sql",
        "icon": "📜",
        "title": "T-SQL ile Programlama ve Akış Kontrolü",
        "priority": "high",
        "subtitle": "T-SQL_1 - Değişkenler, SET vs SELECT, Global Değişkenler, IF-ELSE, CASE, WHILE & TRY-CATCH",
        "content": """
<div class="topic-section">
    <h3>📌 T-SQL Nedir ve Değişken Yönetimi</h3>
    <p>Transact-SQL (T-SQL), Microsoft SQL Server'ın standart SQL'e döngü, şart, değişken ve hata yakalama yetenekleri kazandıran prosedürel genişletmesidir.</p>
    <div class="code-example">-- Değişken Tanımlama (DECLARE)
DECLARE @sayac INT = 0, @ad VARCHAR(50) = 'Ahmet', @fiyat MONEY;

-- Değer Atama: SET vs SELECT
SET @fiyat = 150.50;                          -- Tek değişkene sabit/ifade atar.
SELECT @ad = ad, @fiyat = maas FROM Staff WHERE staffNo = 'SG14'; -- Çoklu atama yapar.</div>
    <div class="info-box warning">
        <strong>⚠️ SELECT Atama Kuralı:</strong> Eğer <code>SELECT @degisken = kolon FROM Tablo</code> sorgusu birden fazla satır döndürürse hata vermez; değişken üzerinde her satır için atama tekrarlanır ve <strong>en son satırdaki değer</strong> değişkende kalır!
    </div>
</div>

<div class="topic-section">
    <h3>🌐 Önemli Global (Sistem) Değişkenleri</h3>
    <table class="table-styled">
        <tr><th>Global Değişken</th><th>Döndürdüğü Bilgi</th></tr>
        <tr><td><code>@@ROWCOUNT</code></td><td>En son çalıştırılan SQL ifadesinden etkilenen veya okunan satır sayısını döndürür.</td></tr>
        <tr><td><code>@@IDENTITY</code></td><td>Mevcut oturumda herhangi bir tabloda en son üretilen otomatik artan IDENTITY değerini döndürür.</td></tr>
        <tr><td><code>SCOPE_IDENTITY()</code></td><td>Yalnızca mevcut kod kapsamında (trigger'lar hariç) üretilen son IDENTITY değerini döndürür (Daha güvenlidir).</td></tr>
        <tr><td><code>@@FETCH_STATUS</code></td><td>Cursor'ın son FETCH işleminin sonucunu döner (0: Başarılı, -1: Bitti/Hata, -2: Satır silinmiş).</td></tr>
        <tr><td><code>@@ERROR</code></td><td>Son işlemde hata varsa hata numarasını, hatasız ise 0 döndürür.</td></tr>
        <tr><td><code>@@VERSION</code></td><td>SQL Server'ın sürüm, mimari ve derleme bilgilerini döndürür.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🔀 Karar Yapıları ve Döngüler</h3>
    <div class="code-example">-- 1. IF ... ELSE (Çok satırda BEGIN ... END zorunludur)
IF (@puan >= 90)
    PRINT 'AA';
ELSE IF (@puan >= 80)
    PRINT 'BA';
ELSE
BEGIN
    PRINT 'Kaldı';
    EXEC sp_BildirimGonder @puan;
END;

-- 2. CASE ... WHEN ... THEN ... ELSE ... END
SELECT staffNo, salary,
    CASE 
        WHEN salary >= 25000 THEN 'Yüksek'
        WHEN salary >= 15000 THEN 'Orta'
        ELSE 'Düşük'
    END AS MaasSeviyesi
FROM Staff;

-- 3. WHILE Döngüsü (BREAK ve CONTINUE)
DECLARE @i INT = 0;
WHILE (@i < 10)
BEGIN
    SET @i += 1;
    IF (@i = 3) CONTINUE; -- 3'ü atlar, döngü başına döner
    IF (@i = 7) BREAK;    -- 7'de döngüyü tamamen kırar ve çıkar
    PRINT @i;
END;</div>
</div>

<div class="topic-section">
    <h3>🛡️ Hata Yakalama (TRY ... CATCH)</h3>
    <div class="code-example">BEGIN TRY
    BEGIN TRANSACTION;
    UPDATE Hesaplar SET bakiye = bakiye - 1000 WHERE hesapNo = 'A1';
    UPDATE Hesaplar SET bakiye = bakiye + 1000 WHERE hesapNo = 'B2';
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION;
    PRINT 'Hata Oluştu: ' + ERROR_MESSAGE();
    PRINT 'Hata Kodu: ' + CAST(ERROR_NUMBER() AS VARCHAR(10));
END CATCH;</div>
</div>
"""
    },
    {
        "id": "stored-procedure",
        "icon": "📦",
        "title": "Saklı Yordamlar (Stored Procedures)",
        "priority": "high",
        "subtitle": "saklıYordam_SP - Parametreler, DEFAULT Değerler, OUTPUT, RETURN & Upsert Deseni",
        "content": """
<div class="topic-section">
    <h3>📌 Saklı Yordam Nedir ve Avantajları</h3>
    <p>Stored Procedure (SP), veritabanı sunucusunda saklanan, derlenmiş (precompiled) ve adıyla çağrılabilen T-SQL kod bloklarıdır.</p>
    <ul>
        <li><strong>Yüksek Performans:</strong> İlk çalıştırmada derlenip Yürütme Planı (Execution Plan) önbelleğe alınır, sonraki çağrılarda çok hızlı çalışır.</li>
        <li><strong>Ağ Trafiğinde Tasarruf:</strong> Yüzlerce satırlık sorgu yerine istemciden sunucuya sadece <code>EXEC sp_Adi</code> komutu gönderilir.</li>
        <li><strong>Güvenlik:</strong> Kullanıcılara tablolara doğrudan SELECT/INSERT yetkisi vermeden sadece SP çalıştırma (EXEC) yetkisi verilerek veri korunur.</li>
        <li><strong>SQL Injection Koruması:</strong> Parametreli çağrılar kullanıcı girdilerini sorgu kodu gibi değil saf veri olarak işler.</li>
    </ul>
</div>

<div class="topic-section">
    <h3>⚙️ Prosedür Tanımlama ve Çağırma Yöntemleri</h3>
    <div class="code-example">-- Prosedür Tanımı (Varsayılan Parametreli)
CREATE PROCEDURE sp_ParaTransfer
    @gonderen VARCHAR(10),
    @alici VARCHAR(10),
    @tutar MONEY = 100 -- Varsayılan değer
AS
BEGIN
    SET NOCOUNT ON;
    IF (SELECT bakiye FROM Hesaplar WHERE hesapNo = @gonderen) >= @tutar
    BEGIN
        UPDATE Hesaplar SET bakiye = bakiye - @tutar WHERE hesapNo = @gonderen;
        UPDATE Hesaplar SET bakiye = bakiye + @tutar WHERE hesapNo = @alici;
        PRINT 'Transfer başarılı.';
    END
    ELSE
        PRINT 'Yetersiz bakiye!';
END;
GO

-- Çağırma 1: Pozisyonel (Sıralı)
EXEC sp_ParaTransfer 'H101', 'H202', 500;

-- Çağırma 2: İsimlendirilmiş (Sıra önemsiz)
EXEC sp_ParaTransfer @alici = 'H202', @tutar = 500, @gonderen = 'H101';

-- Çağırma 3: Varsayılan Değerle (Tutar = 100 alınır)
EXEC sp_ParaTransfer 'H101', 'H202';</div>
</div>

<div class="topic-section">
    <h3>📤 OUTPUT Parametreleri ve RETURN Kullanımı</h3>
    <div class="code-example">-- OUTPUT Parametreli SP
CREATE PROC sp_OgrenciSayisi
    @bolumKod VARCHAR(3),
    @toplamOgrenci INT OUTPUT
AS
BEGIN
    SELECT @toplamOgrenci = COUNT(*) FROM Ogrenci WHERE bolumkod = @bolumKod;
END;
GO

-- OUTPUT Değerini Yakalama
DECLARE @sayi INT;
EXEC sp_OgrenciSayisi @bolumKod = 'BLG', @toplamOgrenci = @sayi OUTPUT;
PRINT 'Öğrenci Sayısı: ' + CAST(@sayi AS VARCHAR(10));</div>
    <div class="info-box">
        <strong>RETURN vs OUTPUT:</strong> <code>RETURN [sayı]</code> yalnızca tek bir tamsayı durum kodu (0 = Başarılı, 1 = Hata) dönmek için kullanılır. Veri döndürmek için <code>OUTPUT</code> parametresi kullanılır.
    </div>
</div>

<div class="topic-section">
    <h3>🔄 Sınav Klasiği: Upsert Deseni (Varsa Güncelle, Yoksa Ekle)</h3>
    <div class="code-example">CREATE PROC sp_MusteriKaydetGuncelle
    @hesapNo INT,
    @ad VARCHAR(30),
    @bakiye INT
AS
BEGIN
    IF EXISTS (SELECT 1 FROM Musteri WHERE HesapNo = @hesapNo)
        UPDATE Musteri SET Ad = @ad, bakiye = @bakiye WHERE HesapNo = @hesapNo;
    ELSE
        INSERT INTO Musteri (HesapNo, Ad, bakiye) VALUES (@hesapNo, @ad, @bakiye);
END;</div>
</div>
"""
    },
    {
        "id": "trigger",
        "icon": "⚡",
        "title": "Tetikleyiciler (Triggers) ve Olay Yönetimi",
        "priority": "high",
        "subtitle": "trigger(tetikleyici) - AFTER vs INSTEAD OF, INSERTED/DELETED Sözde Tabloları & ROLLBACK",
        "content": """
<div class="topic-section">
    <h3>📌 Tetikleyici (Trigger) Nedir ve Temel Kuralları</h3>
    <p>Tetikleyiciler; bir tabloda veya görünümde <strong>INSERT, UPDATE, DELETE</strong> olayları gerçekleştiğinde veritabanı motoru tarafından <strong>otomatik olarak</strong> devreye sokulan özel saklı kod bloklarıdır.</p>
    <ul>
        <li>Dışarıdan <strong>parametre alamazlar</strong>.</li>
        <li>Kullanıcı tarafından <strong>doğrudan EXEC ile çağrılamazlar</strong>.</li>
        <li>Kendilerini tetikleyen DML işlemiyle aynı <strong>Transaction</strong> içinde çalışırlar; trigger içinde <code>ROLLBACK TRANSACTION</code> denilirse tetikleyen asıl işlem de dahil tüm değişiklikler iptal edilir.</li>
    </ul>
</div>

<div class="topic-section">
    <h3>🔄 AFTER (FOR) vs INSTEAD OF Tetikleyicileri</h3>
    <table class="table-styled">
        <tr><th>Özellik</th><th>AFTER (FOR) Trigger</th><th>INSTEAD OF Trigger</th></tr>
        <tr><td><strong>Çalışma Zamanı</strong></td><td>Asıl DML işlemi yapıldıktan hemen sonra çalışır.</td><td>Asıl DML işlemi YAPILMAZ; onun yerine trigger gövdesi çalışır.</td></tr>
        <tr><td><strong>Tanımlandığı Nesneler</strong></td><td><strong>Yalnızca fiziksel tablolarda</strong> tanımlanabilir.</td><td><strong>Hem tablolarda hem de Görünümlerde (VIEW)</strong> tanımlanabilir.</td></tr>
        <tr><td><strong>Olay Başına Limit</strong></td><td>Bir tabloda aynı olay için <strong>birden çok</strong> olabilir.</td><td>Her olay (INSERT/UPDATE/DELETE) için <strong>en fazla 1 adet</strong> olabilir.</td></tr>
        <tr><td><strong>Kullanım Amacı</strong></td><td>Denetim loglama, stok düşme, ikincil tablo güncelleme.</td><td>Normalde güncellenemeyen karmaşık VIEW'leri güncellenebilir kılmak.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🧠 RAM'deki Mantıksal Sözde Tablolar (INSERTED ve DELETED)</h3>
    <table class="table-styled">
        <tr><th>DML Olayı</th><th>INSERTED Tablosunun Durumu</th><th>DELETED Tablosunun Durumu</th></tr>
        <tr><td><strong>INSERT</strong></td><td>Eklenen yeni satırları içerir.</td><td><strong>Boştur (Oluşmaz).</strong></td></tr>
        <tr><td><strong>DELETE</strong></td><td><strong>Boştur (Oluşmaz).</strong></td></tr><td>Silinen kayıtların eski hallerini içerir.</td></tr>
        <tr><td><strong>UPDATE</strong></td><td>Güncellenmiş <strong>YENİ</strong> değerleri içerir.</td><td>Değişmeden önceki <strong>ESKİ</strong> değerleri içerir.</td></tr>
    </table>
    <div class="info-box">
        <strong>UPDATE Mantığı:</strong> RDBMS güncelleme işlemini fiziksel olarak <code>DELETE (eski kaydı sil) + INSERT (yeni kaydı ekle)</code> olarak ele alır. Bu yüzden UPDATE anında her iki tablo da doludur!
    </div>
</div>

<div class="topic-section">
    <h3>💡 Kritik Kod Örnekleri</h3>
    <div class="code-example">-- 1. Fiyat Düşürmeyi Engelleyen AFTER UPDATE Trigger
CREATE TRIGGER tr_FiyatKontrol ON Urun
AFTER UPDATE
AS
BEGIN
    IF EXISTS (SELECT 1 FROM inserted i JOIN deleted d ON i.urunId = d.urunId WHERE i.fiyat < d.fiyat)
    BEGIN
        RAISERROR('Ürün fiyatı asla düşürülemez!', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END
END;

-- 2. Silinen Kayıtları Loglayan AFTER DELETE Trigger
CREATE TRIGGER tr_SilineniLogla ON Notbilgi
AFTER DELETE
AS
BEGIN
    INSERT INTO Notbilgi_Log (ogrno, derskod, vizenot, finalnot, silinmetarihi)
    SELECT ogrno, derskod, vizenot, finalnot, GETDATE() FROM deleted;
END;</div>
</div>
"""
    },
    {
        "id": "cursor",
        "icon": "🎯",
        "title": "İmleçler (Cursors) ve Satır Bazlı İşlemler",
        "priority": "high",
        "subtitle": "Cursor - 5 Adım, @@FETCH_STATUS, SCROLL Hareketleri & WHERE CURRENT OF",
        "content": """
<div class="topic-section">
    <h3>📌 İmleç (Cursor) Nedir ve Ne Zaman Kullanılır?</h3>
    <p>SQL normalde küme tabanlıdır (set-based). Ancak her bir satırın sırayla tek tek okunup dış bir servise parametre olarak verilmesi, özel e-posta atılması veya satır bazlı karmaşık hesaplama yapılması gerektiğinde <strong>Cursor (İmleç)</strong> kullanılır.</p>
</div>

<div class="topic-section">
    <h3>🪜 Bir Cursor'ın 5 Temel Yaşam Adımı</h3>
    <table class="table-styled">
        <tr><th>Adım</th><th>Komut</th><th>Açıklama</th></tr>
        <tr><td><strong>1. Tanımlama</strong></td><td><code>DECLARE cr_adi CURSOR FOR SELECT ...</code></td><td>Cursor'ın hangi SELECT sorgusunu işleyeceğini ve özelliklerini bildirir.</td></tr>
        <tr><td><strong>2. Açma</strong></td><td><code>OPEN cr_adi</code></td><td>Sorguyu çalıştırır, sonuç kümesini (result set) hazırlar, imleci ilk satırın öncesine koyar.</td></tr>
        <tr><td><strong>3. Okuma</strong></td><td><code>FETCH NEXT FROM cr_adi INTO @degiskenler</code></td><td>Geçerli satırdaki verileri değişkenlere aktarır ve imleci bir sonraki satıra kaydırır.</td></tr>
        <tr><td><strong>4. Kapatma</strong></td><td><code>CLOSE cr_adi</code></td><td>Sonuç kümesini kapatır, kilitleri serbest bırakır. Tanım bellekte kalır, tekrar <code>OPEN</code> edilebilir.</td></tr>
        <tr><td><strong>5. Yok Etme</strong></td><td><code>DEALLOCATE cr_adi</code></td><td>Cursor tanımını ve ayrılan tüm sistem kaynaklarını bellekten tamamen siler.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🚦 @@FETCH_STATUS Değerleri ve Anlamları</h3>
    <table class="table-styled">
        <tr><th>Değer</th><th>Durum</th><th>Anlamı</th></tr>
        <tr><td><strong>0</strong></td><td>✅ Başarılı</td><td>FETCH komutu başarıyla bir satır okudu ve değişkenlere atadı.</td></tr>
        <tr><td><strong>-1</strong></td><td>🛑 Bitti / Başarısız</td><td>Sonuç kümesinin sonuna gelindi (okunacak satır kalmadı) veya FETCH başarısız oldu.</td></tr>
        <tr><td><strong>-2</strong></td><td>⚠️ Satır Kayıp</td><td>FETCH edilmek istenen satır başka bir işlem tarafından tablodan silinmiş.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🧭 SCROLL Cursor Hareketleri & Geçerli Satırı Güncelleme</h3>
    <div class="code-example">-- SCROLL Yönlendirme Komutları:
FETCH NEXT FROM cr INTO @x;     -- Bir sonraki satır
FETCH PRIOR FROM cr INTO @x;    -- Bir önceki satır
FETCH FIRST FROM cr INTO @x;    -- En baştaki ilk satır
FETCH LAST FROM cr INTO @x;     -- En sondaki son satır
FETCH ABSOLUTE 5 FROM cr INTO @x; -- Baştan tam 5. satır
FETCH RELATIVE 2 FROM cr INTO @x; -- Mevcut konumdan 2 satır ileri

-- Geçerli Satırı Güncelleme / Silme (WHERE CURRENT OF)
UPDATE Staff SET salary = salary * 1.10 WHERE CURRENT OF cr;
DELETE FROM Staff WHERE CURRENT OF cr;</div>
</div>

<div class="topic-section">
    <h3>📝 Standart T-SQL Cursor Şablonu (Ezberlenmeli!)</h3>
    <div class="code-example">DECLARE @sNo VARCHAR(5), @sal MONEY;
DECLARE cr_staff CURSOR FOR SELECT staffNo, salary FROM Staff;

OPEN cr_staff;
FETCH NEXT FROM cr_staff INTO @sNo, @sal; -- 1. İlk FETCH (Döngü öncesi)

WHILE @@FETCH_STATUS = 0
BEGIN
    PRINT 'Personel: ' + @sNo + ' Maaş: ' + CAST(@sal AS VARCHAR(10));
    
    FETCH NEXT FROM cr_staff INTO @sNo, @sal; -- 2. Sonraki FETCH (Döngü sonunda)
END;

CLOSE cr_staff;
DEALLOCATE cr_staff;</div>
</div>
"""
    },
    {
        "id": "plsql",
        "icon": "🏛️",
        "title": "Oracle PL/SQL Mimarisi ve İleri Nesneler",
        "priority": "high",
        "subtitle": "DBMS_8 Serisi - Blok Yapısı, %TYPE / %ROWTYPE, İstisnalar, Paketler & Koleksiyonlar",
        "content": """
<div class="topic-section">
    <h3>📌 PL/SQL Blok Mimarisi</h3>
    <p>PL/SQL (Procedural Language / SQL), Oracle veritabanının blok yapılı programlama dilidir.</p>
    <div class="code-example">DECLARE       -- İsteğe bağlı: Değişken, sabit, imleç ve tip tanımları
    v_ad Personel.ad%TYPE;
    v_kayit Personel%ROWTYPE;
BEGIN         -- ZORUNLU: Çalıştırılabilir SQL ve kontrol komutları
    SELECT ad INTO v_ad FROM Personel WHERE id = 1;
    DBMS_OUTPUT.PUT_LINE('Ad: ' || v_ad);
EXCEPTION     -- İsteğe bağlı: Hata yakalama ve istisna yönetimi
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Kayıt bulunamadı!');
    WHEN TOO_MANY_ROWS THEN
        DBMS_OUTPUT.PUT_LINE('Birden çok satır döndü!');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Hata Kodu: ' || SQLCODE || ' - ' || SQLERRM);
END;
/</div>
</div>

<div class="topic-section">
    <h3>🧬 Dinamik Veri Tipleri: %TYPE ve %ROWTYPE</h3>
    <ul>
        <li><strong>%TYPE:</strong> Belirtilen tablodaki sütunun veri tipini ve boyutunu dinamik olarak miras alır. Tabloda sütun tipi değişirse kod bozulmaz. (<code>v_maas Staff.salary%TYPE;</code>)</li>
        <li><strong>%ROWTYPE:</strong> Tablonun veya imlecin TÜM satır şemasını tek bir yapılandırılmış kayıt (Record) değişkenine bağlar. (<code>v_personel Staff%ROWTYPE;</code> -> erişim: <code>v_personel.fName</code>)</li>
    </ul>
</div>

<div class="topic-section">
    <h3>📦 Paket (Package) Mimarisi</h3>
    <table class="table-styled">
        <tr><th>Bölüm</th><th>Komut</th><th>Açıklama</th></tr>
        <tr><td><strong>Paket Bildirimi (Specification)</strong></td><td><code>CREATE PACKAGE paket_adi AS ...</code></td><td>Paketin dışarıya açık olan <strong>genel (public)</strong> arayüzüdür. Fonksiyon ve yordamların sadece imzaları yer alır.</td></tr>
        <tr><td><strong>Paket Gövdesi (Body)</strong></td><td><code>CREATE PACKAGE BODY paket_adi AS ...</code></td><td>Yordam ve fonksiyonların asıl kaynak kodlarını ve dışarıya kapalı <strong>özel (private)</strong> öğelerini barındırır.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>📚 PL/SQL Koleksiyon Türleri</h3>
    <table class="table-styled">
        <tr><th>Koleksiyon Türü</th><th>Boyut / Sınır</th><th>İndeks Tipi</th><th>Kullanım Alanı</th></tr>
        <tr><td><strong>Associative Array (Index-By Table)</strong></td><td>Dinamik sınırsız</td><td>PLS_INTEGER veya VARCHAR2</td><td>Hafızada anahtar-değer (Key-Value) sözlük yapıları</td></tr>
        <tr><td><strong>Nested Table (İç İçe Tablo)</strong></td><td>Dinamik sınırsız</td><td>Sıralı tamsayı</td><td>Veritabanı sütununda da saklanabilen tek boyutlu dizi</td></tr>
        <tr><td><strong>VARRAY (Variable-Size Array)</strong></td><td>Sabit üst sınırlı (n)</td><td>1'den n'e sıralı tamsayı</td><td>Eleman sayısı önceden bilinen sabit sıralı koleksiyonlar</td></tr>
    </table>
</div>
"""
    },
    {
        "id": "er-modelleme",
        "icon": "📐",
        "title": "Varlık-İlişki (ER) Modellemesi ve Tasarım",
        "priority": "medium",
        "subtitle": "DBMS_12 - Varlık Tipleri, Nitelikler, İlişkiler, Kardinalite & Dönüşüm Kuralları",
        "content": """
<div class="topic-section">
    <h3>📌 ER Diyagramı Standart Sembolleri</h3>
    <table class="table-styled">
        <tr><th>Kavram</th><th>ER Sembolü</th><th>Açıklama ve Örnek</th></tr>
        <tr><td><strong>Güçlü Varlık (Strong Entity)</strong></td><td>Tek Çizgili Dikdörtgen</td><td>Kendi birincil anahtarına sahip bağımsız varlık (Örn: <code>Ogrenci</code>, <code>Personel</code>).</td></tr>
        <tr><td><strong>Zayıf Varlık (Weak Entity)</strong></td><td>Çift Çizgili Dikdörtgen</td><td>Varlığı başka bir güçlü varlığa bağımlı olan varlık (Örn: Personelin <code>BakmaklaYukumluOlduguKisi</code>).</td></tr>
        <tr><td><strong>Nitelik (Attribute)</strong></td><td>Tek Çizgili Oval</td><td>Varlığın bir özelliğidir (Örn: <code>Ad</code>, <code>Soyad</code>).</td></tr>
        <tr><td><strong>Birincil Anahtar Niteliği</strong></td><td>Altı Çizili Metinli Oval</td><td>Varlığı benzersiz tanımlayan nitelik (Örn: <u><code>OgrNo</code></u>).</td></tr>
        <tr><td><strong>Türetilen Nitelik (Derived)</strong></td><td>Kesikli Çizgili Oval</td><td>Değeri başka bir alandan hesaplanan nitelik (Örn: Doğum tarihinden hesaplanan <code>Yas</code>).</td></tr>
        <tr><td><strong>Çok Değerli Nitelik (Multivalued)</strong></td><td>Çift Çizgili Oval</td><td>Bir varlık için birden fazla değer alabilen nitelik (Örn: <code>TelefonNumaralari</code>).</td></tr>
        <tr><td><strong>İlişki (Relationship)</strong></td><td>Eşkenar Dörtgen (Baklava)</td><td>Varlıklar arasındaki mantıksal bağı temsil eder (Örn: <code>DersAlir</code>).</td></tr>
        <tr><td><strong>Zorunlu Katılım (Total Participation)</strong></td><td>Çift Çizgi</td><td>Varlık kümesindeki her elemanın ilişkide yer almasının zorunlu olması.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🔄 ER Modelini Tablolara Dönüştürme Kuralları</h3>
    <ul>
        <li><strong>1:N (Bire-Çok) İlişkiler:</strong> '1' tarafındaki tablonun birincil anahtarı, 'N' tarafındaki tabloya <strong>Yabancı Anahtar (FK)</strong> olarak eklenir.</li>
        <li><strong>M:N (Çoka-Çok) İlişkiler:</strong> Doğrudan tek tabloya FK eklenemez; her iki tablonun PK'lerini FK olarak alan yeni bir <strong>Bağlantı/Kavşak Tablosu (Junction Table)</strong> oluşturulur.</li>
        <li><strong>Çok Değerli Nitelikler:</strong> 1NF kuralını ihlal etmemek için varlığın PK'si ile birlikte ayrı bir tabloya taşınır.</li>
    </ul>
</div>
"""
    },
    {
        "id": "normalizasyon",
        "icon": "⚖️",
        "title": "Normalizasyon ve Fonksiyonel Bağımlılıklar",
        "priority": "high",
        "subtitle": "DBMS_14 - Anomaliler, 1NF, 2NF, 3NF, BCNF, 4NF, 5NF & Kayıpsız Ayrıştırma",
        "content": """
<div class="topic-section">
    <h3>📌 Normalizasyonun Amacı ve Veritabanı Anomalileri</h3>
    <p>Normalizasyon; ilişkisel veritabanı tasarımında <strong>gereksiz veri tekrarını (redundancy)</strong> en aza indirmek ve veri tutarsızlıklarına yol açan <strong>anomalileri</strong> ortadan kaldırmak için tabloların sistematik olarak ayrıştırılması işlemidir.</p>
    <ul>
        <li><strong>Ekleme Anomalisi (Insertion Anomaly):</strong> Bir bilgiyi kaydedebilmek için ilgisiz başka bir bilginin de zorunlu olarak girilmesinin gerekmesi (Örn: Henüz öğrencisi olmayan yeni bir bölümün sisteme eklenememesi).</li>
        <li><strong>Silme Anomalisi (Deletion Anomaly):</strong> Bir kaydı silerken istemeden o kayda bağlı başka kritik bilgilerin de tamamen yok olması (Örn: Ders kaydı silinen öğrencinin tüm okul kaydının silinmesi).</li>
        <li><strong>Güncelleme Anomalisi (Update Anomaly):</strong> Tekrarlı verinin bir satırda değiştirilip diğer satırlarda unutulması sonucu veritabanının kendi içinde çelişmesi (Veri tutarsızlığı).</li>
    </ul>
</div>

<div class="topic-section">
    <h3>📐 Fonksiyonel Bağımlılık Türleri</h3>
    <table class="table-styled">
        <tr><th>Bağımlılık Türü</th><th>Matematiksel Gösterim</th><th>Açıklama ve İhlal Ettiği Form</th></tr>
        <tr><td><strong>Tam Fonksiyonel Bağımlılık</strong></td><td><code>(A, B) -> C</code></td><td>C niteliği, bileşik anahtarın tamamına bağımlıdır; hiçbir alt parçasına bağımlı değildir.</td></tr>
        <tr><td><strong>Kısmi Bağımlılık (Partial)</strong></td><td><code>(A, B) -> C</code> iken <code>A -> C</code></td><td>Anahtar olmayan C, bileşik anahtarın yalnızca bir parçasına (A) bağlıdır. <strong>2NF'yi ihlal eder!</strong></td></tr>
        <tr><td><strong>Geçişli Bağımlılık (Transitive)</strong></td><td><code>A -> B</code> ve <code>B -> C</code> iken <code>A -> C</code></td><td>Anahtar olmayan C, anahtar olmayan başka bir B niteliğine bağımlıdır. <strong>3NF'yi ihlal eder!</strong></td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🏆 Normal Formlar Merdiveni (1NF - BCNF)</h3>
    <table class="table-styled">
        <tr><th>Normal Form</th><th>Temel Kuralı ve Şartı</th><th>Nasıl Sağlanır?</th></tr>
        <tr><td><strong>1NF (Birinci NF)</strong></td><td>Her hücrede <strong>tek bir atomik değer</strong> olmalıdır; tekrarlayan gruplar ve liste değerler bulunamaz.</td><td>Çoklu değerler satırlara bölünür veya ayrı tabloya taşınır.</td></tr>
        <tr><td><strong>2NF (İkinci NF)</strong></td><td>Tablo 1NF'de olmalı ve <strong>kısmi bağımlılık bulunmamalıdır</strong> (Anahtar olmayan alanlar bileşik PK'nin tamamına bağlı olmalıdır).</td><td>Kısmi bağımlı alanlar belirleyicisiyle birlikte yeni tabloya ayrılır. <br><em>⭐ Not: Tek sütunlu PK'si olan 1NF tablo otomatik olarak 2NF'dir!</em></td></tr>
        <tr><td><strong>3NF (Üçüncü NF)</strong></td><td>Tablo 2NF'de olmalı ve <strong>geçişli bağımlılık bulunmamalıdır</strong> (Anahtar olmayan alan başka bir anahtar olmayana bağlı olamaz).</td><td>Geçişli bağımlı alanlar (B -> C) ayrı bir tabloya taşınır.</td></tr>
        <tr><td><strong>BCNF (Boyce-Codd NF)</strong></td><td>Tablodaki her fonksiyonel bağımlılıkta (X -> Y), sol taraftaki belirleyici (X) mutlaka bir <strong>aday/süper anahtar</strong> olmalıdır.</td><td>Aday anahtar olmayan belirleyiciler ayrı tablolara ayrıştırılır.</td></tr>
    </table>
</div>
"""
    },
    {
        "id": "sql-functions",
        "icon": "⚡",
        "title": "SQL Fonksiyonları & VIEW / FUNCTION / PROCEDURE Karşılaştırması",
        "priority": "high",
        "subtitle": "sql_Functions - Metin/Tarih Fonksiyonları, UDF Türleri & Kapsamlı Karşılaştırma Matrisi",
        "content": """
<div class="topic-section">
    <h3>📊 VIEW vs FUNCTION vs PROCEDURE Karşılaştırma Matrisi (Sınavda Kesin Çıkar!)</h3>
    <table class="table-styled">
        <tr><th>Özellik / Kriter</th><th>Görünüm (VIEW)</th><th>Kullanıcı Fonksiyonu (UDF)</th><th>Saklı Yordam (PROCEDURE)</th></tr>
        <tr><td><strong>Parametre Alabilir mi?</strong></td><td>❌ Hayır (Parametre alamaz)</td><td>✅ Evet (Giriş parametresi alır)</td><td>✅ Evet (IN, OUT, DEFAULT alır)</td></tr>
        <tr><td><strong>Geriye Değer Döndürme</strong></td><td>Sanal Tablo döndürür</td><td><code>RETURNS</code> ile skaler veya tablo döner</td><td><code>OUTPUT</code> parametresi veya durum kodu döner</td></tr>
        <tr><td><strong>Sorgu İçinde Kullanım</strong></td><td><code>SELECT ... FROM ViewAdi</code></td><td><code>SELECT dbo.fn()</code> veya <code>FROM fn()</code></td><td>❌ SELECT/FROM/WHERE içinde çağrılamaz</td></tr>
        <tr><td><strong>Çalıştırma Yöntemi</strong></td><td>SELECT sorgusuyla çağrılır</td><td>SELECT sorgusu içinde çağrılır</td><td><code>EXEC / EXECUTE</code> ile çalıştırılır</td></tr>
        <tr><td><strong>Veritabanını Değiştirme (DML)</strong></td><td>Basit view güncellenebilir</td><td>❌ <strong>YASAKTIR</strong> (Yan etkisiz olmalıdır)</td><td>✅ Evet (INSERT/UPDATE/DELETE serbesttir)</td></tr>
        <tr><td><strong>Önceden Derleme (Execution Plan)</strong></td><td>Sorgu optimizasyonu yapılır</td><td>Önbelleğe alınır</td><td>✅ Evet (Tam derlenmiş yürütme planı)</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🔤 En Çok Sorulan SQL String (Metin) Fonksiyonları</h3>
    <table class="table-styled">
        <tr><th>Fonksiyon</th><th>Açıklama ve Örnek</th><th>Sonuç</th></tr>
        <tr><td><code>SUBSTRING(str, start, len)</code></td><td><code>SUBSTRING('Veritabanı', 5, 3)</code> (1 tabanlı indeksleme)</td><td><code>'tab'</code></td></tr>
        <tr><td><code>CHARINDEX(arana, metin)</code></td><td><code>CHARINDEX('tan', 'Veritabanı')</code> (Konumunu döndürür)</td><td><code>5</code></td></tr>
        <tr><td><code>LEFT(str, n) / RIGHT(str, n)</code></td><td><code>LEFT('Düzce', 3)</code> / <code>RIGHT('Düzce', 2)</code></td><td><code>'Düz'</code> / <code>'ce'</code></td></tr>
        <tr><td><code>LEN(str)</code></td><td><code>LEN('VTYS Final')</code> (Karakter sayısını verir)</td><td><code>10</code></td></tr>
        <tr><td><code>UPPER(str) / LOWER(str)</code></td><td><code>UPPER('ali')</code> / <code>LOWER('AK')</code></td><td><code>'ALİ'</code> / <code>'ak'</code></td></tr>
        <tr><td><code>LTRIM(str) / RTRIM(str)</code></td><td>Metnin solundaki/sağındaki gereksiz boşlukları temizler.</td><td>Temiz metin</td></tr>
        <tr><td><code>CONVERT(VARCHAR, date, 104)</code></td><td>Tarihi Alman/TR standardında nokta ile formatlar.</td><td><code>'17.08.2026'</code></td></tr>
    </table>
</div>
"""
    },
    {
        "id": "transaction",
        "icon": "🛡️",
        "title": "Transaction Yönetimi, ACID İlkeleri ve İzolasyon Seviyeleri",
        "priority": "medium",
        "subtitle": "DBMS_7 - ACID Kuralları, Eşzamanlılık Problemleri (Dirty Read, Phantom), Kilitleme & SAVEPOINT",
        "content": """
<div class="topic-section">
    <h3>📌 ACID İlkeleri (Transaction Temel Taşları)</h3>
    <table class="table-styled">
        <tr><th>İlke</th><th>Açılımı</th><th>Tanım ve Anlamı</th></tr>
        <tr><td><strong>A</strong></td><td><strong>Atomicity (Bölünemezlik)</strong></td><td>'Ya hep ya hiç' kuralıdır. Transaction içindeki tüm adımlar ya eksiksiz tamamlanır (COMMIT) ya da bir hata durumunda hiç yapılmamış gibi geri alınır (ROLLBACK).</td></tr>
        <tr><td><strong>C</strong></td><td><strong>Consistency (Tutarlılık)</strong></td><td>Transaction veritabanını bir geçerli tutarlı durumdan başka bir geçerli duruma geçirir. Tüm bütünlük kısıtları korunur.</td></tr>
        <tr><td><strong>I</strong></td><td><strong>Isolation (Yalıtım)</strong></td><td>Eşzamanlı çalışan işlemler birbirlerinin henüz onaylanmamış ara durumlarını görmez ve birbirlerini bozmaz.</td></tr>
        <tr><td><strong>D</strong></td><td><strong>Durability (Kalıcılık)</strong></td><td>COMMIT edilen bir işlem sistem çökse veya elektrik kesilse bile veritabanında kalıcı olarak saklanır (Transaction log garantisi).</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>⚠️ Eşzamanlılık Problemleri ve İzolasyon Seviyeleri</h3>
    <table class="table-styled">
        <tr><th>İzolasyon Seviyesi</th><th>Kirli Okuma (Dirty Read)</th><th>Tekrarlanamayan Okuma (Non-Repeatable)</th><th>Gölge Okuma (Phantom Read)</th></tr>
        <tr><td><strong>Read Uncommitted</strong></td><td>❌ Oluşabilir</td><td>❌ Oluşabilir</td><td>❌ Oluşabilir</td></tr>
        <tr><td><strong>Read Committed</strong> (Varsayılan)</td><td>✅ Engellenir</td><td>❌ Oluşabilir</td><td>❌ Oluşabilir</td></tr>
        <tr><td><strong>Repeatable Read</strong></td><td>✅ Engellenir</td><td>✅ Engellenir</td><td>❌ Oluşabilir</td></tr>
        <tr><td><strong>Serializable</strong> (En Katı)</td><td>✅ Engellenir</td><td>✅ Engellenir</td><td>✅ Engellenir</td></tr>
    </table>
</div>
"""
    }
]

# Write to topics.js
output = "// =============================================\n"
output += "// VTYS MASTER KONU ANLATIMLARI - 100 Tam Puan Rehberi\n"
output += "// Tüm ders slaytları, deney föyü ve çıkmış sınavlardan derlenmiştir.\n"
output += "// =============================================\n\n"
output += "const TOPICS = [\n"

for i, topic in enumerate(TOPICS_DATA):
    output += "{\n"
    output += f'  id: "{topic["id"]}",\n'
    output += f'  icon: "{topic["icon"]}",\n'
    output += f'  title: "{topic["title"]}",\n'
    output += f'  priority: "{topic["priority"]}",\n'
    output += f'  subtitle: "{topic["subtitle"]}",\n'
    output += f'  content: `{topic["content"].strip()}`\n'
    output += "}"
    if i < len(TOPICS_DATA) - 1:
        output += ","
    output += "\n"

output += "];\n"

with open("topics.js", "w", encoding="utf-8") as f:
    f.write(output)

print(f"topics.js başarıyla oluşturuldu! Toplam konu sayısı: {len(TOPICS_DATA)}")
