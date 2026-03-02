
import joblib
from sklearn.ensemble import GradientBoostingClassifier
from app.ml.features import extract_features
import numpy as np

def train_model(samples):
    X = np.array([extract_features(s) for s in samples])
    y = np.random.randint(0, 2, len(samples))
    model = GradientBoostingClassifier()
    model.fit(X, y)
    joblib.dump(model, "risk_model.pkl")
