"""创建聊天机器人界面，接受用户输入并生成输出的模块"""
import streamlit as st
from streamlit_chat import message


st.set_page_config(
    page_title="生物医学聊天机器人"
)
st.header("生物医学LLM聊天机器人")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''这是一个Web应用程序，允许您与EHR知识图谱，提出生物医学问题或一般问题。'''
    )
st.sidebar.info('''在输入框中输入查询，然后按回车键以接收响应''')

st.sidebar.info('''该应用程序正在积极开发中。有几个问题需要修复''')

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


model = st.radio(
    "你想执行什么任务？",
    ('生物医学KG问答', '生物医学问答', '一般问答'))

if model == '生物医学KG问答':
    st.text("这是药物、制造商和结果的医学KG")
    from gpt import *
if model == '生物医学问答':
    from biogpt import *
if model =='一般问答':
    from falcon import *


user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
