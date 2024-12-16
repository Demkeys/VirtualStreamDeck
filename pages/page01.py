# This page is debug only.

import streamlit as st
import datastorage as ds

st.set_page_config(layout='wide')

def btn_callback(*args, **kwargs):
    st.write(ds.something01)
    ds.something01 += 1
    # st.write(kwargs['some01'])

def test01(*args, **kwargs):
    st.write(kwargs)
    st.text(args)

test01(*(1,2,3), **{'some01':1,'some01_1':2}, **{'some02':5})

st.slider('SomeSlider01')

st.button('SomeBtn01',on_click=btn_callback,
          kwargs={'some01':'test'})
st.button('SomeBtn02',on_click=btn_callback,args=[0],
          kwargs={'some01':'test02'})


st.write('This is page01')
col01, col02, col03, col04, col05 = st.columns(5)

with col01:
    st.button('b010000000000000000000000000',use_container_width=True)
    st.button('b010000000000000000000000000_1',use_container_width=True)
    st.button('b010000000000000000000000000_2',use_container_width=True)
    st.button('b010000000000000000000000000_3',use_container_width=True)
with col02:
    st.button('b020000000000000000000000000',use_container_width=True)
    st.button('b020000000000000000000000000_1',use_container_width=True)
    st.button('b020000000000000000000000000_2',use_container_width=True)
    st.button('b020000000000000000000000000_3',use_container_width=True)
with col03:
    st.button('b030000000000000000000000000',use_container_width=True)
with col04:
    st.button('b040000000000000000000000000',use_container_width=True)