import time
import numpy as np
import streamlit as st

st.title('Pod Intelligent Worthiness Score')


# Add a selectbox to the sidebar:
st.header('Gig economy')
option = st.multiselect('What Gig services are you providing?',
                        ['Goget', 'Foodpanda', 'Lalamove', 'Bungkusit'])
# print(option)

timebase = st.selectbox(
    'What your work for the Gig economy?',
    ('Full-time', 'Part-time')
)
# print(timebase)

# Add a slider to the sidebar:
st.header('Activity')
trips = st.slider(
    'Select the range of total number of trips per day:',
    5, 100, (25, 75)
    ,format="%d trips daily"
)

income = st.slider(
    'What is your monthly net income (based on last month):',
    500, 6000, 2310,
    format="%d RM"
)
print(trips)
print(income)

loan_amount = st.slider('How much do you want to borrow?', 300, 800, 500, format="%d RM")

if st.checkbox('Explore worthiness score: '):
    if (not timebase) or  (len(option) == 0) or (len(trips) == 0) or not income:
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

        if income > 3500:
            st.success(f'Application successful, you are qualified for RM {loan_amount}')

        else: 
            if trips[1] > 50:
                if trips[1] - trips[0] < 20 and loan_amount < 500:
                    st.success(f'Application successful, you are qualified for RM {loan_amount}')
                elif loan_amount > 499 and income > 2499:
                    st.success('Application successful, you are qualified for RM 400')
                # elif income 
                else:
                    st.success('Application successful, you are qualified for RM 300')
            else:
                if income > 2000:
                    st.success('Application successful, you are qualified for RM 400')
                elif income > 1500:
                    st.success('Application successful, you are qualified for RM 300')
                else:
                    st.warning('Application insuccessful, start a goal with pod toqualify for RM 300 in the next month.')