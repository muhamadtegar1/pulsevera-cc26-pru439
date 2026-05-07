"""
Pulsevera — ML Inference API
FastAPI endpoint untuk prediksi risiko penyakit jantung.
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
import pandas as pd
import numpy as np
import joblib
import os

app = FastAPI(
    title="Pulsevera ML API",
    description="API prediksi risiko penyakit jantung — Pulsevera CC26-PRU439",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Load model saat startup ───────────────────────────────────────
# TODO: Ganti path sesuai nama file model hasil training
ML_MODEL_PATH = "models/pulsevera_ml_model.pkl"

ml_model = None

@app.on_event("startup")
def load_model():
    global ml_model
    # TODO: Load model ML (joblib) dan/atau DL (keras) di sini
    pass


# ── Schema ────────────────────────────────────────────────────────
class UserInput(BaseModel):
    sex: str                    = Field(..., example="Male")
    age_category: int           = Field(..., ge=1, le=13, example=7)
    height_meters: float        = Field(..., ge=1.0, le=2.5, example=1.70)
    weight_kg: float            = Field(..., ge=30, le=200, example=70.0)
    sleep_hours: float          = Field(..., ge=1, le=14, example=7.0)
    physical_activities: str    = Field(..., example="Yes")
    smoker_status: str          = Field(..., example="Never")
    alcohol: str                = Field(..., example="No")
    general_health: str         = Field(..., example="Good")
    diabetes: Optional[str]     = Field(default="No", example="No")

class PredictionResult(BaseModel):
    risk_score: float           # probabilitas 0.0–1.0
    risk_label: str             # "Rendah" / "Sedang" / "Tinggi"
    top_risk_factors: list      # ["AgeCategory", "BMI", "SmokerStatus"]
    recommendations: list       # ["Tingkatkan aktivitas fisik", ...]


# ── Preprocessing ─────────────────────────────────────────────────
def preprocess_user_input(user_input: dict) -> pd.DataFrame:
    """
    Konversi 10 field input user ke format fitur model.

    TODO:
    - Sesuaikan encoding dengan pipeline di notebook 03_feature_engineering.ipynb
    - Isi FEATURE_ORDER dengan pd.read_csv('X_train.csv').columns.tolist()
    - Tambahkan feature engineering yang konsisten dengan training (BMI, IsObese, dll.)
    - Pastikan urutan kolom identik dengan X_train
    """
    pass


def get_top_risk_factors(input_df: pd.DataFrame, top_n: int = 3) -> list:
    """
    TODO:
    - Gunakan SHAP (shap.TreeExplainer) untuk model ML
    - Atau gunakan feature importance / gradient untuk model DL
    - Return list nama fitur dengan kontribusi risiko tertinggi
    """
    pass


def generate_recommendations(user_input: dict, risk_factors: list) -> list:
    """
    TODO:
    - Buat rekomendasi gaya hidup berdasarkan risk_factors dan input user
    - Contoh: jika PhysicalActivities=No → sarankan olahraga rutin
    """
    pass


# ── Endpoints ─────────────────────────────────────────────────────
@app.get("/health")
async def health_check():
    return {"status": "ok", "model_loaded": ml_model is not None}


@app.post("/api/v1/predict", response_model=PredictionResult)
async def predict(user_input: UserInput):
    if ml_model is None:
        raise HTTPException(status_code=503, detail="Model belum siap. Jalankan training terlebih dahulu.")

    # TODO:
    # 1. Panggil preprocess_user_input(user_input.dict())
    # 2. Jalankan prediksi: ml_model.predict_proba(input_df)
    # 3. Tentukan risk_label berdasarkan threshold (misal: <0.3 Rendah, <0.6 Sedang, ≥0.6 Tinggi)
    # 4. Panggil get_top_risk_factors(input_df)
    # 5. Panggil generate_recommendations(input_dict, top_factors)
    # 6. Return PredictionResult(...)
    raise HTTPException(status_code=501, detail="Endpoint belum diimplementasikan.")
