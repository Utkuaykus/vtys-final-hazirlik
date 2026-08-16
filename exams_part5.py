# -*- coding: utf-8 -*-
"""
exams_part5.py: Exam 9 and Exam 10
"""
import random
random.seed(109)

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
# EXAM 9: Oracle PL/SQL Mimarisi, Paketler, Koleksiyonlar & İleri Konular
# (Kaynaklar: DBMS_8, DBMS_8_1, DBMS_8_2, veritabanıfinal)
# =========================================================================
e9 = [
    make_q(
        "Oracle PL/SQL blok yapısında bulunması ZORUNLU olan tek bölüm aşağıdakilerden hangisidir?",
        "<code>BEGIN ... END;</code> (Çalıştırılabilir / Yürütme Bölümü)",
        ["<code>DECLARE</code> (Bildirim Bölümü)", "<code>EXCEPTION</code> (Hata Yakalama Bölümü)", "<code>PACKAGE BODY</code>", "<code>HEADER</code>"],
        "PL/SQL bloğunda DECLARE ve EXCEPTION isteğe bağlıdır; ancak BEGIN ... END; yürütülebilir bölümü zorunludur."
    ),
    make_q(
        "PL/SQL'de <code>v_maas Personel.maas%TYPE;</code> tanımlamasındaki <code>%TYPE</code> özniteliği ne sağlar?",
        "v_maas değişkeninin veri tipini ve boyutunu Personel tablosundaki maas sütunu ile dinamik olarak aynı yapar.",
        ["v_maas değişkenini tablonun birincil anahtarı yapar.", "v_maas değişkenine maas sütununun ortalama değerini atar.", "v_maas değişkenini tablonun tüm satırlarını tutacak bir diziye çevirir.", "v_maas değişkenini salt okunur sabit yapar."],
        "%TYPE belirtilen sütunun veri tipini miras alır; tabloda sütun tipi değiştiğinde kod otomatik uyum sağlar."
    ),
    make_q(
        "PL/SQL'de <code>v_kayit Personel%ROWTYPE;</code> tanımlamasındaki <code>%ROWTYPE</code> özniteliği ne sağlar?",
        "v_kayit değişkenini Personel tablosunun tüm sütun yapısını içeren bir kayıt (Record) olarak tanımlar.",
        ["v_kayit değişkenine Personel tablosunun toplam satır sayısını atar.", "v_kayit değişkenini sadece ilk satırı okuyacak şekilde kilitler.", "Personel tablosuna yeni bir satır ekler.", "Personel tablosundaki NULL satırları sayar."],
        "%ROWTYPE tablonun veya cursor'ın tüm satır şemasını tek bir yapılandırılmış kayıt değişkenine bağlar."
    ),
    make_q(
        "PL/SQL'de <code>SELECT ad, maas INTO v_ad, v_maas FROM Personel WHERE id = 1;</code> ifadesi hiç kayıt bulamazsa hangi istisna (exception) tetiklenir?",
        "<code>NO_DATA_FOUND</code>",
        ["<code>TOO_MANY_ROWS</code>", "<code>ZERO_DIVIDE</code>", "<code>VALUE_ERROR</code>", "<code>INVALID_CURSOR</code>"],
        "SELECT ... INTO ifadesi en az 1 satır bekler; hiç satır dönmezse önceden tanımlı NO_DATA_FOUND istisnası oluşur."
    ),
    make_q(
        "PL/SQL'de <code>SELECT INTO</code> ifadesi birden fazla satır (örn: 5 satır) döndürürse hangi istisna tetiklenir?",
        "<code>TOO_MANY_ROWS</code>",
        ["<code>NO_DATA_FOUND</code>", "<code>DUP_VAL_ON_INDEX</code>", "<code>INVALID_NUMBER</code>", "<code>ROWCOUNT_ERROR</code>"],
        "SELECT ... INTO tek bir satır atamak için tasarlanmıştır; birden fazla satır gelirse TOO_MANY_ROWS fırlatılır."
    ),
    make_q(
        "PL/SQL'de ekrana veya çıktı tamponuna metin yazdırmak için hangi paket ve yordam kullanılır?",
        "<code>DBMS_OUTPUT.PUT_LINE('Mesaj');</code>",
        ["<code>PRINT('Mesaj');</code>", "<code>SYSTEM.OUT.PRINTLN('Mesaj');</code>", "<code>CONSOLE.LOG('Mesaj');</code>", "<code>ECHO('Mesaj');</code>"],
        "Oracle PL/SQL'de çıktı üretmek için DBMS_OUTPUT.PUT_LINE kullanılır (istemcide SET SERVEROUTPUT ON gereklidir)."
    ),
    make_q(
        "PL/SQL'de değişkenlere değer atamak için hangi operatör kullanılır?",
        "<code>:=</code> (İki nokta üst üste ve eşit)",
        ["<code>=</code> (Tek eşit)", "<code>==</code> (Çift eşit)", "<code><-</code> (Sol ok)", "<code>SET</code>"],
        "PL/SQL'de değer atama operatörü Pascal/Ada kökenli := operatörüdür (= ise karşılaştırmadır)."
    ),
    make_q(
        "PL/SQL'de <code>CONSTANT</code> anahtar kelimesi ile tanımlanan bir değişkenin özelliği nedir?",
        "Değeri tanımlama anında atanır ve program akışı boyunca bir daha asla değiştirilemez (Sabit değerdir).",
        ["Değeri her saniye otomatik sıfırlanır.", "Değişken tüm veritabanı kullanıcıları tarafından değiştirilebilir.", "Değişken yalnızca negatif sayılar tutabilir.", "Değişken diske kalıcı tablo olarak yazılır."],
        "CONSTANT ile tanımlanan değişkenler sabittir (Örn: PI CONSTANT NUMBER := 3.14;)."
    ),
    make_q(
        "Aşağıdaki PL/SQL döngüsü kaç kez çalışır?\n<code>FOR i IN 1..5 LOOP\n    DBMS_OUTPUT.PUT_LINE(i);\nEND LOOP;</code>",
        "5 kez çalışır (1, 2, 3, 4, 5)",
        ["4 kez çalışır (1..5 aralığında 5 hariç)", "Sonsuz döngüye girer", "Hiç çalışmaz", "1 kez çalışır"],
        "PL/SQL FOR döngüsünde alt ve üst sınır dahildir; sayaç otomatik tanımlanır ve 1'den 5'e kadar 5 kez döner."
    ),
    make_q(
        "Yukarıdaki <code>FOR i IN 1..5 LOOP</code> döngüsünde <code>i</code> değişkeninin geriye doğru (5, 4, 3, 2, 1) sayması için hangi anahtar kelime eklenir?",
        "<code>FOR i IN REVERSE 1..5 LOOP</code>",
        ["<code>FOR i IN 5..1 LOOP</code>", "<code>FOR i IN DESC 1..5 LOOP</code>", "<code>FOR i IN DOWNTO 5..1 LOOP</code>", "<code>FOR i IN BACKWARD 1..5 LOOP</code>"],
        "Geriye doğru döngü için REVERSE anahtar kelimesi kullanılır: FOR i IN REVERSE 1..5 LOOP."
    ),
    make_q(
        "PL/SQL'de kullanıcı tanımlı bir istisna (User-Defined Exception) nasıl fırlatılır?",
        "<code>DECLARE v_hata EXCEPTION; BEGIN ... RAISE v_hata; END;</code>",
        ["<code>THROW v_hata;</code>", "<code>FIRE EXCEPTION v_hata;</code>", "<code>CALL ERROR v_hata;</code>", "<code>CATCH v_hata;</code>"],
        "Kullanıcı tanımlı exception DECLARE'da tanımlanır, RAISE komutu ile açıkça fırlatılır ve EXCEPTION bloğunda yakalanır."
    ),
    make_q(
        "PL/SQL'de yakalanmayan veya adı belirtilmeyen tüm diğer istisnaları genel olarak yakalamak için hangi yapı kullanılır?",
        "<code>WHEN OTHERS THEN ...</code>",
        ["<code>WHEN ALL THEN ...</code>", "<code>DEFAULT EXCEPTION ...</code>", "<code>ELSE ERROR ...</code>", "<code>CATCH ALL ...</code>"],
        "WHEN OTHERS THEN istisna bloğunun en sonuna yazılır ve belirtilmeyen tüm olası hataları yakalar."
    ),
    make_q(
        "PL/SQL yordam ve fonksiyonlarında <code>IN</code> parametre modu ne anlama gelir?",
        "Parametre yalnızca alt programa değer aktarır (Salt okunurdur, yordam içinde değiştirilemez).",
        ["Parametre yordam içinden dışarıya değer döndürür.", "Parametre hem okunur hem yazılır.", "Parametrenin varsayılanı daima NULL'dır.", "Parametre diskte saklanır."],
        "IN modu varsayılan parametre modudur ve alt programa salt okunur (read-only) giriş değeri sağlar."
    ),
    make_q(
        "PL/SQL yordamlarında <code>OUT</code> parametre modu ne anlama gelir?",
        "Alt programın çağıran ortama değer döndürmesini sağlar (Başlangıçta içi boştur, alt program içinde değer atanır).",
        ["Yalnızca alt programa giriş değeri taşır.", "Parametrenin silinmesini sağlar.", "Parametreyi sabit (constant) yapar.", "Sadece metin verilerini aktarır."],
        "OUT modu alt programdan dışarıya veri aktarmak için kullanılır."
    ),
    make_q(
        "PL/SQL yordamlarında <code>IN OUT</code> parametre modu ne anlama gelir?",
        "Hem dışarıdan bir başlangıç değeri alır hem de işlem sonucunda değişen yeni değeri dışarıya aktarır.",
        ["Parametrenin iki farklı veri tipine sahip olmasını sağlar.", "Parametreyi iki katına çıkarır.", "Parametrenin NULL olmasını engeller.", "Parametreyi tabloya dönüştürür."],
        "IN OUT parametresi hem girdi hem çıktı olarak iki yönlü çalışır."
    ),
    make_q(
        "Oracle PL/SQL Paketleri (Package) hangi iki ana bölümden oluşur?",
        "Paket Bildirimi (Package Specification) ve Paket Gövdesi (Package Body)",
        ["Paket Başlığı (Header) ve Paket Sonu (Footer)", "Paket Girdisi (Input) ve Paket Çıktısı (Output)", "Public Bölüm ve Private Tablo", "Paket Arayüzü ve Paket Veritabanı"],
        "Paket iki parçadır: Specification (dışarıya açık arayüz bildirimleri) ve Body (kodların asıl gövdesi/uygulaması)."
    ),
    make_q(
        "Paket Bildirimi (Package Specification) ile ilgili hangisi DOĞRUDUR?",
        "Paketin dışarıdan erişilebilen genel (public) yordam, fonksiyon, değişken ve tip tanımlarını içerir.",
        ["Tüm yordamların ve fonksiyonların ayrıntılı kaynak kodlarını içerir.", "Yalnızca veritabanı tablolarını silmek için kullanılır.", "Mutlaka Package Body oluşturulduktan sonra yazılmalıdır.", "Paket bildirimi olmadan da Package Body tek başına çalışabilir."],
        "Specification paketin halka açık (public) arayüzüdür; önce Specification tanımlanır, sonra Body yazılır."
    ),
    make_q(
        "Paket Gövdesinde (Package Body) tanımlanmış fakat Paket Bildiriminde (Specification) yer almayan bir yordamın özelliği nedir?",
        "Özeldir (Private); paket dışından çağrılamaz, yalnızca paket içindeki diğer yordamlar tarafından kullanılabilir.",
        ["Sözdizimi hatası verir ve paket derlenmez.", "Tüm veritabanı kullanıcıları tarafından serbestçe çağrılabilir.", "Otomatik olarak sistem yordamı haline gelir.", "Diskten kalıcı olarak silinir."],
        "Specification'da bildirilmeyen öğeler private (gizli) kalır ve bilgi gizleme (encapsulation) sağlar."
    ),
    make_q(
        "PL/SQL'de kullanıcı tanımlı bir Kayıt Tipi (Record Type) nasıl oluşturulur?",
        "<code>TYPE kitap_t IS RECORD (baslik VARCHAR2(50), yazar VARCHAR2(50), fiyat NUMBER);</code>",
        ["<code>CREATE RECORD kitap_t (baslik VARCHAR2(50));</code>", "<code>DECLARE RECORD kitap_t AS TABLE;</code>", "<code>NEW RECORD TYPE kitap_t;</code>", "<code>SET TYPE kitap_t = RECORD;</code>"],
        "Kullanıcı tanımlı kayıt: TYPE tip_adi IS RECORD (alan_tanimlari);"
    ),
    make_q(
        "PL/SQL Koleksiyon türlerinden <code>VARRAY(n)</code> (Değişken Boyutlu Dizi) nedir?",
        "Aynı veri tipinde, en fazla n adet eleman barındırabilen, sabit üst sınırlı sıralı bir koleksiyondur.",
        ["Sınırsız sayıda heterojen veriyi tutan tablodur.", "Yalnızca metin anahtarlarla indekslenen bir sözlüktür.", "Diskte kalıcı olarak saklanan ilişkisel tablodur.", "Tek bir skaler sayıyı tutan yapıdır."],
        "VARRAY(n) maksimum n eleman sınırı olan sıralı homojen koleksiyon yapısıdır."
    ),
    make_q(
        "PL/SQL Koleksiyon türlerinden 'Nested Table' (İç İçe Tablo) ne tür bir yapıdır?",
        "Boyutu dinamik olarak büyüyebilen, sırasız ve veritabanı sütununda da saklanabilen tek boyutlu koleksiyondur.",
        ["Maksimum 5 eleman alan sabit bir dizidir.", "Yalnızca hata kodlarını saklayan yapıdır.", "Sadece SELECT sorgularında kullanılan geçici görünümdür.", "İki boyutlu bir matris yapısıdır."],
        "Nested Table dinamik genişleyebilen ve tablolarda sütun tipi olarak da kullanılabilen koleksiyondur."
    ),
    make_q(
        "PL/SQL Koleksiyon türlerinden 'Associative Array' (İlişkili Dizi / Index-By Table) nedir?",
        "Anahtar-değer (Key-Value) mantığıyla çalışan ve anahtarları tamsayı veya metin (VARCHAR2) olabilen koleksiyondur.",
        ["Yalnızca çift sayılı indeksleri kabul eden dizidir.", "Sadece diske yazılabilen kalıcı veri tablosudur.", "Boyutu asla değiştirilemeyen sabit dizidir.", "Yalnızca NULL değerleri tutan yapıdır."],
        "Associative Array (Index-by table) anahtar-değer sözlük yapısıdır (TYPE t_arr IS TABLE OF tip INDEX BY PLS_INTEGER / VARCHAR2)."
    ),
    make_q(
        "PL/SQL koleksiyonlarında koleksiyondaki toplam eleman sayısını veren metot hangisidir?",
        "<code>koleksiyon.COUNT</code>",
        ["<code>koleksiyon.LENGTH</code>", "<code>koleksiyon.SIZE</code>", "<code>koleksiyon.TOTAL</code>", "<code>koleksiyon.ROWS</code>"],
        "Koleksiyon metotları: COUNT (eleman sayısı), FIRST/LAST (ilk/son indeks), EXTEND (yer açma), DELETE (eleman silme)."
    ),
    make_q(
        "PL/SQL koleksiyonuna yeni bir eleman alanı eklemek (bellek genişletmek) için hangi metot kullanılır?",
        "<code>koleksiyon.EXTEND</code>",
        ["<code>koleksiyon.ADD</code>", "<code>koleksiyon.APPEND</code>", "<code>koleksiyon.INSERT</code>", "<code>koleksiyon.NEW</code>"],
        "EXTEND metodu Nested Table ve VARRAY koleksiyonlarına yeni eleman yuvası açar."
    ),
    make_q(
        "PL/SQL'de bir bloğun sonunda kullanılan <code>/</code> (bölü / eğik çizgi) karakterinin görevi nedir?",
        "SQL*Plus veya istemci aracına yazılan PL/SQL bloğunun tamamlandığını ve sunucuya gönderilip yürütülmesi gerektiğini bildirir.",
        ["Bölme işlemi yapar.", "Yorum satırı başlatır.", "Transaction'ı geri alır.", "Belleği temizler."],
        "/ karakteri istemci aracına önceki PL/SQL bloğunu derleyip çalıştırma (Execute) sinyali verir."
    ),
    make_q(
        "Oracle PL/SQL'de <code>DUP_VAL_ON_INDEX</code> standart istisnası ne zaman tetiklenir?",
        "PRIMARY KEY veya UNIQUE indeksli bir sütuna aynı değerden ikinci kez ekleme yapılmak istendiğinde",
        ["Sıfıra bölme işlemi yapıldığında", "Sorgu hiç satır döndürmediğinde", "İndeks tablodan silindiğinde", "Cursor kapatılamadığında"],
        "DUP_VAL_ON_INDEX tekillik kısıtlaması (Unique / Primary Key) ihlal edildiğinde fırlatılır."
    ),
    make_q(
        "Aşağıdaki PL/SQL kodunun çıktısı nedir?\n<code>DECLARE\n    v_x NUMBER := 10;\nBEGIN\n    v_x := v_x + 5;\n    DBMS_OUTPUT.PUT_LINE('Sonuç: ' || v_x);\nEND;</code>",
        "'Sonuç: 15'",
        ["'Sonuç: 10'", "'Sonuç: 5'", "'Sonuç: v_x'", "Hata verir"],
        "v_x 10 ile başlar, +5 ile 15 olur. || metin birleştirme operatörüdür, ekrana 'Sonuç: 15' basılır."
    ),
    make_q(
        "Oracle PL/SQL'de metinleri birbirine bağlamak (String Concatenation) için hangi operatör kullanılır?",
        "<code>||</code> (Çift dikey çubuk)",
        ["<code>+</code> (Artı)", "<code>&</code> (Ve)", "<code>CONCAT_CHAR</code>", "<code>..</code> (İki nokta)"],
        "PL/SQL ve standart Oracle SQL'de metin birleştirme operatörü || (double pipe) sembolüdür."
    ),
    make_q(
        "PL/SQL'de <code>GOTO</code> etiketi nasıl tanımlanır ve yönlendirilir?",
        "Etiket <code><<etiket_adi>></code> ile tanımlanır ve <code>GOTO etiket_adi;</code> ile atlanır.",
        ["Etiket <code>#etiket</code> ile tanımlanır ve <code>JUMP etiket;</code> ile atlanır.", "Etiket <code>LABEL etiket:</code> ile tanımlanır.", "Etiket <code>@etiket</code> ile tanımlanır.", "PL/SQL'de GOTO tamamen yasaktır ve bulunmaz."],
        "PL/SQL'de etiketler <<label>> şeklinde tanımlanır ve GOTO label; ile dallanma yapılır."
    ),
    make_q(
        "PL/SQL'de <code>NULL;</code> ifadesinin yürütülebilir bir bloktaki işlevi nedir?",
        "Hiçbir işlem yapmayan geçerli bir yer tutucu ifadedir (Örn: Boş bir EXCEPTION durumunu geçiştirmek için).",
        ["Tüm değişkenleri NULL yapar.", "Tablodaki verileri siler.", "Programı derhal durdurur.", "Transaction'ı geri alır."],
        "PL/SQL'de boş kod bloğu olamaz; hiçbir işlem yapılmayacaksa sözdizimini tamamlamak için NULL; yazılır."
    ),
    make_q(
        "PL/SQL'de <code>PRAGMA AUTONOMOUS_TRANSACTION</code> direktifi ne sağlar?",
        "Bir yordamın veya trigger'ın, ana transaction'dan bağımsız kendi özel COMMIT veya ROLLBACK işlemine sahip özerk bir transaction yürütmesini",
        ["Trigger'ın otomatik olarak her saniye çalışmasını", "Veritabanının kullanıcı oturumunu kapatmasını", "Tablonun otomatik yedeklenmesini", "Tüm Foreign Key kısıtlamalarını kaldırmasını"],
        "Autonomous transaction ana işlemden bağımsız ayrı bir transaction başlatır (Örn: Hata logunu ana işlem rollback olsa bile kaydetmek için)."
    ),
    make_q(
        "Oracle'da Sequence (Sıra Numarası Üreteci) nesnesinden bir sonraki değeri almak için hangi sözdizimi kullanılır?",
        "<code>sequence_adi.NEXTVAL</code>",
        ["<code>sequence_adi.CURRVAL</code>", "<code>sequence_adi.GET_NEXT()</code>", "<code>NEXT sequence_adi</code>", "<code>INCREMENT sequence_adi</code>"],
        "sequence.NEXTVAL sıradaki yeni numarayı üretip döndürür; sequence.CURRVAL ise en son üretilen geçerli değeri okur."
    ),
    make_q(
        "Aşağıdaki PL/SQL kod bloğunda <code>v_not</code> 85 iken ne yazdırılır?\n<code>IF v_not >= 90 THEN\n    DBMS_OUTPUT.PUT_LINE('AA');\nELSIF v_not >= 80 THEN\n    DBMS_OUTPUT.PUT_LINE('BA');\nELSE\n    DBMS_OUTPUT.PUT_LINE('FF');\nEND IF;</code>",
        "'BA'",
        ["'AA'", "'FF'", "'AA' ve 'BA'", "Hiçbir şey"],
        "85 >= 90 yanlıştır. ELSIF 85 >= 80 doğru olduğu için 'BA' yazdırılır."
    ),
    make_q(
        "PL/SQL'de <code>WHILE</code> döngüsünde koşul baştan FALSE ise döngü gövdesi kaç kez çalışır?",
        "0 kez (Hiç çalışmaz)",
        ["1 kez", "Sonsuz kez", "5 kez", "Hata verir"],
        "WHILE koşul kontrolünü döngü başında yapar; şart baştan yanlışsa döngüye hiç girilmez."
    ),
    make_q(
        "PL/SQL'de <code>LOOP ... EXIT WHEN sart; ... END LOOP;</code> basit döngüsünün özelliği nedir?",
        "Koşulsuz başlar ve gövdedeki EXIT WHEN şartı sağlandığı anda döngüden çıkar.",
        ["Yalnızca tek bir kez çalışır ve kapanır.", "Sayaç otomatik olarak 1'er 1'er artar.", "Hiçbir zaman sonlandırılamaz.", "Yalnızca tablolarda çalışır."],
        "Basit LOOP yapısı EXIT veya EXIT WHEN ile sonlandırılana kadar sonsuz döner."
    ),
    make_q(
        "PL/SQL'de dinamik SQL çalıştırmak için hangi komut kullanılır?",
        "<code>EXECUTE IMMEDIATE v_sql_string;</code>",
        ["<code>RUN SQL v_sql_string;</code>", "<code>EXEC v_sql_string;</code>", "<code>PARSE v_sql_string;</code>", "<code>EVALUATE v_sql_string;</code>"],
        "Oracle PL/SQL'de dinamik SQL cümleleri EXECUTE IMMEDIATE komutu ile yürütülür."
    ),
    make_q(
        "Oracle'da bir paketi (Package) silmek için hangi komut kullanılır?",
        "<code>DROP PACKAGE paket_adi;</code> (veya sadece gövde için <code>DROP PACKAGE BODY paket_adi;</code>)",
        ["<code>DELETE PACKAGE paket_adi;</code>", "<code>REMOVE PACKAGE paket_adi;</code>", "<code>CLEAR PACKAGE paket_adi;</code>", "<code>ALTER PACKAGE paket_adi DROP;</code>"],
        "DROP PACKAGE paketin hem tanımını hem gövdesini siler; DROP PACKAGE BODY sadece gövdeyi kaldırır."
    ),
    make_q(
        "Oracle PL/SQL'de <code>SQLCODE</code> ve <code>SQLERRM</code> özel fonksiyonları ne döndürür?",
        "SQLCODE oluşan hatanın sayısal kodunu, SQLERRM ise hata mesajı metnini döndürür.",
        ["SQLCODE sunucunun IP kodunu, SQLERRM veritabanı adını döndürür.", "SQLCODE satır sayısını, SQLERRM sütun sayısını döndürür.", "SQLCODE sorgu süresini, SQLERRM bellek kullanımını döndürür.", "Her ikisi de transaction durumunu döndürür."],
        "EXCEPTION WHEN OTHERS bloğunda SQLCODE ile hata numarası, SQLERRM ile hata mesajı metni alınır."
    ),
    make_q(
        "PL/SQL'de <code>RETURNING INTO</code> ifadesi hangi DML işlemlerinde üretilen değerleri anında yakalamak için kullanılır?",
        "<code>INSERT</code>, <code>UPDATE</code> ve <code>DELETE</code> işlemlerinde (Örn: Otomatik üretilen kimliği almak için)",
        ["Yalnızca SELECT sorgularında", "Yalnızca CREATE TABLE komutunda", "Yalnızca DROP komutunda", "Yalnızca GRANT komutunda"],
        "INSERT INTO ... VALUES (...) RETURNING id INTO v_id ifadesi eklenen satırın üretilen değerini tek adımda değişkene alır."
    ),
    make_q(
        "Oracle PL/SQL ile T-SQL arasındaki temel sözdizimi farkları ile ilgili hangisi YANLIŞTIR?",
        "T-SQL'de blok sonu <code>END IF;</code> ile biterken, PL/SQL'de <code>END;</code> ile biter.",
        ["T-SQL'de değişkenler <code>@ad</code> şeklinde başlarken, PL/SQL'de <code>@</code> işareti kullanılmaz.", "T-SQL'de atama <code>SET @x = 1</code> iken, PL/SQL'de <code>x := 1;</code> şeklindedir.", "T-SQL'de çıktı için <code>PRINT</code>, PL/SQL'de <code>DBMS_OUTPUT.PUT_LINE</code> kullanılır.", "T-SQL'de hata yakalama <code>TRY...CATCH</code>, PL/SQL'de <code>EXCEPTION...WHEN</code> bloklarıyladır."],
        "Yanlış olan seçenek A'dır: Tam tersine PL/SQL'de 'END IF;' kullanılır, T-SQL'de ise IF için END IF yoktur (BEGIN...END kullanılır)."
    )
]

