# House Price Prediction App

This repository contains a Streamlit app for predicting house prices.

## Quick steps to run locally (Windows PowerShell)

1. Activate the virtual environment:

```powershell
C:\HP\mlev\Scripts\Activate.ps1
```

2. Install requirements (only if not already installed):

```powershell
python -m pip install -r requirements.txt
```

3. Run the Streamlit app:

```powershell
python -m streamlit run app.py
```

4. Open http://localhost:8501 in your browser to use the UI.

--

If you have a file called `model.pkl`, ensure it's in the repo root (it is expected by the app). If the model relies on additional packages, add them to `requirements.txt`.
