import streamlit as st
import pandas as pd
from datetime import date, timedelta
today= date.today ()
period_day = 8
period_window = 2

st.title("💖 Daily Happiness Boost 💖")

# --- Initialize session state correctly ---
if 'mood_data' not in st.session_state or 'reset' not in st.session_state:
    st.session_state.mood_data = pd.DataFrame(columns=['Date', 'Period', 'Weather', 'Smiles'])
    st.session_state.reset = True  # flag to prevent recreating columns

# --- Inputs ---
weather = st.slider("Weather today: 0 = Storm 🌩, 5 = Very Sunny ☀️", 0, 5, 3)
smiles = st.slider("Smiles / laughter today (0 = none, 10 = lots 😄)", 0, 10, 5)

# --- Add entry ---
checked = st.checkbox("Am I already on my period?")
today = date.today()

if st.button("Add Happiness Boost"):
         # --- Determine period status ---
    if checked:
        st.error("BLOOD BLOOD EVERYWHERE — you are on your period 🔴")
        days_until = 30  # approximate next period
    else:
        # Automatic calculation based on current date
        if period_day - period_window <= today.day <= period_day + period_window:
            st.error("BLOOD BLOOD EVERYWHERE — you are on your period 🔴")
            days_until = 30
        else:
            # Determine next 8th
            if today.day < period_day:
                target_date = date(today.year, today.month, period_day)
            else:
                # Next month
                if today.month == 12:
                    target_date = date(today.year + 1, 1, period_day)
                else:
                    target_date = date(today.year, today.month + 1, period_day)
            days_until = (target_date - today).days
            st.success(f"Next period in {days_until} days 🟢")

    # --- Period label ---
        if days_until <= 8:
            period_label = f"{days_until} days 🔴"
        elif days_until <= 15:
            period_label = f"{days_until} days 🟡"
        else:
            period_label = f"{days_until} days 🟢"

    # --- Period-based suggestions ---
        if days_until <= 8:
            st.warning("Period is approaching soon — take extra care of yourself!")
        elif days_until <= 15:
            st.info("Period is a bit away — a good time to plan some self-care!")
        else:
            st.success("Period is far away — enjoy your day! 🌞")

    # --- Weather suggestions ---
    if weather == 0:
        st.info("Stormy day outside 🌩 — maybe stay cozy indoors!")
    elif weather <= 2:
        st.info("A bit gloomy outside 🌧️ — perfect for relaxing!")
    elif weather <= 4:
        st.success("Nice weather ☀️ — a short walk can boost your mood!")
    else:
        st.success("Absolutely sunny 🌞 — enjoy the day!")

    # --- Smiles suggestions ---
    if smiles == 0:
        st.warning("No smiles today? 😔 Try to laugh or watch something funny!")
    elif smiles <= 4:
        st.info("Some smiles today 🙂 — keep it going!")
    elif smiles <= 7:
        st.success("Good job laughing today 😄 — keep your spirits up!")
    else:
        st.success("Awesome! 😆 Lots of laughter today — keep spreading joy!")

    # --- Combined suggestions ---
    if days_until <= 8 and weather <= 1 and smiles <= 2:
        st.error("Tough day ahead 😣 — take care of yourself!")
    elif days_until <= 8 and smiles >= 7:
        st.success("Even close to period, your high spirits shine! 🌟")
    elif weather == 0 and smiles >= 7:
        st.success("Stormy outside but your mood is great 😄 — keep the energy up!")
    