# =========================================================================
# EXAM 10: Kapsamlı Final Simülasyonu, Kod Çıktı Analizleri & Çıkmış Sorular
# (Kaynaklar: Çıkmış Sorular, 2016 vtys final cevaplar, calismaSVTYS)
# =========================================================================
random.seed(110)
e10 = [
    make_q(
        "Bir personel tablosundan yalnızca <code>departman='Yazilim'</code> koşulunu sağlayan kayıtların seçilmesi istenmektedir. İlişkisel cebirde temel olarak hangi işlem kullanılır?",
        "Selection (Seçim - σ)",
        ["Projection (İzdüşüm - π)", "Cartesian Product (Kartezyen Çarpım - ×)", "Union (Birleşim - ∪)", "Difference (Fark - −)"],
        "Hocanın 1. örnek sorusu: Koşula göre satır filtreleme işlemi Selection (σ)'dır."
    ),
    make_q(
        "<code>SELECT ad, fiyat FROM urun WHERE kategori='Elektronik';</code> sorgusunun ilişkisel cebir karşılığı hangisidir?",
        "<code>π_ad,fiyat(σ_kategori='Elektronik'(urun))</code>",
        ["<code>σ_ad,fiyat(π_kategori='Elektronik'(urun))</code>", "<code>π_kategori(σ_ad='Elektronik'(urun))</code>", "<code>σ_kategori='Elektronik'(π_kategori(urun))</code>", "<code>π_ad,fiyat(urun)</code>"],
        "Hocanın 2. örnek sorusu: Önce içteki σ ile filtreleme yapılır, sonra dıştaki π ile ad ve fiyat sütunları seçilir."
    ),
    make_q(
        "Bir cursor tanımlanmış ve açılmıştır. Cursor içerisindeki kayıtları sırayla değişkenlere okumak için hangi komut kullanılır?",
        "<code>FETCH</code>",
        ["<code>EXEC</code>", "<code>COMMIT</code>", "<code>DROP</code>", "<code>RETURN</code>"],
        "Hocanın 3. örnek sorusu: FETCH imlecin gösterdiği satırdaki verileri okur."
    ),
    make_q(
        "Bir T-SQL cursor ile işlemler tamamlanmış ve cursor kapatılmıştır (CLOSE). Cursor için ayrılan kaynakları tamamen serbest bırakmak için hangi komut kullanılmalıdır?",
        "<code>DEALLOCATE</code>",
        ["<code>DELETE</code>", "<code>REMOVE</code>", "<code>ROLLBACK</code>", "<code>TERMINATE</code>"],
        "Hocanın 4. örnek sorusu: CLOSE sonucu kapatır; DEALLOCATE tanımı ve ayrılan tüm belleği serbest bırakır."
    ),
    make_q(
        "Bir musteri kaydı silindiğinde, silinen müşteriye ait bilgilerin otomatik olarak musteri_log tablosuna yazılması istenmektedir. En uygun veritabanı nesnesi hangisidir?",
        "Trigger (Tetikleyici)",
        ["View (Görünüm)", "Cursor (İmleç)", "Index (İndeks)", "Scalar Function"],
        "Hocanın 5. örnek sorusu: DELETE olayı anında otomatik çalışan ve silinen veriyi DELETED'den alan nesne Trigger'dır."
    ),
    make_q(
        "Bir tabloda birincil anahtar <code>(ogrenci_id, ders_id)</code> şeklindedir. <code>ogrenci_adi</code> alanı yalnızca <code>ogrenci_id</code> değerine bağlıdır. Bu durum hangi normalizasyon problemini gösterir?",
        "Kısmi Bağımlılık (Partial Dependency) -> 2NF İhlali",
        ["Geçişli Bağımlılık -> 3NF İhlali", "Çok Değerli Bağımlılık -> 4NF İhlali", "Join Bağımlılığı -> 5NF İhlali", "Özyinelemeli Bağımlılık"],
        "Hocanın 6. örnek sorusu: Bileşik anahtarın parçasına bağımlılık kısmi bağımlılıktır ve 2NF'yi ihlal eder."
    ),
    make_q(
        "<code>Personel(personel_id, departman_id, departman_adi)</code> ilişkisinde <code>personel_id -> departman_id</code> ve <code>departman_id -> departman_adi</code> olduğuna göre <code>departman_adi</code> alanının <code>personel_id</code> üzerinden bağımlılığı hangi türdedir?",
        "Geçişli Bağımlılık (Transitive Dependency) -> 3NF İhlali",
        ["Kısmi Bağımlılık", "Çok Değerli Bağımlılık", "Join Bağımlılığı", "Tekrarlı Bağımlılık"],
        "Hocanın 7. örnek sorusu: A -> B ve B -> C zincirinde anahtar olmayan bir alanın diğerine bağımlılığı geçişli bağımlılıktır."
    ),
    make_q(
        "Bir ilişkinin BCNF (Boyce-Codd Normal Form) koşulunu sağlaması için aşağıdaki ifadelerden hangisi DOĞRUDUR?",
        "İlişkideki her belirleyici (determinant) mutlaka bir aday/süper anahtar olmalıdır.",
        ["Her sütun mutlaka bir yabancı anahtar olmalıdır.", "Tabloda yalnızca iki sütun bulunmalıdır.", "Tabloda hiçbir yabancı anahtar bulunmamalıdır.", "Her tablo yalnızca tek bir kayıt içermelidir."],
        "Hocanın 8. örnek sorusu: BCNF'de tüm işlevsel bağımlılıkların belirleyici tarafı süper/aday anahtar olmak zorundadır."
    ),
    make_q(
        "Bir fonksiyonun kendisine verilen iki sayıyı kullanarak tek bir sayısal sonuç döndürmesi istenmektedir. Hangisi en uygundur?",
        "Skaler Kullanıcı Tanımlı Fonksiyon (Scalar User Defined Function)",
        ["Tablo Değerli Fonksiyon (Table-valued Function)", "DML Tetikleyicisi (Trigger)", "İmleç (Cursor)", "Görünüm (View)"],
        "Hocanın 9. örnek sorusu: Tek bir değer hesaplayıp dönen yapı Skaler UDF'tir."
    ),
    make_q(
        "<code>SELECT m.ad, d.departman_adi FROM personel m JOIN departman d ON m.departman_id = d.departman_id;</code> sorgusunda hangi temel işlemler birlikte kullanılmaktadır?",
        "Birleştirme (Join) ve İzdüşüm (Projection)",
        ["Seçim (Selection) ve Fark (Difference)", "Birleşim (Union) ve Kesişim (Intersection)", "Bölme (Division) ve Seçim (Selection)", "Yalnızca İzdüşüm (Projection)"],
        "Hocanın 10. örnek sorusu: JOIN iki tabloyu birleştirir, SELECT ad, departman_adi sütunları seçer (Projection)."
    ),
    make_q(
        "<code>urun</code> tablosunda bulunan ancak <code>satis_kalemi</code> tablosunda hiç bulunmayan ürünlerin urun_id değerleri istenmektedir. En uygun ilişkisel cebir yaklaşımı hangisidir?",
        "<code>π_urun_id(urun) − π_urun_id(satis_kalemi)</code>",
        ["<code>π_urun_id(urun) ∪ π_urun_id(satis_kalemi)</code>", "<code>π_urun_id(urun) ∩ π_urun_id(satis_kalemi)</code>", "<code>urun × satis_kalemi</code>", "<code>urun ⋈ satis_kalemi</code>"],
        "Hocanın 11. örnek sorusu: İlk kümede olup ikincide olmayanları bulmak için küme farkı (−) kullanılır."
    ),
    make_q(
        "Bir kayıt <code>UPDATE</code> ile değiştirildiğinde SQL Server trigger yapısında eski ve yeni kayıt değerleri nasıl tutulur?",
        "Eski değer <code>DELETED</code> tablosunda, yeni değer <code>INSERTED</code> tablosundadır.",
        ["Eski değer INSERTED, yeni değer DELETED tablosundadır.", "Her iki değer de yalnızca INSERTED tablosundadır.", "Her iki değer de yalnızca DELETED tablosundadır.", "UPDATE işleminde bu tablolar kullanılmaz."],
        "Hocanın 12. örnek sorusu: UPDATE işleminde DELETED eski hali, INSERTED yeni güncel hali tutar."
    ),
    make_q(
        "<code>CREATE PROCEDURE SiparisListele @minTutar MONEY = 1000 AS BEGIN ... END</code> tanımında <code>@minTutar</code> çağrı sırasında gönderilmezse ne olur?",
        "Parametrenin değeri varsayılan olarak 1000 kabul edilir ve prosedür sorunsuz çalışır.",
        ["Procedure kesinlikle derleme hatası verir.", "Parametre otomatik olarak NULL olur.", "Procedure veritabanından silinir.", "Parametre tamamen yok sayılır ve filtre uygulanmaz."],
        "Hocanın 13. örnek sorusu: Parametre varsayılanı (1000) atanmıştır, parametresiz çağrıda 1000 kullanılır."
    ),
    make_q(
        "PL/SQL'de bir prosedürün dışarıdan değer alıp işlem sonucunda aynı parametre üzerinden dışarıya da değer göndermesi istenmektedir. Hangi parametre modu uygundur?",
        "<code>IN OUT</code>",
        ["<code>IN</code>", "<code>OUT</code>", "<code>RETURN</code>", "<code>DEFAULT</code>"],
        "Hocanın 14. örnek sorusu: Hem giriş hem çıkış amacıyla kullanılan iki yönlü parametre modu IN OUT'tur."
    ),
    make_q(
        "Bir PL/SQL geliştiricisi aynı uygulamaya ait çok sayıda prosedür, fonksiyon ve ortak tanımı mantıksal olarak tek çatı altında toplamak istemektedir. En uygun yapı hangisidir?",
        "Paket (Package)",
        ["Tetikleyici (Trigger)", "İmleç (Cursor)", "Görünüm (View)", "Sıra Numaratörü (Sequence)"],
        "Hocanın 15. örnek sorusu: İlişkili programatik nesneleri tek çatı altında gruplayan yapı PACKAGE'dir."
    ),
    make_q(
        "Çıkmış Final Sorusu: Aşağıdakilerden hangisi hepsinin bulunduğu bir SQL sorgusunda en alttan (fiziksel yazım sırasına göre) ikinci olarak bulunur?",
        "<code>HAVING</code> (Sıra: SELECT -> FROM -> WHERE -> GROUP BY -> HAVING -> ORDER BY)",
        ["<code>ORDER BY</code> (En altta birinci)", "<code>GROUP BY</code>", "<code>WHERE</code>", "<code>SELECT</code>"],
        "Düzce Üni Final Test Sorusu: Yazım sırasında en altta ORDER BY (1.), onun hemen üstünde HAVING (alttan 2.) yer alır."
    ),
    make_q(
        "Çıkmış Final Sorusu: Aşağıdaki komutlardan hangisi ile <code>WHERE</code> koşulu KULLANILMAZ?",
        "<code>INSERT</code> (Standart tekli eklemede: INSERT INTO Tablo VALUES(...))",
        ["<code>SELECT</code>", "<code>UPDATE</code>", "<code>DELETE</code>", "<code>None</code>"],
        "Düzce Üni Final Test Sorusu: INSERT ... VALUES ifadesinde satır seçme amaçlı WHERE yan tümcesi kullanılmaz."
    ),
    make_q(
        "Çıkmış Final Sorusu: Bir primary key tanımlandığında otomatik olarak oluşan indeks çeşidi hangisidir?",
        "Clustered Index (Kümelenmiş İndeks)",
        ["Non-Clustered Index", "Unique Index (Clustered olmadan)", "Multiple Index", "XML Index"],
        "Düzce Üni Final Test Sorusu: Primary key kısıtı tanımlandığında SQL Server varsayılan olarak Clustered Index üretir."
    ),
    make_q(
        "Çıkmış Final Sorusu: Yapılmış bir veritabanı uygulamasının uluslararası dil desteğinin (Türkçe, Çince, Arapça vb.) olabilmesi için hangi metinsel veri türü kategorisi kullanılmalıdır?",
        "Unicode (NVARCHAR, NCHAR)",
        ["Non-Unicode (VARCHAR, CHAR)", "ASCII", "Binary", "Latin1"],
        "Düzce Üni Final Test Sorusu: Uluslararası çok dilli karakter desteği Unicode veri tipleri (N-tipleri) ile sağlanır."
    ),
    make_q(
        "Çıkmış Final Sorusu: Alt alta yazılıp çalıştırılan iki sorgudan 'birincide olup ikincide olmayan' kayıtları listelemek için hangi komut kullanılır?",
        "<code>EXCEPT</code> (veya <code>MINUS</code>)",
        ["<code>UNION</code>", "<code>UNION ALL</code>", "<code>INTERSECT</code>", "<code>DISTINCT</code>"],
        "Düzce Üni Final Test Sorusu: Birinci sorguda olup ikincide olmayanları listelemek küme farkı (EXCEPT)'tir."
    ),
    make_q(
        "Çıkmış Final Sorusu: Alt alta yazılıp çalıştırılan iki sorgunun sonuçlarını 'tekrar edilen kayıtları da listeleyecek şekilde birleştirerek' çalıştıran komut hangisidir?",
        "<code>UNION ALL</code>",
        ["<code>UNION</code>", "<code>EXCEPT</code>", "<code>INTERSECT</code>", "<code>DISTINCT</code>"],
        "Düzce Üni Final Test Sorusu: Tekrarları koruyarak birleştiren komut UNION ALL'dur."
    ),
    make_q(
        "Çıkmış Final Sorusu: Bir trigger içerisinde yapılan kontrollerde problem bir durum tespit edildiğinde, kayıtlar üzerindeki değişikliklerin geri alınması için hangi komut kullanılır?",
        "<code>ROLLBACK</code> (veya <code>ROLLBACK TRANSACTION</code>)",
        ["<code>COMMIT</code>", "<code>UNDO</code>", "<code>BACKUP</code>", "<code>DETACH</code>"],
        "Düzce Üni Final Test Sorusu: Trigger içinde hatalı durumu geri almak için ROLLBACK kullanılır."
    ),
    make_q(
        "Çıkmış Final Sorusu: Bir A trigger'ı içerisinden B trigger'ının çağrılmasına/tetiklenmesine ne isim verilir?",
        "İç İçe Tetikleyici (Nested Trigger)",
        ["Özyinelemeli Tetikleyici (Recursive Trigger)", "Alt Tetikleyici (Sub-trigger)", "INSTEAD OF Trigger", "Multiple Trigger"],
        "Düzce Üni Final Test Sorusu: Bir trigger'ın başka bir tablodaki trigger'ı tetiklemesine Nested Trigger denir."
    ),
    make_q(
        "Çıkmış Final Sorusu: 'ulke' alanında bulunan 'Türkiye' verisinden 'kiye' parçasını almak için hangi fonksiyon doğru parametrelerle kullanılır?",
        "<code>SUBSTRING(ulke, 4, 4)</code> (4. karakter 'k'den itibaren 4 karakter)",
        ["<code>CHARINDEX(ulke, 4, 4)</code>", "<code>SUBSTRING(ulke, 3, 4)</code>", "<code>LEFT(ulke, 4)</code>", "<code>RIGHT(ulke, 3)</code>"],
        "Düzce Üni Final Test Sorusu: 'T-ü-r-k-i-y-e' kelimesinde 4. harf 'k'dir. SUBSTRING(ulke, 4, 4) 'kiye' sonucunu üretir."
    ),
    make_q(
        "Çıkmış Final Sorusu: Ad ('Ali') ve Soyad ('Ak') alanlarından 'Ali-AK' formatında çıktı üretmek için hangi SQL fonksiyon ifadesi kullanılır?",
        "<code>Ad + '-' + UPPER(Soyad)</code>",
        ["<code>LOWER(Ad) + '-' + LOWER(Soyad)</code>", "<code>Ad + Soyad</code>", "<code>SUBSTRING(Ad, 1, 3) + Soyad</code>", "<code>UPPER(Ad + Soyad)</code>"],
        "Düzce Üni Final Sorusu: Ad aynen bırakılır, araya tire konur ve Soyad UPPER ile büyük harfe çevrilir."
    ),
    make_q(
        "Çıkmış Final Sorusu: <code>CREATE TABLE notbilgi</code> tablosunda ortalama hesaplama formülü için T-SQL'de <code>(@vizenotu * 0.3) + (@finalnotu * 0.7)</code> yazıldığında, vize=80, final=60 alan bir öğrencinin ortalaması kaç hesaplanır?",
        "66.0 (80 × 0.3 = 24, 60 × 0.7 = 42 -> 24 + 42 = 66)",
        ["70.0", "60.0", "68.0", "72.0"],
        "Vize %30 (24) + Final %70 (42) = 66.0 ortalama elde edilir."
    ),
    make_q(
        "Aşağıdaki T-SQL kodunun çıktısı nedir?\n<code>DECLARE @x INT = 1;\nWHILE @x <= 10\nBEGIN\n    SET @x = @x * 2;\nEND;\nSELECT @x;</code>",
        "16",
        ["8", "10", "12", "32"],
        "@x döngü adımları: 1 -> 2 -> 4 -> 8 -> 16 (16 > 10 olduğundan döngü biter). Sonuç: 16."
    ),
    make_q(
        "Aşağıdaki T-SQL kodunun çıktısı nedir?\n<code>DECLARE @a INT = 5, @b INT = 2;\nSELECT @a / @b;</code>",
        "2 (Tamsayı bölmesi ondalığı atar)",
        ["2.5", "3", "0", "Hata"],
        "Her iki işlenen de INT olduğundan tamsayı bölmesi yapılır ve sonuç 2 olur (2.5 için en az biri ondalıklı olmalıdır)."
    ),
    make_q(
        "Aşağıdaki T-SQL ifadesinin çıktısı nedir?\n<code>SELECT CASE WHEN 10 > 20 THEN 'A' WHEN 5 = 5 THEN 'B' ELSE 'C' END;</code>",
        "'B'",
        ["'A'", "'C'", "'A' ve 'B'", "NULL"],
        "İlk şart (10 > 20) yanlış, ikinci şart (5 = 5) doğru olduğu için 'B' değeri döner."
    ),
    make_q(
        "Aşağıdaki sorguda <code>HAVING COUNT(*) >= 2</code> ne yapar?\n<code>SELECT bolumkod, AVG(vizenot) FROM notbilgi GROUP BY bolumkod HAVING COUNT(*) >= 2</code>",
        "En az 2 adet not kaydı bulunan bölümlerin not ortalamalarını listeler.",
        ["Ortalaması 2'den büyük olan bölümleri listeler.", "Bölüm kodu 2 olan kayıtları listeler.", "Tüm bölümlerden ilk 2 satırı getirir.", "Tüm notları 2 ile çarpar."],
        "GROUP BY sonrası HAVING COUNT(*) >= 2 ile gruptaki kayıt adedi en az 2 olan bölümler filtrelenir."
    ),
    make_q(
        "Bir tabloda <code>ogrno VARCHAR(5) PRIMARY KEY</code> ve <code>tckimlik VARCHAR(11) UNIQUE</code> tanımlıdır. Bu tabloda kaç adet aday anahtar vardır?",
        "En az 2 adet aday anahtar vardır (ogrno ve tckimlik)",
        ["Yalnızca 1 adet aday anahtar vardır.", "Hiç aday anahtar yoktur.", "16 adet aday anahtar vardır.", "Sadece tckimlik aday anahtardır."],
        "Her ikisi de her satırı benzersiz tanımlayabildiği için her ikisi de aday anahtardır; biri (ogrno) PK seçilmiştir."
    ),
    make_q(
        "Aşağıdaki SQL ifadesi ne amaçla yazılmıştır?\n<code>SELECT ad, soyad FROM ogrenci WHERE bolumkod = (SELECT bolumkod FROM bolum WHERE bolumad = 'Bilgisayar') AND ogrno IN (SELECT ogrno FROM notbilgi WHERE ortalama = (SELECT MAX(ortalama) FROM notbilgi));</code>",
        "Bilgisayar bölümünde okuyan ve tüm okulda en yüksek not ortalamasına sahip öğrencinin (öğrencilerin) ad ve soyadını bulmak",
        ["Tüm bilgisayar öğrencilerinin ortalamasını hesaplamak", "Notu en düşük olan bilgisayar öğrencisini silmek", "Bilgisayar bölümünün tüm derslerini listelemek", "En yüksek notu alan öğrencinin bölümünü bilgisayar yapmak"],
        "Alt sorgularla önce 'Bilgisayar' bölüm kodu, ardından en yüksek ortalamaya (MAX) sahip öğrenci numarası bulunup filtrelenir."
    ),
    make_q(
        "<code>CREATE VIEW vw_50_ustu AS SELECT ogrno, vizenot, finalnot, ortalama FROM notbilgi WHERE ortalama >= 50</code> görünümü neyi temsil eder?",
        "notbilgi tablosunda ortalaması 50 ve üzerinde olan başarılı öğrencilerin not bilgilerini gösteren sanal bir görünüm",
        ["Ortalaması 50'den küçük olan öğrencileri tablodan silen prosedür", "notbilgi tablosunun 50 satırlık yedeği", "Tüm öğrencilere 50 puan ekleyen bir trigger", "Ortalaması 50 olan tek bir öğrencinin kaydı"],
        "Bu görünüm (VIEW) ortalaması 50 ve üzeri olan kayıtları dinamik olarak filtreleyen sanal tablodur."
    ),
    make_q(
        "Aşağıdaki T-SQL kodunun çıktısı nedir?\n<code>DECLARE @str VARCHAR(20) = 'Veritabanı';\nSELECT LEN(@str);</code>",
        "10 (Metnin karakter sayısı)",
        ["11", "9", "20", "8"],
        "'Veritabanı' kelimesi 10 harften oluşur; LEN() fonksiyonu karakter uzunluğu olarak 10 döndürür."
    ),
    make_q(
        "Bir transaction içinde sırasıyla şu işlemler yapılıyor:\n<code>BEGIN TRAN;\nINSERT INTO Bolum VALUES('BLG', 'Bilgisayar');\nSAVE TRAN SP1;\nINSERT INTO Bolum VALUES('END', 'Endustri');\nROLLBACK TRAN SP1;\nCOMMIT TRAN;</code>\nSonuçta Bolum tablosuna hangi kayıt eklenmiş olur?",
        "Yalnızca 'BLG' (Bilgisayar) kaydı eklenmiş olur; 'END' kaydı geri alınmıştır.",
        ["Hem 'BLG' hem 'END' kayıtları eklenir.", "Hiçbir kayıt eklenmez, tüm transaction iptal olur.", "Yalnızca 'END' kaydı eklenir.", "Sözdizimi hatası oluşur."],
        "ROLLBACK TRAN SP1 komutu SP1 noktasından sonraki 'END' eklemesini geri alır; öncesindeki 'BLG' kaydı COMMIT ile kalıcı olur."
    ),
    make_q(
        "Aşağıdaki ilişkisel cebir işlemlerinden hangisi iki ilişkinin Kartezyen çarpımının bir kısıtlaması (filtresi) olarak ifade edilebilir?",
        "Birleştirme (Join - ⋈)",
        ["Projeksiyon (Projection - π)", "Yeniden adlandırma (Rename - ρ)", "Bölme (Division - /)", "Tekilleştirme"],
        "Join işlemi kavramsal olarak Kartezyen çarpım (R × S) üzerine birleştirme koşulunun (σ_koşul) uygulanmasıdır."
    ),
    make_q(
        "Bir veritabanı yönetim sisteminde (DBMS) 'Fiziksel Veri Bağımsızlığı' (Physical Data Independence) ne anlama gelir?",
        "Verilerin disk üzerindeki fiziksel saklanma biçimi veya indeksleme yapısı değiştiğinde mantıksal şemanın ve uygulamaların bundan etkilenmemesi",
        ["Veritabanı sunucusunun elektrik kesintilerinden etkilenmemesi", "Kullanıcıların SQL bilmeden veritabanına erişebilmesi", "Tüm verilerin fiziksel olarak tek bir dosyada tutulması", "Donanımın her yıl yenilenmesi zorunluluğu"],
        "Fiziksel veri bağımsızlığı: İç/fiziksel düzeydeki değişikliklerin kavramsal/mantıksal şemayı etkilememesidir."
    ),
    make_q(
        "Bir veritabanı yönetim sisteminde (DBMS) 'Mantıksal Veri Bağımsızlığı' (Logical Data Independence) ne anlama gelir?",
        "Kavramsal/mantıksal şemada yapılan değişikliklerin (örn: yeni sütun/tablo ekleme) dış şemayı (görünümleri ve kullanıcı uygulamalarını) etkilememesi",
        ["Mantıksal operatörlerin (AND/OR) hızlandırılması", "Verilerin mantık kurallarına göre sıralanması", "Kullanıcıların şifrelerinin mantıksal şifrelenmesi", "Tablo isimlerinin mantıklı seçilmesi"],
        "Mantıksal veri bağımsızlığı: Kavramsal düzeydeki değişikliklerden kullanıcı görünümlerinin yalıtılmasıdır."
    ),
    make_q(
        "Aşağıdaki SQL fonksiyonlarından hangisi bir metindeki boşlukları (sağdan ve soldan) temizlemek için kullanılır?",
        "<code>LTRIM(RTRIM(metin))</code> (veya modern SQL'de <code>TRIM(metin)</code>)",
        ["<code>CLEAN(metin)</code>", "<code>STRIP(metin)</code>", "<code>REMOVE_SPACES(metin)</code>", "<code>SUBSTRING(metin, 0)</code>"],
        "LTRIM soldaki, RTRIM sağdaki boşlukları siler; ikisi iç içe veya TRIM() kullanılarak her iki uç temizlenir."
    ),
    make_q(
        "Tüm ders notları ve sınav hazırlık sürecinin özeti olarak: Bir SQL geliştiricisinin en çok dikkat etmesi gereken temel kural nedir?",
        "Küme tabanlı (Set-based) düşünmek, gereksiz cursor kullanımından kaçınmak, doğru indeks ve kısıtlarla veri bütünlüğünü garanti etmek",
        ["Tüm sorguları tek satırda yazmak", "Hiçbir zaman JOIN kullanmamak", "Her sütunu VARCHAR(MAX) tanımlamak", "Primary Key kısıtlamalarını kullanmamak"],
        "RDBMS mimarisinin temeli küme tabanlı operasyonlar, varlık/referans bütünlüğü ve doğru normalizasyon tasarımıdır."
    )
]

print(f"Exam 9: {len(e9)}, Exam 10: {len(e10)}")
