import json
import time
import pandas as pd
import numpy as np
import pydeck as pdk
from math import sqrt
import streamlit as st

st.title('Pod\'s Loan Worthiness Score')


st.header('Personal Information')
age = st.slider(
    'Your age:',
    18,65
    ,format="%d Years"
)
col1, col2 = st.beta_columns(2)
with col1:
    gender = st.selectbox(
        'Gender:',
        ('Female', 'Male', 'Other')
    )
with col2:
    education = st.selectbox(
        'Your highest attained education level?',
        ('SPM', 'Diploma', 'Associate degree', 'Degree', 'Masters', 'Phd')
    )

col3, col4 = st.beta_columns(2)
with col3:
    dependants = st.number_input(
        'Number of dependants:',
        0,30,0,1,'%d'
    )
    ncc = st.number_input(
        'Number of Credit Cards:',
        0,30,0,1,'%d'
    )
    address = st.selectbox(
            'Select your city: ',
            (
                "Johor Bahru",
                "Tebrau",
                "Pasir Gudang",
                "Bukit Indah",
                "Skudai",
                "Kluang",
                "Batu Pahat",
                "Muar",
                "Ulu Tiram",
                "Senai",
                "Segamat",
                "Kulai",
                "Kota Tinggi",
                "Pontian Kechil",
                "Tangkak",
                "Bukit Bakri",
                "Yong Peng",
                "Pekan Nenas",
                "Labis",
                "Mersing",
                "Simpang Renggam",
                "Parit Raja",
                "Kelapa Sawit",
                "Buloh Kasap",
                "Chaah",
                "Sungai Petani",
                "Alor Setar",
                "Kulim",
                "Jitra / Kubang Pasu",
                "Baling",
                "Pendang",
                "Langkawi",
                "Yan",
                "Sik",
                "Kuala Nerang",
                "Pokok Sena",
                "Bandar Baharu",
                "Kota Bharu",
                "Pangkal Kalong",
                "Tanah Merah",
                "Peringat",
                "Wakaf Baru",
                "Kadok",
                "Pasir Mas",
                "Gua Musang",
                "Kuala Krai",
                "Tumpat",
                "Bandaraya Melaka",
                "Bukit Baru",
                "Ayer Keroh",
                "Klebang",
                "Masjid Tanah",
                "Sungai Udang",
                "Batu Berendam",
                "Alor Gajah",
                "Bukit Rambai",
                "Ayer Molek",
                "Bemban",
                "Kuala Sungai Baru",
                "Pulau Sebang",
                "Seremban",
                "Port Dickson",
                "Nilai",
                "Bahau",
                "Tampin",
                "Kuala Pilah",
                "Kuantan",
                "Temerloh",
                "Bentong",
                "Mentakab",
                "Raub",
                "Jerantut",
                "Pekan",
                "Kuala Lipis",
                "Bandar Jengka",
                "Bukit Tinggi",
                "Ipoh",
                "Taiping",
                "Sitiawan",
                "Simpang Empat",
                "Teluk Intan",
                "Batu Gajah",
                "Lumut",
                "Kampung Koh",
                "Kuala Kangsar",
                "Sungai Siput Utara",
                "Tapah",
                "Bidor",
                "Parit Buntar",
                "Ayer Tawar",
                "Bagan Serai",
                "Tanjung Malim",
                "Lawan Kuda Baharu",
                "Pantai Remis",
                "Kampar",
                "Kangar",
                "Kuala Perlis",
                "Bukit Mertajam",
                "Georgetown",
                "Sungai Ara",
                "Gelugor",
                "Ayer Itam",
                "Butterworth",
                "Val d’Or",
                "Perai",
                "Nibong Tebal",
                "Permatang Kucing",
                "Tanjung Tokong",
                "Kepala Batas",
                "Tanjung Bungah",
                "Juru",
                "Kota Kinabalu",
                "Sandakan",
                "Tawau",
                "Lahad Datu",
                "Keningau",
                "Putatan",
                "Donggongon",
                "Semporna",
                "Kudat",
                "Kunak",
                "Papar",
                "Ranau",
                "Beaufort",
                "Kinarut",
                "Kota Belud",
                "Kuching",
                "Miri",
                "Sibu",
                "Bintulu",
                "Limbang",
                "Sarikei",
                "Sri Aman",
                "Kapit",
                "Batu Delapan Bazaar",
                "Kota Samarahan",
                "Subang Jaya",
                "Klang",
                "Ampang Jaya",
                "Shah Alam",
                "Petaling Jaya",
                "Cheras",
                "Kajang",
                "Selayang Baru",
                "Rawang",
                "Taman Greenwood",
                "Semenyih",
                "Banting",
                "Balakong",
                "Gombak Setia",
                "Kuala Selangor",
                "Serendah",
                "Bukit Beruntung",
                "Pengkalan Kundang",
                "Jenjarom",
                "Sungai Besar",
                "Batu Arang",
                "Tanjung Sepat",
                "Kuang",
                "Kuala Kubu Baharu",
                "Batang Berjuntai",
                "Bandar Baru Salak Tinggi",
                "Sekinchan",
                "Sabak",
                "Tanjung Karang",
                "Beranang",
                "Sungai Pelek",
                "Kuala Terengganu",
                "Chukai",
                "Dungun",
                "Kerteh",
                "Kuala Berang",
                "Marang",
                "Paka",
                "Jerteh",
                "Kuala Lumpur",
                "Labuan",
                "Putrajaya"
            )
        )
