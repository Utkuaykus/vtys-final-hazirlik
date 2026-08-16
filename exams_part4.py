# -*- coding: utf-8 -*-
"""
exams_part4.py: Exam 7 and Exam 8
"""
import random
random.seed(107)

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
# EXAM 7: Cursor (İmleçler) & Satır Satır Veri İşleme
# (Kaynaklar: Cursor, T-SQL_1, veritabanıfinal)
# =========================================================================
e7 = [
    make_q(
        "SQL'de İmleç (Cursor) kavramı ne amaçla kullanılır?",
        "Bir sorgunun döndürdüğü sonuç kümesindeki satırları tek tek dolaşarak satır bazlı işlem yapmak için",
        ["Tablodaki tüm verileri tek bir adımda topluca güncellemek için", "Veritabanının tam yedeğini harici diske almak için", "Tablolara otomatik olarak yeni indeksler tanımlamak için", "Yalnızca veritabanı kullanıcı şifrelerini değiştirmek için"],
        "SQL küme tabanlıdır; her satıra özel adım adım işlem yapılması gerektiğinde Cursor ile satır satır dolaşılır."
    ),
    make_q(
        "Bir T-SQL Cursor'ın yaşam döngüsündeki 5 temel adımın DOĞRU sırası aşağıdakilerden hangisidir?",
        "DECLARE -> OPEN -> FETCH -> CLOSE -> DEALLOCATE",
        ["OPEN -> DECLARE -> FETCH -> CLOSE -> DEALLOCATE", "DECLARE -> FETCH -> OPEN -> DEALLOCATE -> CLOSE", "DECLARE -> OPEN -> CLOSE -> FETCH -> DEALLOCATE", "OPEN -> FETCH -> DECLARE -> CLOSE -> DEALLOCATE"],
        "Cursor adımları: 1. DECLARE (tanımla), 2. OPEN (aç), 3. FETCH (oku), 4. CLOSE (kapat), 5. DEALLOCATE (belleği serbest bırak)."
    ),
    make_q(
        "Cursor yaşam döngüsünde <code>OPEN</code> komutunun işlevi nedir?",
        "Cursor tanımındaki SELECT sorgusunu çalıştırır, sonuç kümesini (result set) hazırlar ve imleci ilk satırın öncesine konumlandırır.",
        ["Cursor tanımını veritabanı diskinden tamamen siler.", "Cursor'daki tüm satırları ekrana yazdırır.", "Tablodaki verileri salt okunur kilitler.", "Cursor'ı son satıra taşır."],
        "OPEN sorguyu yürütür ve satırları okumaya hazır hale getirir."
    ),
    make_q(
        "Cursor yaşam döngüsünde <code>FETCH</code> komutunun işlevi nedir?",
        "İmlecin işaret ettiği geçerli satırdaki sütun değerlerini değişkenlere aktarır ve imleci bir sonraki satıra ilerletir.",
        ["Cursor'ın bağlı olduğu tabloyu siler.", "Sadece tablodaki satır sayısını sayar.", "Cursor'ı kapatıp belleği boşaltır.", "Cursor'daki verileri doğrudan diske yazar."],
        "FETCH satırdaki verileri INTO ile belirtilen değişkenlere yükler ve imleci bir adım kaydırır."
    ),
    make_q(
        "T-SQL'de <code>CLOSE</code> komutu ile <code>DEALLOCATE</code> komutu arasındaki temel fark nedir?",
        "CLOSE sonuç kümesini kapatıp kilitleri kaldırır ama tanım kalır (tekrar OPEN edilebilir); DEALLOCATE ise tanımı ve tüm kaynakları tamamen siler.",
        ["CLOSE cursor'ı silerken, DEALLOCATE cursor'ı açar.", "CLOSE yalnızca Oracle'da, DEALLOCATE SQL Server'da çalışır.", "CLOSE tek bir satırı siler, DEALLOCATE tüm tabloyu siler.", "İkisi tamamen aynıdır ve birbirinin yerine kullanılabilir."],
        "CLOSE aktif result set'i boşaltır (tanım kalır); DEALLOCATE cursor nesnesini tamamen yok eder."
    ),
    make_q(
        "T-SQL'de <code>@@FETCH_STATUS</code> global değişkeni ne amaçla kontrol edilir?",
        "En son çalıştırılan FETCH işleminin başarılı olup olmadığını veya sonuç kümesinin sonuna gelinip gelinmediğini anlamak için",
        ["Tablodaki toplam kayıt sayısını öğrenmek için", "Cursor'ın kaçıncı satırda olduğunu öğrenmek için", "Veritabanı sunucusunun IP adresini öğrenmek için", "Cursor'ın adını ekrana yazdırmak için"],
        "WHILE @@FETCH_STATUS = 0 döngüsü ile satırların başarıyla okunmaya devam ettiği kontrol edilir."
    ),
    make_q(
        "T-SQL'de <code>@@FETCH_STATUS</code> değişkeni <code>-1</code> değerini ürettiğinde bu ne anlama gelir?",
        "FETCH ifadesi başarısız oldu veya sonuç kümesinin sonuna gelindi (okunacak başka satır kalmadı).",
        ["FETCH işlemi başarıyla tamamlandı ve satır okundu.", "Okunan satır başka bir kullanıcı tarafından silinmiş.", "Cursor henüz OPEN edilmedi.", "Cursor'da sözdizimi hatası var."],
        "@@FETCH_STATUS: 0 = başarılı, -1 = bitti veya başarısız, -2 = satır kayıp/silinmiş."
    ),
    make_q(
        "Bir Cursor döngüsünde (WHILE) en sık yapılan mantıksal hata nedir?",
        "İlk FETCH'in döngüden önce yapılmaması veya döngü içindeki son satırda bir sonraki FETCH'in unutulup sonsuz döngüye girilmesi",
        ["Cursor adının küçük harfle yazılması", "SELECT listesinde yalnızca tek sütun kullanılması", "CLOSE komutundan sonra DEALLOCATE yazılması", "Değişkenlerin @ sembolü ile başlaması"],
        "İlk FETCH WHILE'dan önce yapılmalı, sonraki FETCH WHILE bloğunun sonunda tekrarlanmalıdır; aksi halde sonsuz döngü oluşur."
    ),
    make_q(
        "Aşağıdaki Cursor şablonunda eksik olan adım hangisidir?\n<code>DECLARE cr_test CURSOR FOR SELECT ...\nOPEN cr_test\nFETCH NEXT FROM cr_test INTO @x\nWHILE @@FETCH_STATUS = 0\nBEGIN ... FETCH NEXT FROM cr_test INTO @x END\nCLOSE cr_test</code>",
        "<code>DEALLOCATE cr_test;</code> (Cursor tanımını ve belleği serbest bırakma adımı)",
        ["<code>COMMIT cr_test;</code>", "<code>RESET cr_test;</code>", "<code>DROP cr_test;</code>", "<code>STOP cr_test;</code>"],
        "CLOSE'dan sonra ayrılan kaynakların serbest bırakılması için DEALLOCATE zorunludur."
    ),
    make_q(
        "<code>SCROLL</code> seçeneği ile tanımlanan bir Cursor'da geriye doğru (bir önceki satıra) gitmek için hangi komut kullanılır?",
        "<code>FETCH PRIOR FROM cr_adi INTO @degiskenler</code>",
        ["<code>FETCH BACK FROM cr_adi</code>", "<code>FETCH PREVIOUS FROM cr_adi</code>", "<code>FETCH REVERSE FROM cr_adi</code>", "<code>FETCH LAST FROM cr_adi</code>"],
        "SCROLL cursor hareketleri: NEXT (sonraki), PRIOR (önceki), FIRST (ilk), LAST (son), ABSOLUTE n, RELATIVE n."
    ),
    make_q(
        "SCROLL bir Cursor'da sonuç kümesinin en sonuncu satırını doğrudan okumak için hangi komut kullanılır?",
        "<code>FETCH LAST FROM cr_adi INTO @degiskenler</code>",
        ["<code>FETCH END FROM cr_adi</code>", "<code>FETCH BOTTOM FROM cr_adi</code>", "<code>FETCH FINAL FROM cr_adi</code>", "<code>FETCH MAX FROM cr_adi</code>"],
        "FETCH LAST sonuç kümesinin son satırını okur."
    ),
    make_q(
        "SCROLL bir Cursor'da baştan tam olarak 5. satıra konumlanıp okuma yapmak için hangi komut kullanılır?",
        "<code>FETCH ABSOLUTE 5 FROM cr_adi INTO @degiskenler</code>",
        ["<code>FETCH RELATIVE 5 FROM cr_adi</code>", "<code>FETCH ROW 5 FROM cr_adi</code>", "<code>FETCH STEP 5 FROM cr_adi</code>", "<code>FETCH EXACT 5 FROM cr_adi</code>"],
        "FETCH ABSOLUTE n sonuç kümesinin baştan n. satırına mutlak konumlanır."
    ),
    make_q(
        "SCROLL bir Cursor'da mevcut bulunulan konumdan 2 satır ileriye atlamak için hangi komut kullanılır?",
        "<code>FETCH RELATIVE 2 FROM cr_adi INTO @degiskenler</code>",
        ["<code>FETCH ABSOLUTE 2 FROM cr_adi</code>", "<code>FETCH FORWARD 2 FROM cr_adi</code>", "<code>FETCH JUMP 2 FROM cr_adi</code>", "<code>FETCH SKIP 2 FROM cr_adi</code>"],
        "FETCH RELATIVE n geçerli satıra göre göreceli olarak n satır ileri (veya negatifse geri) gider."
    ),
    make_q(
        "Cursor üzerinde gezinirken o anki geçerli satırı güncellemek için <code>WHERE</code> koşulunda hangi yapı kullanılır?",
        "<code>UPDATE TabloAdi SET ... WHERE CURRENT OF cr_adi</code>",
        ["<code>UPDATE TabloAdi SET ... WHERE ROWID = cr_adi</code>", "<code>UPDATE TabloAdi SET ... WHERE THIS ROW</code>", "<code>UPDATE TabloAdi SET ... WHERE cr_adi.STATUS = 0</code>", "<code>UPDATE TabloAdi SET ... WHERE FETCH = 1</code>"],
        "WHERE CURRENT OF imleç_adı o an imlecin üzerinde durduğu satırı hedef alarak günceller veya siler."
    ),
    make_q(
        "<code>WHERE CURRENT OF cr_adi</code> ile silme işlemi nasıl yazılır?",
        "<code>DELETE FROM TabloAdi WHERE CURRENT OF cr_adi</code>",
        ["<code>DELETE cr_adi FROM TabloAdi</code>", "<code>DROP CURRENT ROW FROM cr_adi</code>", "<code>REMOVE ROW FROM cr_adi</code>", "<code>TRUNCATE CURRENT FROM cr_adi</code>"],
        "DELETE FROM Tablo WHERE CURRENT OF imlec_adi geçerli imleç satırını siler."
    ),
    make_q(
        "<code>READ_ONLY</code> olarak tanımlanan bir Cursor üzerinde <code>WHERE CURRENT OF</code> ile güncelleme yapılmak istenirse ne olur?",
        "Cursor salt okunur tanımlandığı için veritabanı motoru güncelleme işlemine izin vermez ve hata fırlatır.",
        ["Cursor otomatik olarak yazılabilir moda geçer.", "Güncelleme yapılır ama diske yazılmaz.", "Tablo silinir.", "Değişiklikler başka bir geçici tabloya yazılır."],
        "READ_ONLY cursor'lar veri değişikliklerini engeller; performans açısından da daha hafiftir."
    ),
    make_q(
        "Cursor kullanımının küme tabanlı (Set-based) standart SQL sorgularına göre en büyük DEZAVANTAJI nedir?",
        "Satır satır çalıştığı için aşırı bellek ve CPU tüketmesi, veritabanı kilitlerini uzun tutması ve performansı düşürmesi",
        ["Yalnızca tek bir sütun okuyabilmesi", "Sayısal verilerde çalışamaması", "Veritabanı güvenliğini bozması", "SELECT sorgularını desteklememesi"],
        "Cursor'lar RDBMS'in küme optimizasyonunu devre dışı bırakır; satır başı I/O ve kilit maliyeti nedeniyle yavaştır."
    ),
    make_q(
        "Aşağıdaki durumlardan hangisinde Cursor kullanımı KESİNLİKLE ZORUNLU DEĞİLDİR ve tek bir SQL ifadesiyle yapılmalıdır?",
        "Tüm personelin maaşına %10 zam yapılması gerektiğinde (Basit bir <code>UPDATE Staff SET salary = salary * 1.10</code> yeterlidir)",
        ["Her personele özel karmaşık harici bir web servis API çağrısı yapılması gerektiğinde", "Sırayla her satır için farklı bir işletim sistemi komutu çalıştırılması gerektiğinde", "Bir satırdaki verinin sonucuna göre dinamik yapılandırılmış farklı bir SP çağrılması gerektiğinde", "Her kayıt için ayrı ayrı e-posta gönderimi tetiklenmesi gerektiğinde"],
        "Standart matematiksel güncellemeler tek bir UPDATE ile yapılmalıdır; cursor kullanmak büyük bir tasarım hatasıdır."
    ),
    make_q(
        "T-SQL'de <code>FORWARD_ONLY</code> seçeneği ile tanımlanan bir Cursor'da hangi FETCH komutu KULLANILAMAZ?",
        "<code>FETCH PRIOR</code> (Geriye doğru okuma)",
        ["<code>FETCH NEXT</code> (İleriye doğru okuma)", "<code>OPEN</code>", "<code>CLOSE</code>", "<code>DEALLOCATE</code>"],
        "FORWARD_ONLY cursor yalnızca baştan sona (NEXT) tek yönde ilerleyebilir; geriye veya rastgele satırlara gidemez."
    ),
    make_q(
        "Aşağıdaki T-SQL kodunun amacı nedir?\n<code>DECLARE cr CURSOR FOR SELECT staffNo, salary FROM Staff;\nOPEN cr;\nFETCH NEXT FROM cr INTO @sNo, @sal;\nWHILE @@FETCH_STATUS = 0\nBEGIN\n    PRINT @sNo + ' - ' + CAST(@sal AS VARCHAR(10));\n    FETCH NEXT FROM cr INTO @sNo, @sal;\nEND;\nCLOSE cr;\nDEALLOCATE cr;</code>",
        "Staff tablosundaki tüm personellerin numarasını ve maaşını satır satır okuyup ekrana yazdırmak",
        ["Staff tablosundaki tüm personelleri silmek", "Personel maaşlarını iki katına çıkarmak", "En yüksek maaşlı tek personeli bulmak", "Staff tablosuna yeni personel eklemek"],
        "Bu standart cursor kod şablonudur; tüm satırları sırayla gezip değişkenlere alarak PRINT eder."
    ),
    make_q(
        "Bir Cursor kapatıldıktan sonra (<code>CLOSE cr</code>) aynı oturumda tekrar <code>OPEN cr</code> denilirse ne olur?",
        "Cursor başarıyla yeniden açılır, sorgu baştan çalıştırılır ve imleç ilk satırın öncesine döner.",
        ["Cursor tanımı silindiği için hata verir.", "Veritabanı çöker.", "Cursor otomatik olarak DEALLOCATE olur.", "Yalnızca son satırdan devam eder."],
        "CLOSE sadece result set'i kapatır; tanım bellekte kaldığından tekrar OPEN ile baştan açılabilir."
    ),
    make_q(
        "Bir Cursor serbest bırakıldıktan sonra (<code>DEALLOCATE cr</code>) tekrar <code>OPEN cr</code> denilirse ne olur?",
        "Cursor tanımı tamamen kaldırıldığı için 'cr adlı cursor tanımlı değil' hatası verir.",
        ["Cursor otomatik olarak yeniden tanımlanır.", "Cursor boş küme ile açılır.", "Hatasız çalışır.", "Tablo silinir."],
        "DEALLOCATE cursor tanımını sildiği için artık o isimde bir imleç yoktur, OPEN çağrısı hata verir."
    ),
    make_q(
        "T-SQL'de <code>STATIC</code> (Duyarsız / Insensitive) Cursor ne anlama gelir?",
        "Sorgu sonucunun geçici bir kopyasını tempdb'ye alır; veritabanında sonradan yapılan değişiklikler bu cursor'a yansımaz.",
        ["Cursor'ın asla kapatılamayacağını belirtir.", "Yalnızca sayısal sütunlarda çalışan cursor'dır.", "Veritabanındaki her değişikliği anında yansıtan cursor'dır.", "Cursor'ın tüm veritabanı kullanıcılarına açık olduğunu belirtir."],
        "STATIC cursor verinin anlık fotoğrafını (snapshot) tempdb'ye çeker; temel tablodaki sonradan yapılan güncellemeleri görmez."
    ),
    make_q(
        "T-SQL'de <code>DYNAMIC</code> Cursor ne anlama gelir?",
        "Cursor açıkken tablodaki verilerde yapılan tüm ekleme, güncelleme ve silme değişikliklerini anında dinamik olarak görür.",
        ["Cursor'ın değişken tiplerini dinamik olarak değiştirebilmesidir.", "Cursor'ın her saniye kendi kendine kapanmasıdır.", "Yalnızca tek bir satır tutabilmesidir.", "Cursor'ın diske yazılmamasıdır."],
        "DYNAMIC cursor tablodaki tüm güncel durumları ve satır sırası değişikliklerini gezinme anında dinamik olarak yansıtır."
    ),
    make_q(
        "T-SQL'de <code>KEYSET</code> Cursor'ın çalışma prensibi nedir?",
        "Satırların birincil anahtarlarını (keyset) tempdb'de saklar; satır verileri değiştikçe güncel veriyi çeker ancak yeni eklenen satırları görmez.",
        ["Tüm tabloyu tamamen kilitler.", "Yalnızca yabancı anahtarları listeler.", "Hiçbir satırı okuyamaz.", "Yalnızca tek bir sütun üzerinde çalışır."],
        "KEYSET cursor anahtar kümesini dondurur; mevcut satırların güncellemelerini görür ama yeni eklenen (inserted) satırları görmez."
    ),
    make_q(
        "T-SQL'de <code>FAST_FORWARD</code> seçeneği ne sağlar?",
        "<code>FORWARD_ONLY</code> ve <code>READ_ONLY</code> özelliklerini birleştirerek en yüksek performanslı ve optimize edilmiş imleci oluşturur.",
        ["Cursor'ın geriye doğru iki kat hızlı gitmesini sağlar.", "Cursor'ı otomatik olarak diske yazar.", "Tüm satırları aynı anda siler.", "Cursor'ı şifreler."],
        "FAST_FORWARD, ileri yönlü ve salt okunur en hızlı cursor optimizasyon seçeneğidir."
    ),
    make_q(
        "Oracle PL/SQL'de Örtük İmleç (Implicit Cursor) ne zaman devreye girer?",
        "Herhangi bir DML (INSERT, UPDATE, DELETE) veya tek satırlık <code>SELECT INTO</code> ifadesi çalıştırıldığında Oracle tarafından otomatik oluşturulur.",
        ["Yalnızca DECLARE CURSOR yazıldığında", "Kullanıcı EXECUTE CURSOR komutunu çağırdığında", "Yalnızca veritabanı kilitlendiğinde", "Veritabanı yedeklenirken"],
        "Oracle tüm tekil SQL ifadelerini otomatik olarak SQL örtük imleci (implicit cursor) üzerinden yürütür."
    ),
    make_q(
        "Oracle PL/SQL'de açık bir imlecin henüz açık olup olmadığını denetleyen öznitelik hangisidir?",
        "<code>imlec_adi%ISOPEN</code>",
        ["<code>imlec_adi%FOUND</code>", "<code>imlec_adi%NOTFOUND</code>", "<code>imlec_adi%ROWCOUNT</code>", "<code>imlec_adi%STATUS</code>"],
        "%ISOPEN cursor açıksa TRUE, kapalıysa FALSE döner."
    ),
    make_q(
        "Oracle PL/SQL'de imlecin son FETCH işleminde bir satır bulup bulamadığını denetleyen öznitelik hangisidir?",
        "<code>imlec_adi%FOUND</code> (veya tersi için <code>%NOTFOUND</code>)",
        ["<code>imlec_adi%OPEN</code>", "<code>imlec_adi%COUNT</code>", "<code>imlec_adi%NEXT</code>", "<code>imlec_adi%CHECK</code>"],
        "%FOUND son FETCH başarılı ise TRUE; %NOTFOUND ise satır bulunamadığında TRUE döner."
    ),
    make_q(
        "Oracle PL/SQL'de <code>imlec_adi%ROWCOUNT</code> özniteliği neyi verir?",
        "O ana kadar o imleçten başarıyla okunmuş (FETCH edilmiş) toplam satır sayısını",
        ["Tablodaki tüm satırların toplam sayısını", "Cursor'da kalan okunmamış satır sayısını", "Cursor'ın sütun sayısını", "Cursor'ın bellek boyutunu"],
        "%ROWCOUNT imleçten şimdiye kadar çekilmiş olan kümülatif satır adedini verir."
    ),
    make_q(
        "Oracle PL/SQL'de <code>FOR rec IN imlec_adi LOOP ... END LOOP;</code> (Cursor FOR Loop) yapısının sağladığı en büyük kolaylık nedir?",
        "İmleci OPEN etme, FETCH etme, döngü sonunu kontrol etme (%NOTFOUND) ve CLOSE etme adımlarını otomatik olarak yönetmesi",
        ["Cursor'ın hızını 10 katına çıkarması", "Tablodaki kayıtları silmesi", "Kayıtları otomatik güncellemesi", "Değişken tanımlama ihtiyacını tamamen ortadan kaldırması"],
        "Cursor FOR Loop açma, okuma, döngü sonlandırma ve kapatma adımlarını perde arkasında otomatik yürütür."
    ),
    make_q(
        "Bir Cursor içindeki <code>SELECT</code> sorgusunda <code>ORDER BY</code> kullanılması geçerli midir?",
        "Evet, sonuç kümesinin satırlarının hangi sırada dolaşılacağını belirlemek için ORDER BY kullanılabilir.",
        ["Hayır, Cursor tanımlarında ORDER BY kullanımı kesinlikle yasaktır.", "Yalnızca birincil anahtara göre sıralanabilir.", "Yalnızca SCROLL cursor'larda ORDER BY kullanılabilir.", "Sadece Oracle'da izin verilir."],
        "DECLARE cr CURSOR FOR SELECT ... ORDER BY ... tamamen geçerlidir ve satırların okunma sırasını belirler."
    ),
    make_q(
        "T-SQL'de <code>LOCAL</code> ve <code>GLOBAL</code> cursor kapsamları arasındaki fark nedir?",
        "LOCAL cursor yalnızca tanımlandığı batch, SP veya trigger içinde geçerlidir; GLOBAL cursor ise oturumdaki tüm kodlardan erişilebilir.",
        ["LOCAL cursor diskte saklanır, GLOBAL cursor RAM'de saklanır.", "LOCAL cursor metinlerde, GLOBAL cursor sayılarda çalışır.", "LOCAL cursor kapatılamaz, GLOBAL kapatılabilir.", "İkisi arasında hiçbir fark yoktur."],
        "LOCAL scope tanımlandığı blok bittiğinde sonlanır; GLOBAL scope oturum (connection) düzeyinde yaşar."
    ),
    make_q(
        "Bir Stored Procedure içinde açılan LOCAL bir Cursor, prosedür sonlandığında <code>CLOSE</code> ve <code>DEALLOCATE</code> edilmemişse ne olur?",
        "Prosedür sonlandığında LOCAL cursor otomatik olarak kapatılır ve serbest bırakılır (ancak iyi kodlama pratiği olarak manuel kapatılmalıdır).",
        ["Sunucu kilitlenir ve tüm bağlantılar kopar.", "Veritabanı salt okunur moda geçer.", "Tablodaki tüm satırlar silinir.", "Transaction sonsuza kadar açık kalır."],
        "LOCAL cursor'lar tanımlandığı kapsam sonlanınca otomatik deallocate olur; ancak kaynak sızıntılarını önlemek için açıkça kapatılmalıdır."
    ),
    make_q(
        "Aşağıdaki T-SQL kodunda sonsuz döngü oluşmasının sebebi nedir?\n<code>OPEN cr;\nFETCH NEXT FROM cr INTO @id;\nWHILE @@FETCH_STATUS = 0\nBEGIN\n    PRINT @id;\nEND;\nCLOSE cr;</code>",
        "WHILE döngüsü içerisinde imleci bir sonraki satıra ilerletecek olan <code>FETCH NEXT</code> komutunun yazılmamış olması",
        ["OPEN komutunun yanlış yazılması", "PRINT komutunun kullanılması", "CLOSE komutunun WHILE dışında olması", "cr adının geçersiz olması"],
        "Döngü içinde yeni FETCH yapılmadığı için @@FETCH_STATUS daima 0 kalır ve aynı @id sonsuza kadar basılır."
    ),
    make_q(
        "T-SQL'de <code>CURSOR_STATUS('global', 'cr_adi')</code> sistem fonksiyonu <code>-1</code> döndürürse bu neyi belirtir?",
        "Cursor'ın tanımlı olduğunu fakat o an kapalı (CLOSE durumunda) olduğunu",
        ["Cursor'ın açık ve aktif olduğunu", "Böyle bir cursor'ın hiç var olmadığını", "Cursor'da hata olduğunu", "Cursor'ın silindiğini"],
        "CURSOR_STATUS: 1 = açık, 0 = boş/açık, -1 = kapalı, -3 = nesne yok."
    ),
    make_q(
        "Parametreli bir Cursor (Parameterized Cursor) ne sağlar?",
        "Cursor açılırken (OPEN anında) dışarıdan parametre alarak sorgunun dinamik koşullarla çalışmasını sağlar.",
        ["Cursor'ın adının çalışma anında değiştirilmesini", "Cursor'ın diske parametre kaydetmesini", "Cursor'ın tek satırla sınırlanmasını", "Tüm tabloların birleştirilmesini"],
        "Parametreli cursor'lar OPEN cr(deger) şeklinde parametre alarak farklı değerler için yeniden açılabilir."
    ),
    make_q(
        "Bir Cursor ile 1 milyon satırlık bir tabloyu satır satır dolaşıp UPDATE yapmak yerine tek bir küme tabanlı <code>UPDATE Tablo SET ...</code> yazılması performansı nasıl etkiler?",
        "İşlem süresini dakikalar veya saatler seviyesinden saniyeler seviyesine indirerek muazzam performans artışı sağlar.",
        ["Performansı olumsuz etkiler ve sorguyu yavaşlatır.", "Veritabanı boyutunu iki katına çıkarır.", "Hiçbir performans farkı yaratmaz.", "Yalnızca disk kullanımını artırır."],
        "RDBMS motorları küme tabanlı (set-based) işlemler için optimize edilmiştir; cursor yerine tek UPDATE yazmak binlerce kat hızlıdır."
    ),
    make_q(
        "<code>FETCH NEXT FROM cr INTO @v1, @v2</code> ifadesinde SELECT listesindeki sütun sayısı ile INTO'daki değişken sayısı uyuşmazsa ne olur?",
        "Veritabanı motoru derleme/çalışma zamanında sütun ve değişken sayısı uyumsuzluğu hatası verir.",
        ["Fazla sütunlar otomatik olarak silinir.", "Eksik değişkenler için yeni değişkenler tanımlanır.", "Sorgu NULL değer basarak devam eder.", "İlk sütun iki değişkene birden atanır."],
        "FETCH INTO ifadesindeki değişken adedi ve tipleri SELECT listesindeki sütunlarla birebir örtüşmelidir."
    ),
    make_q(
        "Cursor kullanımı hangi durumlarda meşru ve kabul edilebilir bir çözümdür?",
        "Küme tabanlı SQL komutlarıyla ifade edilemeyen, her satır için harici bir prosedür, genişletilmiş saklı yordam (xp_) veya API çağırmak gerektiğinde",
        ["Tablodaki iki sütunun birbiriyle toplanması gerektiğinde", "Maaşı 5000'den büyük olanların listelenmesinde", "Tabloya 5 satır yeni veri eklenmesinde", "İki tablonun birbiriyle INNER JOIN yapılmasında"],
        "Cursor ancak küme mantığıyla çözülemeyen satır bazlı dış bağımlılıklarda veya karmaşık iterasyonlarda kullanılmalıdır."
    )
]

