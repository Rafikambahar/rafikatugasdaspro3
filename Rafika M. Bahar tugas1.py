data_dictionary = {
    'manda': '1234',
    'acha': '12345',
    'rafika': '2345',
    'hasna': '123456',
    'nurdalifa': '34567',
    'caca': '5678',
    'ela': '4321',
    'nayla': '54321',
    'dina': '654321',
    'serly': '76543'
}

def login(username, password):
    if username in data_dictionary and data_dictionary[username] == password:
        return f"Selamat datang, {username}!"
    else:
        return "Data yang dimasukkan salah."

username = input("Masukkan username: ")
password = input("Masukkan password: ")

result = login(username, password)
print(result)