with col4:
    marital_status = st.radio(
        'Marital status:',
        ("Single", "Married", "Widow", "Divorced")
    )
    pod_user = st.radio(
        'Do you have a saving account with pod?',
        ("No", "Not actively saving", "Yes")
    )
if pod_user == "Yes":
    podgoalcol1, podgoalcol2, podgoalcol3 = st.beta_columns(3)
    with podgoalcol1:
        goals_count = st.number_input(
        'Total number of goals:',
        0,30,0,1,'%d'
        )

    with podgoalcol2:
        compelted_goals = st.number_input(
        'Number of compelted goals:',
        0,30,0,1,'%d'
        )

    with podgoalcol3:
        amount_saved = st.number_input(
                    'Total amount saved:',
                    0,50000,0,100, "%f"
                )

brand, plan = st.beta_columns(2)
with brand:
    phone_brand = st.selectbox(
                'Select your phone brand: ',
                (
                    'vivo'
                    ,'Realme'
                    ,'OnePlus'
                    ,'HUAWEI'
                    ,'Apple'
                    ,'Asus'
                    ,'Samsung'
                    ,'Xiaomi'
                    ,'Google'
                    ,'OPPO'
                    ,'LGE'
                )
    )
with plan:
    data_plan = st.radio(
        'Data plan type:',
        ("Postpaid", "Prepaid")
    )

def formatloan(amount):
    return f"RM {amount}"

def geofile_name(name):
    if name == "Average traveling":
        return "profile1"
    elif name == "Traveling for work":
        return "profile2"
    elif name == "Frequently traveling":
        return "profile3"

@st.cache(allow_output_mutation=True)
def get_state(city):
    with open("citystate.json") as f:
        c = json.load(f)
        for state,j in c.items():
            if city.strip() in j:
                return state
            else:
                return "Not found"

# User type logic
applicant_type = st.radio(
        'Loan applicant type: ',
        ("Employee", "Gig economy worker", "Self Employed")
    )
