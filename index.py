import os
import boto3
import json
import streamlit as st

my_list = []

current_directory = os.getcwd()
print(current_directory)

access_key = "AKIA3RSDCY4Z6PFUVFOJ"
secret_access_key = "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"

bedrock_runtime_client = boto3.client("bedrock-runtime", region_name="us-west-2", 
                                      aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)




body = {
    "prompt": prompt,
    "temperature": 0.5,
    "maxTokens": 200,
}

response = bedrock_runtime_client.invoke_model(
    modelId="ai21.j2-ultra-v1", body=json.dumps(body)
)

response_body = json.loads(response["body"].read())
response_text = response_body["completions"][0]["data"]["text"]

print(response_text)


###########

# 페이지 설정
st.set_page_config(page_title="Symptom Checker", layout="wide")

# CSS 스타일링
st.markdown("""
<style>
.main-header {
    font-size: 40px;
    font-weight: bold;
    color: #0E6EB8;
    text-align: center;
}
.sidebar-style {
    background-color: #F0F2F6;
    padding: 10px;
}
.centered-image {
    display: flex;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

# # 로고 이미지 중앙 정렬
# logo_url = "https://media.npr.org/assets/img/2020/05/05/gettyimages-1216219034_custom-ac3b85749e505dce5dc0db3d086287ad732dd33a.jpg"
# st.markdown(f'<div class="centered-image"><img src="{logo_url}" width="500"></div>', unsafe_allow_html=True)

# 제목
st.markdown('<div class="main-header">Symptom Checker</div>', unsafe_allow_html=True)



# 사이드바 스타일링
with st.sidebar:
    st.markdown('<div class="sidebar-style">', unsafe_allow_html=True)
    st.write("## Symptom Checker Guide")
    st.write("Enter your symptoms and find out possible diseases.")
    st.markdown('</div>', unsafe_allow_html=True)

symptoms = st.text_input("What are your symptoms?", key="symptoms")

if st.button("Find Possible Disease", key="find_disease"):
    if "headache" in symptoms.lower():
        st.success("Possible diseases could be: Migraine, Tension headache")
    elif "fever" in symptoms.lower():
        st.warning("Possible diseases could be: Influenza, COVID-19, Common cold")
    elif "stomachache" in symptoms.lower():
        st.error("Possible diseases could be: Gastroenteritis, Indigestion")
    else:
        st.info("Symptoms are not specific. Please consult a doctor for a proper diagnosis.")

# Create a image
col1, col2, col3 = st.columns(3)

with col1:
    st.image("data/Back_pain.webp", width=180)
    if st.button('Back Pain', key='1'):
        my_list.append("Back Pain")
        st.write('Added')

with col2:
    st.image("data/Coughing.jpeg", width=150)
    if st.button('Coughing', key='2'):
        my_list.append("Coughing")
        st.write('Added')
with col3:
    st.image("data/Difficulty_breathing.jpeg", width=150)
    if st.button('Difficulty in breathing', key='3'):
        my_list.append("Difficulty in breathing")
        st.write('Added')

# Row 2
col4, col5, col6 = st.columns(3)

with col4:
    st.image("data/Fever.jpeg", width=150)
    if st.button('Fever', key='4'):
        my_list.append("Coughing")
        st.write('Added')

with col5:
    st.image('data/Joint_pain.jpeg', width=150)
    if st.button('Joint Pain', key='5'):
        my_list.append("Joint Pain")
        st.write('Added')

with col6:
    st.image("data/Nausea.jpeg", width=150)
    if st.button('Nausea', key='6'):
        my_list.append("Nausea")
        st.write('Added')

# Row 3
col7, col8, col9 = st.columns(3)

with col7:
    st.image("data/Neck_pain.jpg", width=150)
    if st.button('Neck Pain', key='7'):
        my_list.append("Coughing")
        st.write('Added')

with col8:
    st.image("data/Sore_throat.webp", width=150)
    if st.button('Sore Throat', key='8'):
        my_list.append("Sore Throat")
        st.write('Added')

with col9:
    st.image("data/Vomit.jpeg", width=180)
    if st.button('Vomit', key='9'):
        my_list.append("Vomit")
        st.write('Added')

st.write(my_list)

# 확장 섹션
with st.expander("About us"):
    st.write("""
        This is a symptom checker. Please note that this tool is not a replacement for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.
    """)

prompt = "I feel sick, my symptoms are following."
prompt += ' '.join(str(element) for element in my_list)


# 버튼 스타일링
st.markdown('<style>.stButton>button{background-color:#0A9396;color:white;border-radius:5px;padding:10px 15px;}</style>', unsafe_allow_html=True)
