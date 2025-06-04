import pandas as pd
import time 


def recent_data(filepath, window_minutes = 10):
    df = pd.rad_csv(filepath)
    df["Time"] = pd.to_datetime(df['Time'])
    cutoff = datetime.now()
    return df[df['Time'] > cutoff]

def detect_electrode_burnout():
    for col in ["Top","Middle","Bottom","Total"]:
        recent = df[col].dropna()
        if recent.empty:
            continue
    return "sucess"
recent_data()
detect_electrode_burnout()