if applicant_type=="Gig economy worker":
    st.header('Gig economy')
    col5, col6 = st.beta_columns(2)
    with col5:
        gig_platform = st.multiselect('What Gig services are you providing?',
                                ['Goget', 'Foodpanda', 'Lalamove', 'Bungkusit'])
        # print(gig_platform)

    with col6:
        timebase = st.selectbox(
            'What is your work basis for the Gig economy?',
            ('Full-time', 'Part-time')
        )
    # print(timebase)

    # Add a slider to the sidebar:
    # st.header('Activity')
    col7, col8 = st.beta_columns(2)
    spacer = ", "
    with col7:
        gig_duration = st.number_input(
                f'How many months so far working with {spacer.join(gig_platform)}',
                0,120,0,1, "%f"
            )
        gig_w_income = st.slider(
                f'How much is your average weekly income from {spacer.join(gig_platform)} (based on last month):',
                0, 6000, 310,
                format="RM %d"
            )

    with col8:
        gig_insur = st.radio(
            f'Are you covered by insurance under your work with {spacer.join(gig_platform)}',
            ("Yes", "Not sure", "No")
        )

    if timebase != "Full-time":
        # income = st.slider(
        #     f'How much is your monthly net income from {spacer.join(gig_platform)} (based on last month):',
        #     500, 6000, 2310,
        #     format="RM %d"
        # )
    #     continue
    # else:
        col9, col10 = st.beta_columns(2)
        with col9:
            industry = st.selectbox(
            'What industry you work for in your full-time job?',
            ('Public sector (General)'
            ,'Engineering'
            ,'Medical and Pharmaceutical'
            ,'Electrical & Electronics'
            ,'Environment'
            ,'Food Industry / Biotechnology'
            ,'Retail sector'
            ,'Construction'
            ,'Sport'
            ,'Information Technology'
            ,'Banking and Finance'
            ,'Manufacturing'
            ,'Media'
            ,'Professional (of any other industry)'
            )
        )
        with col10:
            income = st.number_input(
                    'How much is your monthly salary :',
                    0,30000,0,100, "%f"
                )

    weekly_gig_amount = np.random.randint(low=400, high=2000, size=8)
    # st.write(weekly_gig_amount)
    # st.write(weekly_gig_amount.mean())
    # st.write(np.median(weekly_gig_amount))
    # st.write(np.std(weekly_gig_amount))

    socmed_consumption_hours = np.random.randint(low=10, high=200, size=28)
    # st.write(socmed_consumption_hours)
    # st.write(socmed_consumption_hours.mean())
    # st.write(np.median(socmed_consumption_hours))
    # st.write(np.std(socmed_consumption_hours))

    # phone_manufactorer = phones[np.random.randint(0,len(phones),1)[0]]
    # Set viewport for the deckgl map
    # Load data
    st.header('Geo-location')
    profile_name = st.selectbox('Choose a geo-activity profile'
                ,['Average traveling', 'Traveling for work', 'Frequently traveling']
                )

    profile = geofile_name(profile_name)

    DATA_URL = (profile+'.csv')

    @st.cache(allow_output_mutation=True)
    def load_data():
        data = pd.read_csv(DATA_URL)
        return data

    # Load rows of data into the dataframe.
    df = load_data()
    view = pdk.ViewState(latitude=2.94485,
                        longitude=101.586463)

    # Create the scatter plot layer
    covidLayer = pdk.Layer(
            "HexagonLayer",
            data=df,
            pickable=False,
            opacity=0.3,
            stroked=True,
            filled=True,
            radius_scale=10,
            radius_min_pixels=5,
            radius_max_pixels=60,
            line_width_min_pixels=1,
            get_position=["Longitude", "Latitude"],
            get_fill_color=[180, 0, 200, 140],
            get_line_color=[255,0,0],
            tooltip="test test",
            elevation_scale=50,
            elevation_range=[0, 3000],
        )

    # Create the deck.gl map
    r = pdk.Deck(
        layers=[covidLayer],
        initial_view_state=view,
        map_style="mapbox://styles/mapbox/light-v10",
    )

    # Render the deck.gl map in the Streamlit app as a Pydeck chart 
    map = st.pydeck_chart(r)

    st.header('Loan')
    loan_amount = st.select_slider('How much do you want to borrow?', options=[300, 500, 800], format_func=formatloan)

    if pod_user == "Yes" and amount_saved >0:
        saved_value = np.log(amount_saved)
    else:
        saved_value = 0

    feature_dic = {
        "age_score": sqrt(age)%5 if age >=25 else 0,
        "marital_score": ["Single", "Married", "Widow", "Divorced"].index(marital_status),
        "education_score": ['SPM', 'Diploma', 'Associate degree', 'Degree', 'Masters', 'Phd'].index(education),
        "dependant_score": 0 if dependants == 0 else 2 if dependants < 4 else 1,
        "ncc_score": 1 if ncc ==0 else 0 if ncc==1 else -1,
        "pod_savings": saved_value
    }
    
    if get_state(address)=="Selangor" or get_state(address)=="Wilayah Persekutuan":
    
        finance_dic = {
            "total_squared_income": sqrt(gig_w_income*4)-5 if timebase=="Full-time" else sqrt(income+gig_w_income*4)-5,
            "weekly_squared_income": (sqrt(gig_w_income*4)/4.5)-5 if timebase=="Full-time" else (sqrt(income+gig_w_income*4)/4.5)-5,#sqrt(np.median(weekly_gig_amount)),
            "insure_score": 1 if gig_insur=="Yes" else 0,
            "duration_score": (gig_duration/10)*3,
            # "pod_user": 1 if pod_user=="Yes" else 0
            "Geo-activity_profile": 10 if profile_name=='Average traveling' else 1 if profile_name=='Traveling for work' else 0,
            "Location weightage": 5
        }
    else:
        finance_dic = {
        "total_squared_income": sqrt(gig_w_income*4) if timebase=="Full-time" else sqrt(income+gig_w_income*4),
        "weekly_squared_income": sqrt(gig_w_income*4)/4.5 if timebase=="Full-time" else sqrt(income+gig_w_income*4)/4.5,#sqrt(np.median(weekly_gig_amount)),
        "insure_score": 1 if gig_insur=="Yes" else 0,
        "duration_score": (gig_duration/10)*3,
        # "pod_user": 1 if pod_user=="Yes" else 0
        "Geo-activity_profile": 10 if profile_name=='Average traveling' else 1 if profile_name=='Traveling for work' else 0,
        "Location weightage": 0
    }

    if st.button("Evaluate", key="evaluate_gig_worker"):
        if (not timebase) or  (len(gig_platform) == 0):
            st.error('Sorry!! fields cannot be empty, please fill missing fields')
        else:
            'Loan Application is being evaluated...'
            # Add a placeholder
            latest_iteration = st.empty()
            bar = st.progress(0)

            rantot = np.random.randint(low=3, high=10, size=3)[0]
            # st.success('This is a success message!')
            # st.info('This is a purely informational message')
            for i in range(100):
                # Update the progress bar with each iteration.
                latest_iteration.text(f'Progress {i+1}%')
                bar.progress(i + 1)
                time.sleep(0.01)

            if sqrt(sum(feature_dic.values())) < 1.99:
                st.error('Loan application rejected due to high risk score!!')            
            else:
                if sqrt(sum(finance_dic.values())) <7.93:
                    st.success('Application successful, you are qualified for RM 300 loan')
                elif sqrt(sum(finance_dic.values())) >=7.93 and sqrt(sum(finance_dic.values())) < 8.89 and loan_amount==500:
                    st.success('Application successful, you are qualified for RM 500 loan')
                elif sqrt(sum(finance_dic.values())) >=7.93 and sqrt(sum(finance_dic.values())) < 8.89 and loan_amount==300:
                    st.success('Application successful, you are qualified for RM 300 loan')
                elif sqrt(sum(finance_dic.values())) >=7.93 and sqrt(sum(finance_dic.values())) < 8.89 and loan_amount>500:
                    st.warning(f'Application qualified for max RM 500 loan.')
                else:
                    st.success(f'Application successful, you are qualified for RM {loan_amount} loan.')


    if st.sidebar.checkbox('Pod Credit Scoring Result: '):
        # st.sidebar.write(feature_dic)
        # st.sidebar.write("Total applicant worthiness score ",sum(feature_dic.values()))
        st.sidebar.write("Total credit score: ",float("{:.2f}".format(sqrt(sum(feature_dic.values()))+sqrt(sum(finance_dic.values())))))
        st.sidebar.info('The minimum score is 9.9 and maximum 20.\napplication details has varying effect in the scoring computation as not all the details weighted equally. Education and being a pod user for a period of time can boost the score especially if coupled with good weekly/monthly income.')
        if st.sidebar.checkbox('Explore credit score: '):
            st.sidebar.write("Total applicant credibility factor ", float("{:.2f}".format(sqrt(sum(feature_dic.values())))))
            st.sidebar.write(feature_dic)
            st.sidebar.info('The minimum threshold to qualify is at least 2 points.\nThis score can be boosted if the person have higher education, older, or has no credit cards.')

            # st.sidebar.write("Total income ",income if timebase=="Full-time" else income+gig_w_income*4)
            # st.sidebar.write("Weekly median income ",np.median(weekly_gig_amount))
            # st.sidebar.write(finance_dic)
            # st.sidebar.write(sum(finance_dic.values()))
            st.sidebar.write("Total applicant finance hygiene ", float("{:.2f}".format(sqrt(sum(finance_dic.values())))))
            st.sidebar.write(finance_dic, get_state(address))
            st.sidebar.info('The minimum threshold is 7.9.\nThis finance can be improved if the person has higher income, covered by insurance, is a pod user, and or been in the gig economy for longer.')


