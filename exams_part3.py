# -*- coding: utf-8 -*-
"""
exams_part3.py: Exam 5 and Exam 6
"""
import random
random.seed(105)

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
# EXAM 5: Saklı Yordamlar (Stored Procedures) & Kullanıcı Tanımlı Fonksiyonlar (UDF)
# (Kaynaklar: saklıYordam_SP, sql_Functions, veritabanıfinal)
# =========================================================================
e5 = [
    make_q(
        "Veritabanında Saklı Yordam (Stored Procedure) kullanmanın temel avantajları arasında hangisi YER ALMAZ?",
        "Tüm veritabanı tablolarının fiziksel olarak diskte kapladığı alanı yarıya indirmesi",
        ["Ağ trafiğini azaltması (Tek bir EXEC çağrısıyla çok sayıda işlemin sunucuda çalışması)", "Önceden derlenmiş (precompiled) yürütme planı sayesinde performans sağlaması", "Kullanıcılara tablolara doğrudan erişim vermeden işlem yaptırarak güvenlik sağlaması", "İş kurallarının ve SQL kodlarının merkezi olarak yönetilmesini sağlaması"],
        "Stored Procedure disk alanını küçültmez; ağ trafiğini azaltır, güvenliği artırır ve derlenmiş planla hız kazandırır."
    ),
    make_q(
        "Bir Stored Procedure'ü çalıştırmak için hangi SQL komutu kullanılır?",
        "<code>EXEC</code> veya <code>EXECUTE</code>",
        ["<code>RUN</code>", "<code>CALL FUNCTION</code>", "<code>START</code>", "<code>SELECT PROC</code>"],
        "Stored procedure'ler EXEC veya EXECUTE komutu ile parametreleri verilerek çalıştırılır."
    ),
    make_q(
        "Aşağıdaki Stored Procedure tanımında varsayılan (DEFAULT) parametre nasıl belirlenmiştir?\n<code>CREATE PROC sp_islem @hesap VARCHAR(10), @tutar MONEY = 100</code>",
        "@tutar parametresine çağrı anında değer verilmezse varsayılan olarak 100 kabul edilir.",
        ["@tutar parametresi zorunlu bir parametredir ve mutlaka gönderilmelidir.", "@tutar parametresi daima 100 ile çarpılarak işlem görür.", "@hesap parametresi gönderilmezse @tutar 100 olur.", "Bu prosedür yalnızca 100 TL'lik hesaplarda çalışabilir."],
        "@parametre VeriTipi = VarsayilanDeger şeklinde tanımlanan parametreler çağrıda girilmezse varsayılan değeri alır."
    ),
    make_q(
        "<code>EXEC sp_para_transfer @para_miktari = 5000, @alacakli_hesap = '6804', @gonderen_hesap = '2543'</code> şeklinde parametre isimleriyle yapılan çağrı için hangisi DOĞRUDUR?",
        "İsimlendirilmiş (Named) çağrı yapıldığı için parametrelerin yazılış sırası önemli değildir.",
        ["Parametre sırası tanım sırasıyla aynı olmadığından SQL motoru hata verir.", "Bu kullanımda tüm parametreler NULL olarak işlem görür.", "Bu kullanım yalnızca Oracle PL/SQL'de geçerlidir, SQL Server desteklemez.", "Yalnızca ilk parametre dikkate alınır, diğerleri atlanır."],
        "Parametre adları açıkça belirtilerek (@param = deger) çağrıldığında parametrelerin sırası önemsizdir."
    ),
    make_q(
        "Bir Stored Procedure'de <code>IF EXISTS (SELECT * FROM Musteri WHERE HesapNo = @HesapNo) UPDATE ... ELSE INSERT ...</code> yapısının amacı nedir?",
        "Müşteri tabloda zaten kayıtlıysa bilgilerini güncellemek, kayıtlı değilse yeni müşteri olarak eklemek (Upsert deseni)",
        ["Tablodaki tüm müşterileri silip baştan eklemek", "Müşterinin bakiyesini kontrol edip kredi vermek", "Müşteri varsa işlemi iptal edip hata fırlatmak", "Müşteri tablosunu yedeklemek"],
        "Bu yapı 'varsa güncelle, yoksa ekle' (Upsert / Merge) mantığını gerçekleştiren standart prosedür desenidir."
    ),
    make_q(
        "Bir Stored Procedure'e joker parametre tanımlanırken <code>@Ad VARCHAR(30) = 'A%'</code> yazılırsa bu prosedür parametresiz çağrıldığında ne listeler?",
        "Adı 'A' harfi ile başlayan tüm müşterileri listeler.",
        ["Adı tam olarak 'A%' olan müşterileri listeler.", "Hiçbir müşteriyi listelemez (Hata verir).", "Tüm müşterileri koşulsuz listeler.", "Yalnızca adı tek harfli olan müşterileri listeler."],
        "Varsayılan değer 'A%' olduğundan parametre gönderilmezse WHERE Ad LIKE 'A%' çalışır ve A ile başlayanları getirir."
    ),
    make_q(
        "Bir Stored Procedure'den dışarıya değer döndürmek (birden çok değer döndürebilmek) için parametre tanımında hangi anahtar kelime kullanılır?",
        "<code>OUTPUT</code> (veya <code>OUT</code>)",
        ["<code>RETURN</code>", "<code>EXPORT</code>", "<code>SEND</code>", "<code>EXTRACT</code>"],
        "Stored procedure'lerde dışarıya değer aktaran parametreler @degisken VeriTipi OUTPUT şeklinde tanımlanır."
    ),
    make_q(
        "Stored Procedure'lerdeki <code>RETURN</code> komutu ile <code>OUTPUT</code> parametresi arasındaki fark nedir?",
        "RETURN yalnızca tek bir tamsayı (genellikle durum/hata kodu) döndürürken, OUTPUT her türden birden fazla değer döndürebilir.",
        ["RETURN tablo döndürürken, OUTPUT skaler değer döndürür.", "RETURN yalnızca Oracle'da çalışırken, OUTPUT SQL Server'da çalışır.", "RETURN parametre alırken, OUTPUT parametre alamaz.", "İkisi tamamen aynıdır, hiçbir fark yoktur."],
        "RETURN tamsayı durum kodu (0 = başarılı vb.) dönmek içindir; veri taşımak için OUTPUT parametreleri kullanılır."
    ),
    make_q(
        "VIEW, FUNCTION ve PROCEDURE karşılaştırmasında aşağıdakilerden hangisi DOĞRUDUR?",
        "View parametre alamaz; Function parametre alır ve sorguda (FROM/WHERE) kullanılır; Procedure parametre alır ve EXEC ile çalışır.",
        ["View parametre alabilir; Function parametre alamaz; Procedure sorguda doğrudan çağrılır.", "Function tablolara serbestçe INSERT/UPDATE yapabilirken Procedure yapamaz.", "Procedure SELECT ifadesinin FROM bloğunda doğrudan bir tablo gibi sorgulanabilir.", "View ve Procedure tamamen aynı nesnelerdir."],
        "Temel kural: View parametresiz sorgulanır, Function parametreli sorgulanır (DML yapamaz), Procedure EXEC ile iş yürütür."
    ),
    make_q(
        "Kullanıcı Tanımlı Skaler Fonksiyon (Scalar UDF) ile ilgili aşağıdakilerden hangisi DOĞRUDUR?",
        "Geriye tek bir skaler değer (INT, VARCHAR, DATE vb.) döndürür ve <code>RETURNS tip</code> ile tanımlanır.",
        ["Geriye daima çok satırlı bir tablo sonuç kümesi döndürür.", "SELECT sorguları içinde kullanılamaz; yalnızca EXEC ile çalıştırılır.", "İçerisinde tablolar üzerinde serbestçe INSERT ve DELETE yapabilir.", "Fonksiyon gövdesinde RETURN komutunun bulunması yasaktır."],
        "Skaler fonksiyon tek bir değer döner (RETURNS INT vb.), BEGIN...END bloğunda RETURN @deger ile sonlanır."
    ),
    make_q(
        "SQL Server'da kullanıcı tanımlı skaler fonksiyon çağrılırken şema adı (örn: <code>dbo.</code>) neden zorunludur?",
        "SQL Server skaler fonksiyonları sistem fonksiyonlarından ayırt etmek için iki parçalı isim (dbo.FonksiyonAdi) kullanımını zorunlu kılar.",
        ["Şema adı yazılmazsa fonksiyon veritabanından kalıcı olarak silinir.", "Şema adı yalnızca yöneticilerin çalıştırmasını sağlamak içindir.", "Fonksiyonun RAM yerine diskte çalışmasını zorunlu kılar.", "Şema adı sadece metin fonksiyonlarında zorunludur."],
        "SQL Server'da skaler kullanıcı fonksiyonları çağrılırken dbo.fn_adi(...) şeklinde şema belirtilmelidir."
    ),
    make_q(
        "Satır İçi Tablo Değerli Fonksiyon (Inline Table-Valued Function) nasıl tanımlanır?",
        "<code>CREATE FUNCTION dbo.fn_Musteri(@seg VARCHAR(15)) RETURNS TABLE AS RETURN (SELECT ...);</code>",
        ["<code>CREATE FUNCTION dbo.fn_Musteri() RETURNS INT AS BEGIN RETURN 1; END;</code>", "<code>CREATE PROCEDURE dbo.fn_Musteri AS RETURN TABLE (SELECT * FROM Musteri);</code>", "<code>CREATE VIEW dbo.fn_Musteri(@seg VARCHAR(15)) AS SELECT ...;</code>", "<code>CREATE TABLE FUNCTION dbo.fn_Musteri() AS SELECT ...;</code>"],
        "Inline Table-Valued Function RETURNS TABLE ile tanımlanır, BEGIN...END içermez, doğrudan tek bir RETURN (SELECT ...) ifadesinden oluşur."
    ),
    make_q(
        "Tablo Değerli bir Fonksiyon (Table-Valued Function) SQL sorgusunda nerede kullanılabilir?",
        "Normal bir tablo gibi <code>FROM</code> veya <code>JOIN</code> yan tümcesinde sorgulanabilir.",
        ["Yalnızca ORDER BY yan tümcesinde sıralama kriteri olarak", "Yalnızca GROUP BY listesinde gruplama fonksiyonu olarak", "Yalnızca CREATE TABLE komutunun içinde", "Sorgularda kullanılamaz, yalnızca PRINT edilebilir"],
        "Table-Valued Function geriye tablo döndürdüğü için SELECT * FROM dbo.fn_adi('B2B') şeklinde FROM içinde kullanılır."
    ),
    make_q(
        "Kullanıcı tanımlı fonksiyonların (UDF) içinde <code>INSERT</code>, <code>UPDATE</code> veya <code>DELETE</code> gibi veritabanı durumunu değiştiren DML komutlarının YASAK olmasının sebebi nedir?",
        "Fonksiyonların sorgu içinde yan etkisiz (side-effect free) çalışmasının ve veri tutarlılığının garanti edilmek istenmesi",
        ["Veritabanı motorunun fonksiyonları derleyememesi", "Fonksiyonların yalnızca salt okunur belleğe yazılması", "Fonksiyonların diske erişim yetkisinin bulunmaması", "Fonksiyonların yalnızca tek bir satır işleyebilmesi"],
        "Fonksiyonlar yan etkisiz olmalıdır; SELECT içinde çağrılan bir fonksiyonun veritabanındaki tabloları değiştirmesine izin verilmez."
    ),
    make_q(
        "Deterministik (Deterministic) fonksiyon ne demektir?",
        "Aynı giriş parametreleri verildiğinde her zaman ve her koşulda aynı sonucu üreten fonksiyonlar (Örn: ABS, SQUARE)",
        ["Her çağrıldığında o anki zamana göre farklı sonuç üreten fonksiyonlar", "Yalnızca hata durumunda çalışan fonksiyonlar", "İçinde rastgele sayı üreten (RAND) fonksiyonlar", "Diskteki tabloları otomatik güncelleyen fonksiyonlar"],
        "Deterministik fonksiyonlar aynı girdiye daima aynı çıktıyı verir. GETDATE(), RAND() gibi fonksiyonlar non-deterministiktir."
    ),
    make_q(
        "Aşağıdaki fonksiyonlardan hangisi Non-Deterministik (belirleyici olmayan) bir fonksiyondur?",
        "<code>GETDATE()</code>",
        ["<code>UPPER('test')</code>", "<code>ABS(-5)</code>", "<code>SQUARE(4)</code>", "<code>LEN('Merhaba')</code>"],
        "GETDATE() çağrıldığı her milisaniyede farklı bir zaman değeri ürettiği için non-deterministiktir."
    ),
    make_q(
        "Bir Stored Procedure'ü silmek için hangi komut kullanılır?",
        "<code>DROP PROCEDURE ProsedurAdi</code> (veya <code>DROP PROC ProsedurAdi</code>)",
        ["<code>DELETE PROCEDURE ProsedurAdi</code>", "<code>REMOVE PROC ProsedurAdi</code>", "<code>ALTER PROCEDURE ProsedurAdi DROP</code>", "<code>CLEAR PROC ProsedurAdi</code>"],
        "Stored procedure'ler DROP PROCEDURE (veya DROP PROC) komutuyla kaldırılır."
    ),
    make_q(
        "Mevcut bir Stored Procedure'ün kodunu yetkilerini ve bağımlılıklarını kaybetmeden değiştirmek için ne kullanılır?",
        "<code>ALTER PROCEDURE ProsedurAdi ...</code>",
        ["<code>DROP PROCEDURE</code> ve ardından <code>CREATE PROCEDURE</code>", "<code>UPDATE PROCEDURE ProsedurAdi</code>", "<code>MODIFY PROC ProsedurAdi</code>", "<code>RENAME PROCEDURE ProsedurAdi</code>"],
        "ALTER PROCEDURE mevcut prosedürün yetki ve ayarlarını koruyarak gövdesini günceller."
    ),
    make_q(
        "Stored Procedure içinde <code>sp_bakiye_degistir @hesap_no='0415', @para=1000, @islem=0</code> çağrısında işlem tipi 0 iken bakiye artırılıyorsa, bu işlem hangi T-SQL yapısıyla kontrol edilir?",
        "<code>IF @islem = 1 UPDATE ... SET bakiye = bakiye - @para ELSE UPDATE ... SET bakiye = bakiye + @para</code>",
        ["<code>WHILE @islem = 0 BREAK</code>", "<code>CASE WHEN @islem = 0 THEN DROP TABLE</code>", "<code>TRY UPDATE CATCH INSERT</code>", "<code>GOTO 0</code>"],
        "IF...ELSE koşul yapısıyla @islem parametresinin değeri kontrol edilerek ilgili UPDATE komutu çalıştırılır."
    ),
    make_q(
        "Bir Stored Procedure içinde tanımlanan yerel değişkenlerin (DECLARE @x INT) etki alanı (scope) nedir?",
        "Yalnızca o Stored Procedure çalışırken ve o prosedürün kendi gövdesi içinde geçerlidir.",
        ["Tüm veritabanındaki bütün kullanıcılar için kalıcı olarak geçerlidir.", "Prosedür bittikten sonra da oturum kapanana kadar bellekte kalır.", "Başka prosedürler tarafından doğrudan okunup değiştirilebilir.", "Veritabanı sunucusu açık kaldığı sürece saklanır."],
        "Prosedür içindeki yerel değişkenler o prosedürün çağrısıyla doğar ve prosedür sonlanınca bellekten silinir."
    ),
    make_q(
        "Aşağıdaki SQL ifadesi ne amaçla yazılmıştır?\n<code>CREATE PROC sp_OgrenciGetir @BolumKod VARCHAR(3) AS SELECT * FROM Ogrenci WHERE BolumKod = @BolumKod</code>",
        "Belirtilen bölüm koduna ait öğrencileri parametre alarak listeleyen bir saklı yordam tanımlamak",
        ["Tüm bölümlerin kodlarını öğrenci tablosuna eklemek", "Öğrenci tablosundaki bölüm kodlarını silmek", "Bölüm koduna göre yeni bir öğrenci tablosu oluşturmak", "Öğrencileri bölüm koduna göre sıralayan bir görünüm oluşturmak"],
        "Bu prosedür @BolumKod parametresi alarak o bölümdeki öğrencileri filtreleyip döndürür."
    ),
    make_q(
        "Bir fonksiyonun tablodan müşteri sayısını hesaplayıp döndürürken <code>SELECT @sayi = COUNT(*) FROM Musteri; RETURN @sayi;</code> kullanması hangi fonksiyon tipine örnektir?",
        "Çok İfadeli Skaler Kullanıcı Tanımlı Fonksiyon (Multi-statement Scalar UDF)",
        ["Satır İçi Tablo Fonksiyonu", "DML Olay Tetikleyicisi", "Dinamik Görünüm (View)", "Geçici Yordam"],
        "BEGIN...END bloğu içinde değişken tanımlayıp hesaplama yapan ve tek bir değer dönen fonksiyon skaler UDF'tir."
    ),
    make_q(
        "Aşağıdakilerden hangisi bir Stored Procedure içinde YAPILAMAZ?",
        "<code>USE VeritabanıAdi</code> ile oturumun varsayılan veritabanını değiştirmek",
        ["Tabloya yeni satır eklemek (INSERT)", "Mevcut kayıtları güncellemek (UPDATE)", "Başka bir Stored Procedure'ü çalıştırmak (EXEC)", "İşlemleri transaction içine alıp ROLLBACK yapmak"],
        "Stored Procedure içinde 'USE database' komutu doğrudan kullanılamaz; prosedür oluşturulduğu veritabanı bağlamında çalışır."
    ),
    make_q(
        "Bir Stored Procedure parametresine <code>@hesapNo VARCHAR(30) = '[0-5]___'</code> varsayılan değeri verilmesi ne anlama gelir?",
        "Parametre verilmezse ilk basamağı 0-5 arası olan ve toplam 4 karakterli hesapları filtreleyecek bir joker kalıp kullanır.",
        ["Hesap numarasının kesinlikle 0 ile 5 arasında bir tam sayı olacağını belirtir.", "Sistemin ilk 5 hesaba otomatik 2000 TL yatıracağını belirtir.", "Hesap numarasının boş geçilmesini engeller.", "Parametrenin 5 elemanlı bir dizi olduğunu gösterir."],
        "[0-5]___ kalıbı LIKE operatörüyle kullanılarak 0-5 arası başlayan 4 karakterli hesapları yakalar."
    ),
    make_q(
        "Stored Procedure'lerde parametrelerin başına <code>@</code> işareti konulmasının nedeni nedir?",
        "T-SQL sözdiziminde parametre ve değişkenlerin sütun isimlerinden ayırt edilmesini sağlayan tanımlayıcı kural olması",
        ["Parametrenin internet üzerinden geldiğini belirtmek", "Parametrenin sayısal veri tipinde olduğunu belirtmek", "Parametrenin şifrelenmiş olduğunu belirtmek", "Parametrenin Primary Key olduğunu belirtmek"],
        "T-SQL'de tüm yerel değişken ve parametreler @ karakteri ile başlar."
    ),
    make_q(
        "Bir Stored Procedure içinde birden fazla <code>SELECT</code> ifadesi yer alıyorsa prosedür çalıştırıldığında ne olur?",
        "Her bir SELECT ifadesi için ayrı bir sonuç kümesi (Result Set) döner ve istemciye sırayla iletilir.",
        ["Yalnızca ilk SELECT ifadesi çalışır, diğerleri iptal edilir.", "SQL Server derleme hatası vererek prosedürü çalıştırmaz.", "Tüm SELECT sonuçları otomatik olarak tek bir tabloda birleştirilir.", "Sonuçların tamamı diske log dosyası olarak yazılır."],
        "Bir prosedür içinde birden çok SELECT sorgusu varsa, istemciye birden çok bağımsız result set döner."
    ),
    make_q(
        "Stored Procedure'lerde <code>WITH ENCRYPTION</code> seçeneği ne işe yarar?",
        "Prosedürün kaynak T-SQL kodunu veritabanı sistem tablolarında şifreleyerek başkalarının kodu okumasını engeller.",
        ["Prosedürün çalıştırdığı sorguların sonuçlarını internette şifreler.", "Prosedürün kullandığı tabloları salt okunur yapar.", "Prosedüre parola koruması ekleyerek şifresiz çalışmasını engeller.", "Prosedürün hızını iki katına çıkarır."],
        "WITH ENCRYPTION nesnenin tanım metnini (syscomments / sys.sql_modules) şifreler."
    ),
    make_q(
        "Kullanıcı tanımlı fonksiyonlarda <code>SCHEMABINDING</code> seçeneği ne sağlar?",
        "Fonksiyonun başvurduğu temel tabloların, fonksiyon silinmeden veya değiştirilmeden yapısının değiştirilmesini/silinmesini engeller.",
        ["Fonksiyonu otomatik olarak sistem şemasına (sys) taşır.", "Fonksiyonun tüm kullanıcılar tarafından çalıştırılabilmesini sağlar.", "Fonksiyonu şifreler.", "Fonksiyonun sadece tek bir tabloda çalışmasını zorunlu kılar."],
        "WITH SCHEMABINDING fonksiyon ile temel nesneler arasında bağ kurarak alt tabloların değiştirilmesini önler."
    ),
    make_q(
        "Aşağıdaki komut ne işe yarar?\n<code>CREATE FUNCTION dbo.fn_KareAl(@x INT) RETURNS INT AS BEGIN RETURN @x * @x; END;</code>",
        "Kendisine verilen tamsayının karesini hesaplayıp döndüren skaler bir kullanıcı fonksiyonu oluşturur.",
        ["Tablodaki tüm x sütunlarının karesini alıp tabloyu günceller.", "KareAl adında yeni bir tablo tanımlar.", "x değerine kadar olan sayıları listeleyen bir tablo fonksiyonudur.", "Verilen sayının karekökünü hesaplar."],
        "Girdi olarak @x alır ve @x * @x sonucunu skaler tamsayı olarak döndürür."
    ),
    make_q(
        "Yukarıda tanımlanan <code>fn_KareAl</code> fonksiyonu bir SELECT sorgusunda nasıl kullanılır?",
        "<code>SELECT dbo.fn_KareAl(5);</code>",
        ["<code>EXEC fn_KareAl 5;</code>", "<code>RUN dbo.fn_KareAl(5);</code>", "<code>CALL fn_KareAl(5);</code>", "<code>SELECT * FROM fn_KareAl(5);</code>"],
        "Skaler fonksiyonlar SELECT listesinde dbo.fn_adi(parametre) şeklinde çağrılır."
    ),
    make_q(
        "Bir fonksiyon içinde <code>WHILE</code> döngüsü kullanılabilir mi?",
        "Evet, fonksiyon gövdesinde (BEGIN...END) değişkenler ve WHILE döngüsü kuralına uygun şekilde kullanılabilir.",
        ["Hayır, fonksiyonlarda döngü kullanımı kesinlikle yasaktır.", "Yalnızca tablo değerli fonksiyonlarda kullanılabilir.", "Yalnızca tek bir satır işleyen döngülere izin verilir.", "Sadece Oracle PL/SQL'de izin verilir."],
        "Çok ifadeli skaler ve tablo değerli fonksiyonların BEGIN...END gövdesinde IF ve WHILE döngüleri kullanılabilir."
    ),
    make_q(
        "Bir Stored Procedure'ün parametre tanımlarken <code>@tarih DATE = GETDATE()</code> yazılması SQL Server'da geçerli midir?",
        "Hayır, parametre varsayılan değeri olarak fonksiyon çağrısı (GETDATE()) yazılamaz; sabit bir değer veya NULL yazılmalıdır.",
        ["Evet, tüm fonksiyonlar parametre varsayılanı olarak doğrudan atanabilir.", "Evet, ancak yalnızca GETDATE() fonksiyonuna izin verilir.", "Evet, ancak tarih formatı 104 olmak zorundadır.", "Evet, bu standart bir T-SQL sözdizimidir."],
        "T-SQL'de parametre varsayılan değeri sabit bir literal (sabit değer) veya NULL olmalıdır; fonksiyon sonucu atanamaz."
    ),
    make_q(
        "Stored Procedure derlenirken (Compilation) oluşturulan ve tekrar tekrar kullanılan yapı nedir?",
        "Yürütme Planı (Execution Plan / Query Plan)",
        ["Yedekleme Dosyası (.bak)", "İlişkisel Şema Ağacı", "Kullanıcı Oturum Anahtarı", "İndeks B-Tree Kökü"],
        "Stored Procedure ilk çalıştığında optimize edilerek derlenir ve Yürütme Planı (Execution Plan) önbelleğe alınarak sonraki çağrılarda hız kazanılır."
    ),
    make_q(
        "Kullanıcı tanımlı fonksiyonlarda <code>TABLE</code> dönüş tipinde birincil anahtar tanımlanabilir mi?",
        "Evet, çok ifadeli tablo değerli fonksiyonlarda (Multi-statement TVF) dönen tablo değişkeni üzerinde PRIMARY KEY tanımlanabilir.",
        ["Hayır, fonksiyonlarda dönen tablolarda hiçbir kısıtlama tanımlanamaz.", "Yalnızca FOREIGN KEY kısıtlaması tanımlanabilir.", "Yalnızca tek sütunlu tablolarda izin verilir.", "Sadece Oracle'da mümkündür."],
        "Multi-statement TVF'de: RETURNS @t TABLE (id INT PRIMARY KEY, ad VARCHAR(50)) şeklinde kısıtlar tanımlanabilir."
    ),
    make_q(
        "Aşağıdaki kodun amacı nedir?\n<code>CREATE PROC sp_DersNotuListele @dersKod VARCHAR(6), @bolumAd VARCHAR(30) AS BEGIN SELECT * FROM notbilgi WHERE derskod = @dersKod AND ogrno IN (SELECT ogrno FROM ogrenci WHERE bolumkod = (SELECT bolumkod FROM bolum WHERE bolumad = @bolumAd)); END</code>",
        "Belirtilen ders kodunu alan ve belirtilen bölümde okuyan öğrencilerin not bilgilerini listelemek",
        ["Ders ve bölüm adlarını silip not tablosunu boşaltmak", "Yeni bir bölüm ve ders kaydı eklemek", "Tüm öğrencilerin not ortalamasını 50 yapmak", "Öğrencinin bölümünü değiştirmek"],
        "İç içe alt sorgularla bölüm adından bolumkod'a, oradan öğrenci numaralarına ulaşıp notbilgi tablosunu filtreleyen prosedürdür."
    ),
    make_q(
        "Bir Stored Procedure içinde dinamik SQL çalıştırmak için hangi komut kullanılır?",
        "<code>sp_executesql</code> veya <code>EXEC(@sqlString)</code>",
        ["<code>RUN_SQL(@sqlString)</code>", "<code>EVAL(@sqlString)</code>", "<code>DYNAMIC_EXEC(@sqlString)</code>", "<code>PARSE(@sqlString)</code>"],
        "Dinamik olarak metin şeklinde oluşturulan SQL sorguları EXEC(@sql) veya sp_executesql ile çalıştırılır."
    ),
    make_q(
        "Stored Procedure kullanımında SQL Enjeksiyonuna (SQL Injection) karşı en güvenli yöntem hangisidir?",
        "Parametreli Stored Procedure ve parametreli <code>sp_executesql</code> kullanımı",
        ["Kullanıcı girdilerini doğrudan string birleştirme ile SQL metnine eklemek", "Tüm parametreleri VARCHAR(MAX) tanımlamak", "EXEC('') içine kontrolsüz string basmak", "Veritabanı şifresini boş bırakmak"],
        "Parametreli çağrılar kullanıcı girdisini kod olarak değil salt veri olarak işlediği için SQL Injection saldırılarını önler."
    ),
    make_q(
        "Bir Stored Procedure içinde tanımlanan <code>DECLARE @sayac INT = 0;</code> ifadesi her EXEC çağrısında ne olur?",
        "Her çağrıda yeniden tanımlanır ve başlangıç değeri olan 0 değerini alır.",
        ["Önceki çağrılardaki son değerini koruyarak üstüne ekler.", "Sunucu kapanana kadar global olarak değerini saklar.", "Diğer kullanıcıların oturumlarıyla ortak senkronize çalışır.", "İkinci çağrıda sözdizimi hatası verir."],
        "Prosedürün yerel değişkenleri her çalıştırmada baştan başlatılır (statik değildir)."
    ),
    make_q(
        "Kullanıcı tanımlı fonksiyonlarda <code>RAND()</code> fonksiyonunun doğrudan kullanılamamasının sebebi nedir?",
        "RAND() fonksiyonunun non-deterministik olması ve fonksiyonların yan etkisiz/öngörülebilir olma kuralını ihlal etmesi",
        ["RAND() fonksiyonunun SQL Server'da bulunmaması", "Fonksiyonların yalnızca tamsayı üretebilmesi", "Rastgele sayıların diske yazılamaması", "Fonksiyonların yalnızca tarih formatında çalışması"],
        "UDF içinde yan etki üreten veya non-deterministik olan RAND(), NEWID(), GETDATE() gibi fonksiyonların doğrudan kullanımına kısıtlama getirilmiştir."
    ),
    make_q(
        "Bir Stored Procedure'ün başarılı şekilde tamamlanıp tamamlanmadığını anlamak için çağıran tarafta ne kontrol edilir?",
        "<code>DECLARE @ret INT; EXEC @ret = sp_Adi;</code> şeklinde dönen dönüş (Return) değeri",
        ["Tablodaki satır sayısının çift olup olmadığı", "Sunucunun IP adresi", "Veritabanı log dosyasının boyutu", "Kullanıcının şifre uzunluğu"],
        "EXEC @DonusKodu = sp_Adi ifadesiyle prosedürün RETURN ettiği tamsayı durum kodu yakalanır."
    )
]

