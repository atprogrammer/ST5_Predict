import tensorflow as tf
from tensorflow import keras
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pickle



_model = keras.models.load_model("my_model")


# x_test =[[0.251717,1,1,1,1,0,1,0,0,0,0,0,0]]
# Z = _model.predict(x_test)
# class_names = ['no', 'yes']
# pred_class = class_names[np.argmax(Z)]


col1,col2,col3 = st.columns(3)
#with col2:
    #st.image("./pics/AIAT-NO-BG.png", caption=None, width=200, use_column_width=None, clamp=False, channels='RGB',output_format='auto')
st.title('ประเมินพลังใจ(RQ) และทำนายผลภาวะเครียด')

#sex = st.selectbox('กรุณาเลือกประเภทผู้ประเมิน', ['ชาย','หญิง'], key='1')

age = st.number_input("กรุณาระบุอายุ : ", min_value=0, max_value=100, value=18, step=1)

#type_data = st.selectbox('กรุณาเลือกประเภทผู้ประเมิน', ['ประชาชนทั่วไป','เจ้าหน้าที่สาธารณสุข','อสม','บุคคลากรทางการศึกษา','ผู้สัมผัสโรคโควิดหรือเสี่ยงสูง','พระภิกษุ/สามเณร/นักบวช/ผู้นำศาสนา','เจ้าหน้าที่หน่วยงานสังกัดอื่น'], key='2')


st.text("ในช่วง 2 สัปดาห์ที่ผ่านมา ท่านมีความเชื่อมั่นในประเด็นต่างๆ ต่อไปนี้เพียงใด โดย 1 หมายถึง น้อย และ 10 หมายถึง มาก")
rq1 = st.slider( "1.) ความยากลำบากทำให้ฉันแกร่งขึ้น : ", min_value=0 , max_value=10 ,value=5 , step=1)
rq2 = st.slider( "2.) ฉันมีกำลังใจและได้รับการสนับสนุนจากคนรอบข้าง : ", min_value=0 , max_value=10 ,value=5 , step=1)
rq3 = st.slider( "3.) การแก้ไขปัญหาทำให้ฉันมีประสบการณ์มากขึ้น : ", min_value=0 , max_value=10 ,value=5 , step=1)


# if type_data == 'บุคคลากรทางการศึกษา':
#     t1 = 1;t2 = 0;t3 = 0
#     t4 = 0;t5 = 0;t6 = 0
#     t7 = 0
# elif type_data == 'ประชาชนทั่วไป':
#     t1 = 0;t2 = 1;t3 = 0
#     t4 = 0;t5 = 0;t6 = 0
#     t7 = 0
# elif type_data == 'ผู้สัมผัสโรคโควิดหรือเสี่ยงสูง':
#     t1 = 0;t2 = 0;t3 = 1
#     t4 = 0;t5 = 0;t6 = 0
#     t7 = 0
# elif type_data == 'พระภิกษุ/สามเณร/นักบวช/ผู้นำศาสนา':
#     t1 = 0;t2 = 0;t3 = 0
#     t4 = 1;t5 = 0;t6 = 0
#     t7 = 0
# elif type_data == 'อสม':
#     t1 = 0;t2 = 0;t3 = 0
#     t4 = 0;t5 = 1;t6 = 0
#     t7 = 0
# elif type_data == 'เจ้าหน้าที่สาธารณสุข':
#     t1 = 0;t2 = 0;t3 = 0
#     t4 = 0;t5 = 0;t6 = 1
#     t7 = 0
# elif type_data == 'เจ้าหน้าที่หน่วยงานสังกัดอื่น':
#     t1 = 0;t2 = 0;t3 = 0
#     t4 = 0;t5 = 0;t6 = 0
#     t7 = 1


submit = st.button('ทำนาย')
if submit:
            # if sex == 'ชาย' :
            #     male = 1
            #     female = 0
            # else :
            #     male = 0
            #     female = 1

            res_age = age / 100
            
            txt_rq = ""
            sum_rq = rq1+rq2+rq3
            if sum_rq >= 24 and sum_rq <= 30:
                txt_rq = "พลังใจ RQ ระดับมาก"
            elif sum_rq >= 15 and sum_rq <= 23:
                txt_rq = "พลังใจ RQ ระดับปานกลาง"
            else:
                txt_rq = "พลังใจ RQ ระดับน้อย"

            x_test =[[res_age,(rq1/10),(rq2/10),(rq3/10)]]
            #x_test =[[1,1,1,1,1,0,1,1,1,1,1,1,1]]
            Z = _model.predict(x_test)
            class_names = ['no', 'yes']
            pred_class = class_names[np.argmax(Z)]
            if pred_class == 'no':
                st.balloons()
                st.success(txt_rq)
                st.success('คุณไม่มีภาวะเสี่ยงความเครียด')
            else:
                st.success(txt_rq)
                st.error("คุณอาจจะมีความเครียดสะสม")
