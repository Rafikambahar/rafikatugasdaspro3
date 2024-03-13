def lists_to_dict(keys, values):
    # Pastikan panjang kedua list sama
    if len(keys) == len(values):
        # Menggunakan fungsi zip untuk menggabungkan dua list
        data_dict = dict(zip(keys, values))
        return data_dict
    else:
        print("Error: Panjang list tidak sama.")
        return None

# Contoh data list
keys_list = ["nama", "usia", "kota"]
values_list = ["Rafika", 18, "Ternate"]

# Mengubah dua data list menjadi data dictionary
result_dict = lists_to_dict(keys_list, values_list)

# Menampilkan hasil
if result_dict:
    print("Data Dictionary:")
    print(result_dict)