# =========================================================================
# EXAM 6: Trigger (Tetikleyiciler) & Olay Tabanlı Yönetim
# (Kaynaklar: trigger(tetikleyici), DBMS_7, 2016 vtys final cevaplar)
# =========================================================================
random.seed(106)
e6 = [
    make_q(
        "Veritabanı Tetikleyicisi (Trigger) ile ilgili aşağıdaki tanımlardan hangisi DOĞRUDUR?",
        "Belirli bir tabloda INSERT, UPDATE veya DELETE olayı gerçekleştiğinde otomatik olarak devreye giren özel saklı kod bloğudur.",
        ["Kullanıcı tarafından parametre verilerek EXEC komutu ile doğrudan çağrılan prosedürdür.", "Sorgularda FROM bloğuna yazılarak çağrılan sanal tablodur.", "Veritabanı çöktüğünde verileri kurtaran donanımsal yapıdır.", "Yalnızca her gece yarısı otomatik çalışan zamanlanmış görevdir."],
        "Trigger bir olaya (INSERT/UPDATE/DELETE) bağlı olarak otomatik tetiklenen, parametre almayan ve doğrudan çağrılamayan özel yapıdır."
    ),
    make_q(
        "Tetikleyicilerin (Trigger) özellikleri ile ilgili aşağıdakilerden hangisi YANLIŞTIR?",
        "Trigger'lar dışarıdan parametre alabilir ve kullanıcı tarafından doğrudan <code>EXEC</code> ile çalıştırılabilir.",
        ["Trigger'lar bir olay gerçekleştiğinde otomatik olarak devreye girer.", "Trigger'lar kendilerini tetikleyen işlemle birlikte bir Transaction bloğu oluşturur.", "Trigger içinde hata tespit edilirse <code>ROLLBACK TRANSACTION</code> ile işlem iptal edilebilir.", "Trigger'lar kullanıcıya doğrudan sonuç kümesi (Result Set) döndürmemelidir."],
        "Trigger'lar asla dışarıdan parametre almaz ve doğrudan kullanıcı tarafından çağrılamaz."
    ),
    make_q(
        "<code>AFTER</code> (veya <code>FOR</code>) trigger ile <code>INSTEAD OF</code> trigger arasındaki en temel fark nedir?",
        "AFTER trigger asıl DML işlemi başarıyla yapıldıktan sonra çalışır; INSTEAD OF trigger ise asıl işlemi yapmaz, onun yerine geçer.",
        ["AFTER trigger yalnızca VIEW'lerde, INSTEAD OF ise yalnızca tablolarda çalışır.", "AFTER trigger parametre alırken, INSTEAD OF trigger parametre alamaz.", "AFTER trigger işlemi geri alamazken, INSTEAD OF her zaman geri alır.", "İkisi arasında hiçbir çalışma zamanı veya mantıksal fark yoktur."],
        "AFTER olayın ardından çalışır (tablolarda); INSTEAD OF ise asıl işlemi durdurup kendi kodunu çalıştırır (tablo ve VIEW'lerde)."
    ),
    make_q(
        "<code>INSTEAD OF</code> tetikleyicileri veritabanında hangi nesneler üzerinde tanımlanabilir?",
        "Hem fiziksel tablolar üzerinde hem de Görünümler (VIEW) üzerinde tanımlanabilir.",
        ["Yalnızca fiziksel tablolar üzerinde tanımlanabilir, VIEW'lerde tanımlanamaz.", "Yalnızca Stored Procedure'ler üzerinde tanımlanabilir.", "Yalnızca geçici (temp) tablolar üzerinde tanımlanabilir.", "Yalnızca veritabanı kullanıcıları üzerinde tanımlanabilir."],
        "INSTEAD OF trigger normalde güncellenemeyen karmaşık VIEW'leri güncellenebilir kılmak için VIEW'ler üzerinde de tanımlanabilir."
    ),
    make_q(
        "Bir tabloya <code>INSERT</code> işlemi yapıldığında tetikleyici içinde hangi mantıksal sözde tablo(lar) oluşur?",
        "Yalnızca <code>INSERTED</code> tablosu oluşur (Yeni eklenen kayıtları içerir); <code>DELETED</code> tablosu boştur (oluşmaz).",
        ["Yalnızca DELETED tablosu oluşur.", "Hem INSERTED hem DELETED tablosu aynı kayıtlarla oluşur.", "UPDATED adında özel bir tablo oluşur.", "Hiçbir sözde tablo oluşmaz."],
        "INSERT anında yalnızca eklenen yeni satırları tutan INSERTED tablosu mevcuttur; DELETED boştur."
    ),
    make_q(
        "Bir tablodan <code>DELETE</code> işlemi yapıldığında tetikleyici içinde hangi mantıksal sözde tablo(lar) oluşur?",
        "Yalnızca <code>DELETED</code> tablosu oluşur (Silinen kayıtların eski hallerini tutar); <code>INSERTED</code> tablosu boştur.",
        ["Yalnızca INSERTED tablosu oluşur.", "Hem INSERTED hem DELETED tablosu oluşur.", "TRUNCATED tablosu oluşur.", "Sözde tablolar silinir."],
        "DELETE anında silinen satırları tutan DELETED tablosu mevcuttur; INSERTED boştur."
    ),
    make_q(
        "Bir tabloda <code>UPDATE</code> işlemi yapıldığında tetikleyici içinde sözde tabloların durumu ne olur?",
        "<code>DELETED</code> tablosu kaydın güncellemeden önceki eski halini, <code>INSERTED</code> tablosu ise güncellenmiş yeni halini tutar.",
        ["Yalnızca INSERTED tablosu oluşur ve eski değerler kaybolur.", "Yalnızca DELETED tablosu oluşur ve yeni değerler yazılmaz.", "UPDATED tablosu eski ve yeni değerleri tek sütunda birleştirir.", "UPDATE işleminde bu sözde tabloların ikisi de oluşturulmaz."],
        "UPDATE mantıksal olarak DELETE + INSERT işlemidir: Eski satır DELETED'e, yeni güncel satır INSERTED'e yazılır."
    ),
    make_q(
        "Tetikleyicilerde kullanılan <code>INSERTED</code> ve <code>DELETED</code> tabloları fiziksel olarak nerede saklanır?",
        "RAM bellekte geçici mantıksal tablolar olarak tutulur ve tetikleyici bitince otomatik temizlenir.",
        ["Veritabanı diskindeki kalıcı sistem tablolarında saklanır.", "Kullanıcının sabit diskindeki geçici text dosyasında saklanır.", "Transaction log dosyasında kalıcı olarak saklanır.", "Yalnızca CPU önbelleğinde saklanır."],
        "INSERTED ve DELETED tetikleyici süresince bellekte (RAM) tutulan mantıksal tablolardır."
    ),
    make_q(
        "Bir INSERT trigger'ı içinde <code>SELECT @faturaKod = faturaKod FROM inserted</code> ifadesi kullanılırken neye dikkat edilmelidir?",
        "Eğer tek seferde çok satırlı INSERT (küme ekleme) yapılmışsa, değişkende yalnızca en son satırın değeri kalır; küme tabanlı kod yazılmalıdır.",
        ["inserted tablosundaki sütun adları ana tablodan farklıdır.", "Bu ifade sözdizimi hatası verir ve trigger derlenmez.", "Değişken değeri daima NULL olur.", "inserted tablosu asla SELECT ile okunamaz."],
        "SQL Server trigger'ları satır başına değil ifade başına çalışır. INSERTED çok satır içerebilir, bu nedenle tek satır varsayımı tuzaktır."
    ),
    make_q(
        "Ürün fiyatlarının düşürülmesini engelleyen bir <code>AFTER UPDATE</code> trigger'ında fiyatın azalıp azalmadığı nasıl kontrol edilir?",
        "<code>IF EXISTS (SELECT 1 FROM inserted i JOIN deleted d ON i.urun_id = d.urun_id WHERE i.fiyat < d.fiyat)</code>",
        ["<code>IF (SELECT COUNT(*) FROM inserted) = 0</code>", "<code>IF EXISTS (SELECT * FROM deleted WHERE fiyat > 0)</code>", "<code>IF UPDATE(fiyat) = 0</code>", "<code>IF (SELECT AVG(fiyat) FROM Urun) < 100</code>"],
        "inserted (yeni fiyat) ile deleted (eski fiyat) urun_id üzerinden birleştirilir ve i.fiyat < d.fiyat şartı aranır."
    ),
    make_q(
        "Tetikleyici içinde geçersiz bir işlem tespit edildiğinde işlemi tamamen iptal edip veritabanını eski haline getirmek için hangi komut çalıştırılır?",
        "<code>ROLLBACK TRANSACTION</code>",
        ["<code>COMMIT TRANSACTION</code>", "<code>STOP TRIGGER</code>", "<code>BREAK</code>", "<code>EXIT</code>"],
        "ROLLBACK TRANSACTION tetikleyiciyi başlatan ana DML işlemini ve trigger'daki tüm değişiklikleri geri alarak işlemi iptal eder."
    ),
    make_q(
        "T-SQL trigger gövdesinde <code>IF UPDATE(liste_fiyat)</code> fonksiyonunun görevi nedir?",
        "UPDATE veya INSERT işlemi sırasında liste_fiyat sütununun güncellenip güncellenmediğini (değer atanıp atanmadığını) kontrol etmek",
        ["liste_fiyat sütununu tablodan silmek", "liste_fiyat sütunundaki tüm değerleri 0 yapmak", "liste_fiyat sütununa yeni indeks oluşturmak", "liste_fiyat sütunundaki değerleri otomatik olarak %10 artırmak"],
        "UPDATE(kolon) fonksiyonu ilgili kolonun UPDATE/INSERT ifadesinde hedef alınıp alınmadığını kontrol eder."
    ),
    make_q(
        "Sipariş eklendiğinde (INSERT) stok miktarını otomatik azaltan tetikleyicide doğru güncelleme ifadesi hangisidir?",
        "<code>UPDATE u SET u.stok = u.stok - i.adet FROM Urun u JOIN inserted i ON u.urun_id = i.urun_id</code>",
        ["<code>UPDATE Urun SET stok = stok - 1</code>", "<code>DELETE FROM Urun WHERE urun_id IN (SELECT urun_id FROM deleted)</code>", "<code>INSERT INTO Urun (stok) SELECT adet FROM inserted</code>", "<code>UPDATE Urun SET stok = 0 WHERE urun_id IN (SELECT urun_id FROM inserted)</code>"],
        "Urun tablosu inserted ile join edilerek eklenen siparişteki adet kadar stok miktarı düşürülür."
    ),
    make_q(
        "Bir tabloda silinen kayıtların eski halini otomatik olarak arşiv/log tablosuna kaydeden <code>AFTER DELETE</code> trigger'ının temel mantığı nedir?",
        "<code>INSERT INTO Notbilgi_Log SELECT *, GETDATE() FROM deleted</code>",
        ["<code>INSERT INTO Notbilgi_Log SELECT * FROM inserted</code>", "<code>UPDATE Notbilgi_Log SET tarih = GETDATE()</code>", "<code>DELETE FROM Notbilgi_Log WHERE id IN (SELECT id FROM deleted)</code>", "<code>TRUNCATE TABLE Notbilgi_Log</code>"],
        "Silinen satırların bilgisi DELETED tablosunda yer aldığından bu kayıtlar log tablosuna eklenir."
    ),
    make_q(
        "Bir tabloda birden fazla <code>AFTER INSERT</code> tetikleyicisi tanımlanabilir mi?",
        "Evet, bir tabloda aynı olay için birden fazla tetikleyici tanımlanabilir.",
        ["Hayır, bir tabloda her olay için yalnızca 1 adet trigger tanımlanabilir.", "Yalnızca INSTEAD OF trigger birden fazla olabilir, AFTER olamaz.", "Yalnızca Primary Key olmayan tablolarda birden fazla olabilir.", "Birden fazla trigger tanımlanırsa ilk trigger dışındakiler silinir."],
        "SQL Server'da aynı olay (INSERT/UPDATE/DELETE) için birden fazla AFTER trigger tanımlanabilir; ilk/son çalışma sp_settriggerorder ile ayarlanabilir."
    ),
    make_q(
        "Bir tabloda aynı olay (örneğin INSERT) için birden fazla <code>INSTEAD OF</code> tetikleyicisi tanımlanabilir mi?",
        "Hayır, bir tablo veya görünüm üzerinde her bir olay (INSERT, UPDATE, DELETE) için en fazla 1 adet INSTEAD OF trigger tanımlanabilir.",
        ["Evet, sınırsız sayıda INSTEAD OF trigger tanımlanabilir.", "Evet, ancak her biri farklı kullanıcılar tarafından çalıştırılmalıdır.", "Yalnızca VIEW'lerde birden fazla olabilir, tablolarda olamaz.", "Evet, ancak isimleri alfabetik sırada olmalıdır."],
        "Kritik kural: Tablo veya view başına her DML olayı için en fazla BİR adet INSTEAD OF trigger tanımlanabilir."
    ),
    make_q(
        "İç İçe Tetikleyici (Nested Trigger) kavramı ne anlama gelir?",
        "Bir trigger'ın yaptığı DML işleminin (örneğin başka bir tabloya INSERT yapması), o tablodaki başka bir trigger'ı tetiklemesi",
        ["Bir trigger içinde başka bir trigger'ın CREATE komutuyla sıfırdan oluşturulması", "Trigger'ın kendi tablosundaki kaydı silip tekrar eklemesi", "Trigger'ın yalnızca SELECT sorgularında çalışması", "Trigger'ın birden fazla veritabanında aynı anda çalışması"],
        "Nested trigger: Trigger A -> Tablo B'yi günceller -> Tablo B'nin Trigger'ı çalışır. SQL Server varsayılan olarak 32 seviyeye kadar destekler."
    ),
    make_q(
        "Özyinelemeli Tetikleyici (Recursive Trigger) ne demektir?",
        "Bir trigger'ın yaptığı işlemin dönüp yine kendi kendisini (doğrudan veya dolaylı olarak) tekrar tetiklemesi",
        ["Trigger'ın her gün aynı saatte otomatik çalışması", "Trigger'ın veritabanındaki tüm tabloları sırayla dolaşması", "Trigger'ın hata verdiğinde baştan başlaması", "Trigger'ın iki farklı dilde derlenmesi"],
        "Direct recursion: Trigger Tablo A'yı günceller -> Tablo A'nın aynı trigger'ı tekrar tetiklenir."
    ),
    make_q(
        "Bir tetikleyiciyi silmeden geçici olarak devre dışı bırakmak için hangi SQL komutu kullanılır?",
        "<code>ALTER TABLE TabloAdi DISABLE TRIGGER TriggerAdi</code>",
        ["<code>DROP TRIGGER TriggerAdi PAUSE</code>", "<code>STOP TRIGGER TriggerAdi ON TabloAdi</code>", "<code>UPDATE TRIGGER TriggerAdi SET durum = 0</code>", "<code>DELETE TRIGGER TriggerAdi</code>"],
        "Tetikleyiciyi geçici olarak kapatmak için ALTER TABLE ... DISABLE TRIGGER komutu kullanılır."
    ),
    make_q(
        "Devre dışı bırakılmış bir tetikleyiciyi yeniden etkinleştirmek için hangi komut kullanılır?",
        "<code>ALTER TABLE TabloAdi ENABLE TRIGGER TriggerAdi</code>",
        ["<code>START TRIGGER TriggerAdi ON TabloAdi</code>", "<code>RESUME TRIGGER TriggerAdi</code>", "<code>CREATE TRIGGER TriggerAdi RESTART</code>", "<code>EXEC sp_enable_trigger TriggerAdi</code>"],
        "Tetikleyiciyi tekrar aktif hale getirmek için ALTER TABLE ... ENABLE TRIGGER komutu kullanılır."
    ),
    make_q(
        "Bir tetikleyiciyi veritabanından tamamen silmek için hangi komut kullanılır?",
        "<code>DROP TRIGGER TriggerAdi</code>",
        ["<code>DELETE TRIGGER TriggerAdi</code>", "<code>REMOVE TRIGGER TriggerAdi</code>", "<code>ALTER TABLE TabloAdi REMOVE TRIGGER TriggerAdi</code>", "<code>CLEAR TRIGGER TriggerAdi</code>"],
        "Tetikleyiciler DROP TRIGGER komutuyla silinir."
    ),
    make_q(
        "Tetikleyicilerin kullanım amaçları arasında aşağıdakilerden hangisi YER ALMAZ?",
        "Kullanıcı arayüzünden doğrudan çağrılarak form verilerini ekrana yazdırmak",
        ["Karmaşık iş kurallarını (business rules) ve veri bütünlüğünü zorunlu kılmak", "Kritik tablolarda yapılan tüm değişikliklerin denetim (audit/log) kaydını tutmak", "İlişkili tablolardaki türetilmiş/özet alanları otomatik güncellemek", "Geçersiz veya kural dışı veritabanı işlemlerini ROLLBACK ile engellemek"],
        "Trigger'lar kullanıcı tarafından doğrudan çağrılamaz; arka planda olay tabanlı çalışırlar."
    ),
    make_q(
        "Aşağıdaki trigger kodunda hangi eksiklik vardır?\n<code>CREATE TRIGGER tr_Test ON Personel AFTER UPDATE AS SELECT * FROM inserted</code>",
        "Trigger'lar istemciye gereksiz sonuç kümesi (Result Set) döndürmemelidir; bu performans kaybına ve uygulama hatalarına yol açar.",
        ["AFTER yerine daima BEFORE kullanılmalıdır.", "Personel tablosuna trigger yazılamaz.", "inserted tablosundan asla SELECT yapılamaz.", "CREATE TRIGGER başında DECLARE yazılmalıdır."],
        "Trigger içinde salt SELECT ile istemciye sonuç basılması kötü bir pratiktir ve uygulamalarda beklenmedik sonuçlara yol açar."
    ),
    make_q(
        "<code>INSTEAD OF INSERT</code> trigger'ı tanımlı bir tabloya <code>INSERT INTO Tablo VALUES(...)</code> çalıştırıldığında ne olur?",
        "Ana tabloya doğrudan hiçbir kayıt eklenmez; bunun yerine trigger içindeki T-SQL kodları yürütülür.",
        ["Kayıt hem ana tabloya eklenir hem de trigger çalışır.", "İşlem hata verir ve INSERT komutu reddedilir.", "Tablodaki tüm eski veriler silinir.", "Veritabanı sunucusu kilitlenir."],
        "INSTEAD OF trigger orijinal DML işlemini bypass eder ve yerine kendi gövdesindeki kodu çalıştırır."
    ),
    make_q(
        "Bir görünüm (VIEW) üzerinde <code>INSTEAD OF INSERT</code> trigger'ı tanımlanmasının temel gerekçesi nedir?",
        "Normal şartlarda güncellenemeyen (örneğin çok tablolu veya JOIN içeren) bir görünüm üzerinden gelen ekleme isteklerini arka plandaki gerçek tablolara paylaştırmak",
        ["Görünümü fiziksel bir tabloya dönüştürmek", "Görünümün indeksini hızlandırmak", "Görünümdeki verileri şifrelemek", "Görünümü salt okunur hale getirmek"],
        "Karmaşık VIEW'ler doğrudan güncellenemez; INSTEAD OF trigger ile gelen veriler parçalanarak temel tablolara eklenir."
    ),
    make_q(
        "Tetikleyicilerde <code>COLUMNS_UPDATED()</code> fonksiyonu ne tür bir değer döndürür?",
        "Tablodaki hangi sütunların güncellendiğini bit düzeyinde gösteren bir VARBINARY (bitmask) değeri",
        ["Güncellenen sütunların adlarını içeren bir metin dizisi", "Toplam güncellenen satır sayısını", "Tetikleyicinin çalışma süresini milisaniye cinsinden", "Hata kodunu"],
        "COLUMNS_UPDATED() tablodaki sütunların güncelleme durumunu bitmask (VARBINARY) olarak döndürür."
    ),
    make_q(
        "Bir trigger içinde geçici tablo (Temporary Table - <code>#temp</code>) oluşturulabilir mi?",
        "Evet, trigger gövdesi içinde yerel geçici tablo (#temp) veya tablo değişkeni tanımlanabilir ve kullanılabilir.",
        ["Hayır, trigger içinde geçici nesneler oluşturmak kesinlikle yasaktır.", "Yalnızca global geçici tablo (##temp) oluşturulabilir.", "Yalnızca INSTEAD OF trigger'larda izin verilir.", "Sadece Oracle PL/SQL'de izin verilir."],
        "Trigger içinde yerel geçici tablolar ve tablo değişkenleri serbestçe kullanılabilir."
    ),
    make_q(
        "Bir trigger çalıştığında oluşan bir hata <code>TRY...CATCH</code> ile yakalanmazsa ne olur?",
        "Tetikleyiciyi başlatan ana DML işlemi ve trigger içindeki tüm işlemler otomatik olarak iptal edilir (Transaction Rollback olur).",
        ["Trigger atlanır ve ana DML işlemi başarıyla kaydedilir.", "Veritabanı tablosu silinir.", "Yalnızca hata veren satır atlanır, diğerleri eklenir.", "Sunucu yeniden başlar."],
        "Trigger bir transaction içinde çalıştığından yakalanmayan bir hata tüm transaction'ın rollback olmasına yol açar."
    ),
    make_q(
        "Aşağıdaki trigger tanımı hangi olay için çalışır?\n<code>CREATE TRIGGER tr_Log ON Musteri FOR INSERT, UPDATE, DELETE AS BEGIN ... END</code>",
        "Musteri tablosunda gerçekleşen INSERT, UPDATE veya DELETE işlemlerinin herhangi birinde çalışır.",
        ["Yalnızca aynı anda hem ekleme hem silme yapıldığında çalışır.", "Sözdizimi hatası verir çünkü tek trigger yalnız tek olay alabilir.", "Yalnızca Musteri tablosu oluşturulduğunda çalışır.", "Yalnızca SELECT sorgularında çalışır."],
        "Tek bir trigger birden fazla olay (INSERT, UPDATE, DELETE) için ortak olarak tanımlanabilir."
    ),
    make_q(
        "Bir <code>AFTER UPDATE</code> trigger'ında hem <code>INSERTED</code> hem <code>DELETED</code> tablosundaki satır sayıları daima birbirine eşit midir?",
        "Evet, güncellenen her bir satır için DELETED'e eski hali, INSERTED'e yeni hali yazıldığından satır sayıları daima eşittir.",
        ["Hayır, INSERTED tablosunda daima daha çok satır bulunur.", "Hayır, DELETED tablosunda daima daha çok satır bulunur.", "Yalnızca tekil anahtarlı tablolarda eşittir.", "Sadece tablodaki satır sayısı çift ise eşittir."],
        "UPDATE satırın yerini değiştirdiği için etkilenen satır adedi her iki tabloda da (INSERTED ve DELETED) kesinlikle aynıdır."
    ),
    make_q(
        "Bir trigger içinde <code>ROLLBACK TRANSACTION</code> çalıştırıldıktan sonra kodun devam etmesini engellemek için ne yapılmalıdır?",
        "ROLLBACK'in hemen ardından <code>RETURN;</code> komutu yazılarak trigger sonlandırılmalıdır.",
        ["<code>COMMIT;</code> yazılmalıdır.", "<code>BREAK;</code> yazılmalıdır.", "<code>WAITFOR;</code> yazılmalıdır.", "<code>DROP TRIGGER;</code> yazılmalıdır."],
        "ROLLBACK transaction'ı iptal eder ama trigger kodunun akışını kesmez; gereksiz kod işletilmemesi için RETURN eklenmelidir."
    ),
    make_q(
        "Aşağıdaki trigger'ın amacı nedir?\n<code>CREATE TRIGGER tr_NotKontrol ON notbilgi AFTER INSERT, UPDATE AS IF EXISTS (SELECT * FROM inserted WHERE vizenot < 0 OR vizenot > 100) BEGIN RAISERROR('Geçersiz vize notu', 16, 1); ROLLBACK TRANSACTION; END</code>",
        "notbilgi tablosuna eklenen veya güncellenen vize notunun 0-100 aralığı dışında olması durumunda işlemi iptal etmek",
        ["Vize notu 0 olan öğrencileri dersten bırakmak", "Tüm vize notlarını 100'e eşitlemek", "Vize notu girilmemiş öğrencilere 50 vermek", "Vize notu 100 olanları ödüllendirmek"],
        "Bu trigger eklenen/güncellenen vizenot değerlerini denetler, 0-100 dışındaysa işlemi ROLLBACK ile geri alır."
    ),
    make_q(
        "Bir tabloda <code>DDL Trigger</code> ne amaçla tanımlanır?",
        "Veritabanında CREATE TABLE, ALTER TABLE veya DROP TABLE gibi yapısal DDL olaylarını izlemek veya engellemek",
        ["INSERT ve UPDATE işlemlerini hızlandırmak", "Tablodaki verileri şifrelemek", "Sadece kullanıcı girişlerini denetlemek", "Bellek kullanımını temizlemek"],
        "DDL Trigger veritabanı veya sunucu düzeyinde DDL komutlarına (CREATE, ALTER, DROP vb.) karşı tetiklenir."
    ),
    make_q(
        "Oracle PL/SQL'de satır düzeyinde tetikleyici (Row-Level Trigger) tanımlamak için hangi ifade kullanılır?",
        "<code>FOR EACH ROW</code>",
        ["<code>FOR EACH TABLE</code>", "<code>PER ROW LOOP</code>", "<code>ROW LEVEL ONLY</code>", "<code>FOR EVERY RECORD</code>"],
        "Oracle PL/SQL'de her satır için ayrı tetiklenen satır düzeyi trigger'lar FOR EACH ROW ifadesi ile tanımlanır."
    ),
    make_q(
        "Oracle PL/SQL satır düzeyi tetikleyicilerinde eski ve yeni değerlere nasıl erişilir?",
        "<code>:OLD.sutun_adi</code> ve <code>:NEW.sutun_adi</code> sözde kayıtları (pseudo-records) ile",
        ["INSERTED ve DELETED tabloları ile", "PRIOR ve NEXT göstericileri ile", "BEFORE ve AFTER değişkenleri ile", "CURRENT ve PREVIOUS fonksiyonları ile"],
        "Oracle PL/SQL'de :OLD (eski değer) ve :NEW (yeni değer) sözde kayıtları kullanılır."
    ),
    make_q(
        "Oracle PL/SQL'de bir kayıt silinmeden veya güncellenmeden önce değerleri kontrol etmek/değiştirmek için hangi trigger zamanlaması kullanılır?",
        "<code>BEFORE</code> Trigger",
        ["<code>AFTER</code> Trigger", "<code>INSTEAD OF</code> Trigger", "<code>WHILE</code> Trigger", "<code>DURING</code> Trigger"],
        "Oracle'da BEFORE trigger DML işlemi gerçekleşmeden önce çalışır ve :NEW alanlarının değiştirilmesine izin verir."
    ),
    make_q(
        "Bir tabloda tanımlı tüm tetikleyicileri tek seferde devre dışı bırakmak için hangi komut kullanılır?",
        "<code>ALTER TABLE TabloAdi DISABLE TRIGGER ALL</code>",
        ["<code>DROP ALL TRIGGERS ON TabloAdi</code>", "<code>STOP ALL TRIGGERS</code>", "<code>UPDATE TRIGGERS SET aktif = 0</code>", "<code>CLEAR TRIGGERS FROM TabloAdi</code>"],
        "DISABLE TRIGGER ALL komutu tablodaki tüm trigger'ları tek seferde pasife alır."
    ),
    make_q(
        "Tetikleyicilerin aşırı ve kontrolsüz kullanımının sistem üzerindeki en büyük olumsuz etkisi nedir?",
        "Veritabanı performansını düşürmesi, karmaşık hata ayıklama süreçlerine yol açması ve gizli yan etkiler üretmesi",
        ["Tabloların disk boyutunu küçültmesi", "Kullanıcıların SELECT sorgusu çekmesini tamamen engellemesi", "Veritabanı lisans maliyetini artırması", "İndekslerin otomatik silinmesine neden olması"],
        "Aşırı trigger kullanımı DML işlemlerini yavaşlatır, arkada gizli işlemler yaptığı için hata takibini zorlaştırır."
    ),
    make_q(
        "SQL Server'da tetikleyicinin oluşturulma tarihini ve kaynak kodunu hangi sistem görünümünden sorgulayabiliriz?",
        "<code>sys.triggers</code> ve <code>sys.sql_modules</code>",
        ["<code>sys.tables</code> ve <code>sys.columns</code>", "<code>sys.databases</code>", "<code>sys.indexes</code>", "<code>sys.users</code>"],
        "sys.triggers tetikleyici metaverilerini, sys.sql_modules ise nesnelerin kaynak SQL kodlarını tutar."
    ),
    make_q(
        "Bir UPDATE trigger'ında <code>SELECT * FROM deleted</code> sonucu boş ise bu ne anlama gelir?",
        "Böyle bir durum imkansızdır; UPDATE işleminde DELETED tablosu asla boş olamaz (etkilenen satır yoksa zaten trigger çalışmaz).",
        ["İşlemin bir INSERT işlemi olduğunu gösterir.", "Güncelleme yapılan sütunun NULL olduğunu gösterir.", "Tabloda birincil anahtar olmadığını gösterir.", "Trigger'ın devre dışı olduğunu gösterir."],
        "UPDATE tetiklendiğinde güncellenen satır sayısı > 0'dır ve eski haller mutlaka DELETED içinde yer alır."
    )
]

print(f"Exam 5: {len(e5)}, Exam 6: {len(e6)}")
