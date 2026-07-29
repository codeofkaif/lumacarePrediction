import pickle
from pathlib import Path

import pandas as pd
import streamlit as st


APP_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="LumaCare | Insurance Intelligence",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_resource
def load_model():
    with open(APP_DIR / "insurance_model.pkl", "rb") as file:
        return pickle.load(file)


@st.cache_data
def load_data():
    return pd.read_csv(APP_DIR / "meddata.csv")


model = load_model()
data = load_data()


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&display=swap');

    :root { --ink: #f8fbff; --muted: #cbd7e8; --glass: rgba(11, 24, 49, .42); --line: rgba(255,255,255,.22); --aqua: #8ff4ea; --violet: #aeb4ff; }
    html, body, [class*="css"] { font-family: "Google Sans", "Product Sans", Arial, sans-serif; }
    .stApp { background: #07152d; color: var(--ink); overflow-x: hidden; }
    .stApp::before, .stApp::after { content:""; position: fixed; pointer-events: none; z-index: 0; width: 52vw; height: 52vw; border-radius: 50%; filter: blur(65px); opacity: .7; animation: drift 18s ease-in-out infinite alternate; }
    .stApp::before { background: radial-gradient(circle, #16b8d7, transparent 68%); left: -20vw; top: -25vw; }
    .stApp::after { background: radial-gradient(circle, #8b5cf6, transparent 68%); right: -22vw; bottom: -28vw; animation-delay: -9s; }
    @keyframes drift { to { transform: translate(12vw, 8vw) scale(1.18); } }
    .main .block-container { position: relative; z-index: 1; max-width: 1220px; padding: 2.1rem 2rem 4rem; }
    [data-testid="stSidebar"] { background: rgba(5, 16, 36, .73); border-right: 1px solid var(--line); backdrop-filter: blur(24px); }
    [data-testid="stSidebar"] * { color: var(--ink) !important; }
    [data-testid="stSidebar"] .stRadio label { padding: .55rem .65rem; border-radius: 14px; transition: .2s; }
    [data-testid="stSidebar"] .stRadio label:hover { background: rgba(255,255,255,.09); }
    .brand { font-size: 1.5rem; font-weight: 700; letter-spacing: -.8px; margin: .35rem 0 .1rem; }
    .brand-mark { display:inline-grid; place-items:center; width:33px; height:33px; margin-right:8px; border:1px solid rgba(255,255,255,.45); border-radius: 11px; background:linear-gradient(135deg,rgba(143,244,234,.55),rgba(174,180,255,.4)); }
    .eyebrow { color: var(--aqua); font-size:.76rem; font-weight:700; letter-spacing:.16em; text-transform:uppercase; }
    .hero { position:relative; overflow:hidden; padding: 2.3rem 2.5rem; border: 1px solid var(--line); border-radius: 32px; background: linear-gradient(115deg,rgba(255,255,255,.15),rgba(255,255,255,.045)); box-shadow: 0 22px 60px rgba(0,0,0,.25), inset 0 1px 1px rgba(255,255,255,.3); backdrop-filter: blur(26px); }
    .hero h1 { margin:.35rem 0 .55rem; max-width:720px; color:white; font-size:clamp(2.25rem,5vw,4.4rem); line-height:.99; letter-spacing:-.065em; }
    .hero p { max-width:590px; color:var(--muted); font-size:1.06rem; line-height:1.6; }
    .motif { position:absolute; right:4%; top:0; width:250px; height:100%; opacity:.38; background-image: radial-gradient(circle at 13px 13px, #a9fff4 0 2px, transparent 2.7px), linear-gradient(45deg, transparent 45%, #d1d7ff 46% 54%, transparent 55%); background-size:44px 44px; transform:rotate(-10deg); mask-image:linear-gradient(90deg,transparent,black); }
    .glass { border: 1px solid var(--line); border-radius: 27px; background: var(--glass); box-shadow: inset 0 1px 1px rgba(255,255,255,.2), 0 20px 50px rgba(0,0,0,.18); backdrop-filter: blur(22px); padding: 1.55rem; }
    .section-title { margin:0 0 .25rem; font-size:1.55rem; letter-spacing:-.04em; }
    .section-copy { color:var(--muted); margin:0 0 1.2rem; line-height:1.55; }
    .mini-card { padding:1.15rem; border:1px solid rgba(255,255,255,.16); border-radius:20px; background:rgba(255,255,255,.07); min-height:110px; }
    .mini-card strong { font-size:1.45rem; display:block; margin-top:.35rem; }
    div[data-baseweb="input"] > div, div[data-baseweb="select"] > div { background:rgba(255,255,255,.10) !important; border:1px solid rgba(255,255,255,.22) !important; border-radius:999px !important; color:white !important; box-shadow: inset 0 1px 1px rgba(255,255,255,.12); }
    div[data-baseweb="input"] input { color:white !important; }
    div[data-baseweb="select"] span { color:white !important; }
    label, .stNumberInput label, .stSelectbox label { color:#edf4ff !important; font-weight:500 !important; }
    .stButton > button, .stFormSubmitButton > button { border:1px solid rgba(255,255,255,.35) !important; border-radius:999px !important; color:#07152d !important; background:linear-gradient(110deg,#a8fff3,#bac5ff 53%,#a8fff3) !important; background-size:200% 100% !important; font-weight:700 !important; letter-spacing:.01em; min-height:48px; box-shadow:0 10px 25px rgba(75,225,225,.2); transition:transform .2s, box-shadow .2s, background-position .5s !important; }
    .stButton > button:hover, .stFormSubmitButton > button:hover { transform:translateY(-2px); box-shadow:0 15px 32px rgba(75,225,225,.35); background-position:100% 0 !important; }
    .result { margin-top:1.25rem; text-align:center; padding:1.35rem; border-radius:22px; color:#fff; background:linear-gradient(135deg,rgba(50,228,208,.28),rgba(146,125,255,.3)); border:1px solid rgba(190,255,248,.38); }
    .result-number { font-size:2.45rem; font-weight:700; letter-spacing:-.06em; }
    .caption { color:var(--muted); font-size:.9rem; }
    .bmi-value { font-size:4.6rem; line-height:1; font-weight:700; letter-spacing:-.08em; color:var(--aqua); }
    .pie { width:210px; height:210px; margin:1rem auto; border-radius:50%; background:conic-gradient(#9cf7eb 0deg var(--score), rgba(255,255,255,.12) var(--score) 360deg); display:grid; place-items:center; box-shadow:0 0 38px rgba(119,236,220,.22); }
    .pie::after { content:attr(data-label); white-space:pre; display:grid; place-items:center; text-align:center; width:160px; height:160px; border-radius:50%; background:#102443; color:white; font-weight:700; line-height:1.25; }
    .metric-line { padding:.8rem 0; border-bottom:1px solid rgba(255,255,255,.12); color:var(--muted); }
    .metric-line b { float:right; color:white; }
    .stTextArea textarea { background:rgba(255,255,255,.10) !important; border:1px solid rgba(255,255,255,.22) !important; border-radius:22px !important; color:white !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("<div class='brand'><span class='brand-mark'>✚</span>LumaCare</div>", unsafe_allow_html=True)
    st.caption("MEDICAL COST INTELLIGENCE")
    page = st.radio("Navigate", ["Predict", "BMI calculator", "Model & accuracy", "About", "Feedback"], label_visibility="collapsed")
    st.markdown("<br><div class='caption'>A calmer way to explore your insurance estimate.</div>", unsafe_allow_html=True)


def hero(title, copy, eyebrow):
    st.markdown(f"""<section class='hero'><div class='motif'></div><div class='eyebrow'>{eyebrow}</div><h1>{title}</h1><p>{copy}</p></section>""", unsafe_allow_html=True)


if page == "Predict":
    hero("A clearer view of care costs.", "Enter a few health and lifestyle details to receive a personalised estimated annual medical-insurance charge.", "Insurance estimate")
    st.write("")
    form_col, info_col = st.columns([1.55, .85], gap="large")
    with form_col:
        st.markdown("<div class='glass'><h2 class='section-title'>Your details</h2><p class='section-copy'>All fields are used only to create this estimate.</p>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", 18, 100, 25)
            bmi = st.number_input("BMI", 10.0, 60.0, 26.5, step=.1)
            children = st.number_input("Number of children", 0, 10, 0)
        with col2:
            sex = st.selectbox("Gender", ["female", "male"])
            smoker = st.selectbox("Do you smoke?", ["no", "yes"])
            region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])
        predict = st.button("Reveal my estimate ✦", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        if predict:
            sample = pd.DataFrame({"age": [age], "sex": [sex], "bmi": [bmi], "children": [children], "smoker": [smoker], "region": [region]})
            prediction = model.predict(sample)[0]
            st.markdown(f"<div class='result'><div class='caption'>ESTIMATED ANNUAL INSURANCE COST</div><div class='result-number'>${prediction:,.2f}</div><div class='caption'>This is a machine-learning estimate, not a quote.</div></div>", unsafe_allow_html=True)
    with info_col:
        st.markdown("<div class='glass'><div class='eyebrow'>How it works</div><h2 class='section-title'>Six simple signals.</h2><p class='section-copy'>Age, BMI, children, gender, smoking status and region are interpreted by the trained model.</p><div class='mini-card'><span class='caption'>MODEL</span><strong>Random Forest</strong></div><br><div class='mini-card'><span class='caption'>OUTPUT</span><strong>Annual cost</strong></div></div>", unsafe_allow_html=True)

elif page == "BMI calculator":
    hero("Find your BMI in a moment.", "BMI is a screening measure that compares weight to height. It is useful context, but it does not replace medical advice.", "Wellness tool")
    st.write("")
    left, right = st.columns([1.15, .85], gap="large")
    with left:
        st.markdown("<div class='glass'><h2 class='section-title'>BMI calculator</h2><p class='section-copy'>Use metric units for an instant calculation.</p>", unsafe_allow_html=True)
        height, weight = st.columns(2)
        with height: height_cm = st.number_input("Height (cm)", 80.0, 250.0, 170.0, step=.1)
        with weight: weight_kg = st.number_input("Weight (kg)", 20.0, 300.0, 65.0, step=.1)
        calculate = st.button("Calculate BMI", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with right:
        if calculate:
            bmi_value = weight_kg / ((height_cm / 100) ** 2)
            if bmi_value < 18.5: category = "Underweight"
            elif bmi_value < 25: category = "Healthy range"
            elif bmi_value < 30: category = "Overweight"
            else: category = "Obesity range"
            st.markdown(f"<div class='glass' style='text-align:center'><div class='caption'>YOUR BMI</div><div class='bmi-value'>{bmi_value:.1f}</div><h3>{category}</h3><p class='section-copy'>For adults, a BMI of 18.5–24.9 is commonly considered the healthy range.</p></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='glass'><h2 class='section-title'>Ready when you are.</h2><p class='section-copy'>Enter your height and weight, then select Calculate BMI to see your result.</p></div>", unsafe_allow_html=True)

elif page == "Model & accuracy":
    hero("A model you can inspect.", "See the learning method behind LumaCare and check its performance on the supplied insurance dataset.", "Transparency")
    st.write("")
    details, accuracy = st.columns([1, 1], gap="large")
    with details:
        st.markdown("<div class='glass'><div class='eyebrow'>Model card</div><h2 class='section-title'>Random Forest regressor</h2><p class='section-copy'>The model combines many decision trees to estimate insurance charges from six input signals. This helps capture non-linear patterns, such as the relationship between BMI, smoking and cost.</p><div class='metric-line'>Training data <b>Medical insurance dataset</b></div><div class='metric-line'>Input features <b>6</b></div><div class='metric-line'>Prediction target <b>Annual charges</b></div><div class='metric-line'>Libraries <b>Streamlit · pandas · scikit-learn</b></div></div>", unsafe_allow_html=True)
    with accuracy:
        st.markdown("<div class='glass'><div class='eyebrow'>Performance check</div><h2 class='section-title'>How accurate is it?</h2><p class='section-copy'>Run a live score against the included dataset. R² measures how much of the variation in charges the model explains.</p>", unsafe_allow_html=True)
        check_accuracy = st.button("Check prediction accuracy", use_container_width=True)
        if check_accuracy:
            features = data[["age", "sex", "bmi", "children", "smoker", "region"]]
            score = model.score(features, data["charges"])
            accuracy_pct = max(0, min(100, score * 100))
            st.markdown(f"<div class='pie' style='--score:{accuracy_pct * 3.6:.1f}deg' data-label='{accuracy_pct:.1f}%&#10;R² score'></div><p class='section-copy' style='text-align:center'>The remaining {100 - accuracy_pct:.1f}% reflects variation the model does not explain.</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif page == "About":
    hero("Care decisions deserve clarity.", "LumaCare turns a machine-learning prediction into an approachable starting point for understanding medical-insurance costs.", "About LumaCare")
    st.write("")
    c1, c2, c3 = st.columns(3)
    for col, title, copy in [(c1, "Purpose", "Make cost estimates easier to explore before you compare formal insurance quotes."), (c2, "Designed with care", "A calm, legible glass interface that keeps the focus on your information."), (c3, "A useful starting point", "Estimates can vary from real premiums. Always consult an insurer for an official quote.")]:
        with col:
            st.markdown(f"<div class='glass'><div class='eyebrow'>LumaCare</div><h2 class='section-title'>{title}</h2><p class='section-copy'>{copy}</p></div>", unsafe_allow_html=True)

else:
    hero("Help us make LumaCare better.", "Share what felt helpful, what did not, or what you would like to see next.", "Feedback")
    st.write("")
    st.markdown("<div class='glass'><h2 class='section-title'>Your feedback</h2><p class='section-copy'>This demo acknowledges your response in the current session.</p>", unsafe_allow_html=True)
    with st.form("feedback_form", clear_on_submit=True):
        name = st.text_input("Name (optional)")
        rating = st.select_slider("How was your experience?", options=["Not great", "Okay", "Good", "Excellent"])
        message = st.text_area("What would you like to tell us?", placeholder="Your thoughts…")
        sent = st.form_submit_button("Send feedback", use_container_width=True)
    if sent:
        st.success("Thank you — your feedback has been received.")
    st.markdown("</div>", unsafe_allow_html=True)