if applicant_type=="Employee":
    st.header('Employee')
    industry = st.selectbox(
        'What industry you work in?',
        ('Public sector (General)'
        ,'Engineering'
        ,'Medical and Pharmaceutical'
        ,'Electrical & Electronics'
        ,'Environment'
        ,'Food Industry / Biotechnology'
        ,'Retail sector'
        ,'Construction'
        ,'Sport'
        ,'Information Technology'
        ,'Banking and Finance'
        ,'Manufacturing'
        ,'Media'
        ,"Academia and or Education"
        ,'Professional (of any other industry)'
        )
    )

    cola, colb = st.beta_columns(2)
    with cola:
        income = st.number_input(
                'Monthly salary :',
                0,30000,0,100, "%f"
            )
        insurance = st.radio(
            f'Do you have medical and life insurance under the employment benefit?',
            ("Yes", "Not sure", "No", "Only Medical")
        )
    with colb:
        experience = st.number_input(
                'Years of experience :',
                0,50,0,1, "%d"
            )
    # Load data
    st.header('Geo-location')
    profile_name = st.selectbox('Choose a geo-activity profile'
                ,['Average traveling', 'Traveling for work', 'Frequently traveling']
                )
    profile = geofile_name(profile_name)

    DATA_URL = (profile+'.csv')

    @st.cache(allow_output_mutation=True)
    def load_data():
        data = pd.read_csv(DATA_URL)
        return data

    # Load rows of data into the dataframe.
    df = load_data()
    view = pdk.ViewState(latitude=2.94485,
                        longitude=101.586463)

    # Create the scatter plot layer
    covidLayer = pdk.Layer(
            "HexagonLayer",
            data=df,
            pickable=False,
            opacity=0.3,
            stroked=True,
            filled=True,
            radius_scale=10,
            radius_min_pixels=5,
            radius_max_pixels=60,
            line_width_min_pixels=1,
            get_position=["Longitude", "Latitude"],
            get_fill_color=[180, 0, 200, 140],
            get_line_color=[255,0,0],
            tooltip="test test",
            elevation_scale=50,
            elevation_range=[0, 3000],
        )

    # Create the deck.gl map
    r = pdk.Deck(
        layers=[covidLayer],
        initial_view_state=view,
        map_style="mapbox://styles/mapbox/light-v10",
    )

    # Render the deck.gl map in the Streamlit app as a Pydeck chart 
    map = st.pydeck_chart(r)

    st.header('Loan')
    loan_amount = st.select_slider('How much do you want to borrow?', options=[300, 500, 800], format_func=formatloan)

    if pod_user == "Yes" and amount_saved >0:
        saved_value = np.log(amount_saved)
    elif pod_user == "Yes" and amount_saved ==0:
        saved_value = 1
    else:
        saved_value = 0

    feature_dic = {
        "age_score": sqrt(age)%5 if age >=25 else 0,
        "marital_score": ["Single", "Married", "Widow", "Divorced"].index(marital_status),
        "education_score": ['SPM', 'Diploma', 'Associate degree', 'Degree', 'Masters', 'Phd'].index(education),
        "dependant_score": 0 if dependants == 0 else 2 if dependants < 4 else 1,
        "ncc_score": 1 if ncc ==0 else 0 if ncc==1 else -1,
        "pod_savings_score": saved_value
    }
    
    if get_state(address)=="Selangor" or get_state(address)=="Wilayah Persekutuan":
    
        finance_dic = {
            "total_squared_income": sqrt(income),
            "weekly_squared_income": (sqrt(income)/4.5),#sqrt(np.median(weekly_gig_amount)),
            "insure_score": 2 if insurance=="Yes" else 1 if insurance=="Only Medical" else 0,
            "duration_score": (experience/10)*3,
            "Geo-activity_profile": 10 if profile_name=='Average traveling' else 1 if profile_name=='Traveling for work' else 0,
            # "Location weightage": 5
        }
    else:
        finance_dic = {
            "total_squared_income": sqrt(income),
                "weekly_squared_income": (sqrt(income)/4.5),#sqrt(np.median(weekly_gig_amount)),
                "insure_score": 2 if insurance=="Yes" else 1 if insurance=="Only Medical" else 0,
                "duration_score": (experience/10)*3,
                "Geo-activity_profile": 10 if profile_name=='Average traveling' else 1 if profile_name=='Traveling for work' else 0,
                # "Location weightage": 0
        }

    if st.button("Evaluate", key="evaluate_employee"):
        if (not income) or  (not experience):
            st.error('Sorry!! fields cannot be empty, please fill missing fields')
        else:
            'Loan Application is being evaluated...'
            # Add a placeholder
            latest_iteration = st.empty()
            bar = st.progress(0)

            rantot = np.random.randint(low=3, high=10, size=3)[0]
            # st.success('This is a success message!')
            # st.info('This is a purely informational message')
            for i in range(100):
                # Update the progress bar with each iteration.
                latest_iteration.text(f'Progress {i+1}%')
                bar.progress(i + 1)
                time.sleep(0.01)

            if sqrt(sum(feature_dic.values())) < 1.99:
                st.error('Loan application rejected due to high risk score!!')            
            else:
                if sqrt(sum(finance_dic.values())) <7.93:
                    st.success('Application successful, you are qualified for RM 300 loan')
                elif sqrt(sum(finance_dic.values())) >=7.93 and sqrt(sum(finance_dic.values())) < 8.89 and loan_amount==500:
                    st.success('Application successful, you are qualified for RM 500 loan')
                elif sqrt(sum(finance_dic.values())) >=7.93 and sqrt(sum(finance_dic.values())) < 8.89 and loan_amount==300:
                    st.success('Application successful, you are qualified for RM 300 loan')
                elif sqrt(sum(finance_dic.values())) >=7.93 and sqrt(sum(finance_dic.values())) < 8.89 and loan_amount>500:
                    st.warning(f'Application qualified for max RM 500 loan.')
                else:
                    st.success(f'Application successful, you are qualified for RM {loan_amount} loan.')



    if st.sidebar.checkbox('Pod Credit Scoring Result: '):
        # st.sidebar.write(feature_dic)
        # st.sidebar.write("Total applicant worthiness score ",sum(feature_dic.values()))
        st.sidebar.write("Total credit score: ",float("{:.2f}".format(sqrt(sum(feature_dic.values()))+sqrt(sum(finance_dic.values())))))
        st.sidebar.info('The minimum score is 9.9 and maximum 20.\napplication details has varying effect in the scoring computation as not all the details weighted equally. Education and being a pod user for a period of time can boost the score especially if coupled with good weekly/monthly income.')
        if st.sidebar.checkbox('Explore credit score: '):
            st.sidebar.write("Total applicant credibility factor ", float("{:.2f}".format(sqrt(sum(feature_dic.values())))))
            st.sidebar.write(feature_dic)
            st.sidebar.info('The minimum threshold to qualify is at least 2 points.\nThis score can be boosted if the person have higher education, older, or has no credit cards.')

            # st.sidebar.write("Total income ",income if timebase=="Full-time" else income+gig_w_income*4)
            # st.sidebar.write("Weekly median income ",np.median(weekly_gig_amount))
            # st.sidebar.write(finance_dic)
            # st.sidebar.write(sum(finance_dic.values()))
            st.sidebar.write("Total applicant finance hygiene ", float("{:.2f}".format(sqrt(sum(finance_dic.values())))))
            # st.sidebar.write(finance_dic, get_state(address))
            st.sidebar.info('The minimum threshold is 7.9.\nThis finance can be improved if the person has higher income, covered by insurance, is a pod user, and or been in the gig economy for longer.')



