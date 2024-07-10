# List data nilai mahasiswa
listdata_nilai = [
    ["Mahasiswa 1", "Algoritma dan Struktur Data", 90], ["Mahasiswa 1", "matematika numerik", 80],
    ["Mahasiswa 2", "Algoritma dan Struktur Data", 50], ["Mahasiswa 2", "matematika numerik", 60],
    ["Mahasiswa 3", "Algoritma dan Struktur Data", 65], ["Mahasiswa 3", "matematika numerik", 70]
]
nilai_mahasiswa = {}
for data in listdata_nilai:
    mahasiswa = data[0]
    nilai = data[2]
    
    if mahasiswa not in nilai_mahasiswa:
        nilai_mahasiswa[mahasiswa] = {"total_nilai": 0, "jumlah_mata_kuliah": 0}
    
    nilai_mahasiswa[mahasiswa]["total_nilai"] += nilai
    nilai_mahasiswa[mahasiswa]["jumlah_mata_kuliah"] += 1

for mahasiswa, nilai in nilai_mahasiswa.items():
    rata_rata = nilai["total_nilai"] / nilai["jumlah_mata_kuliah"]
    print(f"Rata-rata nilai {mahasiswa}: {rata_rata:.2f}")
