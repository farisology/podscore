import time
import numpy as np
from math import sqrt
import streamlit as st

st.title('Pod Intelligent Worthiness Score')


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
        'What is your highest attained education level?',
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
with col4:
    marital_status = st.radio(
        'What is your marital status?',
        ("Single", "Married", "Widow", "Divorced")
    )
    pod_user = st.radio(
        'Do you have a saving account with pod?',
        ("No", "Not actively saving", "Yes")
    )


# Add a selectbox to the sidebar:
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

with col8:
    gig_insur = st.radio(
        f'Are you covered by insurance under your work with {spacer.join(gig_platform)}',
        ("Yes", "Not sure", "No")
    )

if timebase == "Full-time":
    income = st.slider(
        'How much is your monthly net income (based on last month):',
        500, 6000, 2310,
        format="RM %d"
    )
else:
    col9, col10 = st.beta_columns(2)
    with col9:
        income = st.number_input(
                'How much is your monthly salary :',
                0,30000,0,100, "%f"
            )
    with col10:
        gig_income = st.slider(
            f'How much is your monthly income from {spacer.join(gig_platform)} (based on last month):',
            500, 6000, 2310,
            format="RM %d"
        )
# print(trips)
# print(income)

def formatloan(amount):
    return f"RM {amount}"

st.header('Loan')
loan_amount = st.select_slider('How much do you want to borrow?', options=[300, 500, 800], format_func=formatloan)

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

feature_dic = {
    "age_score": sqrt(age)%5 if age >=25 else 0,
    "marital_score": ["Single", "Married", "Widow", "Divorced"].index(marital_status),
    "education_score": ['SPM', 'Diploma', 'Associate degree', 'Degree', 'Masters', 'Phd'].index(education),
    "dependant_score": 0 if dependants == 0 else 2 if dependants < 4 else 1,
    "ncc_score": 1 if ncc ==0 else 0 if ncc==1 else -1
}

finance_dic = {
    "total_squared_income": sqrt(income) if timebase=="Full-time" else sqrt(income+gig_income),
    "weekly_squared_income": sqrt(income)/4.5 if timebase=="Full-time" else sqrt(income+gig_income)/4.5,#sqrt(np.median(weekly_gig_amount)),
    "insure_score": 1 if gig_insur=="Yes" else 0,
    "duration_score": (gig_duration/10)*3,
    "pod_user": 1 if pod_user=="Yes" else 0
}
if st.button("Evaluate"):
    if (not timebase) or  (len(gig_platform) == 0) or not income:
        st.warning('Sorry!! fields cannot be empty, please fill missing fields')
    else:
        'Starting a long computation...'
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
            elif sqrt(sum(finance_dic.values())) >=7.93 and sqrt(sum(finance_dic.values())) < 8.89:
                st.success('Application successful, you are qualified for RM 500 loan')
            else:
                st.success(f'Application successful, you are qualified for RM {loan_amount} loan.')


if st.sidebar.checkbox('Explore worthiness score: '):
    # st.sidebar.write(feature_dic)
    # st.sidebar.write("Total applicant worthiness score ",sum(feature_dic.values()))
    st.sidebar.write("Total applicant credibility factor ", float("{:.2f}".format(sqrt(sum(feature_dic.values())))))
    st.sidebar.info('The minimum threshold to qualify is at least 2 points.\nThis score can be boosted if the person have higher education, older, or has no credit cards.')

    # st.sidebar.write("Total income ",income if timebase=="Full-time" else income+gig_income)
    # st.sidebar.write("Weekly median income ",np.median(weekly_gig_amount))
    # st.sidebar.write(finance_dic)
    # st.sidebar.write(sum(finance_dic.values()))
    st.sidebar.write("Total applicant finance hygiene ", float("{:.2f}".format(sqrt(sum(finance_dic.values())))))
    st.sidebar.info('The minimum threshold is 7.9.\nThis finance can be improved if the person has higher income, covered by insurance, is a pod user, and or been in the gig economy for longer.')