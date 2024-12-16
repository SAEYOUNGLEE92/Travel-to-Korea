import streamlit as st


exchange_rates = {
    '중국': 6.5,   
    '일본': 110.0,  
    '러시아': 74.0, 
    '대만': 28.0,   
    '한국': 1400.0  
}


currency_names = {
    '중국': 'CNY',
    '일본': 'JPY',
    '러시아': 'RUB',
    '대만': 'TWD',
    '한국': 'KRW'
}


st.title("💱 환율 계산기")


usd_amount = st.number_input("USD로 가격을 입력하세요:", min_value=0.0, step=1.0)


selected_country = st.selectbox("환전할 나라를 선택하세요:", list(exchange_rates.keys()))


if st.button("계산"):
    if selected_country in exchange_rates:
        converted_amount = usd_amount * exchange_rates[selected_country]
        currency_code = currency_names[selected_country]
        st.success(f"{usd_amount} USD는 {converted_amount:.2f} {currency_code}입니다.")