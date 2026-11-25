"""Fungsi bersama untuk notebook langkah 4-6 (data, split, metrik).

Dipakai oleh semua notebook agar split dan metrik identik antara SARIMA dan LSTM.
"""
from pathlib import Path

import numpy as np
import pandas as pd

S = 7                    # periode musiman (harian, pola mingguan)
TEST_FRAC = 0.20         # 20% data terakhir dipakai sebagai test
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "jk_pasien.xlsx"
HASIL_DIR = Path(__file__).resolve().parent.parent / "data" / "hasil"  # ikut ter-ignore (data/*)


def muat_data() -> pd.Series:
    df = pd.read_excel(DATA_PATH)
    df["tanggal"] = pd.to_datetime(df["tanggal"])
    return df.sort_values("tanggal").set_index("tanggal")["jk"].astype(float).asfreq("D")


def split_kronologis(y: pd.Series, test_frac: float = TEST_FRAC):
    """Split berdasarkan urutan waktu (tanpa shuffle). Mengembalikan (train, test)."""
    n_test = int(round(len(y) * test_frac))
    return y.iloc[:-n_test], y.iloc[-n_test:]


def rmse(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    return float(np.sqrt(np.mean((a - b) ** 2)))


def mae(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    return float(np.mean(np.abs(a - b)))


def mape(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    return float(np.mean(np.abs((a - b) / a)) * 100)


def metrik(aktual, prediksi) -> dict:
    return {"RMSE": rmse(aktual, prediksi), "MAE": mae(aktual, prediksi),
            "MAPE (%)": mape(aktual, prediksi)}
