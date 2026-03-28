import streamlit as st
import pandas as pd
import joblib

# Mapping class numbers to AQI category names
category_map = {
    0: "Good",
    1: "Satisfactory",
    2: "Moderate",
    3: "Poor",
    4: "Very Poor",
    5: "Severe"
}

st.set_page_config(page_title="AQI Predictor", layout="wide")
st.title("🌫️ Air Quality Index (AQI) Prediction Application")
st.markdown("Upload AQI data file (.xls, .xlsx, or .csv) and get category predictions.")

# Load model
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

uploaded_file = st.file_uploader("📤 Upload AQI data", type=["xls", "xlsx", "csv"])

if uploaded_file is not None:
    try:
        # Read uploaded file
        filename = uploaded_file.name.lower()
        if filename.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif filename.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file, engine="openpyxl")
        elif filename.endswith(".xls"):
            df = pd.read_excel(uploaded_file, engine="xlrd")
        else:
            st.error("Unsupported file type.")
            st.stop()

        st.subheader("📊 Uploaded Data Preview")
        st.dataframe(df, use_container_width=True)  # updated

        # ✅ After df is loaded, now we can safely access it
        # Save City and Date if they exist
        if 'City' in df.columns and 'Date' in df.columns:
            output_df = df[['City', 'Date']].copy()
        else:
            output_df = pd.DataFrame()

        # Expected model input features
        required_features = ['PM2.5', 'PM10', 'NO', 'NO2', 'NOx', 'NH3',
                             'CO', 'SO2', 'O3', 'Benzene', 'Toluene', 'Xylene']

        # Check if all required features exist
        missing = [col for col in required_features if col not in df.columns]
        if missing:
            st.error(f"❌ Missing required columns: {', '.join(missing)}")
            st.stop()

        # Extract and clean feature data
        features = df[required_features].copy()
        features.fillna(features.mean(numeric_only=True), inplace=True)

        # Predict
        predictions = model.predict(features)
        prediction_labels = [category_map.get(p, "Unknown") for p in predictions]

        # Combine results
        output_df["Predicted AQI Category"] = prediction_labels

        st.subheader("✅ Detailed Predictions")
        st.dataframe(output_df)

        # Allow CSV download
        csv = output_df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download Predictions", csv, "aqi_predictions.csv", "text/csv")

    except Exception as e:
        st.error(f"❌ Error: {e}")
else:
    st.info("Please upload a `.xls`, `.xlsx`, or `.csv` file.")

st.markdown(
    """
    <style>
    .custom-footer {
        position: fixed;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 14px;
        color: #6c757d;
        z-index: 100;
        text-align: center;
    }

    @media screen and (max-width: 768px) {
        .custom-footer {
            font-size: 12px;
            bottom: 8px;
        }
    }
    </style>
    <div class="custom-footer">© 2025 Developed by <strong>MUKESH G</strong></div>
    """,
    unsafe_allow_html=True
)
