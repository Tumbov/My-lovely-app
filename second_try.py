import streamlit as st
import pandas as pd
from datetime import date, timedelta
today= date.today ()
period_day = 8
period_window = 2
st.markdown(f'<p style="font-size:10px;"> Rate him today </p>', unsafe_allow_html=True)
sentiment_mapping = ["You must tell him where he should do better", "Hold on, maybe it is not his day", "Well, this is completely okay, everyone has a good and a bad days and periods", "We are in the UP'S, enjoy every second", "TELL HIM HOW MUCH!!"]
selected = st.feedback("stars")

if selected is not None:
    st.markdown(f'<p style="font-size:10px;">{sentiment_mapping[selected]}</p>', unsafe_allow_html=True)

#st.text ('Rate his perfomance today')
#sentiment_mapping = ["You must tell him where he should do better", "Hold on, maybe it is not his day", "Well, this is completely okay, everyone has a good and a bad days and periods", "We are in the UP'S, enjoy every second", "TELL HIM HOW MUCH!!"]
#selected = st.feedback("stars")

#if selected is not None:
    #st.markdown(f"{sentiment_mapping[selected]}")

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
    # --- GIFS, PICTURES, ANYTHING EXTRA --- #
    if smiles == 0:
        st.image("https://media.tenor.com/UGQDrLmTceUAAAAi/cat-transparent.gif", caption="Cheer up! Watch a comedy 🎬")
    elif smiles == 10:
        st.image("https://media.tenor.com/HLrXIleGBToAAAAi/transparent-cat.gif", caption="Keep shining 🌟")
    elif smiles == 5:
        st.image ("https://media1.tenor.com/m/Dwrij1L3z_0AAAAC/gnome-knitting-gnome.gif", caption ="You are getting there darling!")
    elif smiles == 1:
        st.image ("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzZiM3R4NjZ3cTd5aWg3aGk4ZzRzeDB1cnVxaHpxODFnZjYyN2lkYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0MYsDZrZAggnPPGM/giphy.gif", caption = "YOU ARE GETTING THERE !!! better one than none ;)" )
    elif smiles > 5 and smiles < 10:
        st.image ("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmtjcHBzdjczY2hqNTNrY2x4dzd3eXB4enR1Z3F6dWlyc2h1MjFwOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fpmJ0eZWcSZAcGoIv5/giphy.gif", caption = "I am jealous, shere some with me, PLEASE!")     
    elif smiles > 1 and smiles < 5:
        st.image ("https://media.tenor.com/TlC6-doS0XgAAAAi/boing.gif", caption = "Keep going, keep smiling!")
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
    # --- COLOR BACKGROUND --- #
color = st.color_picker("↓↓↓ down here darling, change whatever color you want ;)", "#C17EBB")
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {color};
    }}
    </style>
    """,
    unsafe_allow_html=True

)







