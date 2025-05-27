import streamlit as st

st.title("welcome to my web")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("81e283b2b7084963f89e7667ee2e0a57.jpg", width=200)

st.title("Aplikasi sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap")
else:
    st.writer(f"{angka} adalah bilangan ganjil")
    


