# Peramalan Jumlah Kunjungan Pasien: SARIMA vs LSTM

Tugas Analisis Deret Waktu (ADW), Semester 5. Membandingkan SARIMA dan LSTM pada data
harian jumlah kunjungan pasien rumah sakit.

## Struktur

```
.
├── data/                       # dataset (di-gitignore)
│   └── README.md               # cara menaruh data
├── notebooks/
│   └── cek_stasioneritas.ipynb # Langkah 1-2: eksplorasi & uji stasioneritas
├── requirements.txt
└── README.md
```

## Cara menjalankan

1. `pip install -r requirements.txt`
2. Taruh `jk_pasien.xlsx` di folder `data/`.
3. Jalankan notebook di `notebooks/` dari atas ke bawah.

## Progres

- [x] 1. Eksplorasi data
- [x] 2. Uji stasioneritas (ADF & KPSS), penentuan d dan D
- [ ] 3. ACF/PACF dan kandidat model SARIMA
- [ ] 4. Pembagian train/test
- [ ] 5. LSTM
- [ ] 6. Perbandingan RMSE/MAE/MAPE