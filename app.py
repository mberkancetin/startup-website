import streamlit as st
import requests
import datetime
import pandas as pd
import numpy as np

#st.logo("images/startorb.jpg")
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.write("# StartOrb")

tab1, tab2, tab3, tab5 = st.tabs([":tophat: About StartOrb ",
                                  ":magic_wand: The Lore       ",
                                  ":crystal_ball: Palantir    ",
                                  ":sparkles: Let's Predict  "])

tab1.markdown('''
            ## Unlocking Tomorrow's Success Today
            ##### Harness the Power of Data to Illuminate Your Startup Journey
''')
tab1.image('images/orb.gif')

tab2.subheader("Market and Social Perspectives", divider="rainbow")
tab2.markdown("""
            #### :radio_button: 9 out of 10 Start-Ups fail and go bankrupt!

            #### :radio_button: Private and public investors loose millions due to misallocating funds, which therefore limits funding for viable companies.

            #### :radio_button: Nations with higher startup success are more competitive, attract more talent and have strong economic growth (Think of Meta, Google etc.)

            #### :radio_button: Public entities such as government-backed VCs or state subsidy programs waste public capital due to poor start-up selection and lack of expertise in identifying emerging trends
              """)

tab3.subheader("Palantir: The Crystal Orb", divider="rainbow")

tab3.markdown("""
            #### :radio_button: Crunchbase and Dealroom are comprehensive databases that provide structured and curated data in the domain of startups, venture capital and entrepreneurship
\n
""")

tab3.markdown("""
              #### :radio_button: As for the model, we used two distinctive Neural Network models to identify \n
              #### (1) The success prediction score in percentage, \n
              #### (2) The estimated funding that the given company potentially receive if it goes to the next funding round
              """)

