try:
    # Membaca file tanpa 'with'
    print(3*"=", " Membaca file txt ", 3*"=")
    with open("data.txt", mode="r") as file:
        print(f"status read : {file.readable()}")
        print(f"status write : {file.writable()}")
        print(file.read())  # Membaca seluruh isi file
    print(f"apakah file sudah diclose : {file.closed}")

    # Membaca file dengan 'with'
    print("\n", 3*"=", " Membaca file txt dengan with", 3*"=")
    with open("data.txt", mode="r") as file:
        for line in file:
            print(line.strip())  # Membaca file per baris dan hilangkan newline
    print(f"apakah file sudah diclose : {file.closed}")
    
except FileNotFoundError:
    print("File 'data.txt' tidak ditemukan. Pastikan file berada di lokasi yang benar.")
