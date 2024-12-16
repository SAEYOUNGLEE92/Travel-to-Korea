import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False

font_path = 'NanumGothic.ttf'
font_manager.fontManager.addfont(font_path)
rc('font', family='NanumGothic')




excel_file = 'visitkoreadata.xlsx'
xls = pd.ExcelFile(excel_file, engine='openpyxl')


sheet_names = xls.sheet_names


st.title('📈 잠재 방한 여행객의 주요 특성을 알아보자')

st.markdown("---")

st.write("1️⃣ 잠재 방한 여행객의 주요 특성을 알아봅시다.")
selected_sheet = st.selectbox("아래 버튼을 클릭하여 알고 싶은 특성을 선택하세요:", sheet_names)

df = pd.read_excel(xls, sheet_name=selected_sheet)


df['%'] = pd.to_numeric(df['%'], errors='coerce') 




st.markdown("<hr style='border: 1px dashed #ccc;'>", unsafe_allow_html=True)


st.write("📍 위 내용에 대한 잠재 방한 여행객의 특성은 다음과 같습니다.")
st.dataframe(df)
st.caption("※ 결과값은 소숫점 첫째자리까지 나타내었습니다.")

try:

    categories = df.iloc[:, 0]  
    values = df['%']  


    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title(selected_sheet)


    st.pyplot(fig)
except Exception as e:
    st.error(f"그래프를 생성하는 중 오류가 발생했습니다: {e}")




st.markdown("---")
    

st.write("2️⃣ 표와 그래프를 살펴보고, 1~9에 해당하는 데이터를 분석하여 '여행 프로그램 제작 시 고려할 내용'을 생각하여 봅시다.")
input_text = st.text_area("	💬 아래의 빈 칸에 1~9번을 분석한 내용을 모두 작성한 후 전송 버튼을 눌러주세요.")
st.caption("※ 여러번 전송 버튼을 누르면, 마지막에 입력한 내용만 저장됩니다.")



if st.button("전송"):

    temp_file = os.path.join("temp", "[2차시] 여행 프로그램 구성에 반영할 내용_input.txt")
    os.makedirs("temp", exist_ok=True) 

 
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(input_text)
    
    st.success("내용이 저장되었습니다. 해당 내용은 '[2차시] 여행 프로그램 구성에 반영할 내용'에서 확인할 수 있습니다.")

st.markdown("---")

st.write("📍 모든 과정을 마친 학생은 완료 버튼을 눌러주세요.")




if st.button("완료"):
  
    st.warning(" 🧡 1차시 수업 완료를 축하합니다! '[2차시] 여행 프로그램 구성에 반영할 내용'버튼을 눌러 학습을 시작해봅시다 🧡")
