# LumaCare — Insurance Prediction Demo

LumaCare is a small Streamlit demo that predicts annual medical-insurance charges from six simple features using a Random Forest regression pipeline. It’s a reproducible demo + notebook for training the model and a web UI to interactively get estimates and check model performance.

## Stack
- **Language(s):** Python (primary), Jupyter Notebook
- **Framework / runtime:** Streamlit
- **Notable libraries:** scikit-learn (RandomForest + Pipeline), pandas, numpy, streamlit

## Repository structure
```
app.py                 # Streamlit app (UI pages: Predict, BMI calculator, Model & accuracy, About, Feedback)
medpro.ipynb           # Jupyter notebook: data loading, preprocessing, RandomForest pipeline training, metrics, save model
meddata.csv            # CSV dataset used for training and live accuracy checks
insurance_model.pkl    # Pickled sklearn Pipeline (preprocessor + RandomForest) loaded by app.py
requirements.txt       # Minimal deps: streamlit, pandas, numpy, scikit-learn
.DS_Store              # macOS artifact (can be ignored)
```

## How it fits together
- The notebook (medpro.ipynb) builds a ColumnTransformer + Pipeline with OneHotEncoder and a RandomForestRegressor, trains on meddata.csv, evaluates (R², MAE, RMSE), and saves the pipeline to insurance_model.pkl.
- The Streamlit app (app.py) loads insurance_model.pkl and meddata.csv, offers pages to predict charges from user inputs, compute BMI, and run a live R² accuracy check by scoring the included dataset against the saved model.

## How to run
From a fresh clone, create a virtual environment, install requirements, and run the Streamlit app. Example (POSIX):

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Windows: use `venv\\Scripts\\activate` instead of `source ...`. The app uses the included files `insurance_model.pkl` and `meddata.csv`, so no external data or model download is required. Python 3.8+ is recommended (the notebook metadata shows Python 3.12 but the dependencies are standard).

## Model summary
- Model type: RandomForestRegressor inside an sklearn Pipeline (preprocessor + regressor).
- Features used: age, sex, bmi, children, smoker, region.
- Training dataset: `meddata.csv` (1338 rows, no missing values according to the notebook).
- Example metrics from the notebook: R² ≈ 0.863, MAE ≈ 2528, RMSE ≈ 4604.

## Try asking
- "How exactly was insurance_model.pkl trained — what hyperparameters and preprocessing are in medpro.ipynb?"
- "Can you add input validation and clearer error messages for user inputs in app.py (e.g., enforce realistic BMI/age ranges)?"
- "Can we expose feature importances or a CSV of predictions vs actuals in the app's Model & accuracy page?"

---

If you'd like, I can also:
- Add a short Hindi description at the top.
- Update app.py to improve input validation or add a feature-importance view.
- Open a PR with suggested code changes. Just tell me which you'd prefer.
