# Peramalan Jumlah Kunjungan Pasien: SARIMA vs LSTM

Tugas Analisis Deret Waktu (ADW), Semester 5. Membandingkan SARIMA dan LSTM pada data
harian jumlah kunjungan pasien rumah sakit.

## Struktur

```
.
├── notebooks/
│   ├── cek_stasioneritas.ipynb # Langkah 1-2: eksplorasi & uji stasioneritas
│   ├── acf_pacf_kandidat.ipynb # Langkah 3: ACF/PACF & kandidat model SARIMA
│   ├── 04_split_sarima.ipynb   # Langkah 4: split train/test, estimasi & pilih SARIMA
│   ├── 05_lstm.ipynb           # Langkah 5: LSTM
│   ├── 06_perbandingan.ipynb   # Langkah 6: perbandingan RMSE/MAE/MAPE + uji DM
│   └── common.py               # split, metrik, dan path bersama
├── requirements.txt
└── README.md
```

## Cara menjalankan

1. `pip install -r requirements.txt`
2. Buat folder data lalu taruh file `jk_pasien.xlsx`.
3. Jalankan notebook di `notebooks/` berurutan (04 → 05 → 06). Notebook 04 dan 05 menyimpan prediksi ke `data/hasil/` (ikut ter-ignore git) yang dibaca notebook 06.

## Progres

- [x] 1. Eksplorasi data
- [x] 2. Uji stasioneritas (ADF & KPSS), penentuan d dan D
- [x] 3. ACF/PACF dan kandidat model SARIMA (7 kandidat, semua D=1, Q=1; estimasi setelah split)
- [x] 4. Pembagian train/test kronologis 80/20 (1106/276 hari), estimasi 7 kandidat pada train, terpilih SARIMA(1,0,0)(0,1,1)[7]
- [x] 5. LSTM (window 28, 32 unit, ensemble 5 seed, validasi = ujung train)
- [x] 6. Perbandingan RMSE/MAE/MAPE: SARIMA 226,2 vs LSTM 233,6 (RMSE), selisih tidak signifikan (Diebold-Mariano p = 0,21)