# =========================================================================
# EXAM 8: Normalizasyon, Fonksiyonel Bağımlılıklar & ER Modelleme
# (Kaynaklar: DBMS_4, DBMS_14, veritabanıfinal)
# =========================================================================
random.seed(108)
e8 = [
    make_q(
        "Veritabanı tasarımında Normalizasyonun (Ayrıştırma) temel amacı nedir?",
        "Gereksiz veri tekrarını (redundancy) en aza indirmek ve ekleme, güncelleme, silme anomalilerini önlemek",
        ["Veritabanındaki tablo sayısını azaltarak tek bir dev tablo oluşturmak", "Sorguların her zaman büyük harfle yazılmasını zorunlu kılmak", "Tablolardaki tüm Foreign Key bağlantılarını koparmak", "Veritabanını yalnızca tek bir kullanıcının erişimine açmak"],
        "Normalizasyon veri tekrarını önler, depolama verimliliği sağlar ve anomalileri ortadan kaldırır."
    ),
    make_q(
        "Normalizasyon yapılmamış bir tabloda aynı bilginin birden çok satırda tekrarlanması sonucu bir satır değişip diğerleri değişmezse hangi anomali oluşur?",
        "Güncelleme Anomalisi (Update Anomaly / Veri Tutarsızlığı)",
        ["Ekleme Anomalisi (Insertion Anomaly)", "Silme Anomalisi (Deletion Anomaly)", "Bağımlılık Koruması", "Kayıpsız Birleştirme"],
        "Güncelleme anomalisi: Tekrarlı verinin bir kısmı güncellenip bir kısmı unutulursa veritabanında tutarsızlık oluşur."
    ),
    make_q(
        "Bir tabloda henüz hiç ders kaydı olmayan yeni bir bölümün sisteme eklenememesi durumu hangi anomaliye örnektir?",
        "Ekleme Anomalisi (Insertion Anomaly)",
        ["Silme Anomalisi (Deletion Anomaly)", "Güncelleme Anomalisi (Update Anomaly)", "Kayıpsız Ayrıştırma", "Geçişli Bağımlılık"],
        "Ekleme anomalisi: Bir varlığın kaydedilebilmesi için ilgisiz başka bir varlığın mevcudiyetinin zorunlu olması durumudur."
    ),
    make_q(
        "Bir öğrencinin aldığı tek ders silindiğinde, öğrencinin kendisinin de veritabanından tamamen yok olması hangi anomaliye örnektir?",
        "Silme Anomalisi (Deletion Anomaly)",
        ["Ekleme Anomalisi (Insertion Anomaly)", "Güncelleme Anomalisi (Update Anomaly)", "BCNF Kuralı", "1NF Kuralı"],
        "Silme anomalisi: Bir bilginin silinmesi sırasında istenmeyen başka kritik bilgilerin de kaybolmasıdır."
    ),
    make_q(
        "Fonksiyonel Bağımlılık (Functional Dependency) <code>X -> Y</code> ifadesinin anlamı nedir?",
        "X'in belirli bir değeri için Y'nin daima tek bir değeri belirlenebilir (X belirleyici, Y bağımlıdır).",
        ["Y'nin değeri her zaman X'in değerinden büyüktür.", "X ve Y sütunları aynı veri tipine sahiptir.", "X sütunu tablodan silinirse Y sütunu da silinir.", "X ve Y sütunlarının toplamı sabittir."],
        "X -> Y: X değeri bilindiğinde Y'nin değeri kesin ve tekil olarak tayin edilebilir."
    ),
    make_q(
        "Birinci Normal Formun (1NF) temel kuralı aşağıdakilerden hangisidir?",
        "Her satır-sütun kesişiminde (hücrede) yalnızca tek bir atomik (bölünemez) değer bulunmalı ve tekrarlayan gruplar olmamalıdır.",
        ["Tabloda hiçbir yabancı anahtar bulunmamalıdır.", "Tüm sütunlar birincil anahtarın tamamına tam bağımlı olmalıdır.", "Tabloda hiçbir geçişli bağımlılık yer almamalıdır.", "Tüm belirleyiciler süper anahtar olmalıdır."],
        "1NF: Tablo ilişkisel olmalı, hücreler atomik tekil değer içermeli ve tekrarlayan gruplar (repeating groups) bulunmamalıdır."
    ),
    make_q(
        "Bir öğrencinin 'Telefonlar' hücresinde <code>'0532..., 0542...'</code> şeklinde birden fazla numara yazılması hangi normal formu ihlal eder?",
        "1NF (Birinci Normal Form - Atomiklik ihlali)",
        ["2NF", "3NF", "BCNF", "5NF"],
        "Hücrede birden çok değer bulunması atomiklik kuralını bozar ve doğrudan 1NF ihlalidir."
    ),
    make_q(
        "İkinci Normal Formun (2NF) temel kuralı nedir?",
        "Tablo 1NF'de olmalı ve anahtar olmayan hiçbir nitelik, bileşik birincil anahtarın bir parçasına (kısmi olarak) bağımlı olmamalıdır.",
        ["Tabloda en fazla 3 adet sütun bulunmalıdır.", "Tüm alanlar NULL değer kabul etmelidir.", "Tabloda hiçbir yabancı anahtar bulunmamalıdır.", "Her satır farklı bir dilde yazılmalıdır."],
        "2NF: 1NF + Kısmi fonksiyonel bağımlılıkların (partial dependencies) kaldırılmasıdır."
    ),
    make_q(
        "Bileşik birincil anahtarı <code>(OgrenciNo, DersKod)</code> olan bir tabloda <code>OgrenciAdi</code> alanı yalnızca <code>OgrenciNo</code>'ya bağlıysa bu durum hangi bağımlılık türüdür ve hangi formu ihlal eder?",
        "Kısmi Bağımlılık (Partial Dependency) -> 2NF ihlali",
        ["Geçişli Bağımlılık (Transitive Dependency) -> 3NF ihlali", "Çok Değerli Bağımlılık -> 4NF ihlali", "Tam Bağımlılık -> BCNF ihlali", "Join Bağımlılığı -> 5NF ihlali"],
        "Bileşik anahtarın yalnızca bir parçasına olan bağımlılık kısmi bağımlılıktır ve 2NF'yi bozar."
    ),
    make_q(
        "Birincil anahtarı TEK bir sütundan oluşan (bileşik olmayan) 1NF'deki bir tablo için hangisi KESİNLİKLE DOĞRUDUR?",
        "Bileşik anahtar olmadığı için kısmi bağımlılık oluşamaz; tablo otomatik olarak en az 2NF'dedir.",
        ["Tablo otomatik olarak 3NF'dedir.", "Tablo otomatik olarak BCNF'dedir.", "Tabloda normalizasyon uygulanamaz.", "Tablo 1NF'yi de kaybeder."],
        "Kritik kural: Tek sütunlu Primary Key'in 'parçası' olamayacağından kısmi bağımlılık imkansızdır, tablo doğrudan 2NF olur."
    ),
    make_q(
        "Üçüncü Normal Formun (3NF) temel kuralı nedir?",
        "Tablo 2NF'de olmalı ve anahtar olmayan hiçbir nitelik, anahtar olmayan başka bir niteliğe bağımlı olmamalıdır (Geçişli bağımlılık yokluğu).",
        ["Tablodaki tüm veriler şifrelenmiş olmalıdır.", "Tabloda en az 10 adet indeks bulunmalıdır.", "Her hücrede en az iki değer olmalıdır.", "Birincil anahtar metin tipinde olmalıdır."],
        "3NF: 2NF + Geçişli fonksiyonel bağımlılıkların (transitive dependencies: A -> B -> C) kaldırılmasıdır."
    ),
    make_q(
        "<code>Personel(SicilNo PK, Ad, BirimNo, BirimAdi)</code> tablosunda <code>SicilNo -> BirimNo</code> ve <code>BirimNo -> BirimAdi</code> bağımlılıkları varsa <code>BirimAdi</code>'nın durumu nedir?",
        "BirimAdi, SicilNo'ya BirimNo üzerinden geçişli (transitive) bağımlıdır ve 3NF'yi ihlal eder.",
        ["BirimAdi kısmi bağımlıdır ve 2NF'yi ihlal eder.", "BirimAdi çok değerli bağımlıdır ve 4NF'yi ihlal eder.", "BirimAdi BCNF kuralını sağlar.", "Tablo 1NF'yi ihlal eder."],
        "A -> B ve B -> C zincirinde anahtar olmayan BirimAdi, anahtar olmayan BirimNo'ya bağlıdır; bu geçişli bağımlılıktır (3NF ihlali)."
    ),
    make_q(
        "Yukarıdaki <code>Personel(SicilNo PK, Ad, BirimNo, BirimAdi)</code> tablosunu 3NF'ye getirmek için ne yapılmalıdır?",
        "Tablo ikiye ayrılır: <code>Personel(SicilNo PK, Ad, BirimNo FK)</code> ve <code>Birim(BirimNo PK, BirimAdi)</code>",
        ["BirimAdi sütunu silinir ve hiçbir yere kaydedilmez.", "SicilNo ve BirimNo birlikte birincil anahtar yapılır.", "Tabloya yeni bir indeks eklenir.", "Ad ve BirimNo sütunları birleştirilir."],
        "Geçişli bağımlılığı çözmek için belirleyici (BirimNo) ve bağımlı alan (BirimAdi) ayrı bir Birim tablosuna taşınır."
    ),
    make_q(
        "Boyce-Codd Normal Formunun (BCNF) temel kuralı nedir?",
        "İlişkideki her işlevsel bağımlılıkta (X -> Y), belirleyici olan sol taraf (X) mutlaka bir aday/süper anahtar olmalıdır.",
        ["Tabloda en fazla 2 sütun bulunmalıdır.", "Hiçbir sütun NULL değer almamalıdır.", "Tüm yabancı anahtarlar silinmelidir.", "Her satır yalnızca bir kez güncellenebilir."],
        "BCNF: 'Her belirleyici bir aday anahtardır.' 3NF'nin kapsayamadığı bazı özel bileşik anahtar çakışmalarını çözer."
    ),
    make_q(
        "BCNF ile 3NF arasındaki ilişki nasıldır?",
        "Her BCNF tablosu kesinlikle 3NF'dedir; ancak her 3NF tablosu BCNF koşulunu sağlamayabilir (BCNF daha katıdır).",
        ["Her 3NF tablosu kesinlikle BCNF'dedir.", "3NF ve BCNF tamamen aynı kurala sahiptir.", "BCNF 2NF'den daha gevşektir.", "İki form arasında hiçbir hiyerarşik bağ yoktur."],
        "Normal form hiyerarşisi: 1NF ⊃ 2NF ⊃ 3NF ⊃ BCNF ⊃ 4NF ⊃ 5NF."
    ),
    make_q(
        "Dördüncü Normal Form (4NF) hangi bağımlılık türünü ortadan kaldırmayı hedefler?",
        "Çok Değerli Bağımlılıkları (Multivalued Dependencies - MVD: X ->> Y)",
        ["Kısmi Bağımlılıkları", "Geçişli Bağımlılıkları", "Join Bağımlılıklarını", "Birincil Anahtar Bağımlılıklarını"],
        "4NF: BCNF + Bağımsız çok değerli bağımlılıkların (MVD) ayrı tablolara ayrıştırılmasıdır."
    ),
    make_q(
        "Beşinci Normal Form (5NF / Project-Join Normal Form) neyi hedefler?",
        "Join bağımlılıklarını (Join Dependencies) çözerek tablonun kayıpsız olarak 3 veya daha fazla tabloya ayrıştırılmasını",
        ["Hücrelerin atomik yapılmasını", "Tüm indekslerin kaldırılmasını", "Kısmi bağımlılıkların elenmesini", "Tekrarlı grupların bulunmasını"],
        "5NF (PJNF): Tablonun kayıpsız olarak daha küçük parçalara ayrılıp yeniden kayıpsız join edilebilmesidir."
    ),
    make_q(
        "Kayıpsız Ayrıştırma (Lossless Join Decomposition) ne anlama gelir?",
        "Ayrıştırılan tablolar JOIN ile birleştirildiğinde orijinal tablodaki verinin eksiksiz ve sahte (spurious) satır üretmeden tam olarak elde edilmesi",
        ["Ayrıştırma sırasında hiçbir tablonun silinmemesi", "Veritabanı boyutunun hiç değişmemesi", "İndekslerin kaybolmaması", "Yalnızca iki tablonun birleştirilebilmesi"],
        "Kayıpsız birleştirme: R1 ⋈ R2 = R. Bilgi kaybı veya fazladan hayali satır (spurious tuple) oluşmaz."
    ),
    make_q(
        "Varlık-İlişki (ER) modellemesinde 'Zayıf Varlık' (Weak Entity) ne demektir ve diyagramda nasıl gösterilir?",
        "Varlığı başka bir güçlü varlığa bağımlı olan (kendi başına tekil anahtarı olmayan) varlıktır; Çift Çizgili Dikdörtgen ile gösterilir.",
        ["Hiçbir sütunu olmayan varlıktır; Üçgen ile gösterilir.", "Yalnızca tek bir kaydı olan varlıktır; Daire ile gösterilir.", "Tüm sütunları NULL olan varlıktır; Kesikli Dikdörtgen ile gösterilir.", "İndeksi olmayan varlıktır; Baklava ile gösterilir."],
        "Weak Entity (Zayıf Varlık) güçlü varlığa bağımlıdır ve çift çizgili dikdörtgen ile gösterilir."
    ),
    make_q(
        "ER modellemesinde 'Türetilen Nitelik' (Derived Attribute - örn: Yaş = Bugün - DoğumTarihi) nasıl gösterilir?",
        "Kesikli çizgili oval (Dashed ellipse)",
        ["Çift çizgili oval", "Altı çizili oval", "Tek çizgili dikdörtgen", "Baklava sembolü"],
        "Derived Attribute (Türetilmiş Nitelik) başka niteliklerden hesaplandığı için kesikli çizgili oval ile çizilir."
    ),
    make_q(
        "ER modellemesinde 'Çok Değerli Nitelik' (Multivalued Attribute - örn: Bir kişinin birden çok telefon numarası olması) nasıl gösterilir?",
        "Çift çizgili oval (Double ellipse)",
        ["Kesikli çizgili oval", "Altı çizili oval", "Tek çizgili dikdörtgen", "Üçgen"],
        "Multivalued Attribute (Çok Değerli Nitelik) çift çizgili oval ile gösterilir."
    ),
    make_q(
        "ER modellemesinde 'Birincil Anahtar' (Primary Key) niteliği nasıl gösterilir?",
        "İsminin altı çizili oval (Underlined attribute in ellipse)",
        ["İsminin üstü çizili oval", "Çift çizgili baklava", "Kesikli çizgili dikdörtgen", "Yıldızlı daire"],
        "Anahtar nitelikler oval içinde altı çizili metinle belirtilir."
    ),
    make_q(
        "ER modellemesinde varlıklar arasındaki 'İlişki' (Relationship) hangi sembolle gösterilir?",
        "Baklava (Eşkenar dörtgen / Diamond)",
        ["Dikdörtgen", "Oval", "Daire", "Altıgen"],
        "Varlıklar arasındaki ilişkiler baklava (diamond) sembolü ile modellenir."
    ),
    make_q(
        "ER modelinde Çok-a-Çok (M:N) bir ilişki ilişkisel veritabanı tablolarına dönüştürülürken ne yapılır?",
        "Her iki tablonun birincil anahtarlarını yabancı anahtar (FK) olarak içeren yeni bir 'Kavşak / Bağlantı Tablosu' (Junction Table) oluşturulur.",
        ["M:N ilişkiler doğrudan tek bir tabloda birleştirilir.", "Tablolardan biri tamamen silinir.", "Yalnızca tek tarafa Foreign Key sütunu eklenir.", "M:N ilişkiler veritabanına aktarılamaz."],
        "M:N (Many-to-Many) ilişkileri iki adet 1:N ilişkiye dönüştürmek için araya birleştirme tablosu (junction table) konur."
    ),
    make_q(
        "<code>ProjeGorev(SicilNo, ProjeNo, PersonelAd, ProjeAd, CalismaSaati)</code> tablosunda PK <code>(SicilNo, ProjeNo)</code> ise ve <code>SicilNo -> PersonelAd</code> bağımlılığı varsa, 2NF için tablolar nasıl ayrılmalıdır?",
        "<code>Personel(SicilNo PK, PersonelAd)</code>, <code>Proje(ProjeNo PK, ProjeAd)</code> ve <code>Gorev(SicilNo PK/FK, ProjeNo PK/FK, CalismaSaati)</code>",
        ["Tüm sütunlar tek tabloda tutulmalıdır.", "Yalnızca CalismaSaati tablosu açılmalıdır.", "PersonelAd ve ProjeAd sütunları silinmelidir.", "SicilNo birincil anahtardan çıkarılmalıdır."],
        "Kısmi bağımlılıklar (SicilNo->PersonelAd, ProjeNo->ProjeAd) ayrı tablolara alınır; Gorev tablosunda tam bağımlı CalismaSaati kalır."
    ),
    make_q(
        "Veritabanı tasarımında Denormalizasyon (Denormalization) ne amaçla ve ne zaman uygulanır?",
        "JOIN maliyetini azaltıp okuma/sorgu performansını artırmak amacıyla, kontrollü olarak veri tekrarına izin vermek için",
        ["Veritabanı güvenliğini en üst düzeye çıkarmak için", "Tüm tabloları 5NF'ye yükseltmek için", "Disk alanını tamamen sıfırlamak için", "Foreign Key kısıtlamalarını zorunlu kılmak için"],
        "Denormalizasyon, yoğun okuma yapılan (OLAP/Raporlama) sistemlerde sorgu hızını artırmak için bilinçli olarak normalizasyon seviyesini düşürmektir."
    ),
    make_q(
        "Bir tabloda 'Süper Anahtar' (Super Key) tanımı nedir?",
        "İlişkedeki her bir satırı benzersiz olarak tanımlayabilen herhangi bir nitelik veya nitelikler kümesi",
        ["Yalnızca tek bir sütundan oluşan anahtar", "Yalnızca yabancı anahtarların birleşimi", "Tablodaki tüm metin alanlarının toplamı", "Sadece NULL içerebilen anahtar"],
        "Süper anahtar benzersizliği sağlayan her türlü sütun kümesidir. Minimum süper anahtara ise 'Aday Anahtar' denir."
    ),
    make_q(
        "Aşağıdakilerden hangisi Süper Anahtar ile Aday Anahtar arasındaki farkı doğru açıklar?",
        "Aday anahtar gereksiz hiçbir sütun içermeyen 'minimum' süper anahtardır; süper anahtar ise fazladan sütun içerebilir.",
        ["Süper anahtar tek sütunludur, aday anahtar çok sütunludur.", "Süper anahtar NULL kabul eder, aday anahtar etmez.", "Aday anahtar tabloda tek tanedir, süper anahtar çok tanedir.", "İkisi arasında hiçbir fark yoktur."],
        "Örn: (TCKimlik) aday anahtardır. (TCKimlik, Ad, Soyad) ise bir süper anahtardır (gereksiz alan içerir)."
    ),
    make_q(
        "Bir tabloda <code>A -> B</code> ve <code>B -> C</code> varken <code>A -> C</code> oluşması hangi aksiyom (çıkarım kuralı) ile açıklanır?",
        "Geçişlilik Kuralı (Transitivity Rule - Armstrong Aksiyomları)",
        ["Yansıma Kuralı (Reflexivity Rule)", "Genişletme Kuralı (Augmentation Rule)", "Ayrıştırma Kuralı (Decomposition Rule)", "Birleşim Kuralı (Union Rule)"],
        "Armstrong Aksiyomu: X -> Y ve Y -> Z ise X -> Z geçişlidir (Transitivity)."
    ),
    make_q(
        "Armstrong aksiyomlarından 'Yansıma Kuralı' (Reflexivity Rule) nedir?",
        "Eğer Y, X'in bir alt kümesi ise (Y ⊆ X), o zaman <code>X -> Y</code> geçerlidir (Örn: (SicilNo, Ad) -> SicilNo).",
        ["X -> Y ise Y -> X geçerlidir.", "X -> Y ise XZ -> YZ geçerlidir.", "X -> Y ve Y -> Z ise X -> Z geçerlidir.", "X -> Y ise X -> NULL geçerlidir."],
        "Yansıma (Reflexivity): Bir sütun kümesi kendi alt kümesini daima fonksiyonel olarak belirler."
    ),
    make_q(
        "Aşağıdaki bağımlılıklardan hangisi 'Önemsiz / Aşikar' (Trivial Functional Dependency) bir bağımlılıktır?",
        "<code>(OgrenciNo, Ad) -> OgrenciNo</code> (Sağ taraf sol tarafın bir alt kümesidir)",
        ["<code>OgrenciNo -> Ad</code>", "<code>BolumNo -> BolumAdi</code>", "<code>TCKimlik -> Telefon</code>", "<code>DersKod -> Kredi</code>"],
        "Trivial FD: X -> Y ifadesinde Y ⊆ X ise bu bağımlılık aşikardır / önemsizdir."
    ),
    make_q(
        "Bir normalizasyon sürecinde 'Bağımlılık Koruma' (Dependency Preservation) ne demektir?",
        "Orijinal tablodaki tüm işlevsel bağımlılıkların, tablolar ayrıştırıldıktan sonra da tablolar arası JOIN'e gerek kalmadan tek tek tablolarda doğrulanabilmesi",
        ["Verilerin diske şifreli yazılması", "Tüm birincil anahtarların korunması", "Tablodaki kayıt sayısının değişmemesi", "Sadece metin sütunlarının ayrıştırılması"],
        "Dependency preservation: Ayrıştırılan parçaların bağımlılıklarının birleşimi orijinal bağımlılık kümesini kapsamalıdır."
    ),
    make_q(
        "Bir ilişkide <code>TCKimlik</code> ve <code>OgrenciNo</code> sütunlarının her ikisi de her satırı tekil tanımlıyorsa bunlara ne ad verilir?",
        "Aday Anahtarlar (Candidate Keys)",
        ["Yabancı Anahtarlar (Foreign Keys)", "Birleşik İndeksler", "Geçişli Bağımlılıklar", "Sanal Sütunlar"],
        "Tabloda satırı tekil belirleyen tüm minimal anahtarlar Aday Anahtardır; biri seçilip Primary Key yapılır."
    ),
    make_q(
        "Normalizasyon teorisinde 'Kayıplı Ayrıştırma' (Lossy Decomposition) neden tehlikelidir?",
        "Ayrıştırılan tablolar birleştirildiğinde orijinalde var olmayan 'sahte/hayali satırlar' (spurious tuples) üreterek yanlış bilgiye yol açması",
        ["Veritabanı dosyasının diskten tamamen silinmesi", "Tablodaki tüm sayıların sıfıra dönmesi", "Sorguların derlenemez hale gelmesi", "Yalnızca tek bir kullanıcının erişebilmesi"],
        "Kayıplı birleştirmede tablolar join edildiğinde fazla ve hatalı satırlar türer, verinin doğruluğu bozulur."
    ),
    make_q(
        "Aşağıdaki normal formlardan hangisi 'Çok Değerli Bağımlılık' (MVD) kavramı üzerine kurulmuştur?",
        "4NF",
        ["1NF", "2NF", "3NF", "BCNF"],
        "4NF (Dördüncü Normal Form) bağımsız çok değerli bağımlılıkların ayrıştırılmasını sağlar."
    ),
    make_q(
        "ER diyagramında bir varlığın bir ilişkiye 'Zorunlu Katılımı' (Total / Mandatory Participation) nasıl gösterilir?",
        "Çift çizgi (Double line) ile",
        ["Tek çizgi ile", "Kesikli çizgi ile", "Noktalı çizgi ile", "Ok işareti ile"],
        "Zorunlu katılım (Total participation) varlık ile ilişki arasındaki çift çizgi ile modellenir."
    ),
    make_q(
        "1NF'den 2NF'ye geçişte yapılması gereken temel işlem nedir?",
        "Kısmi bağımlılıkların tespit edilip, bileşik anahtarın parçasına bağlı alanların yeni tablolara taşınması",
        ["Hücrelerdeki virgüllü değerlerin temizlenmesi", "Geçişli bağımlılıkların elenmesi", "Tüm tablolara yabancı anahtar eklenmesi", "Her sütunun VARCHAR yapılması"],
        "1NF -> 2NF: Kısmi bağımlılıkların ayrıştırılması adımıdır."
    ),
    make_q(
        "2NF'den 3NF'ye geçişte yapılması gereken temel işlem nedir?",
        "Anahtar olmayan bir alanın başka bir anahtar olmayan alana olan geçişli bağımlılıklarının (Transitive dependencies) ayrı tabloya taşınması",
        ["Tekrarlayan grupların ayrılması", "Kısmi bağımlılıkların ayrılması", "Tüm tabloların birleştirilmesi", "İndekslerin silinmesi"],
        "2NF -> 3NF: Geçişli bağımlılıkların ortadan kaldırılması adımıdır."
    ),
    make_q(
        "Aşağıdakilerden hangisi bir normalizasyon problemi DEĞİLDİR?",
        "Sorgu sonucunda sıralı liste elde etmek için <code>ORDER BY</code> kullanılması",
        ["Ekleme anomalisi yaşanması", "Silme sırasında ilişkisiz verilerin kaybolması", "Aynı bilginin birden çok satırda gereksiz tekrarlanması", "Güncelleme sırasında veri tutarsızlığı oluşması"],
        "ORDER BY standart bir sorgu işlemidir; anomaliler ve veri tekrarı ise normalizasyon problemleridir."
    ),
    make_q(
        "Bir tabloda <code>(DersKod, Ogretmen) -> Sinif</code> ve <code>Sinif -> Ogretmen</code> bağımlılıkları varsa ve anahtar <code>(DersKod, Ogretmen)</code> ise, <code>Sinif -> Ogretmen</code> bağımlılığı hangi formu ihlal eder?",
        "BCNF (Çünkü Sinif bir aday anahtar değildir ama bir belirleyicidir)",
        ["1NF", "2NF", "4NF", "5NF"],
        "Sinif belirleyicidir fakat aday anahtar değildir; bu durum 3NF'de tolere edilse bile BCNF'yi kesinlikle ihlal eder."
    )
]

print(f"Exam 7: {len(e7)}, Exam 8: {len(e8)}")
