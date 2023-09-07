import streamlit as st
from datetime import datetime

st.title("Primbon")

nama = st.text_input("Masukkan nama kamu")

tl = st.date_input(
    "Masukkan tanggal lahir"
    ,min_value=datetime.strptime('1945-01-01','%Y-%m-%d'))

hari_lahir_num = tl.isoweekday()
hari = {
    1:'Senin',
    2:'Selasa',
    3:'Rabu',
    4:'Kamis',
    5:'Jumat',
    6:'Sabtu',
    7:'Minggu'
}

watak = {
    1:
    """
    Berdasarkan ilmu astrologi, orang yang lahir pada hari Senin berada di bawah pengaruh bulan yang membuat seseorang berdedikasi pada kebaikan dan keluarga. Karakter berdasarkan hari lahir yang jatuh pada hari Senin adalah seseorang yang baik, sensitif, dan mudah beradaptasi dengan lingkungan.

Selain itu, ia juga adalah orang yang kreatif tapi terkadang suka menyimpan ide untuk diri sendiri. Ia juga selalu mengutamakan keluarga dan sahabat dekatnya.
    """,
    2:
    """
    Orang yang lahir pada hari selasa dipengaruhi oleh planet Mars. Dalam mitologi Yunani dan Romania, Mars juga dikenal sebagai Ares, sang Dewa Perang sehingga orang yang memiliki hari kelahiran Selasa punya semangat juang tinggi. Ia dikenal pemberani, energik dan aktif.

Selain itu, ia juga memiliki sifat mudah stress terhadap sesuatu yang tidak bisa dikontrol olehnya. Saat menyampaikan sesuatu ia sangat jujur dan apa adanya. Hanya saja, ketika marah mereka akan membuat orang-orang di dekatnya ketakutan. Ia juga mudah emosi untuk hal-hal yang bisa saja sangat sepele.
    """,
    3:
    """
    Orang yang lahir pada hari rabu dipengaruhi oleh Merkurius yang merupakan dewa keuangan, travel dan komunikasi. Orang yang memiliki hari lahir Rabu adalah individu yang terbuka dan sedikit tidak peduli walaupun sangat komunikatif, mudah belajar tentang hal baru dan baik dalam mengerjakan tugas.

Selain itu, ia juga adalah orang yang easy going dan menyukai belajar dari sekitarnya. Ia adalah pribadi yang tenang dan bijaksana. Namun ketika sakit hati, ia akan sangat mengerikan dan pendendam.
    """,
    4:
    """
    Thur adalah Thursday atau Kamis dalam mitologi Yunani berasal dari Dewa Thor. Orang yang lahir pada hari Kamis memiliki kepribadian yang seru, optimis dan lucu. Ia juga dihargai oleh orang disekitarnya dan merupakan seorang pemimpin yang baik.

Selain itu, ia juga mudah menarik perhatian karena berkarisma dan menyenangkan. Ia pun sering tertarik oleh beberapa hal namun mudah bosan. Tak hanya menyenangkan, orang yang lahir di hari Kamis merupakan pribadi yang apa adanya dan tak suka menyembunyikan sesuatu. Ia juga sangat sensitif dan mudah termakan bujuk rayu orang di sekitarnya.
    """,
    5:
    """
    Orang yang lahir pada hari Jumat dipengaruhi oleh Venus, planet penuh cinta, romantis, elegan dan kesenangan. Orang yang lahir hari Jumat adalah pecinta binatang, seni dan terobsesi dengan hal-hal berkaitan dengan cinta asmara.

Ia juga memiliki sifat sensitif jika berbicara tentang hubungan asmara.Orang tersebut juga cenderung bijak tentang dunia dan bersikap dewasa. Orang yang lahir Jumat dikatakan adalah pribadi yang ramah, menyenangkan dan jarang marah. Mereka juga senang mengalah demi kebahagiaan orang lain.
    """,
    6:
    """
    Orang yang lahir pada hari Sabtu berada di bawah pengaruh Saturnus, dewa kekayaan, kebebasan dan agrikultur. Meski begitu bukan berarti bahwa ia akan kaya, tetapi rendah hati, bijak dan tegas. Selain itu, ia adalah orang yang dipercaya dan bertanggung jawab atas banyak tugas.

Namun ia kerap terjebak pada masa lalu atau terlalu memikirkan masa depan, sehingga seakan tidak pernah berada di waktu yang sekarang. Ia juga mudah cemburu dan salah sangka ke pasangannya.
    """,
    7:
    """
    Menurut astrologi, orang-orang yang lahir di hari Minggu merupakan orang yang sangat beruntung. Biasanya ia adalah orang yang ceria, berpikiran maju dan dermawan. Ia juga orang yang berbakat menjadi pemimpin karena penampilannya yang positif. Namun ia memiliki sifat yang sensitif pada pendapat orang lain. Ia juga mudah frustasi dan sering meninggalkan pekerjaan jika bosan.
    """
}


st.subheader(f'Hello, {nama}!')
st.subheader(f'Kamu lahir hari {hari[hari_lahir_num]}!')
st.write(watak[hari_lahir_num])