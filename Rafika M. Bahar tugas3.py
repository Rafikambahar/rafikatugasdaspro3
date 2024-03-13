def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Membuat salinan dari dictionary pertama
    merged_dict.update(dict2)   # Menggabungkan dictionary kedua ke dalam dictionary pertama
    return merged_dict

# Contoh data dictionary
jadwalDasproIf2 = {
    "Senin": "Pemrograman Dasar",
    "Selasa": "Algoritma dan Struktur Data",
    "Rabu": "Pemrograman Dasar",
}

jadwalDasproIf3 = {
    "Kamis": "Algoritma dan Struktur Data",
    "Jumat": "Pemrograman Dasar",
    "Sabtu": "Pemrograman Web",
}

# Menggabungkan dua data dictionary
result_dict = merge_dicts(jadwalDasproIf2, jadwalDasproIf3)

# Menampilkan hasil
print("Hasil Penggabungan:")
print(result_dict)
