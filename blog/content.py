POSTS = [
    {
        "slug": "pengantar-arsitektur-perangkat-lunak",
        "title": "Pengantar Arsitektur Perangkat Lunak",
        "category": "Fondasi",
        "source_file": "Pengantar_Arsitektur_Perangkat_Lunak-1.pdf",
        "reading_time": "7 menit baca",
        "summary": (
            "Arsitektur perangkat lunak membantu kita melihat bentuk besar sistem "
            "sebelum masuk ke detail kode, framework, dan database."
        ),
        "intro": [
            (
                "Bayangkan kita diminta membangun sebuah aplikasi. Cara paling cepat "
                "memang langsung menulis kode. Tetapi semakin besar sistemnya, semakin "
                "mudah kita tersesat: fitur saling menabrak, database menjadi lambat, "
                "dan perubahan kecil bisa merusak bagian lain."
            ),
            (
                "Di sinilah arsitektur perangkat lunak masuk. Ia bukan sekadar diagram "
                "kotak-kotak, melainkan cara berpikir untuk menentukan bagian sistem, "
                "hubungan antarbagian, dan alasan kenapa keputusan itu dipilih."
            ),
        ],
        "story": (
            "Anggap sistem seperti gedung kampus. Sebelum membangun ruang kelas, "
            "laboratorium, dan jalur listrik, kita perlu denah. Dalam software, denah "
            "itu adalah arsitektur: ia menunjukkan mana bagian tampilan, mana logika "
            "bisnis, mana penyimpanan data, dan bagaimana semuanya berbicara."
        ),
        "steps": [
            {
                "title": "Mulai dari masalah yang ingin diselesaikan",
                "body": (
                    "Arsitektur yang baik tidak dimulai dari pertanyaan 'pakai teknologi "
                    "apa?', tetapi dari 'sistem ini harus melayani siapa, beban seperti "
                    "apa, dan risiko apa yang paling berbahaya?'."
                ),
            },
            {
                "title": "Pecah sistem menjadi bagian yang masuk akal",
                "body": (
                    "Biasanya kita membedakan bagian antarmuka, proses aplikasi, aturan "
                    "domain, penyimpanan data, dan integrasi luar. Pemisahan ini membuat "
                    "sistem lebih mudah dipahami."
                ),
            },
            {
                "title": "Tentukan cara bagian-bagian itu berkomunikasi",
                "body": (
                    "Ada bagian yang cukup berbicara lewat HTTP biasa, ada yang perlu "
                    "message broker, dan ada yang lebih cocok diproses secara asinkron. "
                    "Pilihan komunikasi menentukan performa dan kompleksitas."
                ),
            },
            {
                "title": "Catat alasan di balik keputusan",
                "body": (
                    "Keputusan arsitektur hampir selalu punya trade-off. Misalnya, "
                    "microservices bisa lebih mudah diskalakan, tetapi operasionalnya "
                    "lebih rumit daripada monolith."
                ),
            },
        ],
        "key_points": [
            "Arsitektur adalah gambaran besar sistem dan alasan teknis di baliknya.",
            "Tujuannya membantu sistem tetap mudah diubah, diuji, dan dikembangkan.",
            "Keputusan arsitektur harus dikaitkan dengan kebutuhan nyata, bukan tren.",
        ],
        "takeaway": (
            "Kalau kode adalah batu bata, arsitektur adalah cara kita memastikan "
            "bangunannya tidak roboh saat dipakai banyak orang."
        ),
    },
    {
        "slug": "architectural-drivers",
        "title": "Architectural Drivers: Yang Mengarahkan Desain Sistem",
        "category": "Decision Making",
        "source_file": "Architectural_Drivers_Mengarahkan_Desain_Sistem.pdf",
        "reading_time": "8 menit baca",
        "summary": (
            "Architectural drivers adalah alasan utama yang membuat sebuah desain "
            "dipilih: kebutuhan bisnis, batasan teknis, atribut kualitas, dan risiko."
        ),
        "intro": [
            (
                "Setiap sistem punya arah. Ada sistem yang harus murah dulu, ada yang "
                "harus tahan jutaan pengguna, ada juga yang paling penting harus aman. "
                "Arah inilah yang disebut architectural drivers."
            ),
            (
                "Driver membantu arsitek menentukan prioritas. Tanpa driver, desain "
                "mudah berubah menjadi daftar teknologi yang terlihat keren, tetapi "
                "tidak menjawab kebutuhan sistem."
            ),
        ],
        "story": (
            "Misalnya sebuah aplikasi kesehatan di resort senior living harus tetap "
            "jalan walau koneksi pusat putus. Driver utamanya bukan tampilan yang cantik, "
            "melainkan availability, keamanan data medis, dan sinkronisasi saat jaringan "
            "pulih."
        ),
        "steps": [
            {
                "title": "Kenali tujuan bisnis",
                "body": (
                    "Pertama, cari tahu sistem ini dibuat untuk apa. Apakah untuk MVP "
                    "cepat, transaksi kritis, layanan publik, atau sistem internal? "
                    "Tujuan bisnis menentukan seberapa jauh arsitektur harus disiapkan."
                ),
            },
            {
                "title": "Daftar kebutuhan fungsional",
                "body": (
                    "Kebutuhan fungsional menjelaskan apa yang sistem lakukan: login, "
                    "membuat kontrak, memproses gift, menyimpan sensor kesehatan, dan "
                    "sejenisnya."
                ),
            },
            {
                "title": "Daftar kebutuhan kualitas",
                "body": (
                    "Kebutuhan kualitas menjelaskan seberapa baik sistem harus bekerja: "
                    "cepat, aman, tersedia, mudah diskalakan, atau mudah dirawat."
                ),
            },
            {
                "title": "Catat constraint dan risiko",
                "body": (
                    "Constraint bisa berupa teknologi wajib, deadline, biaya, tim kecil, "
                    "atau aturan keamanan. Risiko adalah hal yang mungkin merusak sistem "
                    "jika tidak dipikirkan sejak awal."
                ),
            },
            {
                "title": "Pilih desain yang paling cocok dengan prioritas",
                "body": (
                    "Jika driver utamanya burst traffic, pola seperti event-driven atau "
                    "space-based lebih relevan. Jika driver utamanya simplicity, monolith "
                    "yang rapi bisa lebih masuk akal."
                ),
            },
        ],
        "key_points": [
            "Driver adalah kompas desain, bukan hiasan dokumentasi.",
            "Driver biasanya berasal dari tujuan bisnis, atribut kualitas, constraint, dan risiko.",
            "Satu keputusan desain bisa bagus untuk satu driver tetapi buruk untuk driver lain.",
        ],
        "takeaway": (
            "Sebelum memilih pola arsitektur, tanyakan dulu: masalah terpenting apa "
            "yang harus diselamatkan oleh desain ini?"
        ),
    },
    {
        "slug": "architectural-quality-attributes",
        "title": "Quality Attributes: Mengukur Kualitas Sistem",
        "category": "Quality Attribute",
        "source_file": "Architectural_Quality_Attributes-1.pdf",
        "reading_time": "9 menit baca",
        "summary": (
            "Quality attributes seperti availability, security, performance, dan "
            "scalability membantu kita menilai apakah arsitektur benar-benar cocok."
        ),
        "intro": [
            (
                "Sistem tidak cukup hanya 'bisa jalan'. Dalam arsitektur, kita juga "
                "bertanya: apakah sistem tetap hidup saat jaringan putus, aman dari "
                "akses ilegal, cepat saat ramai, dan bisa tumbuh saat pengguna bertambah?"
            ),
            (
                "Pertanyaan itu disebut quality attributes. Ia membuat kualitas sistem "
                "lebih mudah dibicarakan dan diukur."
            ),
        ],
        "story": (
            "Pada studi kasus Lifebond, sensor kesehatan tidak boleh berhenti hanya "
            "karena koneksi ke pusat putus. Di saat yang sama, data medis tidak boleh "
            "tersebar tanpa perlindungan. Jadi arsitektur harus menyeimbangkan "
            "availability dan security."
        ),
        "steps": [
            {
                "title": "Ubah kata umum menjadi ukuran",
                "body": (
                    "Jangan berhenti di kata 'cepat' atau 'aman'. Ubah menjadi ukuran: "
                    "latency p95, uptime, RTO, RPO, audit log, enkripsi, atau jumlah "
                    "request per detik."
                ),
            },
            {
                "title": "Tulis quality attribute scenario",
                "body": (
                    "Gunakan pola source, stimulus, environment, artifact, response, "
                    "dan response measure. Contoh: saat fiber pusat putus, service lokal "
                    "tetap membaca sensor dan menyimpan data vital."
                ),
            },
            {
                "title": "Cari trade-off",
                "body": (
                    "Availability bisa naik dengan replika lokal, tetapi security jadi "
                    "lebih sulit karena data tersebar. Cache mempercepat response, tetapi "
                    "bisa membuat data pusat tidak langsung konsisten."
                ),
            },
            {
                "title": "Tentukan mitigasi",
                "body": (
                    "Jika data tersebar, gunakan enkripsi, mTLS, RBAC, audit log, secret "
                    "rotation, dan monitoring. Jika sinkronisasi rawan gagal, gunakan "
                    "transactional outbox dan idempotency key."
                ),
            },
        ],
        "key_points": [
            "Availability berbicara tentang sistem tetap melayani saat ada gangguan.",
            "Security berbicara tentang perlindungan data dan operasi.",
            "Performance dan scalability berhubungan, tetapi tidak sama.",
            "ATAM membantu membaca trade-off, risiko, dan titik keputusan penting.",
        ],
        "takeaway": (
            "Quality attribute membuat arsitektur lebih jujur: setiap keputusan harus "
            "bisa dijelaskan dampak plus dan minusnya."
        ),
    },
    {
        "slug": "visualisasi-uml-c4-model",
        "title": "Visualisasi Arsitektur: UML dan C4 Model",
        "category": "Visualisasi",
        "source_file": "Visualisasi_Arsitektur_UML_dan_C4_Model-2.pdf",
        "reading_time": "8 menit baca",
        "summary": (
            "Diagram membantu pembaca melihat sistem dari jauh dulu, lalu masuk ke "
            "detail container, database, broker, dan hubungan antar komponen."
        ),
        "intro": [
            (
                "Arsitektur yang hanya dijelaskan dengan paragraf sering membuat pembaca "
                "lelah. Diagram membantu kita melihat siapa pengguna sistem, batas sistem, "
                "aplikasi apa saja yang berjalan, dan arah komunikasinya."
            ),
            (
                "UML berguna untuk banyak kebutuhan pemodelan, sedangkan C4 Model populer "
                "karena memandu kita melihat sistem secara bertahap: context, container, "
                "component, lalu code."
            ),
        ],
        "story": (
            "Bayangkan menjelaskan sistem SaaS kontrak. Kalau langsung bicara worker, "
            "queue, dan database, pembaca bisa bingung. Dengan C4, kita mulai dari user, "
            "lalu masuk ke Svelte Web UI, Go API, RabbitMQ, worker, dan database."
        ),
        "steps": [
            {
                "title": "Mulai dari siapa yang memakai sistem",
                "body": (
                    "Di C4, aktor disebut Person. Tuliskan perannya, misalnya User, Klien, "
                    "atau Admin. Fokus pada peran, bukan nama orang."
                ),
            },
            {
                "title": "Gambar batas sistem",
                "body": (
                    "System boundary adalah kotak besar yang menandai bagian mana yang "
                    "menjadi milik sistem. Ini penting agar pembaca tahu mana internal "
                    "dan mana sistem eksternal."
                ),
            },
            {
                "title": "Masukkan container utama",
                "body": (
                    "Container adalah aplikasi, proses, atau data store yang bisa dijalankan "
                    "terpisah. Contohnya Svelte Web UI, Go API Backend, RabbitMQ, Go Worker, "
                    "dan Contract DB."
                ),
            },
            {
                "title": "Beri label pada panah",
                "body": (
                    "Panah tanpa label sering membingungkan. Tulis protokol atau data yang "
                    "mengalir: HTTPS, publish job, consume queue, read/write DB, atau update status."
                ),
            },
            {
                "title": "Jangan campur semua level sekaligus",
                "body": (
                    "Level container cukup menunjukkan aplikasi dan data store utama. Detail "
                    "class atau fungsi kecil sebaiknya masuk ke diagram level lebih rendah."
                ),
            },
        ],
        "key_points": [
            "Diagram yang baik menjawab 'siapa berbicara dengan apa'.",
            "C4 Level 2 cocok untuk menjelaskan container dan teknologi utama.",
            "Label teknologi dan arah komunikasi membuat diagram jauh lebih bermakna.",
        ],
        "takeaway": (
            "Diagram arsitektur bukan gambar dekoratif. Ia adalah peta agar orang lain "
            "bisa memahami sistem tanpa harus membaca seluruh kode."
        ),
    },
    {
        "slug": "layered-dan-monolith",
        "title": "Pola Fundamental: Layered Architecture dan Monolith",
        "category": "Architecture Pattern",
        "source_file": "Pola_Arsitektur_Fundamental_Layered_dan_Monolith-1.pdf",
        "reading_time": "8 menit baca",
        "summary": (
            "Layered architecture dan monolith sering menjadi titik awal yang masuk akal, "
            "asalkan batas tanggung jawabnya dibuat jelas."
        ),
        "intro": [
            (
                "Tidak semua sistem harus langsung menjadi microservices. Banyak aplikasi "
                "kampus, admin, dan bisnis kecil justru lebih sehat dimulai dari monolith "
                "yang rapi."
            ),
            (
                "Kuncinya ada pada layered architecture: memisahkan tampilan, logika "
                "aplikasi, aturan domain, dan akses data agar perubahan tidak menyebar "
                "ke mana-mana."
            ),
        ],
        "story": (
            "Anggap aplikasi seperti warung makan. Pelanggan tidak perlu masuk ke dapur, "
            "kasir tidak perlu mengatur stok beras langsung, dan dapur tidak perlu tahu "
            "cara tampilan menu di layar. Setiap lapisan punya tugas."
        ),
        "steps": [
            {
                "title": "Kenali lapisan presentation",
                "body": (
                    "Lapisan ini berurusan dengan halaman web, form, tombol, dan tampilan. "
                    "Tugasnya menerima input pengguna dan menampilkan hasil."
                ),
            },
            {
                "title": "Pisahkan application layer",
                "body": (
                    "Application layer mengatur alur use case: validasi permintaan, memanggil "
                    "aturan bisnis, menyimpan data, dan mengatur response."
                ),
            },
            {
                "title": "Jaga domain layer tetap bersih",
                "body": (
                    "Domain layer berisi aturan inti. Semakin sedikit ia bergantung pada "
                    "framework, semakin mudah ia diuji dan dipahami."
                ),
            },
            {
                "title": "Letakkan detail teknis di infrastructure",
                "body": (
                    "Database, API eksternal, file storage, dan message broker adalah detail "
                    "infrastruktur. Detail ini boleh berubah tanpa merusak aturan domain."
                ),
            },
            {
                "title": "Waspadai monolith yang terlalu menempel",
                "body": (
                    "Monolith menjadi masalah ketika semua modul saling bergantung, satu "
                    "fitur gagal menjatuhkan semua, dan scaling harus dilakukan untuk "
                    "seluruh aplikasi sekaligus."
                ),
            },
        ],
        "key_points": [
            "Monolith bukan musuh; monolith yang tidak terstruktur adalah masalah.",
            "Layer membantu memisahkan tanggung jawab agar kode mudah dirawat.",
            "N-Tier monolith cocok untuk beban stabil, tetapi lemah pada burst traffic besar.",
        ],
        "takeaway": (
            "Mulai sederhana itu boleh. Yang penting, kesederhanaannya tetap punya batas "
            "yang jelas agar sistem bisa tumbuh."
        ),
    },
    {
        "slug": "pola-arsitektur-kinerja-tinggi",
        "title": "Pola Arsitektur Kinerja Tinggi",
        "category": "Scalability",
        "source_file": "Pola_Arsitektur_Kinerja_Tinggi-1.pdf",
        "reading_time": "10 menit baca",
        "summary": (
            "Saat traffic naik ekstrem, sistem perlu backpressure, queue, cache, rate limit, "
            "dan pola yang membuat database tidak langsung dihantam."
        ),
        "intro": [
            (
                "Masalah kinerja tinggi bukan hanya server kurang kuat. Sering kali masalahnya "
                "adalah semua request dipaksa diproses saat itu juga, database menerima beban "
                "terlalu besar, dan tidak ada mekanisme untuk menahan lonjakan."
            ),
            (
                "Materi ini membahas cara sistem tetap tenang saat traffic mendadak naik, "
                "misalnya kasus live streaming yang tiba-tiba diserbu jutaan pengguna."
            ),
        ],
        "story": (
            "Bayangkan Dragon Live mendapat lonjakan 10.000 persen dalam 3 detik. Jika setiap "
            "gift langsung menulis ke database pusat, server akan penuh, koneksi habis, dan "
            "timeout menyebar. Arsitektur harus membuat lonjakan itu antre dan diproses bertahap."
        ),
        "steps": [
            {
                "title": "Jangan biarkan semua request langsung masuk ke inti sistem",
                "body": (
                    "Gunakan load balancer, rate limit, dan token bucket agar traffic liar "
                    "tidak langsung memakan semua resource."
                ),
            },
            {
                "title": "Ubah pekerjaan berat menjadi asinkron",
                "body": (
                    "Event-driven architecture memakai broker atau stream agar producer "
                    "cukup mengirim event, lalu consumer memprosesnya sesuai kapasitas."
                ),
            },
            {
                "title": "Gunakan queue sebagai peredam lonjakan",
                "body": (
                    "Queue memberi backpressure. Jika consumer belum sanggup, pekerjaan "
                    "menunggu, bukan membuat server aplikasi langsung tumbang."
                ),
            },
            {
                "title": "Pakai cache atau in-memory grid untuk data sementara",
                "body": (
                    "Space-based architecture cocok untuk burst ekstrem karena data sementara "
                    "seperti session, ranking, atau gift bisa diproses di memory grid yang "
                    "dipartisi."
                ),
            },
            {
                "title": "Siapkan graceful degradation",
                "body": (
                    "Saat sistem sangat ramai, fitur non-kritis boleh dikurangi sementara. "
                    "Yang penting fitur inti tetap berjalan dan pengguna mendapat response "
                    "yang jelas."
                ),
            },
        ],
        "key_points": [
            "Burst traffic menguji backpressure, elastisitas, dan isolasi failure.",
            "Event-driven cocok untuk pekerjaan asinkron yang bisa antre.",
            "Space-based cocok untuk lonjakan real-time yang sangat besar.",
            "Circuit breaker dan graceful degradation mencegah kegagalan menyebar.",
        ],
        "takeaway": (
            "Sistem kinerja tinggi bukan sistem yang memproses semuanya sekaligus, tetapi "
            "sistem yang tahu kapan harus menahan, mengantre, dan memprioritaskan."
        ),
    },
    {
        "slug": "modern-data-blueprint",
        "title": "Modern Data Blueprint",
        "category": "Data Architecture",
        "source_file": "Modern_Data_Blueprint.pdf",
        "reading_time": "9 menit baca",
        "summary": (
            "Blueprint data modern menjelaskan perjalanan data dari sumber, ingestion, "
            "penyimpanan, pemrosesan, penyajian, sampai governance."
        ),
        "intro": [
            (
                "Setiap aplikasi menghasilkan data. Tetapi data yang hanya tersimpan di "
                "database operasional belum tentu siap dipakai untuk analitik, laporan, "
                "machine learning, atau pengambilan keputusan."
            ),
            (
                "Modern data blueprint membantu kita melihat jalur data secara utuh: dari "
                "mana data datang, bagaimana ia dibersihkan, di mana ia disimpan, siapa yang "
                "boleh mengakses, dan bagaimana hasilnya dipakai."
            ),
        ],
        "story": (
            "Bayangkan sistem e-commerce. Ada data transaksi, stok, klik pengguna, pembayaran, "
            "dan pengiriman. Jika semuanya tersebar tanpa peta, tim analitik akan kesulitan. "
            "Blueprint data membuat aliran itu lebih jelas."
        ),
        "steps": [
            {
                "title": "Mulai dari sumber data",
                "body": (
                    "Sumber bisa berupa aplikasi utama, log server, sensor, file CSV, API "
                    "eksternal, atau event dari message broker. Setiap sumber perlu diketahui "
                    "pemilik dan formatnya."
                ),
            },
            {
                "title": "Masukkan data lewat ingestion",
                "body": (
                    "Ingestion bisa batch atau streaming. Batch cocok untuk laporan berkala, "
                    "sedangkan streaming cocok untuk kebutuhan hampir real-time seperti fraud "
                    "detection atau monitoring."
                ),
            },
            {
                "title": "Simpan data sesuai bentuknya",
                "body": (
                    "Data mentah bisa masuk ke data lake. Data yang sudah rapi untuk analitik "
                    "bisa masuk ke warehouse atau lakehouse. Pilihan ini tergantung kebutuhan "
                    "query, biaya, dan tata kelola."
                ),
            },
            {
                "title": "Proses dan rapikan data",
                "body": (
                    "Tahap transformasi membersihkan data, menyatukan format, menghapus "
                    "duplikasi, dan membuat model yang siap dipakai dashboard atau analisis."
                ),
            },
            {
                "title": "Sajikan data untuk pengguna akhir",
                "body": (
                    "Hasil akhirnya bisa berupa dashboard, laporan, API data, fitur rekomendasi, "
                    "atau dataset untuk machine learning."
                ),
            },
            {
                "title": "Jaga governance dari awal",
                "body": (
                    "Governance mencakup kualitas data, hak akses, lineage, katalog data, "
                    "audit, dan kebijakan privasi. Tanpa ini, data cepat menjadi sulit dipercaya."
                ),
            },
        ],
        "key_points": [
            "Blueprint data memetakan perjalanan data dari sumber sampai pemakaian.",
            "Batch dan streaming dipilih sesuai kebutuhan waktu dan biaya.",
            "Data lake, warehouse, dan lakehouse punya peran yang berbeda.",
            "Governance membuat data lebih aman, terlacak, dan bisa dipercaya.",
        ],
        "takeaway": (
            "Data architecture yang baik membuat data tidak hanya tersimpan, tetapi benar-benar "
            "bisa digunakan untuk memahami sistem dan mengambil keputusan."
        ),
    },
]


