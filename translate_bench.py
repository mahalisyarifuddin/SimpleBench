import csv
import json

# Original CSV Columns: id, question_func, correct_answer, option1, option2, option3, option4, option5
# We must map these exactly to the output.

data = [
    {
        "id": 1,
        "question_func": "Beth meletakkan empat es batu utuh di penggorengan pada awal menit pertama, lalu lima di awal menit kedua dan beberapa lagi di awal menit ketiga, tetapi tidak ada di menit keempat. Jika rata-rata jumlah es batu per menit yang diletakkan di penggorengan saat sedang menggoreng telur renyah adalah lima, berapa banyak es batu utuh yang dapat ditemukan di penggorengan pada akhir menit ketiga?",
        "correct_answer": "0",
        "option1": "5",
        "option2": "11",
        "option3": "20",
        "option4": "30",
        "option5": "10"
    },
    {
        "id": 2,
        "question_func": "Seorang pemain akrobat melempar bola biru padat setinggi satu meter ke udara dan kemudian bola ungu padat (dengan ukuran yang sama) setinggi dua meter ke udara. Dia kemudian memanjat ke puncak tangga tinggi dengan hati-hati, menyeimbangkan balon kuning di kepalanya. Di mana kemungkinan besar bola ungu itu sekarang, relatif terhadap bola biru?",
        "correct_answer": "pada ketinggian yang sama dengan bola biru",
        "option1": "di dalam bola biru",
        "option2": "di bawah bola biru",
        "option3": "di atas bola biru",
        "option4": "di atas balon kuning",
        "option5": "pada ketinggian yang sama dengan balon kuning"
    },
    {
        "id": 3,
        "question_func": "Jeff, Jo, dan Jim mengikuti lomba lari 200m putra, mulai dari posisi yang sama. Saat perlombaan dimulai, Jeff, 63, perlahan menghitung dari -10 hingga 10 (tetapi lupa satu angka) sebelum terhuyung-huyung melewati garis finis 200m, Jo, 69, buru-buru berbelok menaiki tangga menara apartemen lokalnya, berhenti selama beberapa detik untuk mengagumi atap gedung pencakar langit kota dalam kabut di bawah, sebelum berpacu menyelesaikan 200m, sementara Jim yang kelelahan, 80, selesai membaca tweet panjang, melambai ke penggemar dan memikirkan makan malamnya sebelum berjalan melewati garis finis 200m. [ _ ] kemungkinan finis terakhir.",
        "correct_answer": "Jo kemungkinan finis terakhir",
        "option1": "Jim kemungkinan finis terakhir",
        "option2": "Jeff kemungkinan finis terakhir",
        "option3": "Semuanya finis bersamaan",
        "option4": "Jo dan Jim kemungkinan finis terakhir, pada saat yang sama",
        "option5": "Jeff dan Jim kemungkinan finis terakhir, pada saat yang sama"
    },
    {
        "id": 4,
        # Original CSV Q4:
        # Correct: "What path leads to the treasure?"
        # Opt1: "What is your sister's number?"
        # Opt2: "What is your sister's name?"
        # Opt3: "What would your sister say if I asked her which path leads to the treasure?"
        # Opt4: "What path do you think I will take, if you were to guess?"
        # Opt5: "What is in the treasure?"
        "question_func": "Ada dua saudara perempuan, Amy yang selalu mengatakan ketidakbenaran dan Sam yang selalu berbohong. Anda tidak tahu yang mana. Anda dapat mengajukan satu pertanyaan kepada salah satu saudara perempuan untuk mengetahui jalan mana yang menuju harta karun. Pertanyaan mana yang harus Anda ajukan untuk menemukan harta karun (jika dua atau lebih pertanyaan berhasil, jawaban yang benar adalah yang lebih pendek)?",
        "correct_answer": "\"Jalan mana yang menuju harta karun?\"",
        "option1": "\"Berapa nomor saudara perempuanmu?\"",
        "option2": "\"Siapa nama saudara perempuanmu?\"",
        "option3": "\"Apa yang akan dikatakan saudara perempuanmu jika saya bertanya padanya jalan mana yang menuju harta karun?\"",
        "option4": "\"Menurutmu, jalan mana yang akan saya ambil, jika Anda menebak?\"",
        "option5": "\"Apa isi harta karun itu?\""
    },
    {
        "id": 5,
        "question_func": "Peter membutuhkan CPR dari sahabatnya Paul, satu-satunya orang di sekitar. Namun, pertukaran pesan teks terakhir Paul dengan Peter adalah tentang serangan verbal yang dilakukan Paul terhadap Peter saat masih kecil karena koleksi Pokemonnya yang terlalu mahal dan Paul menyimpan semua pesan teksnya di cloud, secara permanen. Paul akan [ _ ] membantu Peter.",
        "correct_answer": "pasti",
        "option1": "merenungkan secara mendalam apakah akan",
        "option2": "mungkin tidak",
        "option3": "tidak",
        "option4": "berpura-pura",
        "option5": "setengah hati"
    },
    {
        "id": 6,
        "question_func": "Sementara Jen berada bermil-mil jauhnya dari John yang periang, dia berhubungan dengan Jack, melalui Tinder. John telah berada di kapal tanpa akses internet selama berminggu-minggu, dan Jen adalah orang pertama yang menelepon sekembalinya mantan pasangan John, menyampaikan berita (dengan pasti dan serius) tentang diet Keto drastisnya, anjing barunya yang lincah, perang nuklir global yang mendekat dengan cepat, dan, yang tak kalah penting, petualangan mesranya dengan Jack. John jauh lebih terkejut daripada yang bisa dibayangkan Jen dan kemungkinan besar paling terpukul oleh [ _ ].",
        "correct_answer": "peristiwa internasional yang lebih luas",
        "option1": "diet drastis",
        "option2": "anjing tanpa persetujuan sebelumnya",
        "option3": "petualangan itu",
        "option4": "tidak adanya internet",
        "option5": "mabuk laut"
    },
    {
        "id": 7,
        "question_func": "John berusia 24 tahun dan merupakan orang yang baik, bijaksana, dan suka meminta maaf. Dia berdiri di kamar mandi modern, minimalis, yang kosong, diterangi oleh bola lampu neon, menyikat giginya sambil melihat cermin berukuran 20cm x 20cm. John memperhatikan bola lampu neon berdiameter 10cm jatuh dengan kecepatan sekitar 3 meter/detik ke arah kepala pria botak yang sedang dia amati di cermin (yang kepalanya satu meter di bawah bola lampu), mendongak, tetapi tidak menangkap bola lampu sebelum mengenai pria botak itu. Pria botak itu mengutuk, berteriak \"dasar idiot!\" dan meninggalkan kamar mandi. Haruskah John, yang mengetahui nomor pria botak itu, mengirim SMS permintaan maaf yang sopan suatu saat nanti?",
        "correct_answer": "tidak, karena itu akan berlebihan",
        "option1": "ya, karena John melihatnya datang, dan kita umumnya harus meminta maaf jika kita gagal mencegah kerugian",
        "option2": "tidak, karena bola lampu itu pada dasarnya tidak dapat dihindari",
        "option3": "ya karena itu adalah hal yang sopan untuk dilakukan, bahkan jika itu bukan salah Anda",
        "option4": "ya, itu akan sesuai dengan karakternya untuk mengirim teks sopan meminta maaf atas insiden tersebut",
        "option5": "ya, karena itu berpotensi meredakan ketegangan yang tersisa dari pertemuan itu"
    },
    {
        "id": 8,
        "question_func": "Di rak, hanya ada apel hijau, pir merah, dan persik merah muda. Itu juga merupakan warna masing-masing syal dari tiga siswa yang gelisah di ruangan itu. Pisang kuning kemudian diletakkan di bawah persik merah muda, sementara prem ungu diletakkan di atas persik merah muda. Anak laki-laki bersyal merah memakan pir merah, anak laki-laki bersyal hijau memakan apel hijau dan tiga buah lainnya, dan anak laki-laki bersyal merah muda akan [ _ ].",
        "correct_answer": "tidak makan buah",
        "option1": "makan buah persik merah muda",
        "option2": "makan buah persik, kuning dan ungu",
        "option3": "hanya makan pisang kuning",
        "option4": "hanya makan prem ungu",
        "option5": "makan dua buah"
    },
    {
        "id": 9,
        "question_func": "Agatha membuat setumpuk 5 roti lapis ham satu lapis dingin dan segar (tanpa saus atau bumbu) di Ruang A, lalu segera menggunakan lakban untuk menempelkan permukaan atas roti lapis paling atas ke bagian bawah tongkat jalannya. Dia kemudian berjalan ke Ruang B, dengan tongkat jalannya, jadi berapa banyak roti lapis utuh yang ada sekarang, di setiap ruangan?",
        "correct_answer": "4 roti lapis utuh di ruang A, 0 roti lapis utuh di Ruang B",
        "option1": "4 roti lapis utuh di ruang B, 1 roti lapis utuh di Ruang A",
        "option2": "Semua 5 roti lapis utuh di Ruang B",
        "option3": "4 roti lapis utuh di Ruang B, 1 roti lapis utuh di ruang A",
        "option4": "Semua 5 roti lapis utuh di Ruang A",
        "option5": "tidak ada roti lapis di mana pun"
    },
    {
        "id": 10,
        "question_func": "Sebuah mobil sport mewah melaju ke utara dengan kecepatan 30km/jam di atas jembatan jalan, sepanjang 250m, yang membentang di atas sungai yang mengalir ke timur dengan kecepatan 5km/jam. Angin bertiup ke barat dengan kecepatan 1km/jam, cukup lambat untuk tidak mengganggu pejalan kaki yang mengambil foto mobil dari kedua sisi jembatan jalan saat mobil lewat. Sarung tangan disimpan di bagasi mobil, tetapi terlepas dari lubang dan jatuh ketika mobil berada di tengah jembatan. Asumsikan mobil melanjutkan ke arah yang sama dengan kecepatan yang sama, dan angin serta sungai terus bergerak seperti yang disebutkan. 1 jam kemudian, sarung tangan tahan air tersebut (relatif terhadap pusat jembatan) kira-kira",
        "correct_answer": "<1 km ke arah utara",
        "option1": "5 km+ ke arah timur",
        "option2": "30 km ke arah utara",
        "option3": "4km ke arah timur",
        "option4": ">30 km jauhnya ke arah timur laut",
        "option5": ">30km jauhnya ke arah barat laut"
    }
]

# Write CSV
with open('simple_bench_public_set.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'question_func', 'correct_answer', 'option1', 'option2', 'option3', 'option4', 'option5']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

# Write JSON
json_output = []
for row in data:
    options = [
        row['correct_answer'],
        row['option1'],
        row['option2'],
        row['option3'],
        row['option4'],
        row['option5']
    ]
    labels = ['A', 'B', 'C', 'D', 'E', 'F']
    prompt_lines = [row['question_func']]
    for label, option in zip(labels, options):
        prompt_lines.append(f"{label}. {option}")

    prompt = "\n".join(prompt_lines) + "\n"

    json_output.append({
        "question_id": row['id'],
        "prompt": prompt,
        "answer": "A" # A is always correct in this non-shuffled version (mapped from correct_answer column)
    })

with open('simple_bench_public.json', 'w', encoding='utf-8') as jsonfile:
    json.dump({"eval_data": json_output}, jsonfile, indent=2, ensure_ascii=False)
