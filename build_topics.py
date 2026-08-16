# -*- coding: utf-8 -*-
"""
Script to build the ultimate, highly detailed, exhaustive VTYS subject study guide (topics.js).
Covers all 15 master chapters based on all 237 lecture slides, lab sheets, specialized PDFs,
and past exam questions.
"""

import os
import json

TOPICS = [
    # -------------------------------------------------------------
    # 1. VTYS MİMARİSİ, ANSI/SPARC & TEMEL KAVRAMLAR
    # -------------------------------------------------------------
    {
        "id": "vtys-mimari-temel",
        "icon": "🏛️",
        "title": "VTYS Mimarisi, ANSI/SPARC & Temel Kavramlar",
        "priority": "medium",
        "subtitle": "DBMS_1_ & Deney Föyü - Dosya Sistemleri vs VTYS, 3 Seviyeli ANSI/SPARC Mimarisi, Veri Bağımsızlığı & DBA",
        "content": """<div class="topic-section">
    <h3>📌 Geleneksel Dosya Sistemleri ve VTYS Karşılaştırması</h3>
    <p>Geleneksel dosya tabanlı sistemlerde veriler işletim sistemi dosyalarında (örneğin txt, csv, dat) saklanır ve her uygulama kendi dosyasını yönetir. Bu durum büyük kurumsal yapılarda ciddi problemlere yol açmıştır. <strong>Veritabanı Yönetim Sistemi (VTYS / DBMS)</strong>, verilerin merkezi, yapılandırılmış, güvenli ve bağımsız bir şekilde tanımlanmasını, depolanmasını ve sorgulanmasını sağlayan sistem yazılımıdır.</p>
    
    <table class="table-styled">
        <tr><th>Kriter / Karşılaştırma</th><th>Geleneksel Dosya Sistemi</th><th>Veritabanı Yönetim Sistemi (VTYS)</th></tr>
        <tr><td><strong>Veri Fazlalığı (Redundancy)</strong></td><td>Yüksek. Aynı veri (örn: öğrenci adresi) birden fazla departman dosyasında tekrar tekrar tutulur.</td><td>Minimum düzeyde. Veri merkezi olarak tek bir yerde tutulur, tekrarlar önlenir.</td></tr>
        <tr><td><strong>Veri Tutarsızlığı (Inconsistency)</strong></td><td>Çok yüksek. Bir dosyada güncellenen adres diğer dosyada eski kalır (Veri uyuşmazlığı).</td><td>Engellenir. Veri tek bir kaynaktan güncellenir, tüm kullanıcılar anlık tutarlı veriyi görür.</td></tr>
        <tr><td><strong>Veri İzolasyonu & Ayrıklığı</strong></td><td>Veriler farklı formatlardaki dosyalara dağılmıştır; birleştirmek yeni program yazmayı gerektirir.</td><td>Standart sorgu dilleri (SQL) ile ilişkili tablolar kolayca birleştirilir (JOIN).</td></tr>
        <tr><td><strong>Eşzamanlı Erişim (Concurrency)</strong></td><td>Aynı anda birden fazla kullanıcının yazması durumunda dosya bozulur veya kilitlenir.</td><td>Gelişmiş kilit mekanizmaları (Locking) ve Transaction yönetimi ile eşzamanlı erişim tam kontrol altındadır.</td></tr>
        <tr><td><strong>Veri Bütünlüğü (Integrity)</strong></td><td>Kısıtlar (örneğin not 0-100 arası olmalı) uygulama kodunun içine gömülmek zorundadır.</td><td>Bütünlük kısıtları (Constraints: PK, FK, CHECK) doğrudan veritabanı şemasında merkezi tanımlanır.</td></tr>
        <tr><td><strong>Güvenlik ve Yetkilendirme</strong></td><td>Dosya düzeyinde kaba izinler verilebilir; sütun veya satır bazında gizlilik sağlanamaz.</td><td>Kullanıcı ve rol bazlı ince ayarlı yetkilendirme (GRANT/REVOKE), View'ler ve şifreleme mevcuttur.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🏗️ ANSI/SPARC 3 Düzeyli Veritabanı Mimarisi</h3>
    <p>1975 yılında ANSI/SPARC komitesi tarafından önerilen bu mimarinin temel amacı <strong>kullanıcı uygulamaları ile fiziksel veritabanını birbirinden ayırmak (Veri Bağımsızlığı sağlamak)</strong>tır.</p>
    
    <div class="info-box">
        <strong>1. Dış Düzey (External Level / View Level - Görünüm Seviyesi):</strong><br>
        Son kullanıcıların ve uygulama programlarının veriyi gördüğü seviyedir. Farklı kullanıcı gruplarına (Muhasebe, İK, Öğrenci) yalnızca ihtiyaç duydukları veriler <em>View (Görünüm)</em> yapıları aracılığıyla özelleştirilerek gösterilir. Kullanıcı, veritabanının geri kalanından izoledir.
    </div>
    
    <div class="info-box">
        <strong>2. Kavramsal / Mantıksal Düzey (Conceptual Level / Logical Level):</strong><br>
        Tüm veritabanının mantıksal yapısının eksiksiz tanımlandığı seviyedir. Hangi varlıkların (tabloların), hangi niteliklerin (sütunların), hangi ilişkilerin ve bütünlük kısıtlamalarının (PK, FK, CHECK vb.) bulunduğu burada belirlenir. Fiziksel depolama detayları (diskte nasıl saklandığı) bu seviyede yer almaz.
    </div>
    
    <div class="info-box">
        <strong>3. İç / Fiziksel Düzey (Internal Level / Physical Level):</strong><br>
        Verilerin fiziksel depolama aygıtlarında (HDD, SSD) nasıl saklandığını belirten en alt seviyedir. Veri yapıları, dosya organizasyonları (B-Tree, Hash), indeksleme teknikleri, blok boyutları, sıkıştırma ve şifreleme algoritmaları burada yer alır.
    </div>
</div>

<div class="topic-section">
    <h3>🔄 Veri Bağımsızlığı (Data Independence)</h3>
    <p>Veri bağımsızlığı, üst düzeydeki şemaları veya uygulama programlarını değiştirmek zorunda kalmadan alt düzeydeki şemaları değiştirebilme yeteneğidir.</p>
    <ul>
        <li><strong>Mantıksal Veri Bağımsızlığı (Logical Data Independence):</strong> Kavramsal şemada yapılan değişikliklerin (örneğin yeni bir tablo veya sütun eklenmesi, iki tablonun bölünmesi) dış şemaları (View'leri) ve mevcut uygulama programlarını etkilememesidir. Sağlanması fiziksel veri bağımsızlığına göre daha zordur.</li>
        <li><strong>Fiziksel Veri Bağımsızlığı (Physical Data Independence):</strong> Fiziksel depolama yapısında veya indeksleme yöntemlerinde yapılan değişikliklerin (örneğin yeni bir Non-Clustered Index oluşturulması, RAID disk yapısına geçilmesi, dosya konumunun değiştirilmesi) kavramsal şemayı ve kullanıcı programlarını kesinlikle değiştirmemesidir.</li>
    </ul>
</div>

<div class="topic-section">
    <h3>👨‍💼 Veritabanı Yöneticisinin (DBA) Temel Görevleri</h3>
    <ul>
        <li><strong>Şema Tanımlama ve Değiştirme:</strong> Kavramsal ve fiziksel veritabanı şemalarının DDL komutlarıyla oluşturulması ve güncellenmesi.</li>
        <li><strong>Depolama Yapısı ve Erişim Yöntemleri:</strong> İndekslerin tasarlanması, disk alanı yönetimi ve optimizasyon.</li>
        <li><strong>Güvenlik ve Yetkilendirme:</strong> Kullanıcı hesaplarının açılması, rollere göre erişim haklarının (DCL: GRANT, REVOKE) verilmesi.</li>
        <li><strong>Yedekleme ve Kurtarma (Backup & Recovery):</strong> Sistem çökmelerine, donanım arızalarına ve felaket durumlarına karşı periyodik yedek alma ve geri yükleme planlarını yönetme.</li>
        <li><strong>Performans İzleme ve Ayarlama (Tuning):</strong> Yavaş çalışan sorguların tespiti, Execution Plan analizi ve darboğazların giderilmesi.</li>
        <li><strong>Bütünlük Kısıtlarının Korunması:</strong> Veri tutarlılığını garanti eden kural ve tetikleyicilerin denetimi.</li>
    </ul>
</div>

<div class="topic-section">
    <h3>⚠️ Sınav Püf Noktaları ve Klasik Sorular</h3>
    <div class="info-box warning">
        <strong>💡 Soru:</strong> Fiziksel veri bağımsızlığı mı yoksa mantıksal veri bağımsızlığı mı daha zordur?<br>
        <strong>Cevap:</strong> <em>Mantıksal Veri Bağımsızlığı</em> çok daha zordur. Çünkü kavramsal düzeyde bir varlık veya ilişki bölündüğünde veya değiştirildiğinde, o varlığa bağlı çalışan onlarca uygulama kodunun ve dış görünümün bozulmadan kalması gelişmiş View mimarisi gerektirir.
    </div>
</div>"""
    },

    # -------------------------------------------------------------
    # 2. İLİŞKİSEL MODEL & BÜTÜNLÜK KURALLARI
    # -------------------------------------------------------------
    {
        "id": "iliskisel-model",
        "icon": "🔗",
        "title": "İlişkisel Model & Bütünlük Kuralları",
        "priority": "medium",
        "subtitle": "DBMS_4 - E.F. Codd (1970) İlişkisel Modeli, Tablo Yapısı, Anahtar Hiyerarşisi & 4 Bütünlük Kuralı",
        "content": """<div class="topic-section">
    <h3>📌 İlişkisel Modelin Doğuşu ve Matematiksel Temeli</h3>
    <p>İlişkisel Veri Modeli, 1970 yılında <strong>Edgar Frank Codd (E.F. Codd)</strong> tarafından IBM laboratuvarlarında matematiksel küme teorisi ve birinci dereceden mantık üzerine kurulmuştur. Bu modelde tüm veriler iki boyutlu <strong>ilişkiler (relations / tablolar)</strong> şeklinde temsil edilir.</p>
    
    <ul>
        <li><strong>İlişki (Relation / Tablo):</strong> Satır ve sütunlardan oluşan iki boyutlu matematiksel kümedir.</li>
        <li><strong>Demet (Tuple / Satır / Kayıt / Record):</strong> İlişkideki tek bir varlığa ait bilgileri içeren yatay veri satırıdır.</li>
        <li><strong>Nitelik (Attribute / Sütun / Alan / Field):</strong> Bir varlığın adlandırılmış özelliğidir (Örn: <code>ad</code>, <code>maas</code>, <code>dogum_tarihi</code>).</li>
        <li><strong>Etki Alanı (Domain):</strong> Bir niteliğin alabileceği geçerli, atomik (bölünemez) değerler kümesidir (Örn: Vize Notu için <code>[0, 100]</code> aralığındaki tamsayılar).</li>
        <li><strong>Derece (Degree / Arity):</strong> Bir tablodaki toplam nitelik (sütun) sayısıdır.</li>
        <li><strong>Kardinalite (Cardinality):</strong> Bir tablodaki toplam demet (satır) sayısıdır.</li>
    </ul>

    <div class="info-box">
        <strong>📐 Matematiksel Tanım:</strong><br>
        D₁, D₂, ..., Dₙ etki alanları olsun. Kartezyen Çarpım: D₁ × D₂ × ... × Dₙ kümesidir.<br>
        Bir <strong>İlişki (R)</strong>, bu Kartezyen çarpım kümesinin herhangi bir alt kümesidir: <code>R ⊆ (D₁ × D₂ × ... × Dₙ)</code>.
    </div>
</div>

<div class="topic-section">
    <h3>📐 İlişkilerin (Tabloların) 5 Temel Matematiksel Özelliği</h3>
    <ol>
        <li><strong>Hücre Değerleri Atomiktir:</strong> Tablonun herhangi bir satır ve sütun kesişiminde (hücresinde) yalnızca TEK bir bölünemez değer bulunabilir. (Çok değerli nitelik veya dizi saklanamaz - 1NF kuralı).</li>
        <li><strong>Nitelik İsimleri Benzersizdir:</strong> Aynı tablo içerisinde aynı isimde iki sütun bulunamaz.</li>
        <li><strong>Niteliklerin (Sütunların) Sırası Önemsizdir:</strong> Sütunların soldan sağa diziliş sırası tablonun anlamını veya matematiksel eşitliğini değiştirmez.</li>
        <li><strong>Demetlerin (Satırların) Sırası Önemsizdir:</strong> Satırların yukarıdan aşağıya dizilişi anlamsızdır; çünkü ilişki bir kümedir ve kümelerde sıra yoktur.</li>
        <li><strong>Yinelenen (Duplicate) Satır Olamaz:</strong> Matematiksel küme tanımı gereği bir ilişkide birbirinin tamamen kopyası olan iki özdeş satır bulunamaz (Anahtar varlığı zorunludur).</li>
    </ol>
</div>

<div class="topic-section">
    <h3>🔑 Anahtar (Key) Hiyerarşisi ve Türleri</h3>
    <table class="table-styled">
        <tr><th>Anahtar Türü</th><th>Tanımı ve Özellikleri</th><th>Örnek / Sınav Notu</th></tr>
        <tr><td><strong>Süper Anahtar (Super Key - SK)</strong></td><td>Tablodaki her bir satırı tekil (unique) olarak belirleyen herhangi bir nitelik veya nitelikler kümesidir. İçinde gereksiz, fazladan sütunlar barındırabilir.</td><td><code>(TCKimlikNo, Ad, Soyad)</code> bir süper anahtardır.</td></tr>
        <tr><td><strong>Aday Anahtar (Candidate Key - CK)</strong></td><td>Gereksiz hiçbir nitelik içermeyen <strong>minimal süper anahtardır</strong>. Kendisinden herhangi bir sütun çıkarıldığında tekillik özelliği kaybolur. Asla NULL içeremez.</td><td><code>TCKimlikNo</code>, <code>OgrenciNo</code>, <code>Eposta</code></td></tr>
        <tr><td><strong>Birincil Anahtar (Primary Key - PK)</strong></td><td>Aday anahtarlar arasından veritabanı tasarımcısı tarafından tablonun ana tanımlayıcısı olarak seçilen tekil anahtardır. <strong>Asla NULL olamaz ve yinelenemez!</strong></td><td><code>OgrenciNo</code></td></tr>
        <tr><td><strong>Alternatif / İkincil Anahtar (Alternate Key - AK)</strong></td><td>Aday anahtarlar arasından birincil anahtar olarak seçilmeyen diğer aday anahtarlardır. Veritabanında <code>UNIQUE</code> kısıtı verilerek korunur.</td><td><code>TCKimlikNo</code> (Eğer PK OgrenciNo seçildiyse)</td></tr>
        <tr><td><strong>Yabancı Anahtar (Foreign Key - FK)</strong></td><td>Bir tablodaki satırı başka bir tablonun birincil (veya tekil) anahtarına bağlayan referans sütunudur. İlişkiler arası referans bütünlüğünü sağlar. <strong>NULL değer alabilir!</strong></td><td><code>BolumKod</code> (Ogrenci tablosundaki FK, Bolum tablosunun PK'sine işaret eder)</td></tr>
        <tr><td><strong>Bileşik Anahtar (Composite / Compound Key)</strong></td><td>Birden fazla sütunun bir araya gelerek tek bir birincil anahtar oluşturması durumudur.</td><td><code>(OgrenciNo, DersKod)</code> Notlar tablosunda.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🛡️ İlişkisel Bütünlük Kuralları (Integrity Constraints)</h3>
    <div class="info-box">
        <strong>1. Varlık Bütünlüğü (Entity Integrity):</strong><br>
        Temel bir ilişkinin Birincil Anahtarını (PK) oluşturan hiçbir sütun <strong>NULL (boş/bilinmeyen) DEĞER ALAMAZ</strong> ve her satırda mutlaka benzersiz olmalıdır.
    </div>
    <div class="info-box">
        <strong>2. Referans Bütünlüğü (Referential Integrity):</strong><br>
        Bir yabancı anahtar (FK) değeri NULL değilse, mutlaka hedef tablodaki geçerli ve mevcut bir Birincil Anahtar değerine eşit olmalıdır. Hedefte var olmayan bir değere referans verilemez ("Yetim kayıt / Orphan record" oluşamaz).
    </div>
    <div class="info-box warning">
        <strong>3. Etki Alanı Bütünlüğü (Domain Integrity):</strong><br>
        Her sütun yalnızca kendi etki alanında tanımlanan geçerli veri tipine, uzunluğa, formata ve CHECK kısıtlamalarına uygun atomik değerler alabilir.
    </div>
    <div class="info-box warning">
        <strong>4. Kurumsal / İş Kuralı Bütünlüğü (Enterprise Integrity):</strong><br>
        Kurumun özel iş mantığını zorunlu kılan kısıtlamalardır (Örn: Maaş asgari ücretten düşük olamaz, bir müşteri en fazla 5 aktif sipariş verebilir). Trigger ve CHECK kısıtları ile zorlanır.
    </div>
</div>"""
    },

    # -------------------------------------------------------------
    # 3. İLİŞKİSEL CEBİR & İLİŞKİSEL HESAP
    # -------------------------------------------------------------
    {
        "id": "iliskisel-cebir",
        "icon": "🧮",
        "title": "İlişkisel Cebir & İlişkisel Hesap (Formal Query Languages)",
        "priority": "high",
        "subtitle": "DBMS_5 & iliskiselCebir__.docx - Semboller (σ, π, ⋈, ×, ÷, ρ, ⟕, γ), Kapanma Özelliği & SQL Karşılıkları",
        "content": """<div class="topic-section">
    <h3>📌 İlişkisel Cebir Nedir? Kapanma Özelliği</h3>
    <p>İlişkisel cebir, bir veya daha fazla ilişkiyi girdi olarak alıp, girdi tablolarını değiştirmeden sonuç olarak <strong>yeni bir ilişki (tablo)</strong> üreten <strong>prosedürel (adımlı) bir sorgu dilidir</strong>.</p>
    <div class="info-box success">
        <strong>Kapanma (Closure) Özelliği:</strong> İlişkisel cebirdeki her işlemin çıktısı yine bir ilişkisel tablodur. Bu sayede işlemler iç içe (nested) ve zincirleme olarak birleştirilebilir: <code>π_ad(σ_maas>5000(Personel))</code>.
    </div>
</div>

<div class="topic-section">
    <h3>📐 Temel ve Türetilmiş Operatörler Tablosu</h3>
    <table class="table-styled">
        <tr><th>İşlem Adı</th><th>Sembol</th><th>Matematiksel Gösterim</th><th>SQL Eşdeğeri</th><th>Açıklama</th></tr>
        <tr><td><strong>Seçim (Selection)</strong></td><td>σ (sigma)</td><td>σ<sub>koşul</sub>(R)</td><td><code>WHERE</code></td><td>Koşulu sağlayan satırları (yatay filtreleme) seçer. Kardinalite azalabilir, derece değişmez.</td></tr>
        <tr><td><strong>İzdüşüm (Projection)</strong></td><td>π (pi)</td><td>π<sub>sütun1, sütun2</sub>(R)</td><td><code>SELECT DISTINCT</code></td><td>Belirtilen sütunları (dikey filtreleme) seçer, tekrarlı satırları otomatik eler. Derece değişir.</td></tr>
        <tr><td><strong>Birleşim (Union)</strong></td><td>∪</td><td>R ∪ S</td><td><code>UNION</code></td><td>İki tablonun tüm satırlarını tekrarsız birleştirir. Tablolar <em>Birleşim Uyumlu</em> olmalıdır.</td></tr>
        <tr><td><strong>Küme Farkı (Difference)</strong></td><td>−</td><td>R − S</td><td><code>EXCEPT / MINUS</code></td><td>R ilişkisinde bulunup S ilişkisinde bulunmayan kayıtları verir.</td></tr>
        <tr><td><strong>Kesişim (Intersection)</strong></td><td>∩</td><td>R ∩ S = R − (R − S)</td><td><code>INTERSECT</code></td><td>Her iki tabloda da ortak bulunan satırları döndürür.</td></tr>
        <tr><td><strong>Kartezyen Çarpım</strong></td><td>×</td><td>R × S</td><td><code>CROSS JOIN</code></td><td>Tüm olası satır çiftlerini üretir. Derece = Deg(R)+Deg(S), Kardinalite = |R| × |S|.</td></tr>
        <tr><td><strong>Teta Birleştirme</strong></td><td>⋈<sub>θ</sub></td><td>R ⋈<sub>θ</sub> S = σ<sub>θ</sub>(R × S)</td><td><code>JOIN ... ON koşul</code></td><td>Kartezyen çarpım üzerine genel bir karşılaştırma koşulu (θ: =, &lt;, &gt;, ≤, ≥, &lt;&gt;) uygular.</td></tr>
        <tr><td><strong>Doğal Birleştirme</strong></td><td>⋈</td><td>R ⋈ S</td><td><code>NATURAL JOIN</code></td><td>Aynı isimli sütunlarda eşitlik sağlar ve yinelenen ortak sütunu sonuçta TEKE indirir.</td></tr>
        <tr><td><strong>Bölme (Division)</strong></td><td>÷ veya /</td><td>R ÷ S</td><td>'Tümünü içeren' sorgular</td><td>S'deki tüm değerlerle ilişkili olan R kayıtlarını bulur (Örn: Tüm dersleri alan öğrenciler).</td></tr>
        <tr><td><strong>Yeniden Adlandırma</strong></td><td>ρ (rho)</td><td>ρ<sub>S</sub>(R) veya ρ<sub>(A1,A2)</sub>(R)</td><td><code>AS alias</code></td><td>İlişkiye veya sütunlarına yeni isim/takma ad verir.</td></tr>
        <tr><td><strong>Yarı Birleşim (Semijoin)</strong></td><td>⋉</td><td>R ⋉ S = π<sub>R</sub>(R ⋈ S)</td><td><code>WHERE EXISTS</code></td><td>S ile eşleşen R satırlarını döndürür, ancak sonuçta sadece R'nin sütunları yer alır.</td></tr>
        <tr><td><strong>Karşıt Birleşim (Antijoin)</strong></td><td>▷ veya ⋈̸</td><td>R ▷ S = R − (R ⋉ S)</td><td><code>WHERE NOT EXISTS</code></td><td>S ile eşleşmeyen R satırlarını döndürür.</td></tr>
        <tr><td><strong>Sol Dış Birleştirme</strong></td><td>⟕</td><td>R ⟕ S</td><td><code>LEFT JOIN</code></td><td>R'deki tüm kayıtlar gelir, S'de eşleşmeyen sütunlar NULL ile dolar.</td></tr>
        <tr><td><strong>Sağ Dış Birleştirme</strong></td><td>⟖</td><td>R ⟖ S</td><td><code>RIGHT JOIN</code></td><td>S'deki tüm kayıtlar gelir, R'de eşleşmeyenler NULL ile dolar.</td></tr>
        <tr><td><strong>Tam Dış Birleştirme</strong></td><td>⟗</td><td>R ⟗ S</td><td><code>FULL OUTER JOIN</code></td><td>Her iki tablodaki tüm kayıtlar gelir, eşleşmeyen yerler NULL olur.</td></tr>
        <tr><td><strong>Gruplama & Toplama</strong></td><td>γ (gamma)</td><td><sub>grup</sub>γ<sub>fonk(sütun)</sub>(R)</td><td><code>GROUP BY + Aggregate</code></td><td>Verileri gruplar ve SUM, COUNT, AVG gibi toplama fonksiyonlarını uygular.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>💡 Çıkmış Sınav Soruları ve Adım Adım SQL Dönüşümleri</h3>
    
    <div class="code-example">-- Soru 1: Üretilen ('URET') tüm ürünlerin stok kodlarını ve adlarını listeleyin.
-- SQL:
SELECT stok_kodu, ad FROM Urun WHERE uret_satinal = 'URET';
-- İLİŞKİSEL CEBİR:
π_stok_kodu, ad ( σ_uret_satinal='URET' (Urun) )</div>

    <div class="code-example">-- Soru 2: Yazılım bölümünde çalışan personellerin ad ve maaşlarını bulun.
-- SQL:
SELECT p.ad, p.maas FROM Personel p JOIN Bolum b ON p.bolum_no = b.bolum_no WHERE b.bolum_ad = 'Yazilim';
-- İLİŞKİSEL CEBİR:
π_ad, maas ( σ_bolum_ad='Yazilim' (Personel ⋈_Personel.bolum_no=Bolum.bolum_no Bolum) )</div>

    <div class="code-example">-- Soru 3: Bölme İşlemi - 'Veritabanı' bölümündeki TÜM dersleri alan öğrencilerin adları.
-- D = π_DersKod(σ_DersAd='Veritabanı'(Ders))
-- İLİŞKİSEL CEBİR:
π_OgrAd ( (π_OgrAd, DersKod (Notlar ⋈ Ogrenci)) ÷ D )</div>
</div>

<div class="topic-section">
    <h3>🎓 İlişkisel Hesap (Relational Calculus)</h3>
    <ul>
        <li><strong>Demet İlişkisel Hesap (Tuple Relational Calculus - TRC):</strong> Bildirimseldir (Declarative). <em>"Nasıl elde edileceğini"</em> değil, <em>"Neyin istendiğini"</em> belirtir: <code>{ t | P(t) }</code>.</li>
        <li><strong>Etki Alanı İlişkisel Hesap (Domain Relational Calculus - DRC):</strong> Değişkenler demetler üzerinde değil, etki alanları (nitelik değerleri) üzerinde tanımlanır: <code>{ &lt;x₁, x₂, ..., xₙ&gt; | P(x₁, x₂, ..., xₙ) }</code>.</li>
    </ul>
</div>"""
    },

    # -------------------------------------------------------------
    # 4. SQL DQL & DML: TEMEL SORGULAR, FİLTRELEME & GRUPLAMA
    # -------------------------------------------------------------
    {
        "id": "sql-temel",
        "icon": "🔍",
        "title": "SQL DQL & DML: Temel Sorgular, Filtreleme ve Gruplama",
        "priority": "high",
        "subtitle": "DBMS_6 & SQL Öğrenme Rehberi - Mantıksal Çalışma Sırası, WHERE, NULL Mantığı, GROUP BY & HAVING",
        "content": """<div class="topic-section">
    <h3>⚙️ SQL Sorgusunun Mantıksal Çalışma Sırası (Logical Query Processing)</h3>
    <p>SQL yazılırken <code>SELECT</code> ilk yazılır; ancak veritabanı motoru sorguyu çok farklı bir mantıksal sıra ile çalıştırır. Sınavlarda ve optimizasyonda en kritik konu bu sıradır:</p>
    
    <div class="code-example">1. FROM & JOIN     --> Hangi tablolardan veri alınacak? Tablolar birleştirilir.
2. ON              --> JOIN koşulu uygulanır.
3. WHERE           --> Satırlar koşula göre filtrelenir (Toplama fonksiyonu KULLANILAMAZ!).
4. GROUP BY        --> Kalan satırlar belirtilen sütunlara göre gruplanır.
5. HAVING          --> Gruplanmış veriler filtrelenir (Toplama fonksiyonu KULLANILABİLİR!).
6. SELECT          --> İstenen sütunlar hesaplanır ve listelenir.
7. DISTINCT        --> Yinelenen satırlar elenir.
8. ORDER BY        --> Sonuçlar sıralanır (ASC / DESC).
9. TOP / OFFSET    --> Belirtilen satır adedi veya aralığı alınır.</div>
    
    <div class="info-box warning">
        <strong>⚠️ Hayati Sınav Tuzağı:</strong> <code>SELECT</code> aşamasında tanımlanan bir sütun takma adı (Alias - Örn: <code>SELECT maas*12 AS YillikMaas</code>), <code>WHERE</code> veya <code>HAVING</code> içinde <strong>KULLANILAMAZ</strong>! Çünkü WHERE ve HAVING adımları SELECT'ten ÖNCE çalışır! Ancak <code>ORDER BY</code> aşamasında KULLANILABİLİR çünkü ORDER BY SELECT'ten sonra çalışır.
    </div>
</div>

<div class="topic-section">
    <h3>🔍 Filtreleme Operatörleri ve NULL Mantığı</h3>
    <table class="table-styled">
        <tr><th>Operatör</th><th>Kullanım Amacı</th><th>Örnek</th></tr>
        <tr><td><code>LIKE</code></td><td>Karakter kalıbı eşleştirme</td><td><code>ad LIKE 'A%'</code> (A ile başlayan), <code>ad LIKE '_a%'</code> (2. harfi a olan), <code>kod LIKE '[A-Z][0-9]%'</code></td></tr>
        <tr><td><code>BETWEEN ... AND</code></td><td>Sınırlar dahil aralık kontrolü</td><td><code>maas BETWEEN 5000 AND 10000</code> (5000 ve 10000 dahildir!)</td></tr>
        <tr><td><code>IN (...)</code></td><td>Liste içi eleman kontrolü</td><td><code>sehir IN ('Ankara', 'İzmir', 'Bursa')</code></td></tr>
        <tr><td><code>IS NULL / IS NOT NULL</code></td><td>Bilinmeyen/boş değer kontrolü</td><td><code>WHERE mudur_id IS NULL</code> (Kesinlikle <code>= NULL</code> YAZILAMAZ!)</td></tr>
    </table>

    <div class="info-box danger">
        <strong>⚡ Üç Değerli Mantık (Three-Valued Logic - TRUE, FALSE, UNKNOWN):</strong><br>
        SQL'de NULL bir değer değil, <em>bilinmezliktir</em>. NULL ile yapılan her türlü matematiksel ve mantıksal karşılaştırma (<code>maas = NULL</code> veya <code>maas &lt; NULL</code>) <strong>UNKNOWN (Bilinmeyen)</strong> üretir.<br>
        <code>WHERE</code> cümlesi yalnızca sonucu <strong>TRUE</strong> olan satırları getirir, <code>FALSE</code> ve <code>UNKNOWN</code> olanları eler!
    </div>
</div>

<div class="topic-section">
    <h3>📊 Toplama Fonksiyonları ve GROUP BY / HAVING Ayrımı</h3>
    <ul>
        <li><code>COUNT(*)</code>: NULL olanlar dahil tablodaki tüm satırları sayar.</li>
        <li><code>COUNT(sutun)</code>: Yalnızca ilgili sütunda <strong>NULL olmayan</strong> satırları sayar!</li>
        <li><code>COUNT(DISTINCT sutun)</code>: Tekrarsız ve NULL olmayan farklı değerleri sayar.</li>
        <li><code>SUM()</code>, <code>AVG()</code>, <code>MIN()</code>, <code>MAX()</code>: NULL değerleri hesaplamaya katmaz (ihmal eder).</li>
    </ul>

    <table class="table-styled">
        <tr><th>Karşılaştırma</th><th>WHERE</th><th>HAVING</th></tr>
        <tr><td><strong>Çalışma Zamanı</strong></td><td>Gruplamadan (GROUP BY) ÖNCE çalışır.</td><td>Gruplamadan (GROUP BY) SONRA çalışır.</td></tr>
        <tr><td><strong>Filtreleme Hedefi</strong></td><td>Bireysel satırları eler.</td><td>Oluşturulmuş grupları eler.</td></tr>
        <tr><td><strong>Toplama Fonksiyonu</strong></td><td><code>WHERE AVG(maas) > 5000</code> <strong>YAZILAMAZ! (HATA)</strong></td><td><code>HAVING AVG(maas) > 5000</code> <strong>KULLANILIR!</strong></td></tr>
    </table>

    <div class="code-example">-- Örnek: Çalışan sayısı 5'ten fazla olan departmanların ortalama maaşları
SELECT bolum_id, AVG(maas) AS OrtMaas, COUNT(*) AS KisiSayisi
FROM Personel
WHERE durum = 'Aktif'         -- 1. Satır bazında filtreleme
GROUP BY bolum_id             -- 2. Gruplama
HAVING COUNT(*) > 5           -- 3. Grup bazında filtreleme
ORDER BY OrtMaas DESC;        -- 4. Sıralama</div>
</div>

<div class="topic-section">
    <h3>✏️ DML Komutları (Data Manipulation Language)</h3>
    <div class="code-example">-- 1. INSERT (Tekli ve Çoklu Ekleme)
INSERT INTO Ogrenci (ogrno, ad, soyad, bolumkod) 
VALUES ('12345', 'Ahmet', 'Yılmaz', 'YAZ'),
       ('12346', 'Ayşe', 'Demir', 'BLG');

-- 2. INSERT INTO ... SELECT (Başka tablodan kopyalayarak ekleme)
INSERT INTO ArsivPersonel (id, ad, maas)
SELECT id, ad, maas FROM Personel WHERE cikis_tarihi IS NOT NULL;

-- 3. UPDATE (Güncelleme)
UPDATE Personel 
SET maas = maas * 1.15, prim = 500 
WHERE bolum_id = 2; -- DİKKAT: WHERE unutulursa tüm tablo güncellenir!

-- 4. DELETE (Silme)
DELETE FROM Personel WHERE cikis_tarihi < '2020-01-01'; -- WHERE unutulursa tüm satırlar silinir!</div>
</div>"""
    },

    # -------------------------------------------------------------
    # 5. JOIN TÜRLERİ, ALT SORGULAR & KÜME OPERATÖRLERİ
    # -------------------------------------------------------------
    {
        "id": "sql-joins-subqueries",
        "icon": "🔀",
        "title": "JOIN Türleri, Alt Sorgular (Subqueries) & Küme Operatörleri",
        "priority": "high",
        "subtitle": "DBMS_6 & Deney Föyü - INNER/OUTER/CROSS/SELF JOIN, Correlated Subqueries, EXISTS vs IN & UNION/EXCEPT",
        "content": """<div class="topic-section">
    <h3>🔀 JOIN Türleri ve Karşılaştırma Matrisi</h3>
    <table class="table-styled">
        <tr><th>JOIN Türü</th><th>Dönen Satırlar</th><th>Eşleşmeyen Satırların Durumu</th></tr>
        <tr><td><strong>INNER JOIN</strong></td><td>Yalnızca iki tabloda da birleştirme koşulunu sağlayan ortak satırlar.</td><td>Eşleşmeyen satırlar sonuç kümesine dahil edilmez.</td></tr>
        <tr><td><strong>LEFT (OUTER) JOIN</strong></td><td>Sol tablodaki TÜM satırlar + Sağ tablodan eşleşen satırlar.</td><td>Sağ tabloda eşleşme yoksa o tablonun sütunları <code>NULL</code> gelir.</td></tr>
        <tr><td><strong>RIGHT (OUTER) JOIN</strong></td><td>Sağ tablodaki TÜM satırlar + Sol tablodan eşleşen satırlar.</td><td>Sol tabloda eşleşme yoksa sol sütunlar <code>NULL</code> gelir.</td></tr>
        <tr><td><strong>FULL (OUTER) JOIN</strong></td><td>Her iki tablodaki TÜM satırlar.</td><td>Eşleşmeyen tüm alanlar <code>NULL</code> ile doldurulur.</td></tr>
        <tr><td><strong>CROSS JOIN</strong></td><td>İki tablonun Kartezyen Çarpımı (Her satır diğerinin her satırıyla eşleşir).</td><td>Koşul almaz. Satır sayısı = <code>|R| × |S|</code>.</td></tr>
        <tr><td><strong>SELF JOIN</strong></td><td>Bir tablonun kendisiyle birleştirilmesidir (Farklı alias'lar verilir).</td><td>Hiyerarşik yapılarda kullanılır (Örn: Personel tablosunda personel ile müdürünü eşleştirme).</td></tr>
    </table>

    <div class="code-example">-- SELF JOIN Örneği: Her personelin kendi müdürünün adıyla listelenmesi
SELECT p.ad AS CalisanAd, m.ad AS MudurAd
FROM Personel p
LEFT JOIN Personel m ON p.mudur_id = m.personel_id;</div>
</div>

<div class="topic-section">
    <h3>🔍 Alt Sorgular (Subqueries) ve Türleri</h3>
    <ul>
        <li><strong>1. Skalar Alt Sorgu (Scalar Subquery):</strong> Tam olarak tek bir satır ve tek bir sütun (tek bir atomik değer) döndürür. <code>=</code>, <code>&gt;</code>, <code>&lt;</code> gibi standart karşılaştırma operatörleriyle kullanılır.
            <div class="code-example">SELECT ad, maas FROM Personel WHERE maas > (SELECT AVG(maas) FROM Personel);</div>
        </li>
        <li><strong>2. Çok Satırlı Alt Sorgu (Multi-Row Subquery):</strong> Tek sütunlu birden fazla satır döndürür. <code>IN</code>, <code>NOT IN</code>, <code>ANY / SOME</code>, <code>ALL</code> operatörleriyle kullanılır.
            <ul>
                <li><code>&gt; ALL (alt_sorgu)</code>: Alt sorgudaki EN BÜYÜK değerden bile daha büyük olanlar.</li>
                <li><code>&gt; ANY (alt_sorgu)</code>: Alt sorgudaki EN KÜÇÜK değerden büyük olan herhangi biri.</li>
            </ul>
        </li>
        <li><strong>3. İlişkili Alt Sorgu (Correlated Subquery):</strong> İçteki alt sorgu dıştaki sorgunun geçerli satırına referans verir. Dış sorgunun her bir satırı için iç sorgu baştan tekrar tekrar çalıştırılır.
            <div class="code-example">-- Kendi departmanının ortalama maaşından fazla alan personeller
SELECT p1.ad, p1.maas, p1.bolum_id
FROM Personel p1
WHERE p1.maas > (SELECT AVG(p2.maas) FROM Personel p2 WHERE p2.bolum_id = p1.bolum_id);</div>
        </li>
    </ul>
</div>

<div class="topic-section">
    <h3>⚡ EXISTS vs IN Karşılaştırması</h3>
    <table class="table-styled">
        <tr><th>Kriter</th><th>IN Operatörü</th><th>EXISTS Operatörü</th></tr>
        <tr><td><strong>Çalışma Mantığı</strong></td><td>Alt sorgunun tüm sonuç listesini belleğe çeker ve aranan değerin bu listede olup olmadığını test eder.</td><td>Alt sorguda koşulu sağlayan EN AZ BİR satır bulunduğu anda aramayı durdurur (Kısa devre / Short-circuit TRUE döner).</td></tr>
        <tr><td><strong>NULL Tehlikesi</strong></td><td><code>NOT IN</code> alt sorgusunda tek bir NULL değer dönerse tüm sonuç <strong>BOŞ (UNKNOWN)</strong> döner!</td><td><code>NOT EXISTS</code> NULL değerlerden etkilenmez, güvenle çalışır.</td></tr>
        <tr><td><strong>Performans</strong></td><td>Küçük sabit listelerde hızlıdır.</td><td>Büyük ilişkili alt sorgularda ve indeksli tablolarda çok daha performanslıdır.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>📦 Küme Operatörleri (Set Operators)</h3>
    <ul>
        <li><code>UNION</code>: İki sorgunun sonuçlarını birleştirir ve <strong>yinelenen satırları eler (DISTINCT yapar - yavaştır)</strong>.</li>
        <li><code>UNION ALL</code>: İki sorgunun sonuçlarını yinelenenleri elemeden olduğu gibi alt alta ekler (<strong>Çok daha hızlıdır!</strong>).</li>
        <li><code>INTERSECT</code>: Her iki sorgunun da ortak ürettiği satırları verir.</li>
        <li><code>EXCEPT</code> (Oracle'da <code>MINUS</code>): Birinci sorguda olup ikinci sorguda bulunmayan satırları verir.</li>
    </ul>
    <div class="info-box">
        <strong>⚠️ Küme Uyumluluğu Kuralı:</strong> Küme operatörleriyle birleştirilen tüm sorguların SELECT listesindeki <strong>sütun sayısı aynı</strong> ve karşılıklı sütunların <strong>veri tipleri uyumlu</strong> olmalıdır!
    </div>
</div>"""
    },

    # -------------------------------------------------------------
    # 6. SQL DDL, KISITLAR, VIEW & İNDEKSLER
    # -------------------------------------------------------------
    {
        "id": "sql-ddl",
        "icon": "🏗️",
        "title": "SQL DDL, Veri Tipleri, Kısıtlar, VIEW & İndeksler",
        "priority": "high",
        "subtitle": "DBMS_7 & Deney Föyü - CREATE/ALTER TABLE, Kısıtlar (Cascade), TRUNCATE vs DELETE, VIEW (CHECK OPTION) & B-Tree İndeks",
        "content": """<div class="topic-section">
    <h3>🧱 Veri Tanımlama Dili (DDL) ve Tablo Kısıtları (Constraints)</h3>
    <div class="code-example">CREATE TABLE Bolum (
    bolum_id INT IDENTITY(1,1) PRIMARY KEY,
    bolum_kod VARCHAR(3) CONSTRAINT ck_bolumkod CHECK (bolum_kod LIKE '[A-Z][A-Z][A-Z]') UNIQUE,
    bolum_ad NVARCHAR(50) NOT NULL
);

CREATE TABLE Personel (
    personel_id INT PRIMARY KEY,
    tc_no CHAR(11) CONSTRAINT uq_tc UNIQUE NOT NULL,
    ad NVARCHAR(30) NOT NULL,
    soyad NVARCHAR(30) NOT NULL,
    maas DECIMAL(10,2) CONSTRAINT ck_maas CHECK (maas >= 0),
    bolum_id INT,
    CONSTRAINT fk_personel_bolum FOREIGN KEY (bolum_id) 
        REFERENCES Bolum(bolum_id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);</div>
</div>

<div class="topic-section">
    <h3>🛡️ Referans Eylemleri (Referential Actions - ON DELETE / ON UPDATE)</h3>
    <ul>
        <li><code>CASCADE</code>: Ana tablodaki satır silindiğinde/güncellendiğinde, ona bağlı tüm yabancı anahtarlı satırlar da otomatik olarak silinir / güncellenir.</li>
        <li><code>SET NULL</code>: Ana tablodaki satır silindiğinde/güncellendiğinde, bağlı FK sütunları <code>NULL</code> yapılır.</li>
        <li><code>SET DEFAULT</code>: Ana satır silindiğinde bağlı FK sütununa varsayılan (DEFAULT) değeri atanır.</li>
        <li><code>NO ACTION / RESTRICT</code>: Varsayılandır. Eğer bağlı kayıt varsa ana satırın silinmesine/güncellenmesine <strong>İZİN VERMEZ, HATA FIRLATIR</strong>.</li>
    </ul>
</div>

<div class="topic-section">
    <h3>🔥 DELETE vs TRUNCATE vs DROP Derin Karşılaştırması</h3>
    <table class="table-styled">
        <tr><th>Kriter</th><th>DELETE</th><th>TRUNCATE TABLE</th><th>DROP TABLE</th></tr>
        <tr><td><strong>Komut Türü</strong></td><td>DML (Veri İşleme)</td><td>DDL (Veri Tanımlama)</td><td>DDL (Veri Tanımlama)</td></tr>
        <tr><td><strong>Silme Yöntemi</strong></td><td>Satır satır siler; her satırı Transaction Log'a tek tek yazar.</td><td>Veri sayfalarını (Data Pages) deallocate eder; minimalist log tutar.</td><td>Tablo şemasını, verilerini ve indekslerini tamamen siler.</td></tr>
        <tr><td><strong>WHERE Şartı</strong></td><td>Kullanılabilir (İstenen satırlar seçilip silinebilir).</td><td><strong>KULLANILAMAZ!</strong> Tüm tabloyu boşaltır.</td><td>Kullanılamaz.</td></tr>
        <tr><td><strong>Hız / Performans</strong></td><td>Büyük tablolarda çok yavaştır.</td><td><strong>Son derece hızlıdır</strong> (Sayfa bazlı serbest bırakma).</td><td>Hızlıdır.</td></tr>
        <tr><td><strong>DML Trigger</strong></td><td>DELETE trigger'larını tetikler.</td><td><strong>Trigger'ları TETİKLEMEZ!</strong></td><td>Trigger'ları tetiklemez.</td></tr>
        <tr><td><strong>IDENTITY Sıfırlama</strong></td><td>Sayacı sıfırlamaz; kaldığı sayıdan devam eder.</td><td>IDENTITY sayacını başlangıç değerine (Seed) <strong>sıfırlar</strong>.</td><td>Tablo yok olur.</td></tr>
        <tr><td><strong>FK Kısıtı Varlığında</strong></td><td>Başka tablo tarafından FK ile referans verilse bile çalışabilir (bağlı satır yoksa).</td><td>Başka tablo tarafından referans veriliyorsa <strong>ÇALIŞMAZ (HATA VERİR)</strong>.</td><td>Referans varsa silinmez.</td></tr>
        <tr><td><strong>ROLLBACK Edilebilirlik</strong></td><td>Transaction içinde geri alınabilir.</td><td>Transaction içinde <strong>GERİ ALINABİLİR (ROLLBACK)</strong> (Yaygın sınav yanılgısı!).</td><td>Transaction içinde geri alınabilir.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>👓 Görünümler (Views) ve WITH CHECK OPTION</h3>
    <p>View, veritabanında fiziksel olarak veri saklamayan, saklanmış bir SELECT sorgusundan oluşan <strong>sanal tablodur</strong>.</p>
    <ul>
        <li><strong>Kullanım Amaçları:</strong> Güvenlik (kullanıcıdan hassas maaş vb. sütunları gizleme), karmaşık JOIN sorgularını basitleştirme, veri bağımsızlığı sağlama.</li>
        <li><strong>WITH CHECK OPTION:</strong> View üzerinden yapılan <code>INSERT</code> veya <code>UPDATE</code> işlemlerinin, View'in <code>WHERE</code> koşuluna uymasını zorunlu kılar. Koşula uymayan ekleme/güncellemeleri reddeder!</li>
    </ul>

    <div class="code-example">CREATE VIEW vw_YazilimPersonelleri AS
SELECT personel_id, ad, soyad, bolum_id, maas
FROM Personel
WHERE bolum_id = 1
WITH CHECK OPTION; -- Bu view üzerinden bolum_id <> 1 olan kayıt EKLENEMEZ!</div>
</div>

<div class="topic-section">
    <h3>🌲 İndeksler (Indexes): Clustered vs Non-Clustered Index</h3>
    <p>İndeksler, tablodaki satırlara çok daha hızlı erişebilmek için B-Tree (Dengeli Ağaç) yapısında oluşturulan özel arama veri yapılarıdır.</p>
    
    <table class="table-styled">
        <tr><th>Özellik</th><th>Kümeli İndeks (Clustered Index)</th><th>Kümesiz İndeks (Non-Clustered Index)</th></tr>
        <tr><td><strong>Fiziksel Sıralama</strong></td><td>Tablodaki fiziksel satırların diskteki diziliş sırasını belirler.</td><td>Fiziksel veriyi sıralamaz; ayrı bir alfabetik fihrist/işaretçi ağacı tutar.</td></tr>
        <tr><td><strong>Tablo Başına Adet</strong></td><td><strong>Her tabloda EN FAZLA 1 TANE olabilir!</strong></td><td>Bir tabloda çok sayıda (SQL Server'da 999'a kadar) olabilir.</td></tr>
        <tr><td><strong>Yaprak Düğümler (Leaf Nodes)</strong></td><td>Yaprak düğümler tablonun <strong>gerçek veri sayfalarının (Data Pages) ta kendisidir</strong>.</td><td>Yaprak düğümler, asıl satıra işaret eden <strong>satır işaretçileri (Row Pointer / Clustered Key)</strong> içerir.</td></tr>
        <tr><td><strong>Otomatik Oluşma</strong></td><td>Tabloda <code>PRIMARY KEY</code> tanımlandığında varsayılan olarak Clustered Index oluşturulur.</td><td><code>UNIQUE</code> kısıtı tanımlandığında varsayılan olarak Non-Clustered Index oluşturulur.</td></tr>
    </table>
</div>"""
    },

    # -------------------------------------------------------------
    # 7. T-SQL PROGRAMLAMA, DEĞİŞKENLER & AKIŞ KONTROLÜ
    # -------------------------------------------------------------
    {
        "id": "t-sql",
        "icon": "⚡",
        "title": "T-SQL Programlama, Değişkenler, Akış Kontrolü & Geçici Tablolar",
        "priority": "high",
        "subtitle": "T-SQL_1 & DBMS_8 - Değişkenler, SET vs SELECT, @@ROWCOUNT, @@IDENTITY, IF/WHILE & Geçici Tablo Türleri",
        "content": """<div class="topic-section">
    <h3>💻 T-SQL Programlama Temelleri ve Değişkenler</h3>
    <p>Transact-SQL (T-SQL), Microsoft SQL Server tarafından kullanılan, standart SQL'e değişkenler, koşul blokları, döngüler ve hata yakalama yetenekleri ekleyen prosedürel uzantıdır.</p>
    
    <div class="code-example">-- Değişken Tanımlama ve Değer Atama
DECLARE @vize INT = 70, @final INT = 85;
DECLARE @ortalama FLOAT;

-- SET ile atama: Tek bir değişkene değer atar
SET @ortalama = (@vize * 0.4) + (@final * 0.6);

-- SELECT ile atama: Aynı anda birden fazla değişkene tablodan değer atayabilir
DECLARE @ad NVARCHAR(30), @maas MONEY;
SELECT @ad = ad, @maas = maas FROM Personel WHERE personel_id = 101;</div>

    <table class="table-styled">
        <tr><th>Karşılaştırma</th><th>SET Komutu</th><th>SELECT Komutu</th></tr>
        <tr><td><strong>Standartlık</strong></td><td>ANSI SQL standardıdır.</td><td>T-SQL uzantısıdır.</td></tr>
        <tr><td><strong>Aynı Anda Atama</strong></td><td>Tek seferde yalnızca 1 değişkene atama yapabilir.</td><td>Tek bir deyimde birden fazla değişkene değer atayabilir.</td></tr>
        <tr><td><strong>Sorgu Sonucu Çok Satır Dönerse</strong></td><td><strong>HATA FIRLATIR</strong> (Subquery returned more than 1 value).</td><td>Hata vermez; <strong>en son satırdaki değeri</strong> değişkene yazar (riskli!).</td></tr>
        <tr><td><strong>Sorgu Sonucu 0 Satır Dönerse</strong></td><td>Değişkenin değerini <code>NULL</code> yapar.</td><td>Değişkenin <strong>eski değerini KORUR</strong>, değiştirmez.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🌐 Kritik Sistem Değişkenleri (Global Variables)</h3>
    <ul>
        <li><code>@@ROWCOUNT</code>: En son çalıştırılan SQL ifadesinden etkilenen (okunan, güncellenen, silinen veya eklenen) toplam satır sayısını döndürür.</li>
        <li><code>@@IDENTITY</code>: Geçerli bağlantıda (tüm kapsamlarda ve tetikleyiciler dahil) üretilen en son IDENTITY (otomatik artan) değerini döndürür.</li>
        <li><code>SCOPE_IDENTITY()</code>: <strong>(ÖNERİLEN)</strong> Yalnızca geçerli kod bloğu (scope) içinde üretilen son identity değerini döndürür; trigger'ların ürettiği değerlerden etkilenmez.</li>
        <li><code>IDENT_CURRENT('TabloAdi')</code>: Belirtilen tabloda herhangi bir kullanıcı/oturum tarafından üretilen son identity değerini verir.</li>
        <li><code>@@ERROR</code>: Son çalıştırılan ifadenin hata kodunu döner (Hata yoksa 0 döner).</li>
    </ul>
</div>

<div class="topic-section">
    <h3>🔀 Karar ve Döngü Yapıları (IF-ELSE, WHILE, CASE)</h3>
    <div class="code-example">-- IF - ELSE ve BEGIN - END Blokları
DECLARE @stok INT;
SELECT @stok = stok_miktari FROM Urunler WHERE urun_id = 5;

IF @stok &lt; 10
BEGIN
    PRINT 'Kritik stok seviyesi! Acil sipariş verilmeli.';
    UPDATE Urunler SET siparis_durum = 'Verildi' WHERE urun_id = 5;
END
ELSE
BEGIN
    PRINT 'Stok seviyesi yeterli: ' + CAST(@stok AS VARCHAR(10));
END;

-- WHILE Döngüsü (BREAK ve CONTINUE ile)
DECLARE @sayac INT = 1;
WHILE @sayac &lt;= 10
BEGIN
    IF @sayac = 5
    BEGIN
        SET @sayac = @sayac + 1;
        CONTINUE; -- 5'i atla
    END;
    IF @sayac = 9 BREAK; -- 9'da döngüyü tamamen sonlandır
    
    PRINT 'Adım: ' + CAST(@sayac AS VARCHAR(5));
    SET @sayac = @sayac + 1;
END;</div>
</div>

<div class="topic-section">
    <h3>🛡️ Hata Yönetimi: TRY - CATCH Blokları</h3>
    <div class="code-example">BEGIN TRY
    BEGIN TRANSACTION;
        UPDATE Hesaplar SET bakiye = bakiye - 500 WHERE hesap_no = 'A1';
        UPDATE Hesaplar SET bakiye = bakiye + 500 WHERE hesap_no = 'B2';
    COMMIT TRANSACTION;
    PRINT 'Transfer başarıyla tamamlandı.';
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
    PRINT 'Hata Oluştu!';
    PRINT 'Hata No: ' + CAST(ERROR_NUMBER() AS VARCHAR(10));
    PRINT 'Hata Mesajı: ' + ERROR_MESSAGE();
END CATCH;</div>
</div>

<div class="topic-section">
    <h3>📦 Geçici Tablolar, Tablo Değişkenleri ve CTE Karşılaştırması</h3>
    <table class="table-styled">
        <tr><th>Yapı</th><th>Tanımlama Sözdizimi</th><th>Kapsam ve Yaşam Süresi</th><th>Fiziksel Depolama</th></tr>
        <tr><td><strong>Yerel Geçici Tablo</strong></td><td><code>CREATE TABLE #GeciciTablo (...)</code></td><td>Yalnızca oluşturan oturumda (session) görünür. Oturum kapanınca silinir.</td><td><code>tempdb</code> veritabanında fiziksel diskte saklanır. İndeks alabilir.</td></tr>
        <tr><td><strong>Global Geçici Tablo</strong></td><td><code>CREATE TABLE ##GlobalTablo (...)</code></td><td>Tüm kullanıcılar ve bağlantılar görebilir. Oluşturan oturum kapanınca silinir.</td><td><code>tempdb</code> veritabanında saklanır.</td></tr>
        <tr><td><strong>Tablo Değişkeni</strong></td><td><code>DECLARE @TabloVar TABLE (...)</code></td><td>Yalnızca tanımlandığı batch/fonksiyon içinde yaşar. <strong>Rollback'ten ETKİLENMEZ!</strong></td><td>Bellekte (RAM) ve gerektiğinde tempdb'de saklanır. Küçük verilerde çok hızlıdır.</td></tr>
        <tr><td><strong>CTE (Ortak Tablo İfadesi)</strong></td><td><code>WITH CteAdi AS (SELECT ...)</code></td><td>Yalnızca kendisini takip eden tek bir sorgu (SELECT/INSERT/UPDATE) boyunca yaşar.</td><td>Bellekte anlık işletilir. <strong>Özyinelemeli (Recursive) sorguları destekler!</strong></td></tr>
    </table>
</div>"""
    },

    # -------------------------------------------------------------
    # 8. SAKLI YORDAMLAR (STORED PROCEDURES - SP)
    # -------------------------------------------------------------
    {
        "id": "stored-procedure",
        "icon": "⚙️",
        "title": "Saklı Yordamlar (Stored Procedures - SP)",
        "priority": "high",
        "subtitle": "saklıYordam_SP.pdf, DBMS_8 & Deney Föyü - Pre-compiled Mimari, OUTPUT Parametreleri, Güvenlik & Sınav Kodları",
        "content": """<div class="topic-section">
    <h3>📌 Saklı Yordam (Stored Procedure) Nedir? Mimarisi</h3>
    <p>Saklı Yordam (Stored Procedure), veritabanı sunucusunda derlenmiş (pre-compiled) olarak saklanan, parametre alabilen, iş kurallarını ve SQL komutlarını içeren programatik veri tabanı nesnesidir.</p>
    
    <div class="info-box success">
        <strong>🚀 Stored Procedure Kullanmanın 4 Temel Avantajı:</strong><br>
        1. <strong>Üstün Performans (Hız):</strong> İlk çalıştırıldığında Parse edilir, Optimize edilir ve Derlenmiş Yürütme Planı (Execution Plan) sunucu önbelleğine (Buffer Cache) alınır. Sonraki çağrılarda derlenmeden doğrudan önbellekten ışık hızında çalışır.<br>
        2. <strong>Ağ Trafiğini Azaltma:</strong> İstemciden sunucuya yüzlerce satırlık SQL komutu göndermek yerine yalnızca <code>EXEC sp_Adi 1, 2</code> komutu gönderilir.<br>
        3. <strong>Güvenlik ve SQL Injection Koruması:</strong> Kullanıcılara tablolara doğrudan erişim yetkisi vermek yerine sadece SP çalıştırma yetkisi (<code>GRANT EXECUTE</code>) verilir. Parametreli yapısı sayesinde zararlı SQL kodlarının enjekte edilmesini (SQL Injection) kesin olarak engeller.<br>
        4. <strong>Modülerlik ve Bakım Kolaylığı:</strong> İş mantığı tek bir merkezde güncellenir; istemci uygulamaları yeniden derleyip dağıtmaya gerek kalmaz.
    </div>
</div>

<div class="topic-section">
    <h3>📝 Stored Procedure Sözdizimi ve Parametre Türleri</h3>
    <div class="code-example">CREATE PROCEDURE sp_OgrenciNotGuncelle
    @ogr_no VARCHAR(10),            -- Giriş Parametresi (Input)
    @ders_kod VARCHAR(10),          -- Giriş Parametresi
    @vize_not INT = 0,              -- Varsayılan Değerli Parametre
    @final_not INT = 0,             -- Varsayılan Değerli Parametre
    @yeni_ortalama FLOAT OUTPUT     -- Çıkış Parametresi (Output)
AS
BEGIN
    SET NOCOUNT ON; -- Ağ trafiğini azaltır (etkilenen satır mesajını kapatır)
    
    -- Notu güncelle
    UPDATE NotBilgi 
    SET vizenot = @vize_not, finalnot = @final_not,
        ortalama = (@vize_not * 0.4) + (@final_not * 0.6)
    WHERE ogrno = @ogr_no AND derskod = @ders_kod;
    
    -- Çıkış parametresine değeri ata
    SELECT @yeni_ortalama = ortalama 
    FROM NotBilgi 
    WHERE ogrno = @ogr_no AND derskod = @ders_kod;
    
    RETURN 0; -- Başarı durum kodu döner
END;</div>
</div>

<div class="topic-section">
    <h3>⚡ Stored Procedure Çalıştırma (EXEC / EXECUTE)</h3>
    <div class="code-example">-- SP'yi Çağırma ve OUTPUT Değerini Alma
DECLARE @sonuc FLOAT;

-- Parametre isimleriyle çağırma (Sıra bağımsızdır):
EXEC sp_OgrenciNotGuncelle 
    @ogr_no = '12345', 
    @ders_kod = 'VTYS101', 
    @vize_not = 80, 
    @final_not = 90, 
    @yeni_ortalama = @sonuc OUTPUT;

PRINT 'Hesaplanan Yeni Ortalama: ' + CAST(@sonuc AS VARCHAR(10));</div>
</div>

<div class="topic-section">
    <h3>⚠️ RETURN vs OUTPUT Parametresi Sınav Farkı</h3>
    <table class="table-styled">
        <tr><th>Özellik</th><th>RETURN Komutu</th><th>OUTPUT Parametresi</th></tr>
        <tr><td><strong>Dönüş Veri Tipi</strong></td><td><strong>Yalnızca TAMSAYI (INTEGER)</strong> durum/hata kodu döndürebilir!</td><td>Her türlü SQL veri tipini (VARCHAR, DATE, FLOAT, DECIMAL vb.) döndürebilir.</td></tr>
        <tr><td><strong>Dönen Değer Sayısı</strong></td><td>Tek bir SP çağrısında yalnızca <strong>1 adet</strong> değer dönebilir.</td><td>Tek bir SP içinde <strong>istediğiniz sayıda (birden çok)</strong> OUTPUT parametresi dönebilir.</td></tr>
        <tr><td><strong>Temel Amacı</strong></td><td>İşlemin başarı durumunu (0: Başarılı, >0: Hata Kodu) bildirmek.</td><td>İşlem sonucunda üretilen verileri dışarı aktarmak.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>💡 Çıkmış Sınav Sorusu: Bakiye Kontrollü Para Transferi SP'si</h3>
    <div class="code-example">-- Soru: Hesaplar arası para transferi yapan, gönderen hesabın bakiyesi yetersizse
-- işlemi engelleyip hata mesajı veren SP'yi yazınız.
CREATE PROCEDURE sp_ParaTransferi
    @GonderenHesap VARCHAR(10),
    @AliciHesap VARCHAR(10),
    @Tutar MONEY
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @MevcutBakiye MONEY;
    
    SELECT @MevcutBakiye = bakiye FROM Hesaplar WHERE hesap_no = @GonderenHesap;
    
    IF @MevcutBakiye IS NULL
    BEGIN
        PRINT 'Gönderen hesap bulunamadı!';
        RETURN -1;
    END;
    
    IF @MevcutBakiye >= @Tutar
    BEGIN
        BEGIN TRANSACTION;
            UPDATE Hesaplar SET bakiye = bakiye - @Tutar WHERE hesap_no = @GonderenHesap;
            UPDATE Hesaplar SET bakiye = bakiye + @Tutar WHERE hesap_no = @AliciHesap;
        COMMIT TRANSACTION;
        PRINT 'Transfer başarıyla gerçekleşti.';
        RETURN 0;
    END
    ELSE
    BEGIN
        PRINT 'Yetersiz Bakiye! İşlem iptal edildi.';
        RETURN -2;
    END;
END;</div>
</div>"""
    },

    # -------------------------------------------------------------
    # 9. KULLANICI TANIMLI FONKSİYONLAR (UDF)
    # -------------------------------------------------------------
    {
        "id": "sql-functions",
        "icon": "📐",
        "title": "Kullanıcı Tanımlı Fonksiyonlar (User-Defined Functions - UDF)",
        "priority": "high",
        "subtitle": "sql_Functions.pdf, DBMS_8 & Deney Föyü - Skalar, Inline TVF, Multi-Statement TVF & SP vs Fonksiyon 6 Kritik Fark",
        "content": """<div class="topic-section">
    <h3>📌 Kullanıcı Tanımlı Fonksiyon (UDF) Nedir? Neden İhtiyaç Duyulur?</h3>
    <p>Kullanıcı tanımlı fonksiyonlar (UDF), SQL Server ve diğer VTYS'lerde hesaplama mantığını tek bir yerde toplayıp <strong>SELECT, WHERE, HAVING, JOIN</strong> ifadelerinin içinde doğrudan çağırabilmemizi sağlayan programatik nesnelerdir.</p>
    
    <div class="info-box">
        <strong>💡 Neden View veya Stored Procedure Yetmez?</strong><br>
        • View'ler dışarıdan parametre <strong>ALAMAZLAR</strong>; ancak fonksiyonlar parametre alır!<br>
        • Stored Procedure'ler bir <code>SELECT</code> sorgusunun <code>WHERE</code> veya <code>FROM</code> kısmında doğrudan <strong>KULLANILAMAZLAR</strong>; ancak fonksiyonlar sorgu içinde rahatça çağrılır.
    </div>
</div>

<div class="topic-section">
    <h3>🏷️ 3 Temel Fonksiyon Türü ve Kod Örnekleri</h3>
    
    <h4>1. Skalar Fonksiyonlar (Scalar Functions)</h4>
    <p>Girdi parametrelerini alıp sonuçta tek bir skalar değer (INT, VARCHAR, MONEY, FLOAT vb.) döndürür.</p>
    <div class="code-example">CREATE FUNCTION dbo.fn_KdvDahilFiyat
    (@Fiyat MONEY, @KdvOrani FLOAT = 0.20)
RETURNS MONEY
AS
BEGIN
    DECLARE @Sonuc MONEY;
    SET @Sonuc = @Fiyat * (1 + @KdvOrani);
    RETURN @Sonuc;
END;

-- Çağrılışı (DİKKAT: Skalar fonksiyonlarda şema adı 'dbo.' yazılması ZORUNLUDUR!):
SELECT urun_ad, fiyat, dbo.fn_KdvDahilFiyat(fiyat, 0.20) AS KdvliFiyat 
FROM Urunler 
WHERE dbo.fn_KdvDahilFiyat(fiyat, 0.20) > 1000;</div>

    <h4>2. Satır İçi Tablo Değerli Fonksiyonlar (Inline Table-Valued Functions)</h4>
    <p>Sonuç olarak bir tablo döndürür. Gövdesinde <code>BEGIN ... END</code> <strong>YOKTUR!</strong> Tek bir <code>RETURN (SELECT ...)</code> ifadesinden oluşur. Parametreli View gibi çalışır ve optimize edici tarafından doğrudan sorgu planına dahil edildiği için son derece performanslıdır.</p>
    <div class="code-example">CREATE FUNCTION dbo.fn_BolumPersonelleri (@BolumId INT)
RETURNS TABLE
AS
RETURN (
    SELECT personel_id, ad, soyad, maas, ise_giris_tarihi
    FROM Personel
    WHERE bolum_id = @BolumId
);

-- Çağrılışı (Tablo gibi FROM içinde kullanılır, dbo. zorunlu değildir):
SELECT * FROM fn_BolumPersonelleri(3) WHERE maas > 15000;</div>

    <h4>3. Çok Deyimli Tablo Değerli Fonksiyonlar (Multi-Statement TVF)</h4>
    <p>Gövdesinde bir tablo değişkeni tanımlar (<code>RETURNS @Tablo TABLE (...)</code>), <code>BEGIN ... END</code> blokları içinde karmaşık döngüler, koşullar çalıştırıp tablo değişkenini doldurur ve sonuçta bu tabloyu döndürür.</p>
    <div class="code-example">CREATE FUNCTION dbo.fn_OgrenciDurumRaporu (@DersKod VARCHAR(10))
RETURNS @Rapor TABLE (
    OgrNo VARCHAR(10),
    Ortalama FLOAT,
    Durum VARCHAR(20)
)
AS
BEGIN
    INSERT INTO @Rapor
    SELECT ogrno, ortalama,
           CASE WHEN ortalama >= 50 THEN 'GEÇTİ' ELSE 'KALDI' END
    FROM NotBilgi
    WHERE derskod = @DersKod;
    
    RETURN;
END;</div>
</div>

<div class="topic-section">
    <h3>🔥 Stored Procedure (SP) ile Fonksiyon (UDF) Arasındaki 6 Kritik Sınav Farkı</h3>
    <table class="table-styled">
        <tr><th>Karşılaştırma Kriteri</th><th>Stored Procedure (SP)</th><th>Kullanıcı Tanımlı Fonksiyon (UDF)</th></tr>
        <tr><td><strong>1. Dönüş Değeri Zorunluluğu</strong></td><td>Değer döndürmek zorunda DEĞİLDİR (0 veya N adet dönebilir).</td><td><strong>MUTLAKA tek bir değer veya tablo döndürmek ZORUNDADIR!</strong></td></tr>
        <tr><td><strong>2. Sorgu İçinde Kullanılabilirlik</strong></td><td><code>SELECT</code>, <code>WHERE</code>, <code>JOIN</code> içinde <strong>DOĞRUDAN KULLANILAMAZ!</strong> <code>EXEC</code> ile çağrılır.</td><td><code>SELECT</code>, <code>WHERE</code>, <code>HAVING</code>, <code>JOIN</code> içinde doğrudan çağrılabilir.</td></tr>
        <tr><td><strong>3. DML İzni (Veritabanı Değişikliği)</strong></td><td>Kalıcı tablolarda <code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code> yapabilir; veritabanı durumunu değiştirebilir.</td><td>Kalıcı tablolarda <strong>DML YASAKTIR!</strong> Yalnızca lokal tablo değişkenine yazabilir, veritabanı durumunu değiştiremez.</td></tr>
        <tr><td><strong>4. Transaction Yönetimi</strong></td><td><code>BEGIN TRANSACTION</code>, <code>COMMIT</code>, <code>ROLLBACK</code> blokları kullanabilir.</td><td>Transaction komutları <strong>KULLANAMAZ!</strong></td></tr>
        <tr><td><strong>5. Çıkış (OUTPUT) Parametresi</strong></td><td><code>OUTPUT</code> parametreleri tanımlanabilir.</td><td><code>OUTPUT</code> parametresi <strong>ALAMAZ!</strong> Sadece giriş parametresi alır.</td></tr>
        <tr><td><strong>6. Çağırma Biçimi</strong></td><td><code>EXEC sp_Ad parametreler</code></td><td><code>SELECT dbo.fn_Ad(parametreler)</code></td></tr>
    </table>
</div>"""
    },

    # -------------------------------------------------------------
    # 10. TETİKLEYİCİLER (TRIGGERS)
    # -------------------------------------------------------------
    {
        "id": "trigger",
        "icon": "⚡",
        "title": "Tetikleyiciler (Triggers)",
        "priority": "high",
        "subtitle": "trigger(tetikleyici).pdf, DBMS_8_2 & Deney Föyü - AFTER/INSTEAD OF, inserted/deleted Tabloları & Sınav Senaryoları",
        "content": """<div class="topic-section">
    <h3>📌 Tetikleyici (Trigger) Nedir? Çalışma Prensibi</h3>
    <p>Tetikleyici (Trigger), tablolarda veya görünümlerde belirli bir olay (INSERT, UPDATE, DELETE veya DDL olayları) gerçekleştiğinde <strong>otomatik olarak veritabanı motoru tarafından devreye sokulan</strong> özel saklı yordam türüdür. Doğrudan <code>EXEC</code> ile çağrılamazlar; olay tabanlı (event-driven) çalışırlar.</p>
</div>

<div class="topic-section">
    <h3>🏷️ Tetikleyici Türleri</h3>
    <div class="info-box">
        <strong>1. AFTER / FOR Triggers (Sonradan Çalışan Tetikleyiciler):</strong><br>
        Olay (INSERT/UPDATE/DELETE) gerçekleştikten, tüm kısıtlamalar (Constraints) kontrol edilip doğrulandıktan sonra çalışır. <strong>Yalnızca temel tablolarda tanımlanabilir</strong> (View'lerde AFTER trigger tanımlanamaz).
    </div>
    <div class="info-box warning">
        <strong>2. INSTEAD OF Triggers (Yerine Çalışan Tetikleyiciler):</strong><br>
        Olayın ASIL İŞLEMİNİN YERİNE çalışır! Yani asıl INSERT/UPDATE/DELETE komutu icra edilmez; onun yerine tetikleyicinin gövdesindeki T-SQL komutları icra edilir.<br>
        <strong>Kritik Sınav Özelliği:</strong> Hem tablolarda hem de <strong>Görünümlerde (Views)</strong> tanımlanabilir. Birden fazla tablodan oluşan ve doğrudan güncellenemeyen (non-updatable) View'leri güncellenebilir kılmak için <code>INSTEAD OF Trigger</code> kullanılır!
    </div>
    <div class="info-box">
        <strong>3. DDL Triggers:</strong><br>
        <code>CREATE_TABLE</code>, <code>ALTER_TABLE</code>, <code>DROP_TABLE</code> gibi DDL komutlarında sunucu veya veritabanı düzeyinde tetiklenir (Tablo silinmesini engellemek veya şema değişikliklerini loglamak için).
    </div>
</div>

<div class="topic-section">
    <h3>🪄 Sanal Bellek Tabloları: inserted ve deleted Tabloları (Magic Tables)</h3>
    <p>Tetikleyiciler çalışırken SQL Server arka planda RAM'de iki geçici sanal tablo oluşturur: <code>inserted</code> ve <code>deleted</code>. Bu tabloların şeması tetikleyicinin bağlı olduğu tablonun şemasıyla birebir aynıdır.</p>
    
    <table class="table-styled">
        <tr><th>DML İşlemi</th><th><code>inserted</code> Tablosunun Durumu</th><th><code>deleted</code> Tablosunun Durumu</th><th>Açıklama</th></tr>
        <tr><td><strong>INSERT</strong></td><td><strong>YENİ eklenen satırları</strong> içerir.</td><td><strong>BOŞTUR</strong> (Hiçbir satır yoktur).</td><td>Yeni kayıtlar inserted tablosundadır.</td></tr>
        <tr><td><strong>DELETE</strong></td><td><strong>BOŞTUR</strong>.</td><td><strong>SİLİNEN eski satırları</strong> içerir.</td><td>Silinen kayıtlar deleted tablosundan okunabilir.</td></tr>
        <tr><td><strong>UPDATE</strong></td><td>Güncelleme sonrası <strong>YENİ değerleri</strong> içerir.</td><td>Güncelleme öncesi <strong>ESKİ değerleri</strong> içerir.</td><td>UPDATE işlemi mantıksal olarak "Eski satırı sil (deleted) + Yeni satırı ekle (inserted)" işlemidir!</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>⚠️ Tetikleyicilerde Hayati Sınav Kuralları ve Tuzaklar</h3>
    <ul>
        <li><strong>Çok Satırlı İşlem Tuzağı (Multi-row Statement):</strong> Tetikleyici tek satırlık işlemde de, 10.000 satırlık toplu INSERT işleminde de <strong>YALNIZCA BİR KEZ ÇALIŞIR</strong> (Statement-level trigger). Bu yüzden tetikleyici içinde <code>SELECT @x = sutun FROM inserted</code> yazmak HATALIDIR! Mutlaka <code>JOIN inserted</code> veya <code>JOIN deleted</code> kullanılmalıdır!</li>
        <li><code>UPDATE(sutun_adi)</code> Fonksiyonu: Belirli bir sütunun güncellenip güncellenmediğini kontrol etmek için IF bloğunda <code>IF UPDATE(maas)</code> şeklinde kullanılır.</li>
        <li><code>ROLLBACK TRANSACTION</code>: Tetikleyici içinde bir iş kuralı ihlali tespit edildiğinde çağrılırsa, tetikleyiciyi ateşleyen ana DML işlemi tamamen iptal edilir ve geri alınır.</li>
    </ul>
</div>

<div class="topic-section">
    <h3>💡 Çıkmış Sınav Senaryoları ve Çözümlü Kodlar</h3>
    
    <div class="code-example">-- Senaryo 1: Silinen müşterileri otomatik olarak 'Musteri_Log' tablosuna arşivleyen Trigger
CREATE TRIGGER trg_MusteriSilindiLog
ON Musteri
AFTER DELETE
AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO Musteri_Log (musteri_id, ad, soyad, silinme_tarihi, silen_kullanici)
    SELECT musteri_id, ad, soyad, GETDATE(), SUSER_SNAME()
    FROM deleted; -- Silinen kayıtlar deleted tablosundan toplu çekilir
END;</div>

    <div class="code-example">-- Senaryo 2: Stok miktarından fazla satış yapılmasını engelleyen Trigger
CREATE TRIGGER trg_SatisKontrol
ON Satislar
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;
    -- Eğer satılan miktar stoktan fazlaysa işlemi iptal et
    IF EXISTS (
        SELECT 1 
        FROM inserted i 
        JOIN Urunler u ON i.urun_id = u.urun_id 
        WHERE i.adet > u.stok_miktari
    )
    BEGIN
        RAISERROR ('Yetersiz stok! Satış işlemi gerçekleştirilemez.', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END;
    
    -- Stok yeterliyse stok miktarını düş
    UPDATE u
    SET u.stok_miktari = u.stok_miktari - i.adet
    FROM Urunler u
    JOIN inserted i ON u.urun_id = i.urun_id;
END;</div>
</div>"""
    },

    # -------------------------------------------------------------
    # 11. İMLEÇLER (CURSORS)
    # -------------------------------------------------------------
    {
        "id": "cursor",
        "icon": "🎯",
        "title": "İmleçler (Cursors)",
        "priority": "high",
        "subtitle": "Cursor.pptx, DBMS_8 & Deney Föyü - Satır Satır (RBAR) İşlem, 6 Aşamalı Yaşam Döngüsü, @@FETCH_STATUS & Türler",
        "content": """<div class="topic-section">
    <h3>📌 İmleç (Cursor) Mantığı: RBAR vs Set-Based</h3>
    <p>İlişkisel veritabanları doğası gereği <strong>küme tabanlı (Set-Based)</strong> çalışır; yani tek bir sorguyla binlerce satır aynı anda işlenir. Ancak bazen her bir satır üzerinde ayrı ayrı karmaşık döngüler, koşullar veya dış sistem çağrıları yapılması gerekir. Bir SELECT sorgusunun sonuç kümesindeki satırları <strong>satır satır (Row-By-Agonizing-Row - RBAR)</strong> gezinmeye yarayan mekanizmaya <strong>İmleç (Cursor)</strong> denir.</p>
    
    <div class="info-box warning">
        <strong>⚠️ İmleçlerin Dezavantajları:</strong> İmleçler sunucu belleğinde (RAM) kaynak tüketir, kilitleri uzun süre tutarak eşzamanlılığı düşürür ve küme tabanlı SQL'e göre çok daha yavaştır. Bu yüzden yalnızca başka alternatif olmadığında tercih edilmelidir.
    </div>
</div>

<div class="topic-section">
    <h3>🔄 6 Aşamalı İmleç Yaşam Döngüsü (Cursor Lifecycle)</h3>
    <ol>
        <li><strong>1. DECLARE CURSOR:</strong> İmlecin adı ve gezeceği SELECT sorgusu tanımlanır.</li>
        <li><strong>2. OPEN:</strong> İmleç açılır, SELECT sorgusu çalıştırılır ve sonuç kümesi belleğe alınır; gösterici ilk satırın öncesine konumlanır.</li>
        <li><strong>3. FETCH NEXT:</strong> İlk satır okunur ve değerler <code>INTO @degiskenler</code> ile değişkenlere atanır.</li>
        <li><strong>4. WHILE @@FETCH_STATUS = 0:</strong> Döngü başlatılır; satır işlenir ve döngü sonunda bir sonraki satırı okumak için tekrar <code>FETCH NEXT</code> çağrılır.</li>
        <li><strong>5. CLOSE:</strong> İmleç kapatılır, veri seti ve kilitler serbest bırakılır (ancak imleç tanımı hafızadadır, tekrar <code>OPEN</code> yapılabilir).</li>
        <li><strong>6. DEALLOCATE:</strong> İmleç referansı bellekten tamamen silinir.</li>
    </ol>
</div>

<div class="topic-section">
    <h3>⚙️ @@FETCH_STATUS Değerleri ve Anlamları</h3>
    <table class="table-styled">
        <tr><th>Dönen Değer</th><th>Durum Anlamı</th><th>Döngü Davranışı</th></tr>
        <tr><td><code>0</code></td><td><strong>Başarılı!</strong> Satır başarıyla okundu ve değişkenlere yüklendi.</td><td>Döngü devam eder (<code>WHILE @@FETCH_STATUS = 0</code>).</td></tr>
        <tr><td><code>-1</code></td><td><strong>Başarısız / Sona Gelindi!</strong> Okunacak başka satır kalmadı veya imleç sınırlarının dışına çıkıldı.</td><td>Döngüden çıkılır.</td></tr>
        <tr><td><code>-2</code></td><td><strong>Satır Kayıp / Silinmiş!</strong> Okunmak istenen satır başka bir kullanıcı tarafından silinmiş.</td><td>Döngüden çıkılır.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>💻 Eksiksiz İmleç Kod Şablonu (Çıkmış Sınav Sorusu)</h3>
    <div class="code-example">-- Soru: Personel tablosundaki çalışanların maaşlarını kıdem yıllarına göre
-- satır satır inceleyip güncelleyen T-SQL imlecini yazınız.
DECLARE @id INT, @maas MONEY, @yil INT;

-- 1. İmleci Tanımla
DECLARE cur_MaasGuncelle CURSOR FOR
SELECT personel_id, maas, DATEDIFF(YEAR, ise_giris, GETDATE())
FROM Personel;

-- 2. İmleci Aç
OPEN cur_MaasGuncelle;

-- 3. İlk Satırı Oku
FETCH NEXT FROM cur_MaasGuncelle INTO @id, @maas, @yil;

-- 4. Döngü ile Tüm Satırları Gez
WHILE @@FETCH_STATUS = 0
BEGIN
    IF @yil >= 10
        UPDATE Personel SET maas = @maas * 1.20 WHERE personel_id = @id;
    ELSE IF @yil >= 5
        UPDATE Personel SET maas = @maas * 1.10 WHERE personel_id = @id;
    
    -- Bir sonraki satıra geç (DİKKAT: Unutulursa sonsuz döngüye girer!)
    FETCH NEXT FROM cur_MaasGuncelle INTO @id, @maas, @yil;
END;

-- 5. İmleci Kapat
CLOSE cur_MaasGuncelle;

-- 6. Bellekten Tamamen Temizle
DEALLOCATE cur_MaasGuncelle;</div>
</div>

<div class="topic-section">
    <h3>🧭 İmleç Türleri ve SCROLL Seçenekleri</h3>
    <ul>
        <li><code>FAST_FORWARD</code>: Yalnızca ileri yönlü okuma yapan, salt okunur (read-only) ve en yüksek performanslı imleç türüdür.</li>
        <li><code>STATIC</code>: Verilerin anlık bir kopyasını tempdb'ye alır. Diğer kullanıcıların yaptığı değişiklikleri görmez.</li>
        <li><code>DYNAMIC</code>: Tablodaki tüm ekleme, silme ve güncellemeleri anlık olarak imlece yansıtır.</li>
        <li><code>SCROLL</code>: İki yönlü serbest gezinmeyi sağlar. Desteklediği FETCH komutları:
            <ul>
                <li><code>FETCH FIRST</code>: İlk satıra gider.</li>
                <li><code>FETCH LAST</code>: Son satıra gider.</li>
                <li><code>FETCH PRIOR</code>: Bir önceki satıra döner.</li>
                <li><code>FETCH ABSOLUTE n</code>: Baştan n. sıradaki satıra doğrudan gider.</li>
                <li><code>FETCH RELATIVE n</code>: Geçerli konumdan n satır ileri/geri gider.</li>
            </ul>
        </li>
    </ul>
</div>"""
    },

    # -------------------------------------------------------------
    # 12. ORACLE PL/SQL PROGRAMLAMA & PAKETLER
    # -------------------------------------------------------------
    {
        "id": "plsql",
        "icon": "🏛️",
        "title": "Oracle PL/SQL Programlama & Paketler",
        "priority": "high",
        "subtitle": "DBMS_8, DBMS_8_1, DBMS_8_2 & Deney Föyü - Blok Yapısı, %TYPE, %ROWTYPE, Cursor FOR Loop, Exceptions & Packages",
        "content": """<div class="topic-section">
    <h3>📌 PL/SQL Temel Blok Mimarisi</h3>
    <p>PL/SQL (Procedural Language/SQL), Oracle veritabanının SQL'e prosedürel programlama yetenekleri kazandıran blok yapılı dilidir.</p>
    
    <div class="code-example">DECLARE
    -- 1. Bildirim Bölümü (İsteğe Bağlı): Değişkenler, sabitler, imleçler, istisnalar
    v_ad Personel.ad%TYPE;
    v_maas Personel.maas%TYPE;
BEGIN
    -- 2. Yürütme Bölümü (Zorunlu): SQL ve PL/SQL ifadeleri
    SELECT ad, maas INTO v_ad, v_maas FROM Personel WHERE id = 101;
    DBMS_OUTPUT.PUT_LINE('Personel: ' || v_ad || ' - Maaş: ' || v_maas);
EXCEPTION
    -- 3. İstisna Yakalama Bölümü (İsteğe Bağlı): Hata işleme kodları
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Belirtilen ID ile kayıt bulunamadı!');
    WHEN TOO_MANY_ROWS THEN
        DBMS_OUTPUT.PUT_LINE('Sorgu birden fazla satır döndürdü!');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Bilinmeyen Hata: ' || SQLERRM);
END;
/</div>
</div>

<div class="topic-section">
    <h3>🏷️ Dinamik Veri Nitelikleri: %TYPE ve %ROWTYPE</h3>
    <table class="table-styled">
        <tr><th>Nitelik</th><th>Kullanım Amacı</th><th>Örnek Tanımlama</th><th>Avantajı</th></tr>
        <tr><td><code>%TYPE</code></td><td>Bir tablonun belirli bir sütununun veya başka bir değişkenin veri tipini dinamik olarak miras alır.</td><td><code>v_maas Personel.maas%TYPE;</code></td><td>Tablodaki sütunun veri tipi (örn: NUMBER(8,2) -> NUMBER(10,2)) değiştiğinde PL/SQL kodunu değiştirmek gerekmez.</td></tr>
        <tr><td><code>%ROWTYPE</code></td><td>Bir tablonun, görünümün veya imlecin <strong>tüm satır yapısını (tüm sütunlarını)</strong> içeren bir Kayıt (Record) değişkeni oluşturur.</td><td><code>emp_rec Personel%ROWTYPE;</code></td><td>Tüm satır tek bir değişken içinde <code>emp_rec.ad</code>, <code>emp_rec.maas</code> şeklinde kolayca taşınır.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🔄 PL/SQL Döngüleri ve İmleç FOR Döngüsü (Cursor FOR Loop)</h3>
    <div class="info-box success">
        <strong>🚀 İmleç FOR Döngüsü (Cursor FOR Loop):</strong><br>
        Oracle PL/SQL'in en zarif yapılarından biridir. İmleci otomatik olarak <code>OPEN</code> yapar, her adımda <code>FETCH</code> eder, kayıt değişkenini otomatik tanımlar ve veri bittiğinde (<code>%NOTFOUND</code>) otomatik olarak <code>CLOSE</code> eder!
    </div>
    
    <div class="code-example">-- İmleç FOR Döngüsü ile Tüm Personelleri Listeleme
BEGIN
    FOR rec IN (SELECT ad, soyad, maas FROM Personel WHERE bolum_id = 10)
    LOOP
        DBMS_OUTPUT.PUT_LINE(rec.ad || ' ' || rec.soyad || ' -> ' || rec.maas);
    END LOOP;
END;
/</div>
</div>

<div class="topic-section">
    <h3>🛡️ Ön Tanımlı İstisnalar ve Özel Hata Fırlatma</h3>
    <ul>
        <li><code>NO_DATA_FOUND</code>: <code>SELECT INTO</code> ifadesi hiçbir satır bulamadığında fırlatılır.</li>
        <li><code>TOO_MANY_ROWS</code>: <code>SELECT INTO</code> ifadesi birden fazla satır döndürdüğünde fırlatılır (SELECT INTO tek satır bekler!).</li>
        <li><code>ZERO_DIVIDE</code>: Sıfıra bölme hatası yapıldığında.</li>
        <li><code>DUP_VAL_ON_INDEX</code>: Birincil anahtar (PK) veya UNIQUE sütuna yinelenen değer girilmeye çalışıldığında.</li>
        <li><code>RAISE_APPLICATION_ERROR(hata_kodu, mesaj)</code>: Kullanıcı tanımlı hata fırlatır. Hata kodları <strong>-20000 ile -20999</strong> aralığında olmak zorundadır!</li>
    </ul>
</div>

<div class="topic-section">
    <h3>📦 PL/SQL Paketleri (Packages): Spec vs Body</h3>
    <p>Paketler, birbiriyle ilişkili prosedürleri, fonksiyonları, değişkenleri ve imleçleri tek bir çatı altında toplayan nesne yönelimli modüler yapılardır.</p>
    <ul>
        <li><strong>Paket Tanımı (Package Specification - Spec):</strong> Paketin dış dünyaya açılan arayüzüdür (Header). Sadece dışarıdan çağrılabilecek fonksiyon ve prosedürlerin imzaları yer alır.</li>
        <li><strong>Paket Gövdesi (Package Body):</strong> Spec'te tanımlanan fonksiyon ve prosedürlerin gerçek kaynak kodlarını ve sadece pakete özel (private) yardımcı elemanları içerir.</li>
    </ul>
</div>"""
    },

    # -------------------------------------------------------------
    # 13. VARLIK-İLİŞKİ (ER) MODELLEMESİ & ŞEMA DÖNÜŞÜMÜ
    # -------------------------------------------------------------
    {
        "id": "er-modelleme",
        "icon": "📊",
        "title": "Varlık-İlişki (ER) Modellemesi & İlişkisel Şemaya Dönüşüm",
        "priority": "medium",
        "subtitle": "DBMS_12 - ER Sembolleri, Zayıf Varlık, Min-Max Notasyonu & 7 Adımda İlişkisel Şemaya Dönüşüm",
        "content": """<div class="topic-section">
    <h3>📌 ER Modeli Temel Yapı Taşları ve Notasyonlar</h3>
    <table class="table-styled">
        <tr><th>Kavram</th><th>ER Şema Sembolü</th><th>Tanım ve Açıklama</th></tr>
        <tr><td><strong>Güçlü Varlık (Entity)</strong></td><td>Tek Çizgili Dikdörtgen</td><td>Kendi birincil anahtarına sahip, bağımsız olarak var olabilen nesne kümesi (Örn: <code>Ogrenci</code>, <code>Bolum</code>).</td></tr>
        <tr><td><strong>Zayıf Varlık (Weak Entity)</strong></td><td><strong>Çift Çizgili Dikdörtgen</strong></td><td>Kendi başına bir birincil anahtara sahip olmayan; varlığı başka bir güçlü varlığa (Sahip Varlık) bağlı olan varlık (Örn: Personelin <code>BakmaklaYukumluOlduguKisi</code>).</td></tr>
        <tr><td><strong>Tanımlayıcı İlişki</strong></td><td><strong>Çift Çizgili Baklava (Elmas)</strong></td><td>Zayıf varlığı güçlü sahibine bağlayan ilişki.</td></tr>
        <tr><td><strong>Basit Nitelik</strong></td><td>Tek Çizgili Elips</td><td>Tekil ve bölünemez özellik (Örn: <code>maas</code>).</td></tr>
        <tr><td><strong>Bileşik Nitelik</strong></td><td>Ağaç şeklinde dallanan Elipsler</td><td>Daha küçük alt parçalara bölünebilen nitelik (Örn: <code>Adres -> Il, Ilce, Sokak</code> veya <code>AdSoyad -> Ad, Soyad</code>).</td></tr>
        <tr><td><strong>Çok Değerli Nitelik</strong></td><td><strong>Çift Çizgili Elips</strong></td><td>Aynı varlık için birden fazla değer alabilen nitelik (Örn: <code>TelefonNumaralari</code>, <code>YabanciDiller</code>).</td></tr>
        <tr><td><strong>Türetilmiş Nitelik</strong></td><td><strong>Kesikli Çizgili Elips</strong></td><td>Veritabanında fiziksel saklanmayıp başka bir nitelikten hesaplanan özellik (Örn: <code>Yas</code> niteliği <code>DogumTarihi</code>'nden türetilir).</td></tr>
        <tr><td><strong>Anahtar Nitelik</strong></td><td>İçindeki yazı <strong>Altı Çizili</strong> Elips</td><td>Varlıkları tekil tanımlayan anahtar (Örn: <code><u>OgrenciNo</u></code>).</td></tr>
        <tr><td><strong>Kısmi Anahtar (Discriminator)</strong></td><td>İçindeki yazı <strong>Kesikli Altı Çizili</strong> Elips</td><td>Zayıf varlığın kayıtlarını kendi içinde ayırt etmeye yarayan anahtar parçası.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🔗 Katılım Kısıtları ve Kardinalite Oranları</h3>
    <ul>
        <li><strong>Kardinalite Oranları:</strong> <code>1:1</code> (Bire-Bir), <code>1:N</code> (Bire-Çok), <code>M:N</code> (Çoka-Çok).</li>
        <li><strong>Tam Katılım (Total Participation / Zorunlu - Çift Çizgi):</strong> Varlık kümesindeki her bir varlık ilişkide mutlaka yer almalıdır (Örn: Her bölümün mutlaka bir yöneticisi olmalı).</li>
        <li><strong>Kısmi Katılım (Partial Participation / İsteğe Bağlı - Tek Çizgi):</strong> Varlıkların bir kısmı ilişkide yer almayabilir (Örn: Her çalışan yönetici olmak zorunda değildir).</li>
        <li><strong>Min-Max Notasyonu (min..max):</strong> <code>(0..1)</code>, <code>(1..1)</code>, <code>(0..N)</code>, <code>(1..N)</code> şeklinde minimum ve maksimum katılımı kesin olarak belirtir.</li>
    </ul>
</div>

<div class="topic-section">
    <h3>🗺️ 7 Adımda ER Modelinden İlişkisel Şemaya (Tablolara) Dönüşüm Algoritması</h3>
    
    <div class="info-box">
        <strong>Adım 1: Güçlü Varlıkların Dönüşümü:</strong><br>
        Her güçlü varlık için ayrı bir tablo açılır. Basit nitelikler sütun yapılır. Bileşik niteliklerin ise yalnızca <em>en uçtaki atomik alt nitelikleri</em> sütun olarak eklenir. Birincil anahtar tablonun PK'si olur.
    </div>

    <div class="info-box">
        <strong>Adım 2: Zayıf Varlıkların Dönüşümü:</strong><br>
        Zayıf varlık için ayrı bir tablo açılır. Sahip olduğu güçlü varlığın PK'si bu tabloya <strong>Yabancı Anahtar (FK)</strong> olarak eklenir. Tablonun Birincil Anahtarı: <code>(Sahip_PK + Zayıf_Kısmi_Anahtar)</code> birleşimi olan <strong>Bileşik Anahtardır (Composite PK)</strong>.
    </div>

    <div class="info-box">
        <strong>Adım 3: 1:1 İlişkilerin Dönüşümü:</strong><br>
        İlişkinin <em>Tam Katılımlı (Total)</em> olduğu taraftaki tabloya diğer tablonun PK'si FK olarak eklenir (ve UNIQUE kısıtı verilir). Eğer iki taraf da tam katılımlıysa iki varlık tek bir tabloda birleştirilebilir.
    </div>

    <div class="info-box warning">
        <strong>Adım 4: 1:N İlişkilerin Dönüşümü (ÇOK ÖNEMLİ):</strong><br>
        İlişkinin <strong>N (Çok) tarafındaki tabloya</strong>, 1 tarafındaki tablonun Birincil Anahtarı (PK) <strong>Yabancı Anahtar (FK)</strong> olarak eklenir! (Örn: Her öğrencinin bir bölümü vardır -> Ogrenci tablosuna BolumId FK olarak eklenir).
    </div>

    <div class="info-box danger">
        <strong>Adım 5: M:N İlişkilerin Dönüşümü (KAVŞAK TABLOSU):</strong><br>
        M:N ilişkiler doğrudan tablolara FK eklenerek çözülemez! Mutlaka <strong>YENİ BİR BAĞLANTI / KAVŞAK TABLOSU (Junction / Bridge Table)</strong> oluşturulur. Bu tablonun PK'si, her iki tablonun PK'lerinin birleşiminden oluşan bileşik anahtardır: <code>(Tablo1_PK, Tablo2_PK)</code>. Varsa ilişkinin kendi nitelikleri de bu tabloya eklenir.
    </div>

    <div class="info-box">
        <strong>Adım 6: Çok Değerli Niteliklerin Dönüşümü:</strong><br>
        Her çok değerli nitelik için AYRI BİR TABLO oluşturulur. Varlığın PK'si FK olarak alınır. Tablonun PK'si: <code>(Varlik_PK + Nitelik_Degeri)</code> bileşik anahtarıdır.
    </div>

    <div class="info-box">
        <strong>Adım 7: n-li (Ternary vb.) İlişkilerin Dönüşümü:</strong><br>
        Yeni bir tablo oluşturulur ve ilişkiye katılan tüm varlıkların PK'leri FK olarak eklenir.
    </div>
</div>"""
    },

    # -------------------------------------------------------------
    # 14. NORMALİZASYON & FONKSİYONEL BAĞIMLILIKLAR
    # -------------------------------------------------------------
    {
        "id": "normalizasyon",
        "icon": "⚖️",
        "title": "Normalizasyon, Fonksiyonel Bağımlılıklar & Ayrıştırma",
        "priority": "high",
        "subtitle": "DBMS_14 - Veritabanı Anomalileri, Armstrong Aksiyomları, Aday Anahtar Bulma & 1NF, 2NF, 3NF, BCNF Adımları",
        "content": """<div class="topic-section">
    <h3>📌 Normalizasyonun Amacı ve Veritabanı Anomalileri</h3>
    <p>Normalizasyon, veritabanındaki <strong>veri tekrarını (redundancy) en aza indirmek</strong> ve veri bütünlüğünü bozan <strong>güncelleme, ekleme ve silme anomalilerini ortadan kaldırmak</strong> için tabloları belirli kurallara göre daha küçük, ilişkili tablolara ayrıştırma (decomposition) sürecidir.</p>
    
    <table class="table-styled">
        <tr><th>Anomali Türü</th><th>Tanım ve Tehlikesi</th><th>Örnek</th></tr>
        <tr><td><strong>Ekleme Anomalisi (Insertion Anomaly)</strong></td><td>Bir varlığa ait bilgiyi, onunla ilişkili başka bir bağımsız varlık olmadan veritabanına ekleyememe durumu.</td><td>Henüz hiç öğrencisi kayıt olmamış yeni bir bölümü, Ogrenci-Ders tablosuna öğrenci bilgisi olmadan ekleyememek.</td></tr>
        <tr><td><strong>Silme Anomalisi (Deletion Anomaly)</strong></td><td>Bir kaydı silerken, onunla birlikte kaybolmaması gereken tamamen farklı bir bilginin de kazara silinmesi.</td><td>Bir bölümdeki son öğrenciyi sildiğimizde, o bölümün varlığına ait tüm bilgilerin de sistemden yok olması.</td></tr>
        <tr><td><strong>Güncelleme Anomalisi (Update Anomaly)</strong></td><td>Tekrarlayan verinin bir satırda güncellenip diğer satırlarda unutulması sonucu veritabanının tutarsız hale gelmesi.</td><td>Bölüm başkanının adı değiştiğinde, 1000 öğrenci satırından 900'ünde güncellenip 100'ünde eski kalması.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>📐 Fonksiyonel Bağımlılık (FD) ve Armstrong Aksiyomları</h3>
    <p>Bir ilişkide X ve Y nitelik kümeleri olsun. Eğer her bir X değeri benzersiz olarak tam bir Y değerini belirliyorsa, <strong>"Y, X'e fonksiyonel bağımlıdır"</strong> denir ve <code>X -> Y</code> şeklinde gösterilir (X: Belirleyici / Determinant).</p>
    
    <div class="info-box">
        <strong>Armstrong Aksiyomları (Temel Kurallar):</strong><br>
        1. <strong>Yansıma (Reflexivity):</strong> Eğer Y ⊆ X ise, o zaman <code>X -> Y</code> dir (Örn: <code>(TC, Ad) -> TC</code>).<br>
        2. <strong>Artırma (Augmentation):</strong> Eğer <code>X -> Y</code> ise, o zaman her Z için <code>XZ -> YZ</code> dir.<br>
        3. <strong>Geçişlilik (Transitivity):</strong> Eğer <code>X -> Y</code> ve <code>Y -> Z</code> ise, o zaman <code>X -> Z</code> dir.<br>
        <strong>İkincil Türetilmiş Kurallar:</strong><br>
        • Birleşim (Union): <code>X -> Y</code> ve <code>X -> Z</code> ise <code>X -> YZ</code> dir.<br>
        • Ayrıştırma (Decomposition): <code>X -> YZ</code> ise <code>X -> Y</code> ve <code>X -> Z</code> dir.
    </div>
</div>

<div class="topic-section">
    <h3>🔍 Nitelik Kapanışı (X⁺) ve Aday Anahtar Bulma Algoritması</h3>
    <p>Bir X niteliğinin kapanışı (<code>X⁺</code>), mevcut bağımlılıklar kullanılarak X'ten erişilebilen tüm niteliklerin kümesidir.</p>
    <div class="code-example">Örnek: R(A, B, C, D, E) tablosu ve Bağımlılıklar: { A -> B, B -> C, C -> D, D -> E }
1. A'nın kapanışını hesaplayalım:
   A⁺ = { A } (kendisi)
   A -> B olduğu için: A⁺ = { A, B }
   B -> C olduğu için: A⁺ = { A, B, C }
   C -> D olduğu için: A⁺ = { A, B, C, D }
   D -> E olduğu için: A⁺ = { A, B, C, D, E } = R
2. A⁺ tablodaki TÜM nitelikleri kapsadığı için A bir SÜPER ANAHTARDIR.
3. A tek bir nitelik olduğundan hiçbir alt kümesi yoktur; dolayısıyla A bir ADAY ANAHTARDIR!</div>
</div>

<div class="topic-section">
    <h3>🏆 Normal Formlar Hiyerarşisi (1NF, 2NF, 3NF, BCNF)</h3>
    <table class="table-styled">
        <tr><th>Normal Form</th><th>Gereksinim / Sağlanması Gereken Şart</th><th>Ortadan Kaldırılan Problem</th></tr>
        <tr><td><strong>1NF (1. Normal Form)</strong></td><td>Tüm hücreler <strong>atomik (bölünemez)</strong> tekil değerler içermeli. Tekrarlayan gruplar ve diziler bulunmamalı.</td><td>Çok değerli nitelikler ve dizi karmaşası kalkar.</td></tr>
        <tr><td><strong>2NF (2. Normal Form)</strong></td><td>Tablo 1NF'de olmalı VE <strong>Kısmi Fonksiyonel Bağımlılık (Partial Dependency) OLMAMALIDIR!</strong> (Hiçbir asal olmayan nitelik, bileşik aday anahtarın bir parçasına bağımlı olamaz; anahtarın TAMAMINA tam bağımlı olmalıdır).<br><em>Not: Aday anahtarı tek sütundan oluşan bir tablo 1NF'deyse otomatik olarak 2NF'dedir!</em></td><td>Bileşik anahtarın parçasına bağlı veri tekrarları önlenir.</td></tr>
        <tr><td><strong>3NF (3. Normal Form)</strong></td><td>Tablo 2NF'de olmalı VE <strong>Geçişli Bağımlılık (Transitive Dependency) OLMAMALIDIR!</strong> (Asal olmayan bir nitelik başka bir asal olmayan niteliği belirleyemez: X -> Y ve Y -> Z durumu kalkmalıdır).<br><strong>Resmi Kural:</strong> Her <code>X -> A</code> bağımlılığı için; ya X bir <em>Süper Anahtar</em> olmalı YA DA A bir <em>Asal Nitelik</em> (Aday anahtar parçası) olmalıdır.</td><td>Anahtar dışı sütunlar arası bağımlılıklar ve veri anomalileri kalkar.</td></tr>
        <tr><td><strong>BCNF (Boyce-Codd Normal Form)</strong></td><td><strong>Güçlü 3NF'dir.</strong> Tablodaki HER <code>X -> A</code> fonksiyonel bağımlılığında belirleyici olan X <strong>MUTLAKA BİR SÜPER ANAHTAR OLMALIDIR!</strong> (3NF'deki "A asaldır" istisnasını kabul etmez!).</td><td>Aday anahtar parçalarının birbirini belirlemesinden doğan tüm anomaliler sıfırlanır.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>💡 Çözümlü Normalizasyon Sınav Sorusu</h3>
    <div class="code-example">Tablo: SiparisDetay (<u>SiparisNo</u>, <u>UrunNo</u>, UrunAd, BirimFiyat, Adet, MusteriNo, MusteriAd)
Bağımlılıklar:
  (SiparisNo, UrunNo) -> Adet
  UrunNo -> UrunAd, BirimFiyat          (Kısmi Bağımlılık!)
  SiparisNo -> MusteriNo, MusteriAd     (Kısmi Bağımlılık!)
  MusteriNo -> MusteriAd                (Geçişli Bağımlılık!)

1. ADIM (2NF'ye Dönüştürme - Kısmi Bağımlılıkları Ayır):
   - Tablo 1 (SiparisUrun): (<u>SiparisNo</u>, <u>UrunNo</u>, Adet)
   - Tablo 2 (Urun): (<u>UrunNo</u>, UrunAd, BirimFiyat)
   - Tablo 3 (Siparis): (<u>SiparisNo</u>, MusteriNo, MusteriAd)

2. ADIM (3NF'ye Dönüştürme - Siparis tablosundaki Geçişli Bağımlılığı Ayır):
   - Tablo 3a (Siparis): (<u>SiparisNo</u>, MusteriNo)
   - Tablo 3b (Musteri): (<u>MusteriNo</u>, MusteriAd)

SONUÇ: 4 adet 3NF/BCNF uyumlu tablo elde edildi! Sıfır anomali, sıfır gereksiz tekrar!</div>
</div>"""
    },

    # -------------------------------------------------------------
    # 15. İŞLEM YÖNETİMİ (TRANSACTIONS), EŞZAMANLILIK & KİLİTLEME
    # -------------------------------------------------------------
    {
        "id": "transaction",
        "icon": "🔒",
        "title": "İşlem Yönetimi (Transactions), Eşzamanlılık & Kilitleme",
        "priority": "high",
        "subtitle": "Deney Föyü & veritabanıfinal - ACID İlkeleri, Eşzamanlılık Problemleri, İzolasyon Seviyeleri & 2PL Kilitleme",
        "content": """<div class="topic-section">
    <h3>📌 İşlem (Transaction) Nedir? ACID İlkeleri</h3>
    <p>Bir Transaction (İşlem), veritabanında mantıksal olarak <strong>bölünemez tek bir iş birimi (Atomic Unit of Work)</strong> oluşturan bir veya daha fazla SQL komutunun bütünüdür.</p>
    
    <div class="info-box success">
        <strong>💎 ACID İlkeleri (Veritabanının 4 Temel Taşı):</strong><br>
        • <strong>A - Atomicity (Atomiklik / Bölünemezlik):</strong> "Ya hep ya hiç" kuralıdır. İşlemdeki tüm komutlar ya tamamen başarıyla tamamlanır (COMMIT) ya da herhangi bir hata durumunda tüm değişiklikler geri alınarak veritabanı işlem öncesi haline döndürülür (ROLLBACK).<br>
        • <strong>C - Consistency (Tutarlılık):</strong> İşlem başlamadan önce veritabanı geçerli ve tutarlı bir durumdadır; işlem bittiğinde de tüm bütünlük kısıtlarına (PK, FK, CHECK vb.) uygun tutarlı bir duruma geçmelidir.<br>
        • <strong>I - Isolation (Yalıtım / İzolasyon):</strong> Eşzamanlı çalışan işlemler birbirinden izoledir. Bir işlemin tamamlanmamış ara sonuçları diğer işlemler tarafından görülemez.<br>
        • <strong>D - Durability (Dayanıklılık / Kalıcılık):</strong> Başarıyla tamamlanan (COMMIT edilmiş) bir işlemin sonuçları, sistem çökse, elektrik kesilse dahi kalıcıdır ve asla kaybolmaz (Write-Ahead Logging / Transaction Log sayesinde).
    </div>
</div>

<div class="topic-section">
    <h3>⚡ Eşzamanlılık Problemleri (Concurrency Anomalies)</h3>
    <table class="table-styled">
        <tr><th>Problem</th><th>Açıklama ve Senaryo</th></tr>
        <tr><td><strong>Kirli Okuma (Dirty Read)</strong></td><td>Bir işlemin (T1) henüz COMMIT etmediği değiştirilmiş veriyi başka bir işlemin (T2) okumasıdır. Eğer T1 daha sonra ROLLBACK yaparsa, T2'nin okuduğu veri tamamen hayali/çöp (kirli) olur.</td></tr>
        <tr><td><strong>Tekrarlanamayan Okuma (Non-Repeatable Read)</strong></td><td>Bir işlem (T1) aynı satırı işlem içinde iki kez okuduğunda; araya giren başka bir işlemin (T2) o satırı güncelleyip (UPDATE) COMMIT etmesi sonucu iki okumada farklı değerler görmesidir.</td></tr>
        <tr><td><strong>Hayalet Okuma (Phantom Read)</strong></td><td>Bir işlem (T1) belirli bir aralık koşuluyla (örn: <code>maas > 5000</code>) satırları okurken; araya giren başka bir işlemin (T2) o aralığa uyan yeni bir satır eklemesi (INSERT) veya silmesi sonucu, T1 aynı sorguyu tekrar çalıştırdığında daha önce var olmayan "hayalet" yeni satırlar görmesidir.</td></tr>
        <tr><td><strong>Kayıp Güncelleme (Lost Update)</strong></td><td>İki işlemin aynı anda aynı veriyi okuyup bağımsız güncellemeler yapması sonucu, son yazan işlemin ilk yazan işlemin güncellemesini ezerek yok etmesidir.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🛡️ 4 Temel SQL İzolasyon Seviyesi Karşılaştırma Matrisi</h3>
    <table class="table-styled">
        <tr><th>İzolasyon Seviyesi</th><th>Kirli Okuma (Dirty Read)</th><th>Tekrarlanamayan Okuma (Non-Repeatable)</th><th>Hayalet Okuma (Phantom Read)</th><th>Performans & Kilitlenme</th></tr>
        <tr><td><code>READ UNCOMMITTED</code></td><td><strong>İzin Verir (Yaşanır!)</strong></td><td>İzin Verir</td><td>İzin Verir</td><td>En Hızlı / En Güvensiz</td></tr>
        <tr><td><code>READ COMMITTED</code> (Varsayılan)</td><td><strong>ENGELLER ✅</strong></td><td>İzin Verir</td><td>İzin Verir</td><td>Hızlı ve Dengeli</td></tr>
        <tr><td><code>REPEATABLE READ</code></td><td><strong>ENGELLER ✅</strong></td><td><strong>ENGELLER ✅</strong></td><td>İzin Verir</td><td>Orta / Okuma kilitleri tutar</td></tr>
        <tr><td><code>SERIALIZABLE</code></td><td><strong>ENGELLER ✅</strong></td><td><strong>ENGELLER ✅</strong></td><td><strong>ENGELLER ✅</strong></td><td>En Yavaş / En Katı (Aralık Kilitleri)</td></tr>
        <tr><td><code>SNAPSHOT</code></td><td><strong>ENGELLER ✅</strong></td><td><strong>ENGELLER ✅</strong></td><td><strong>ENGELLER ✅</strong></td><td>Satır Sürümleme (Row Versioning) ile kilit koymadan tutarlı anlık görüntü sağlar.</td></tr>
    </table>
</div>

<div class="topic-section">
    <h3>🔒 Kilit Türleri (Locks) ve İki Fazlı Kilitleme (2PL)</h3>
    <ul>
        <li><strong>Paylaşımlı Kilit (Shared Lock - S):</strong> Okuma (<code>SELECT</code>) işlemlerinde konulur. Birden fazla işlem aynı anda aynı veri üzerinde S kilidi tutabilir (Okumalar birbirini engellemez).</li>
        <li><strong>Özel / Ayrıcalıklı Kilit (Exclusive Lock - X):</strong> Yazma (<code>INSERT, UPDATE, DELETE</code>) işlemlerinde konulur. Başka hiçbir kilitle (S veya X) uyuşmaz; veri üzerinde tam tekel kurar.</li>
        <li><strong>Güncelleme Kilidi (Update Lock - U):</strong> Veri güncellenmeden önceki arama aşamasında konulur; olası kilitlenmeleri (Deadlock) önler.</li>
        <li><strong>İki Fazlı Kilitleme Protokolü (2PL - Two-Phase Locking):</strong> Seri hale getirilebilirliği (Serializability) garanti eder.
            <ul>
                <li><strong>1. Büyüme Fazı (Growing Phase):</strong> İşlem yalnızca yeni kilitler alabilir, elindeki hiçbir kilidi bırakamaz.</li>
                <li><strong>2. Küçülme Fazı (Shrinking Phase):</strong> İşlem kilitleri serbest bırakmaya başlar, kesinlikle yeni bir kilit talep edemez.</li>
            </ul>
        </li>
        <li><strong>Ölümcül Kilitlenme (Deadlock):</strong> İki veya daha fazla işlemin birbirinin elinde tuttuğu kilitleri karşılıklı olarak sonsuza kadar beklemesi durumudur. VTYS Deadlock Dedektörü döngüyü tespit eder ve en az maliyetli işlemi <strong>Kurban (Victim)</strong> seçerek ROLLBACK eder.</li>
    </ul>
</div>"""
    }
]

# Generate JavaScript file
js_content = "// ==========================================================================\n"
js_content += "// VTYS MASTER DERS NOTLARI VE EKSİKSİZ SINAV REHBERİ (15 BÖLÜM)\n"
js_content += "// 237 Ders Slaytı, Deney Föyü, Özel PDF'ler ve Çıkmış Sınav Sorularından Derlenmiştir.\n"
js_content += "// ==========================================================================\n\n"
js_content += "const TOPICS = " + json.dumps(TOPICS, ensure_ascii=False, indent=2) + ";\n"

out_path = os.path.join(r"c:\Users\bekir\Masaüstü\veritabanı sınav hazırlık\vtys-sinav-site", "topics.js")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Successfully generated {out_path} with {len(TOPICS)} comprehensive chapters!")
