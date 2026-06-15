import joblib
import pandas as pd

MODEL_PATH = "models/predict_flag_invoice.pkl"
SCALER_PATH = "models/scaler.pkl"


def load_model():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    return model, scaler


def predict_invoice_risk(input_data):
    model, scaler = load_model()

    input_df = pd.DataFrame(input_data)

    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)

    input_df["Predicted_Flag"] = prediction

    return input_df


if __name__ == "__main__":

    sample_data = {
        "invoice_quantity": [100],
        "invoice_dollars": [15000],
        "Freight": [200],
        "total_item_quantity": [120],
        "total_item_dollars": [14800]
    }

    result = predict_invoice_risk(sample_data)

    print(result)