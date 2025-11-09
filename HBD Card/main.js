console.log("vell")


let namaPengguna; // Deklarasikan variabel nama di luar perulangan

// Perulangan akan terus berjalan selama 'nama' masih kosong atau null
while (!namaPengguna) {
    // Tampilkan prompt untuk meminta nama
    namaPengguna = prompt("Nama harus diisi. Silakan masukkan nama Anda.");

    // Cek jika pengguna menekan tombol 'Batal'
    if (namaPengguna === null) {
        alert("Anda membatalkan pengisian. Program akan dihentikan.");
        break; // Keluar dari perulangan
    }

    // Trim spasi di awal dan akhir untuk memastikan tidak hanya spasi kosong
    namaPengguna = namaPengguna.trim();
}

// Jika perulangan selesai (nama sudah terisi), tampilkan pesan
if (namaPengguna) {
    alert("Halo, " + namaPengguna + "!");
}
window.alert( namaPengguna + ', ada sesuatu nih buat kamu dari Vandi semoga suka yaa')