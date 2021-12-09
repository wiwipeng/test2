import streamlit as st
ar_simulation = {'gas_warning':1, 'speed_limit':100, 'temp_warning':30, 'turn':12000}
gas = st.number_input('油量的資料收集:油箱滿是10格 =>')
speed= st.number_input('車速的資料收集:限速100 =>')
temp = st.number_input('溫度的資料收集:限溫30 =>')
tur=int(input('轉速資料的收集:限轉12000 =>'))
import streamlit as st
if cofirm_input:
      st.write('第六組')
   if gas <= car_simulation.get('gas_warning'):
      st.write('油箱只剩', gas, '格! 準備加油!!')
   else:
      st.write('油箱還剩', gas, '格。')
   if speed>=car_simulation.get('speed_limit'):
      st.write('即將超速')
   else:
      st.write('安全')
   if temp>=car_simulation.get('temp_warning'):
      st.write('過熱')
   else:
      st.write('正常')
   if tur>=car_simulation.get('turn'):
      st.write('即將超過轉速')
   else:
      st.write('正常')
