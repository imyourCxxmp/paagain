import streamlit as st
import pandas as pd
import json
import openai

user_api_key = st.sidebar.text_input("OpenAI API key", type="password")
client = openai.OpenAI(api_key=user_api_key)
prompt = """Act as an english exam writer who want student to develop their reading comprehension skills. 
1.Your task is generating reading comprehension exam from keyword provided by user. 
2.You have to fact check and prove before using the information.
3.The article should be 100-200 words , vocabulary should be B1-B2 following the CEFR level and grammar must correct and no error.
4.The exam should be 5 questions with 4 multiple choice which is complex and challenging that require deeper comprehension and interpretation.
5.Then, you have to provide the answer key description with proper reasons for every questions in the table.
"""

st.title('Reading exam generator')
st.markdown('AI ช่วยแต่งข้อสอบพาร์ต Reading เพียงแค่เขียน keyword ที่จะต้องการ \n Article จะมีความยาว 400-500 คำ ความยากระดับ B1-B2 และมีข้อสอบทั้งหมด 10 ข้อ')
user_input = st.text_area('text your keyword here')

if st.button('Click'):
    messages_so_far = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': user_input},
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_so_far
    )
    st.markdown('**AI response:**')
    answer = response.choices[0].message.content
    sd = json.loads(answer)

    print (sd)
    ans = pd.DataFrame.from_dict(sd)
    print(ans)
    st.table(ans)