if applicant_type=="Self Employed":
    st.header('Self Employed')
    industry = st.selectbox(
        'Industry: ',
        ('IT Freelancing'
        ,'Engineering'
        ,'Medical and Pharmaceutical'
        ,'Electrical & Electronics'
        ,'Environment'
        ,'Food Industry / Biotechnology'
        ,'Retail sector'
        ,'Construction'
        ,'Sport'
        ,'Information Technology'
        ,'Banking and Finance'
        ,'Manufacturing'
        ,'Media'
        ,"Academia and or Education"
        ,'Professional (of any other industry)'
        )
    )

    coli, colii = st.beta_columns(2)
    with coli:
        income = st.number_input(
                'Monthly Revenue :',
                0,150000,3000,1000, "%f"
            )
    with colii:
        experience = st.number_input(
                'Years in business :',
                0,50,1,1, "%d"
            )
        
    coliii, colvi = st.beta_columns(2)
    with coliii:
        insurance = st.radio(
            f'Do you have medical and life insurance under the employment benefit?',
            ("Yes", "Not sure", "No", "Only Medical")
        )
        
    with colvi:
        typeofbusiness = st.radio(
            'Registration type of business',
            ("Enterprise", "Sole proprietorship", "SDN BHD", "Not registered")
        )
        business_reg_num = st.text_input("Business registration number")

    # Load data
    st.header('Geo-location')
    profile_name = st.selectbox('Choose a geo-activity profile'
                ,['Average traveling', 'Traveling for work', 'Frequently traveling']
                )
    profile = geofile_name(profile_name)

    DATA_URL = (profile+'.csv')

    @st.cache(allow_output_mutation=True)
    def load_data():
        data = pd.read_csv(DATA_URL)
        return data

    # Load rows of data into the dataframe.
    df = load_data()
    view = pdk.ViewState(latitude=2.94485,
                        longitude=101.586463)

    # Create the scatter plot layer
    covidLayer = pdk.Layer(
            "HexagonLayer",
            data=df,
            pickable=False,
            opacity=0.3,
            stroked=True,
            filled=True,
            radius_scale=10,
            radius_min_pixels=5,
            radius_max_pixels=60,
            line_width_min_pixels=1,
            get_position=["Longitude", "Latitude"],
            get_fill_color=[180, 0, 200, 140],
            get_line_color=[255,0,0],
            tooltip="test test",
            elevation_scale=50,
            elevation_range=[0, 3000],
        )

    # Create the deck.gl map
    r = pdk.Deck(
        layers=[covidLayer],
        initial_view_state=view,
        map_style="mapbox://styles/mapbox/light-v10",
    )

    # Render the deck.gl map in the Streamlit app as a Pydeck chart 
    map = st.pydeck_chart(r)

    st.header('Loan')
    loan_amount = st.select_slider('How much do you want to borrow?', options=[300, 500, 800], format_func=formatloan)

    if pod_user == "Yes" and amount_saved >0:
        saved_value = np.log(amount_saved)
    elif pod_user == "Yes" and amount_saved ==0:
        saved_value = 1
    else:
        saved_value = 0

    feature_dic = {
        "age_score": sqrt(age)%5 if age >=25 else 0,
        "marital_score": ["Single", "Married", "Widow", "Divorced"].index(marital_status),
        "education_score": ['SPM', 'Diploma', 'Associate degree', 'Degree', 'Masters', 'Phd'].index(education),
        "dependant_score": 0 if dependants == 0 else 2 if dependants < 4 else 1,
        "ncc_score": 1 if ncc ==0 else 0 if ncc==1 else -1,
        "pod_savings_score": saved_value
    }
    
    if get_state(address)=="Selangor" or get_state(address)=="Wilayah Persekutuan":
    
        finance_dic = {
            "total_squared_income": sqrt(income),
            "weekly_squared_income": (sqrt(income)/4.5),#sqrt(np.median(weekly_gig_amount)),
            "insure_score": 2 if insurance=="Yes" else 1 if insurance=="Only Medical" else 0,
            "duration_score": (experience/10)*3,
            "Geo-activity_profile": 10 if profile_name=='Average traveling' else 1 if profile_name=='Traveling for work' else 0,
            # "Location weightage": 5
        }
    else:
        finance_dic = {
            "total_squared_income": sqrt(income),
                "weekly_squared_income": (sqrt(income)/4.5),#sqrt(np.median(weekly_gig_amount)),
                "insure_score": 2 if insurance=="Yes" else 1 if insurance=="Only Medical" else 0,
                "duration_score": (experience/10)*3,
                "Geo-activity_profile": 10 if profile_name=='Average traveling' else 1 if profile_name=='Traveling for work' else 0,
                # "Location weightage": 0
        }

    if st.button("Evaluate", key="evaluate_selfemployed"):
        if (not income) or  (not experience) or (not business_reg_num):
            st.error('Sorry!! fields cannot be empty, please fill missing fields')
        else:
            'Loan Application is being evaluated...'
            # Add a placeholder
            latest_iteration = st.empty()
            bar = st.progress(0)

            rantot = np.random.randint(low=3, high=10, size=3)[0]
            # st.success('This is a success message!')
            # st.info('This is a purely informational message')
            for i in range(100):
                # Update the progress bar with each iteration.
                latest_iteration.text(f'Progress {i+1}%')
                bar.progress(i + 1)
                time.sleep(0.01)

            if sqrt(sum(feature_dic.values())) < 1.99:
                st.error('Loan application rejected due to high risk score!!')            
            else:
                if sqrt(sum(finance_dic.values())) <7.93:
                    st.success('Application successful, you are qualified for RM 300 loan')
                elif sqrt(sum(finance_dic.values())) >=7.93 and sqrt(sum(finance_dic.values())) < 8.89 and loan_amount==500:
                    st.success('Application successful, you are qualified for RM 500 loan')
                elif sqrt(sum(finance_dic.values())) >=7.93 and sqrt(sum(finance_dic.values())) < 8.89 and loan_amount==300:
                    st.success('Application successful, you are qualified for RM 300 loan')
                elif sqrt(sum(finance_dic.values())) >=7.93 and sqrt(sum(finance_dic.values())) < 8.89 and loan_amount>500:
                    st.warning(f'Application qualified for max RM 500 loan.')
                else:
                    st.success(f'Application successful, you are qualified for RM {loan_amount} loan.')

    if st.sidebar.checkbox('Pod Credit Scoring Result: '):
        # st.sidebar.write(feature_dic)
        # st.sidebar.write("Total applicant worthiness score ",sum(feature_dic.values()))
        st.sidebar.write("Total credit score: ",float("{:.2f}".format(sqrt(sum(feature_dic.values()))+sqrt(sum(finance_dic.values())))))
        st.sidebar.info('The minimum score is 9.9 and maximum 20.\napplication details has varying effect in the scoring computation as not all the details weighted equally. Education and being a pod user for a period of time can boost the score especially if coupled with good weekly/monthly income.')
        if st.sidebar.checkbox('Explore credit score: '):
            st.sidebar.write("Total applicant credibility factor ", float("{:.2f}".format(sqrt(sum(feature_dic.values())))))
            st.sidebar.write(feature_dic)
            st.sidebar.info('The minimum threshold to qualify is at least 2 points.\nThis score can be boosted if the person have higher education, older, or has no credit cards.')

            # st.sidebar.write("Total income ",income if timebase=="Full-time" else income+gig_w_income*4)
            # st.sidebar.write("Weekly median income ",np.median(weekly_gig_amount))
            # st.sidebar.write(finance_dic)
            # st.sidebar.write(sum(finance_dic.values()))
            st.sidebar.write("Total applicant finance hygiene ", float("{:.2f}".format(sqrt(sum(finance_dic.values())))))
            # st.sidebar.write(finance_dic, get_state(address))
            st.sidebar.write(finance_dic)
            st.sidebar.info('The minimum threshold is 7.9.\nThis finance can be improved if the person has higher income, covered by insurance, is a pod user, and or been in the gig economy for longer.')