TOPICS = [
    "Architectural Drivers",
    "Quality Attributes",
    "ATAM",
    "C4 Model",
    "Layered Architecture",
    "Monolith",
    "Event-Driven",
    "Space-Based",
    "Microservices",
    "Modern Data Blueprint",
]


ARCHITECTURE_NOTES = [
    "Baca dari fondasi dulu: kenali arsitektur, lalu pahami driver dan atribut kualitas.",
    "Setiap artikel memakai alur cerita agar konsep teknis terasa seperti perjalanan sistem.",
    "Bagian step by step disiapkan agar materi mudah dipakai untuk belajar ulang sebelum ujian.",
]


POST_EXTRAS = {
    "pengantar-arsitektur-perangkat-lunak": {
        "image": "blog/images/pengantar-arsitektur.svg",
        "image_alt": "Diagram empat lapisan arsitektur perangkat lunak.",
        "deep_dive": [
            {
                "title": "Kenapa arsitektur penting sejak awal?",
                "body": (
                    "Tanpa arsitektur, sistem biasanya tumbuh berdasarkan kebutuhan paling "
                    "dekat. Awalnya cepat, tetapi lama-lama sulit dirawat karena setiap "
                    "fitur baru menempel ke fitur lama tanpa batas yang jelas."
                ),
            },
            {
                "title": "Apa bedanya desain dan arsitektur?",
                "body": (
                    "Desain sering membahas detail solusi pada modul tertentu, sedangkan "
                    "arsitektur membahas keputusan besar yang memengaruhi banyak bagian "
                    "sistem: pembagian komponen, komunikasi, data, deployment, dan risiko."
                ),
            },
            {
                "title": "Bagaimana cara membaca arsitektur?",
                "body": (
                    "Mulailah dari tujuan sistem, lalu lihat komponennya, aliran data, "
                    "dependency, titik risiko, dan alasan kenapa pola tertentu dipilih."
                ),
            },
        ],
        "example": {
            "title": "Contoh ringan",
            "body": (
                "Aplikasi blog sederhana bisa dimulai dari monolith Django. Tetapi sejak awal "
                "kita tetap memisahkan template, view, data artikel, dan static files agar "
                "nanti mudah ditambah database atau dashboard admin."
            ),
        },
        "quiz": [
            {
                "question": "Apa fungsi utama arsitektur perangkat lunak?",
                "options": [
                    "Menentukan warna tombol aplikasi",
                    "Melihat bentuk besar sistem dan keputusan pentingnya",
                    "Menghapus kebutuhan dokumentasi",
                ],
                "answer": "Melihat bentuk besar sistem dan keputusan pentingnya",
            },
            {
                "question": "Kenapa sistem perlu dipisah menjadi beberapa bagian?",
                "options": [
                    "Agar lebih mudah dipahami, diuji, dan diubah",
                    "Agar semua kode wajib berada di satu file",
                    "Agar database tidak perlu dibuat",
                ],
                "answer": "Agar lebih mudah dipahami, diuji, dan diubah",
            },
        ],
        "checklist": [
            "Apa tujuan utama sistem?",
            "Bagian apa saja yang perlu dipisahkan?",
            "Data mengalir dari mana ke mana?",
            "Keputusan apa yang paling sulit diubah nanti?",
        ],
    },
    "architectural-drivers": {
        "image": "blog/images/architectural-drivers.svg",
        "image_alt": "Diagram driver arsitektur yang mengarah ke keputusan desain.",
        "deep_dive": [
            {
                "title": "Driver bisnis",
                "body": (
                    "Driver bisnis menjawab alasan sistem dibuat: mempercepat layanan, "
                    "menurunkan biaya, membuka produk baru, atau memenuhi aturan tertentu."
                ),
            },
            {
                "title": "Driver teknis",
                "body": (
                    "Driver teknis muncul dari kondisi lapangan: tim hanya menguasai stack "
                    "tertentu, server terbatas, integrasi wajib, atau sistem lama harus tetap "
                    "dipakai."
                ),
            },
            {
                "title": "Driver risiko",
                "body": (
                    "Risiko sering menjadi penentu desain. Jika risiko terbesar adalah data "
                    "hilang, desain harus mengutamakan durability. Jika risiko terbesar "
                    "adalah traffic meledak, desain harus punya backpressure."
                ),
            },
        ],
        "example": {
            "title": "Contoh keputusan",
            "body": (
                "Jika aplikasi kontrak harus MVP cepat dan tim kecil, monolith modular lebih "
                "masuk akal. Jika tiap modul tumbuh dengan beban berbeda dan tim sudah besar, "
                "microservices mulai layak dipertimbangkan."
            ),
        },
        "quiz": [
            {
                "question": "Apa itu architectural driver?",
                "options": [
                    "Alasan utama yang mengarahkan pilihan desain sistem",
                    "Nama lain dari halaman login",
                    "Daftar warna untuk tampilan website",
                ],
                "answer": "Alasan utama yang mengarahkan pilihan desain sistem",
            },
            {
                "question": "Contoh constraint dalam arsitektur adalah...",
                "options": [
                    "Deadline, biaya, teknologi wajib, atau aturan keamanan",
                    "Judul artikel yang terlalu panjang",
                    "Ukuran font pada paragraf",
                ],
                "answer": "Deadline, biaya, teknologi wajib, atau aturan keamanan",
            },
        ],
        "checklist": [
            "Apa target bisnis terpenting?",
            "Atribut kualitas apa yang paling prioritas?",
            "Constraint apa yang tidak bisa ditawar?",
            "Risiko apa yang harus dimitigasi sejak desain awal?",
        ],
    },
    "architectural-quality-attributes": {
        "image": "blog/images/quality-attributes.svg",
        "image_alt": "Diagram empat atribut kualitas utama sistem.",
        "deep_dive": [
            {
                "title": "Availability",
                "body": (
                    "Availability melihat kemampuan sistem tetap melayani saat ada gangguan. "
                    "Ukuran yang sering dipakai adalah uptime, MTTR, RTO, dan RPO."
                ),
            },
            {
                "title": "Security",
                "body": (
                    "Security bukan hanya login. Ia mencakup autentikasi, otorisasi, enkripsi, "
                    "audit log, threat model, dan kebijakan akses data."
                ),
            },
            {
                "title": "Performance dan scalability",
                "body": (
                    "Performance membahas seberapa cepat sistem merespons pada kondisi tertentu. "
                    "Scalability membahas apakah kapasitas bisa naik saat resource ditambah."
                ),
            },
        ],
        "example": {
            "title": "Contoh ATAM singkat",
            "body": (
                "Saat jaringan pusat Lifebond putus, service lokal harus tetap membaca sensor "
                "dan menyimpan data vital. Responsnya diukur dari data tidak hilang, alarm tetap "
                "jalan, dan konflik sinkronisasi bisa diselesaikan saat koneksi pulih."
            ),
        },
        "quiz": [
            {
                "question": "Quality attribute menjelaskan tentang apa?",
                "options": [
                    "Seberapa baik sistem bekerja dalam kondisi tertentu",
                    "Jumlah gambar yang dipakai pada website",
                    "Nama folder untuk menyimpan template",
                ],
                "answer": "Seberapa baik sistem bekerja dalam kondisi tertentu",
            },
            {
                "question": "Kalau sistem harus tetap berjalan saat ada gangguan, atribut yang dibahas adalah...",
                "options": [
                    "Availability",
                    "Typography",
                    "Branding",
                ],
                "answer": "Availability",
            },
        ],
        "checklist": [
            "Apa stimulus yang memicu masalah?",
            "Bagian sistem apa yang terkena dampak?",
            "Respons apa yang diharapkan?",
            "Ukuran suksesnya apa?",
            "Trade-off apa yang muncul?",
        ],
    },
    "visualisasi-uml-c4-model": {
        "image": "blog/images/c4-model.svg",
        "image_alt": "Diagram C4 level container untuk sistem web sederhana.",
        "deep_dive": [
            {
                "title": "UML untuk model yang lebih formal",
                "body": (
                    "UML berguna saat kita perlu menjelaskan use case, class, sequence, atau "
                    "deployment dengan notasi yang lebih baku."
                ),
            },
            {
                "title": "C4 untuk komunikasi arsitektur",
                "body": (
                    "C4 lebih ramah untuk diskusi tim karena dimulai dari level tinggi. Pembaca "
                    "tidak langsung dipaksa melihat detail class atau fungsi."
                ),
            },
            {
                "title": "Label panah adalah kunci",
                "body": (
                    "Panah harus menjelaskan komunikasi: HTTPS, publish event, consume queue, "
                    "read/write DB, atau call API eksternal. Tanpa label, diagram mudah ambigu."
                ),
            },
        ],
        "example": {
            "title": "Contoh container",
            "body": (
                "Untuk SaaS kontrak: User membuka Svelte Web UI, UI memanggil Go API lewat "
                "HTTPS, API menyimpan data ke database, lalu menerbitkan job validasi ke "
                "RabbitMQ untuk diproses worker."
            ),
        },
        "quiz": [
            {
                "question": "Apa tujuan utama C4 Model?",
                "options": [
                    "Menjelaskan sistem bertahap dari konteks sampai detail",
                    "Mengganti semua kode menjadi diagram",
                    "Membuat database otomatis",
                ],
                "answer": "Menjelaskan sistem bertahap dari konteks sampai detail",
            },
            {
                "question": "Agar diagram mudah dipahami, setiap panah sebaiknya diberi...",
                "options": [
                    "Label komunikasi seperti HTTPS, event, atau read/write DB",
                    "Warna acak tanpa arti",
                    "Nomor halaman PDF",
                ],
                "answer": "Label komunikasi seperti HTTPS, event, atau read/write DB",
            },
        ],
        "checklist": [
            "Apakah aktor sudah jelas?",
            "Apakah batas sistem sudah digambar?",
            "Apakah container punya nama dan teknologi?",
            "Apakah setiap panah punya label?",
        ],
    },
    "layered-dan-monolith": {
        "image": "blog/images/layered-monolith.svg",
        "image_alt": "Diagram layered architecture di dalam monolith.",
        "deep_dive": [
            {
                "title": "Layer bukan sekadar folder",
                "body": (
                    "Layer berarti arah dependency dijaga. Presentation boleh memanggil "
                    "application, application memakai domain, dan infrastructure menyediakan "
                    "detail teknis."
                ),
            },
            {
                "title": "Monolith modular",
                "body": (
                    "Monolith tetap bisa sehat jika modulnya jelas. Setiap modul punya batas "
                    "fitur, aturan, dan data yang tidak sembarang disentuh modul lain."
                ),
            },
            {
                "title": "Kapan monolith mulai menyakitkan?",
                "body": (
                    "Tanda awalnya adalah deploy makin menakutkan, satu perubahan kecil "
                    "memecahkan bagian jauh, dan semua fitur harus diskalakan bersama."
                ),
            },
        ],
        "example": {
            "title": "Contoh pembagian",
            "body": (
                "Dalam blog Django ini, template mengurus tampilan, views mengatur alur request, "
                "content.py menyimpan materi, dan static files mengurus CSS serta gambar."
            ),
        },
        "quiz": [
            {
                "question": "Apa manfaat layered architecture?",
                "options": [
                    "Membagi tanggung jawab sistem ke lapisan yang jelas",
                    "Mencampur semua logika ke template",
                    "Menghilangkan kebutuhan testing",
                ],
                "answer": "Membagi tanggung jawab sistem ke lapisan yang jelas",
            },
            {
                "question": "Monolith modular berarti...",
                "options": [
                    "Satu aplikasi, tetapi modul dan batas fiturnya tetap rapi",
                    "Satu file berisi semua fitur",
                    "Setiap tombol menjadi service terpisah",
                ],
                "answer": "Satu aplikasi, tetapi modul dan batas fiturnya tetap rapi",
            },
        ],
        "checklist": [
            "Apakah setiap layer punya tanggung jawab jelas?",
            "Apakah domain logic bebas dari detail tampilan?",
            "Apakah akses data tidak tersebar sembarangan?",
            "Apakah modul bisa diuji tanpa menjalankan seluruh aplikasi?",
        ],
    },
    "pola-arsitektur-kinerja-tinggi": {
        "image": "blog/images/high-performance.svg",
        "image_alt": "Diagram arsitektur kinerja tinggi dengan queue dan worker.",
        "deep_dive": [
            {
                "title": "Backpressure",
                "body": (
                    "Backpressure adalah cara sistem berkata 'tunggu dulu' ketika beban masuk "
                    "lebih cepat daripada kemampuan proses. Queue, rate limit, dan circuit "
                    "breaker adalah contoh mekanismenya."
                ),
            },
            {
                "title": "Event-driven",
                "body": (
                    "Event-driven memisahkan pengirim dan pemroses. Producer menerbitkan event, "
                    "consumer memproses sesuai kapasitas, dan broker membantu menahan lonjakan."
                ),
            },
            {
                "title": "Space-based",
                "body": (
                    "Space-based memakai in-memory data grid untuk menahan data sementara dan "
                    "memprosesnya paralel. Cocok untuk burst besar, tetapi lebih kompleks."
                ),
            },
        ],
        "example": {
            "title": "Contoh mitigasi burst",
            "body": (
                "Pada Dragon Live, request gift masuk lewat load balancer dan rate limit, lalu "
                "event gift masuk ke broker. Ranking sementara dibaca dari cache, sedangkan "
                "settlement saldo diproses worker secara bertahap."
            ),
        },
        "quiz": [
            {
                "question": "Apa fungsi queue pada arsitektur kinerja tinggi?",
                "options": [
                    "Menahan lonjakan pekerjaan agar bisa diproses bertahap",
                    "Menghapus semua request dari pengguna",
                    "Mengubah tampilan website menjadi gelap",
                ],
                "answer": "Menahan lonjakan pekerjaan agar bisa diproses bertahap",
            },
            {
                "question": "Pekerjaan berat sebaiknya dibuat async ketika...",
                "options": [
                    "Tidak harus selesai langsung di request utama",
                    "Harus selalu memblokir halaman pengguna",
                    "Tidak punya hubungan dengan performa",
                ],
                "answer": "Tidak harus selesai langsung di request utama",
            },
        ],
        "checklist": [
            "Apakah endpoint kritis punya rate limit?",
            "Apakah pekerjaan berat bisa dibuat async?",
            "Apakah queue punya DLQ dan retry policy?",
            "Apakah database terlindungi dari lonjakan langsung?",
            "Apakah fitur non-kritis bisa diturunkan sementara?",
        ],
    },
    "modern-data-blueprint": {
        "image": "blog/images/modern-data-blueprint.svg",
        "image_alt": "Diagram alur modern data blueprint dari sumber sampai dashboard.",
        "deep_dive": [
            {
                "title": "Operational data dan analytical data",
                "body": (
                    "Operational data dipakai aplikasi untuk transaksi harian. Analytical data "
                    "dipakai untuk laporan, dashboard, prediksi, dan pengambilan keputusan."
                ),
            },
            {
                "title": "Batch dan streaming",
                "body": (
                    "Batch memproses data pada jadwal tertentu. Streaming memproses data saat "
                    "mengalir. Keduanya bisa dipakai bersama sesuai kebutuhan bisnis."
                ),
            },
            {
                "title": "Governance",
                "body": (
                    "Governance menjaga data tetap dapat dipercaya: siapa pemiliknya, dari mana "
                    "asalnya, siapa yang boleh mengakses, dan kualitasnya seperti apa."
                ),
            },
        ],
        "example": {
            "title": "Contoh alur data",
            "body": (
                "Data transaksi masuk ke database operasional, event transaksi dikirim ke "
                "pipeline, data mentah disimpan di lake, lalu ditransformasi menjadi tabel "
                "analitik untuk dashboard penjualan."
            ),
        },
        "quiz": [
            {
                "question": "Apa perbedaan sederhana operational data dan analytical data?",
                "options": [
                    "Operational untuk transaksi harian, analytical untuk laporan dan analisis",
                    "Operational hanya untuk gambar, analytical hanya untuk CSS",
                    "Keduanya selalu sama dan tidak perlu dibedakan",
                ],
                "answer": "Operational untuk transaksi harian, analytical untuk laporan dan analisis",
            },
            {
                "question": "Governance data membantu memastikan...",
                "options": [
                    "Data jelas pemiliknya, aksesnya, asalnya, dan kualitasnya",
                    "Semua orang bebas melihat data sensitif",
                    "Data tidak perlu dibersihkan",
                ],
                "answer": "Data jelas pemiliknya, aksesnya, asalnya, dan kualitasnya",
            },
        ],
        "checklist": [
            "Apa saja sumber data utama?",
            "Data mana yang butuh real-time?",
            "Di mana data mentah disimpan?",
            "Bagaimana data dibersihkan dan ditransformasi?",
            "Siapa yang boleh mengakses data sensitif?",
        ],
    },
}


for post in POSTS:
    post.update(POST_EXTRAS[post["slug"]])
