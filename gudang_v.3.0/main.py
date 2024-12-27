import mysql.connector

db = mysql.connector.connect(
    host ="localhost",
    user="root",
    passwd="",
    database="gudang"
)

cursor = db.cursor()

# Fungsi untuk memasukkan barang
def insert_barang(nama_barang, stok_barang, tgl_masuk, expired):
    query = "INSERT INTO barang (nama_barang, stok_barang, tgl_masuk, expired) VALUES (%s, %s, %s, %s)"
    data = (nama_barang, stok_barang, tgl_masuk, expired)
    cursor.execute(query, data)
    db.commit()

# Fungsi untuk mengambil barang
def get_barang():
    query = "SELECT * FROM barang"
    cursor.execute(query)
    return cursor.fetchall()

# Fungsi untuk mengupdate stok barang
def update_stok(id, stok_barang):
    query = "UPDATE barang SET stok_barang = %s WHERE id = %s"
    data = (stok_barang, id)
    cursor.execute(query, data)
    db.commit()


while True:
    print('''
        1. Tambah Barang
        2. mengambil
        3. mengupdate stok
        4. melihat data 
        0. keluar
    ''')
    pilih = int(input('silahkan pilih nomor intruksi: '))
    if pilih == 1:
        nama_barang = input('masukkan nama barang: ')
        stok_barang = int(input('masukkan stok barang: '))
        tgl_masuk = input('masukkan tanggal masuk: ')
        expired = input('masukkan expired: ')
        insert_barang(nama_barang, stok_barang, tgl_masuk, expired)
    elif pilih == 2:
        get_barang()
    elif pilih == 3:
        id = int(input('masukkan id barang: '))
        stok_barang = int(input('masukkan stok barang: '))
        update_stok(id, stok_barang)
    elif pilih == 4:
        get_barang()
    elif pilih == 0:
        cursor.close()
        db.close()
        break