@st.experimental_dialog("The Orb's Verdict", width="large")
def submitted_fun():
    # Display the success prediction
    st.markdown(
        f"""
        <div style="text-align: center; font-size: 14px;">
            Your Success Prediction Score: \n
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="text-align: center; font-size: 36px;">
            {st.session_state.success_prediction}%
        </div>
        """,
        unsafe_allow_html=True
    )

    # Display the success prediction
    st.markdown(
        f"""
        <div style="text-align: center; font-size: 14px;">
            Estimated Funding for the Next Investment Round: \n
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="text-align: center; font-size: 36px;">
            {int(st.session_state.next_stage_funding):,}
            \n
            \n

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.write("")
    # def page_change():

    colx, coly = st.columns(2)

    with colx:
        if st.button("Industry Benchmarks"):
            st.switch_page("pages/IndustryBenchmarks.py")

    with coly:
        if st.button("Company Insights"):
            st.switch_page("pages/CompanyInsights.py")


# Initialize session state variables if not already set
if 'founded_date' not in st.session_state:
    st.session_state.founded_date = datetime.date(2019, 1, 1)
if 'month_founded' not in st.session_state:
    st.session_state.month_founded = 65
if 'location' not in st.session_state:
    st.session_state.location = 'Berlin'
if 'location_city' not in st.session_state:
    st.session_state.location_city = 'Berlin'
if 'company_size' not in st.session_state:
    st.session_state.company_size = '11-50'
if 'no_founders' not in st.session_state:
    st.session_state.no_founders = 1.0
if 'funding_status' not in st.session_state:
    st.session_state.funding_status = 'Pre-Seed'
if 'revenue_range' not in st.session_state:
    st.session_state.revenue_range = 'Less than $1M'
if 'industry' not in st.session_state:
    st.session_state.industry = 'Technology and Software'
if 'next_stage_funding' not in st.session_state:
    st.session_state.next_stage_funding = 1000000
if 'has_debt_financing' not in st.session_state:
    st.session_state.has_debt_financing = False
if 'has_grant' not in st.session_state:
    st.session_state.has_grant = False
if 'lat_city' not in st.session_state:
    st.session_state.lat_city = 52.5200
if 'lon_city' not in st.session_state:
    st.session_state.lon_city = 13.4050
if 'success_prediction' not in st.session_state:
    st.session_state.success_prediction = 85.23

# Define callback functions to update session state
def update_founded_date():
    st.session_state.founded_date = st.session_state.founded_date_input
def update_month_founded():
    st.session_state.month_founded = st.session_state.month_founded
def update_location():
    st.session_state.location = st.session_state.location_input
def update_location_city():
    st.session_state.location_city = st.session_state.location_city_input
def update_company_size():
    st.session_state.company_size = st.session_state.company_size_input
def update_no_founders():
    st.session_state.no_founders = st.session_state.no_founders_input
def update_funding_status():
    st.session_state.funding_status = st.session_state.funding_status_input
def update_revenue_range():
    st.session_state.revenue_range = st.session_state.revenue_range_input
def update_industry():
    st.session_state.industry = st.session_state.industry_input
def update_total_funding():
    st.session_state.total_funding = st.session_state.total_funding_input
def update_has_debt_financing():
    st.session_state.has_debt_financing = st.session_state.has_debt_financing_input
def update_has_grant():
    st.session_state.has_grant = st.session_state.has_grant_input
def update_lat_city():
    st.session_state.lat_city = st.session_state.lat_city
def update_lon_city():
    st.session_state.lon_city = st.session_state.lon_city
def update_success_prediction():
    st.session_state.success_prediction = st.session_state.success_prediction

# User input form

cola, colb = tab5.columns(2)
founded_date = cola.date_input('Year Your Company Was Founded:', value=st.session_state.founded_date, key="founded_date_input", on_change=update_founded_date)
location = cola.selectbox("Select Your Company’s Headquarters Location (Region):", [
    'Baden-Wurttemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg', 'Hessen',
    'Mecklenburg-Vorpommern', 'Niedersachsen', 'Nordrhein-Westfalen', 'Rheinland-Pfalz',
    'Saarland', 'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thuringen'
], index=['Baden-Wurttemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg', 'Hessen',
    'Mecklenburg-Vorpommern', 'Niedersachsen', 'Nordrhein-Westfalen', 'Rheinland-Pfalz',
    'Saarland', 'Sachsen', 'Sachsen-Anhalt', 'Schleswig-Holstein',
    'Thuringen'].index(st.session_state.location), key="location_input", on_change=update_location)

city_dict = {'Hessen': ['Sulzbach',
                        'Marburg',
                        'Dreieich',
                        'Kassel',
                        'Butzbach',
                        'Frankfort',
                        'Borken',
                        'Bad Homburg Vor Der Höhe',
                        'Weiterstadt',
                        'Hofheim Am Taunus',
                        'Rosbach Vor Der Höhe',
                        'Wiesbaden',
                        'Pfungstadt',
                        'Bensheim',
                        'Frankfurt',
                        'Darmstadt',
                        'Schwalbach',
                        'Trebur',
                        'Breuna',
                        'Oberursel',
                        'Eschborn'],
            'Schleswig-Holstein': ['Weißenhaus',
                        'Kiel',
                        'Neumünster',
                        'Flensburg',
                        'Halstenbek',
                        'Itzehoe',
                        'Kölln-reisiek',
                        'Lübeck',
                        'Süderlügum',
                        'Holm',
                        'Schenefeld',
                        'Kaltenkirchen',
                        'Norderstedt'],
            'Baden-Wurttemberg': ['Pfullendorf',
                        'Ulm',
                        'Heilbronn',
                        'Freiburg Im Breisgau',
                        'Schönaich',
                        'Leinfelden-echterdingen',
                        'Waghäusel',
                        'Wittenberg',
                        'Freiburg',
                        'Großrinderfeld',
                        'Leonberg',
                        'Karlsruhe',
                        'Pforzheim',
                        'Ettlingen',
                        'Balgheim',
                        'Kehl',
                        'Markdorf',
                        'Sindelfingen',
                        'Reutlingen',
                        'Konstanz',
                        'Ostfildern',
                        'Offenburg',
                        'Bruchsal',
                        'Heidelberg',
                        'Aalen',
                        'Wernau',
                        'Schömberg',
                        'Birkenfeld',
                        'Tübingen',
                        'Metzingen',
                        'Stuttgart',
                        'Wendelsheim',
                        'Mannheim',
                        'Esslingen'],
            'Niedersachsen': ['Osnabrück',
                        'Jelmstorf',
                        'Norwegen',
                        'Munster',
                        'Derental',
                        'Göttingen',
                        'Bad Salzdetfurth',
                        'Quakenbrück',
                        'Grafschaft',
                        'Buxtehude',
                        'Uetze',
                        'Salzgitter',
                        'Dinklage',
                        'Hanover',
                        'Brunswick',
                        'Oldenburg',
                        'Braunschweig'],
            'Rheinland-Pfalz': ['Kaiserslautern',
                        'Bingen',
                        'Speyer',
                        'Deuselbach',
                        'Bad Dürkheim',
                        'Remagen',
                        'Osann-monzel',
                        'Koblenz',
                        'Urbar',
                        'Föhren',
                        'Mainz'],
            'Bayern': ['Weißenburg In Bayern',
                        'Garching',
                        'Baierbrunn',
                        'Weßling',
                        'Grub Am Forst',
                        'Baiern',
                        'Pullach',
                        'Freising',
                        'Wildpoldsried',
                        'Ottobrunn',
                        'Reichenschwand',
                        'Unterhaching',
                        'Straßlach-dingharting',
                        'Eßlingen',
                        'Gilching',
                        'Unterschleißheim',
                        'Unterpleichfeld',
                        'Holzkirchen',
                        'Traunstein',
                        'Uffenheim',
                        'Erlangen',
                        'Munich',
                        'Taufkirchen',
                        'Tutzing',
                        'Würzburg',
                        'Gersthofen',
                        'Martinsried',
                        'Alling',
                        'Kempten',
                        'Regensburg',
                        'Garching Bei München',
                        'Fürth',
                        'Gars',
                        'Bernau Am Chiemsee',
                        'Greifenberg',
                        'Eibelstadt',
                        'Landshut',
                        'Rosenheim',
                        'Grünwald',
                        'Burghausen',
                        'Monaco',
                        'Eschenbach In Der Oberpfalz',
                        'Dachau',
                        'Nuremberg',
                        'Nürnberg',
                        'Feldafing',
                        'Oberhaching',
                        'Ismaning',
                        'Alzenau',
                        'Seibersdorf',
                        'Poing',
                        'Eisenberg',
                        'Bayreuth',
                        'Unterföhring',
                        'Ebene',
                        'Augsburg',
                        'Gauting',
                        'Starnberg',
                        'Pfaffenhofen An Der Glonn',
                        'München',
                        'Planegg'],
            'Nordrhein-Westfalen': ['Bonn',
                        'Jülich',
                        'Düsseldorf',
                        'Wuppertal',
                        'Neuss',
                        'Bielefeld',
                        'Leverkusen',
                        'Siegen',
                        'Hilden',
                        'Gelsenkirchen',
                        'England',
                        'Lippstadt',
                        'Hörde',
                        'Duisburg',
                        'Münster',
                        'Essen',
                        'Mönchengladbach',
                        'Lüdenscheid',
                        'Cologne',
                        'Hückelhoven',
                        'Dortmund',
                        'Paderborn',
                        'Solingen',
                        'Hagen',
                        'Steinhagen',
                        'Hennef',
                        'Aachen',
                        'Köln',
                        'Bochum',
                        'Herdecke',
                        'Gütersloh',
                        'Wesseling'],
            'Brandenburg': ['Wildau',
                        'Schönefeld',
                        'Bernau',
                        'Bestensee',
                        'Hoppegarten',
                        'Kleinmachnow',
                        'Gallin',
                        'Hennigsdorf',
                        'Potsdam',
                        'Marienwerder'],
            'Sachsen': ['Deutsch',
                        'Dresden',
                        'Zwickau',
                        'Chemnitz',
                        'Freital',
                        'Leipzig',
                        'Pausa',
                        'Ebersbach',
                        'Radebeul',
                        'Mittweida'],
            'Hamburg': ['Hamburg'],
            'Sachsen-Anhalt': ['Ostrau',
                                'Leuna', 'Halle', 'Magdeburg', 'Hessen'],
            'Thuringen': ['Suhl',
                            'Jena', 'Weimar', 'Ilmenau'],
            'Saarland': ['Sankt Wendel',
                            'Friedrichsthal', 'Saarbrücken'],
            'Berlin': ['Berlin',
                    'Kreuzberg',
                        'Adlershof',
                        'Gartenfeld',
                        'Prenzlauer Berg'
                        ],
            'Mecklenburg-Vorpommern': ['Schwerin',
                        'Greifswald',
                        'Rostock',
                        'Murchin',
                        'Stralsund'],
            'Bremen': ['Bremen']}
# location_city = st.selectbox("Select location", city_dict[location])
location_city = cola.selectbox("Select Your Company’s Headquarters Location (City):", city_dict[location], key="location_city_input", on_change=update_location_city)

german_cities = {
    'Pullach': {'lat': 48.0675, 'lon': 11.5231},
    'Rosbach Vor Der Höhe': {'lat': 50.2833, 'lon': 8.6833},
    'Gartenfeld': {'lat': 49.9667, 'lon': 8.3500},
    'Brunswick': {'lat': 52.2659, 'lon': 10.5267},
    'Poing': {'lat': 48.1700, 'lon': 11.8167},
    'Schönaich': {'lat': 48.6583, 'lon': 9.0669},
    'Magdeburg': {'lat': 52.1205, 'lon': 11.6276},
    'Weißenhaus': {'lat': 54.3000, 'lon': 10.8167},
    'Bad Homburg Vor Der Höhe': {'lat': 50.2225, 'lon': 8.6197},
    'Munich': {'lat': 48.1374, 'lon': 11.5755},
    'Schenefeld': {'lat': 53.6000, 'lon': 9.8333},
    'Cologne': {'lat': 50.9375, 'lon': 6.9603},
    'Bochum': {'lat': 51.4818, 'lon': 7.2162},
    'Dinklage': {'lat': 52.6667, 'lon': 8.2333},
    'Baiern': {'lat': 47.9500, 'lon': 11.8000},
    'Hoppegarten': {'lat': 52.5000, 'lon': 13.6667},
    'Pausa': {'lat': 50.5833, 'lon': 12.1333},
    'Greifswald': {'lat': 54.0958, 'lon': 13.3815},
    'Trebur': {'lat': 49.9167, 'lon': 8.4167},
    'Weimar': {'lat': 50.9795, 'lon': 11.3235},
    'Wuppertal': {'lat': 51.2562, 'lon': 7.1508},
    'Solingen': {'lat': 51.1652, 'lon': 7.0675},
    'Kiel': {'lat': 54.3233, 'lon': 10.1394},
    'Bonn': {'lat': 50.7374, 'lon': 7.0982},
    'Burghausen': {'lat': 48.1667, 'lon': 12.8333},
    'Leinfelden-echterdingen': {'lat': 48.6921, 'lon': 9.1624},
    'Planegg': {'lat': 48.1056, 'lon': 11.4208},
    'Unterföhring': {'lat': 48.1925, 'lon': 11.6469},
    'Fürth': {'lat': 49.4774, 'lon': 10.9886},
    'Schönefeld': {'lat': 52.3800, 'lon': 13.5200},
    'Gilching': {'lat': 48.1067, 'lon': 11.3000},
    'Kleinmachnow': {'lat': 52.4167, 'lon': 13.2167},
    'Bremen': {'lat': 53.0793, 'lon': 8.8017},
    'Deutsch': {'lat': 52.966221, 'lon': 11.583962},
    'Paderborn': {'lat': 51.7189, 'lon': 8.7544},
    'Stralsund': {'lat': 54.3139, 'lon': 13.0897},
    'Bestensee': {'lat': 52.2333, 'lon': 13.6333},
    'Berlin': {'lat': 52.5200, 'lon': 13.4050},
    'Tübingen': {'lat': 48.5216, 'lon': 9.0576},
    'Göttingen': {'lat': 51.5413, 'lon': 9.9158},
    'Karlsruhe': {'lat': 49.0069, 'lon': 8.4037},
    'Grub Am Forst': {'lat': 50.2333, 'lon': 11.0333},
    'Hofheim Am Taunus': {'lat': 50.0906, 'lon': 8.4500},
    'Gauting': {'lat': 48.0667, 'lon': 11.3833},
    'Kehl': {'lat': 48.5722, 'lon': 7.8150},
    'Leverkusen': {'lat': 51.0333, 'lon': 6.9833},
    'Leonberg': {'lat': 48.8000, 'lon': 9.0167},
    'Holm': {'lat': 53.6333, 'lon': 9.7000},
    'Dachau': {'lat': 48.2583, 'lon': 11.4356},
    'Bad Salzdetfurth': {'lat': 52.0500, 'lon': 10.0083},
    'Sindelfingen': {'lat': 48.7137, 'lon': 9.0030},
    'Weßling': {'lat': 48.0833, 'lon': 11.2500},
    'Hennigsdorf': {'lat': 52.6333, 'lon': 13.2000},
    'Butzbach': {'lat': 50.4333, 'lon': 8.6667},
    'Hamburg': {'lat': 53.5511, 'lon': 9.9937},
    'Freital': {'lat': 51.0167, 'lon': 13.6500},
    'Alzenau': {'lat': 50.0833, 'lon': 9.0667},
    'Salzgitter': {'lat': 52.1500, 'lon': 10.3333},
    'Hessen': {'lat': 52.017856, 'lon': 10.779785},
    'Breuna': {'lat': 51.4167, 'lon': 9.1833},
    'Weißenburg In Bayern': {'lat': 49.0333, 'lon': 11.1667},
    'Leuna': {'lat': 51.3167, 'lon': 12.0167},
    'Neumünster': {'lat': 54.0729, 'lon': 9.9840},
    'München': {'lat': 48.1374, 'lon': 11.5755},
    'Bingen': {'lat': 49.9667, 'lon': 7.9000},
    'Siegen': {'lat': 50.8748, 'lon': 8.0243},
    'Speyer': {'lat': 49.3172, 'lon': 8.4311},
    'Köln': {'lat': 50.9375, 'lon': 6.9603},
    'Dreieich': {'lat': 50.0167, 'lon': 8.7000},
    'Kassel': {'lat': 51.3127, 'lon': 9.4797},
    'Darmstadt': {'lat': 49.8728, 'lon': 8.6512},
    'Osnabrück': {'lat': 52.2799, 'lon': 8.0472},
    'Murchin': {'lat': 53.9833, 'lon': 13.6167},
    'Oldenburg': {'lat': 53.1439, 'lon': 8.2139},
    'Bernau': {'lat': 52.6798, 'lon': 13.5871},
    'Bad Dürkheim': {'lat': 49.4616, 'lon': 8.1639},
    'Hörde': {'lat': 51.4933, 'lon': 7.4886},
    'Uetze': {'lat': 52.4667, 'lon': 10.2000},
    'Erlangen': {'lat': 49.5897, 'lon': 11.0111},
    'Halstenbek': {'lat': 53.6500, 'lon': 9.8333},
    'Wendelsheim': {'lat': 49.7500, 'lon': 8.0833},
    'Adlershof': {'lat': 52.4377, 'lon': 13.5472},
    'Schömberg': {'lat': 48.2167, 'lon': 8.6667},
    'Wernau': {'lat': 48.7100, 'lon': 9.4167},
    'Jena': {'lat': 50.9272, 'lon': 11.5899},
    'Dresden': {'lat': 51.0504, 'lon': 13.7373},
    'Frankfort': {'lat': 50.1109, 'lon': 8.6821},
    'Ismaning': {'lat': 48.2333, 'lon': 11.6833},
    'Jelmstorf': {'lat': 53.1333, 'lon': 10.5667},
    'Grafschaft': {'lat': 50.5667, 'lon': 7.0167},
    'Lüdenscheid': {'lat': 51.2167, 'lon': 7.6333},
    'Seibersdorf': {'lat': 48.0167, 'lon': 16.5333},
    'Heidelberg': {'lat': 49.3988, 'lon': 8.6724},
    'Freising': {'lat': 48.4029, 'lon': 11.7486},
    'Weiterstadt': {'lat': 49.9000, 'lon': 8.6000},
    'Eisenberg': {'lat': 49.5500, 'lon': 8.0731},
    'Wesseling': {'lat': 50.8200, 'lon': 6.9800},
    'Markdorf': {'lat': 47.7205, 'lon': 9.3960},
    'Aachen': {'lat': 50.7753, 'lon': 6.0839},
    'Radebeul': {'lat': 51.1069, 'lon': 13.6668},
    'Jülich': {'lat': 50.9226, 'lon': 6.3627},
    'Dortmund': {'lat': 51.5139, 'lon': 7.4653},
    'Flensburg': {'lat': 54.7819, 'lon': 9.4366},
    'Esslingen': {'lat': 48.7406, 'lon': 9.3108},
    'Gelsenkirchen': {'lat': 51.5177, 'lon': 7.0857},
    'Mittweida': {'lat': 50.9867, 'lon': 12.9800},
    'Unterpleichfeld': {'lat': 49.8703, 'lon': 10.0342},
    'Mönchengladbach': {'lat': 51.1854, 'lon': 6.4417},
    'Oberursel': {'lat': 50.2000, 'lon': 8.5833},
    'Aalen': {'lat': 48.8378, 'lon': 10.0936},
    'Offenburg': {'lat': 48.4728, 'lon': 7.9449},
    'Unterhaching': {'lat': 48.0667, 'lon': 11.6167},
    'Bensheim': {'lat': 49.6803, 'lon': 8.6189},
    'Chemnitz': {'lat': 50.8333, 'lon': 12.9167},
    'Wildpoldsried': {'lat': 47.7333, 'lon': 10.4000},
    'Oberhaching': {'lat': 48.0311, 'lon': 11.5411},
    'Baierbrunn': {'lat': 48.0333, 'lon': 11.5167},
    'Schwalbach': {'lat': 50.1500, 'lon': 8.5500},
    'Starnberg': {'lat': 48.0000, 'lon': 11.3333},
    'Rosenheim': {'lat': 47.8561, 'lon': 12.1289},
    'England': {'lat': 53.022274, 'lon': 8.371281},
    'Traunstein': {'lat': 47.8711, 'lon': 12.6436},
    'Ettlingen': {'lat': 48.9392, 'lon': 8.4039},
    'Eßlingen': {'lat': 48.7406, 'lon': 9.3108},
    'Bayreuth': {'lat': 49.9456, 'lon': 11.5713},
    'Ottobrunn': {'lat': 48.0667, 'lon': 11.6667},
    'Steinhagen': {'lat': 52.0333, 'lon': 8.4000},
    'Holzkirchen': {'lat': 47.8813, 'lon': 11.6919},
    'Waghäusel': {'lat': 49.2478, 'lon': 8.4958},
    'Ebene': {'lat': 47.6603, 'lon': 10.0155},
    'Eibelstadt': {'lat': 49.7269, 'lon': 10.0039},
    'Regensburg': {'lat': 49.0134, 'lon': 12.1016},
    'Sankt Wendel': {'lat': 49.4667, 'lon': 7.1667},
    'Gütersloh': {'lat': 51.9060, 'lon': 8.3785},
    'Kaiserslautern': {'lat': 49.4447, 'lon': 7.7689},
    'Marburg': {'lat': 50.8100, 'lon': 8.7700},
    'Würzburg': {'lat': 49.7913, 'lon': 9.9534},
    'Mainz': {'lat': 49.9929, 'lon': 8.2473},
    'Halle': {'lat': 51.4828, 'lon': 11.9697},
    'Borken': {'lat': 51.8438, 'lon': 6.8577},
    'Balgheim': {'lat': 48.0667, 'lon': 8.8667},
    'Gersthofen': {'lat': 48.4167, 'lon': 10.8833},
    'Kölln-reisiek': {'lat': 53.7833, 'lon': 9.7000},
    'Pfullendorf': {'lat': 47.9200, 'lon': 9.2667},
    'Schwerin': {'lat': 53.6355, 'lon': 11.4012},
    'Kaltenkirchen': {'lat': 53.8333, 'lon': 9.9667},
    'Munster': {'lat': 52.2000, 'lon': 10.1000},
    'Kempten': {'lat': 47.7333, 'lon': 10.3167},
    'Eschborn': {'lat': 50.1433, 'lon': 8.5711},
    'Nürnberg': {'lat': 49.4539, 'lon': 11.0775},
    'Deuselbach': {'lat': 49.7333, 'lon': 7.1333},
    'Remagen': {'lat': 50.5833, 'lon': 7.2333},
    'Koblenz': {'lat': 50.3564, 'lon': 7.5938},
    'Herdecke': {'lat': 51.4000, 'lon': 7.4333},
    'Martinsried': {'lat': 48.1089, 'lon': 11.4598},
    'Itzehoe': {'lat': 53.9256, 'lon': 9.5153},
    'Friedrichsthal': {'lat': 49.3000, 'lon': 7.1167},
    'Lübeck': {'lat': 53.8655, 'lon': 10.6866},
    'Feldafing': {'lat': 47.9667, 'lon': 11.3000},
    'Potsdam': {'lat': 52.4009, 'lon': 13.0591},
    'Bielefeld': {'lat': 52.0211, 'lon': 8.5347},
    'Quakenbrück': {'lat': 52.6667, 'lon': 7.9500},
    'Stuttgart': {'lat': 48.7775, 'lon': 9.1800},
    'Norderstedt': {'lat': 53.7000, 'lon': 10.0000},
    'Freiburg Im Breisgau': {'lat': 47.9990, 'lon': 7.8421},
    'Uffenheim': {'lat': 49.5333, 'lon': 10.2500},
    'Ilmenau': {'lat': 50.6833, 'lon': 10.9167},
    'Unterschleißheim': {'lat': 48.2833, 'lon': 11.5667},
    'Düsseldorf': {'lat': 51.2217, 'lon': 6.7762},
    'Wiesbaden': {'lat': 50.0825, 'lon': 8.2400},
    'Rostock': {'lat': 54.0924, 'lon': 12.0991},
    'Nuremberg': {'lat': 49.4539, 'lon': 11.0775},
    'Konstanz': {'lat': 47.6603, 'lon': 9.1758},
    'Hückelhoven': {'lat': 51.0500, 'lon': 6.2167},
    'Eschenbach In Der Oberpfalz': {'lat': 49.7531, 'lon': 11.8295},
    'Ostrau': {'lat': 51.615625, 'lon': 12.010272},
    'Garching Bei München': {'lat': 48.2514, 'lon': 11.6510},
    'Hennef': {'lat': 50.7754, 'lon': 7.2848},
    'Prenzlauer Berg': {'lat': 52.5388, 'lon': 13.4244},
    'Braunschweig': {'lat': 52.2659, 'lon': 10.5267},
    'Derental': {'lat': 51.6667, 'lon': 9.3833}, # Approximate coordinates
    'Großrinderfeld': {'lat': 49.6647, 'lon': 9.7347},
    'Monaco': {'lat': 43.7384, 'lon': 7.4246},
    'Straßlach-dingharting': {'lat': 48.0000, 'lon': 11.5170},
    'Hanover': {'lat': 52.3705, 'lon': 9.7332},
    'Mannheim': {'lat': 49.4891, 'lon': 8.4669},
    'Augsburg': {'lat': 48.3715, 'lon': 10.8985},
    'Wittenberg': {'lat': 51.8667, 'lon': 12.6500},
    'Münster': {'lat': 51.9624, 'lon': 7.6257},
    'Metzingen': {'lat': 48.5369, 'lon': 9.2833},
    'Buxtehude': {'lat': 53.4672, 'lon': 9.6864},
    'Lippstadt': {'lat': 51.6737, 'lon': 8.3448},
    'Birkenfeld': {'lat': 49.6500, 'lon': 7.1833},
    'Heilbronn': {'lat': 49.1399, 'lon': 9.2205},
    'Grünwald': {'lat': 48.04866, 'lon': 11.53007},
    'Süderlügum': {'lat': 54.87256, 'lon': 8.90738},
    'Zwickau': {'lat': 50.72724, 'lon': 12.48839},
    'Reichenschwand': {'lat': 49.512238, 'lon': 11.371579},
    'Frankfurt': {'lat': 50.110924, 'lon': 8.682127},
    'Taufkirchen': {'lat': 48.045998, 'lon': 11.615190},
    'Pfungstadt': {'lat': 49.805570, 'lon': 8.603070},
    'Norwegen': {'lat': 62.000000, 'lon': 10.000000},
    'Bruchsal': {'lat': 49.124119, 'lon': 8.598024},
    'Osann-Monzel': {'lat': 49.92167, 'lon': 6.95528},
    'Osann-Monzel': {'lat': 49.92167, 'lon': 6.95528},
    'Freiburg': {'lat': 47.9959, 'lon': 7.85222},
    'Landshut': {'lat': 48.52961, 'lon': 12.16179},
    'Pfaffenhofen An Der Glonn': {'lat': 48.29562, 'lon': 11.16387},
    'Sulzbach': {'lat': 49.299583, 'lon': 7.061639},
    'Hagen': {'lat': 51.36081, 'lon': 7.47168},
    'Leipzig': {'lat': 51.33962, 'lon': 12.37129},
    'Duisburg': {'lat': 51.43247, 'lon': 6.76516},
    'Pforzheim': {'lat': 48.88436, 'lon': 8.69892},
    'Gallin': {'lat': 53.6667, 'lon': 11.3167}, # Approximate coordinates
    'Alling': {'lat': 48.14034, 'lon': 11.30144},
    'Greifenberg': {'lat': 48.07062000, 'lon': 11.08349000},
    'Wildau': {'lat': 52.31667, 'lon': 13.63333},
    'Bernau Am Chiemsee': {'lat': 47.811630, 'lon': 12.373393},
    'Ebersbach': {'lat': 51.0076, 'lon': 14.5862},
    'Garching': {'lat': 48.2514, 'lon': 11.6510},
    'Essen': {'lat': 51.45657000, 'lon': 7.01228000},
    'Kreuzberg': {'lat': 52.49973000, 'lon': 13.40338000},
    'Neuss': {'lat': 51.19807, 'lon': 6.68504},
    'Föhren': {'lat': 49.858658, 'lon': 6.766662},
    'Hilden': {'lat': 51.167858, 'lon': 6.935225},
    'Reutlingen': {'lat': 48.49144, 'lon': 9.20427},
    'Marienwerder': {'lat': 52.85055, 'lon': 13.60000},
    'Saarbrücken': {'lat': 49.23262, 'lon': 7.00982},
    'Ostfildern': {'lat': 48.72704, 'lon': 9.24954},
    'Suhl': {'lat': 50.6091, 'lon': 10.6940},
    'Urbar': {'lat': 50.3817, 'lon': 7.6248},
    'Ulm': {'lat': 48.39841, 'lon': 9.99155},
    'Gars': {'lat': 48.1532, 'lon': 12.5309}, # Approximate coordinates
    'Tutzing': {'lat': 47.9086, 'lon': 11.2798},
}
lat_city = float(german_cities[st.session_state.location_city]["lat"])
lon_city = float(german_cities[st.session_state.location_city]["lon"])

company_size = colb.selectbox('Choose Your Company Size Category:', ['11-50', '51-100', '101-250',
                                                    '251-500', '501-1000', '1001-5000',
                                                    '5001-10000', '10001+'], key="company_size_input", on_change=update_company_size)
no_founders = colb.number_input("How Many Founders Does Your Company Have?", min_value=1, step=1, key="no_founders_input", on_change=update_no_founders)
funding_status = colb.selectbox("The Latest Investment Stage", ["Pre-Seed", "Seed",
                                                                        "Series A", "Series B",
                                                                        "Series C", "Further Stages"], key="funding_status_input", on_change=update_funding_status)
revenue_range = colb.selectbox('Select Your Company’s Current Annual Revenue Range:', ['Less than $1M', '$1M to $10M', '$10M to $50M', '$50M to $100M',
                                                    '$100M to $500M', '$500M to $1B', '$1B to $10B',
                                                    '$10B+'], key="revenue_range_input", on_change=update_revenue_range)
industry = cola.selectbox('Choose the Industry Your Company Operates In:', ['Energy and Natural Resources', 'Technology and Software',
                                            'Business Services', 'Community and Lifestyle',
                                            'Finance and Payments', 'Other', 'Hardware and Electronics',
                                            'Consumer Products', 'Manufacturing and Industry', 'Media and Entertainment',
                                            'Telecommunications and Internet Services', 'Healthcare and Biotechnology',
                                            'Travel and Tourism', 'Retail and E-commerce', 'Transportation and Logistics',
                                            'Education and Training', 'Government and Public Services',
                                            'Science and Engineering'], key="industry_input", on_change=update_industry)
# total_funding = st.number_input('Total Funding Amount (in USD)', min_value=0, key="total_funding_input", on_change=update_total_funding)
tab5.markdown('''
            List Any Additional Sources of Financing Your Company Has Secured:
            ''')
colc, cold = tab5.columns(2)
has_debt_financing = colc.checkbox('Debt Financing', key="has_debt_financing_input", on_change=update_has_debt_financing)
has_grant = cold.checkbox('Grant', key="has_grant_input", on_change=update_has_grant)

submitted = tab5.button("Submit")
if submitted:
    # Clear the page
    st.empty()
    # Display the animation
    # st.image('images/red-orb.gif', use_column_width=True)
    st.session_state.month_founded = int((pd.to_datetime('today') - pd.to_datetime(st.session_state.founded_date)).days / 30.44)
    params = {
        "months_since_founded": st.session_state.month_founded,
        "lat": float(st.session_state.lat_city),
        "lon": float(st.session_state.lon_city),
        "company_size": str(st.session_state.company_size),
        "no_founders": float(st.session_state.no_founders),
        "industry_groups": str(st.session_state.industry),
        "funding_status": str(st.session_state.funding_status),
        "revenue_range": str(st.session_state.revenue_range),
        "total_funding": float(1000000.00),
        "has_debt_financing": bool(st.session_state.has_debt_financing),
        "has_grant": bool(st.session_state.has_grant),
    }
    # st.write(params)

    # predict the success probability
    url = "https://newmodel-jagyvvkiea-ew.a.run.app/predict"
    response = requests.get(url=url, params=params)
    success_prediction = response.json()["Success Probability"]
    if success_prediction < 0.6:
        st.session_state.success_prediction = round(success_prediction * 100, 2)
    else:
        st.session_state.success_prediction = round(np.power(success_prediction, np.e) * 100, 2)
    # Display the success prediction
    #
    # st.markdown(
    #    f"""
    #    <div style="text-align: center; font-size: 24px;">
    #        Your Success Prediction Score: {success_prediction}%
    #    </div>
    #    """,
    #    unsafe_allow_html=True
    #)

    x_status = "Seed"
    stage = 1
    if st.session_state.funding_status == "Pre-Seed":
        x_status = "Seed"
        stage = 0
    else:
        x_status = funding_status
        stage = 1

    params_x = params
    params_x["funding_status"] = str(x_status)
    # st.write(params_x)

    # predict the next stage funding
    url = "https://newmodel-jagyvvkiea-ew.a.run.app/regressor"
    response = requests.get(url=url, params=params_x)
    next_score = response.json()["Extimated Funding for the Next Round"]

    if stage == 0:
        next_score = float(next_score) / 2.9
    st.session_state.next_stage_funding = round(next_score, -4)

    # Display the success prediction
    #st.markdown(
    #    f"""
    #    <div style="text-align: center; font-size: 24px;">
    #        Estimated Funding for the Next Investment Round: {st.session_state.next_stage_funding}
    #    </div>
    #    """,
    #    unsafe_allow_html=True
    #)
    submitted_fun()
