import streamlit as st
import pandas as pd
import datastorage as ds
import networking as net
import copy

# ds.create_blank_data_structure()
ds.load_data_structure()

st.set_page_config(layout='wide')

if 'debug_obj01' not in st.session_state:
    st.session_state['debug_obj01'] = 0

if 'current_mode' not in st.session_state:
    st.session_state['current_mode'] = 'Normal'

df = pd.DataFrame({
    'col01':[1,2,30,4],
    'col02':[1,20,3,4],
    'col03':[1,25,3,4]
})

def addr_input_changed(**kwargs):
    net.set_target_addr(kwargs['addr'])

def save_preset_btn_click():
    # st.session_state['debug_obj01'] = ds.editing_data['DesktopData'][st.session_state['current_preset']]['Button01']
    ds.write_presets_to_file()

def on_mode_changed(**kwargs):
    # if st.session_state['current_mode'] == 'Edit':
    #     # Store current_data into editing_data. Further edits will be made
    #     # to the dataset later.
    #     ds.editing_data = ds.current_data
    pass

def btn_on_click(**kwargs):
    # st.write(kwargs)
    net.test01(kwargs['btn_data'])
    # st.write(kwargs['btn_data']['EventName'])
    
    pass

def slider_on_change(**kwargs):
    kwargs['slider_data']['EventValue'] = st.session_state[kwargs['key_name']]
    net.test01(kwargs['slider_data'])


def edit_mode_text_input_changed(**kwargs):
    ds.editing_data['DesktopData']\
        [st.session_state.current_preset]\
            [kwargs['ControlName']]['EventName'] = \
                st.session_state[kwargs['key']]
    # ds.editing_data['DesktopData'][st.session_state.current_preset][kwargs['ControlName']]['EventName'] = st.session_state[kwargs['key']]
    # print(st.session_state[kwargs['key']])
    # print(ds.editing_data['DesktopData'][st.session_state.current_preset][kwargs['ControlName']])
    st.session_state['debug_obj01'] = ds.editing_data['DesktopData']\
        [st.session_state.current_preset]\
            [kwargs['ControlName']]['EventName']
    # st.session_state['debug_obj01'] = st.session_state['current_preset']
    # pass

# Pads string until it is max_length chars long.
def padded_text(val,pad_char,max_length):
    if len(val) < max_length:
        for i in range(max_length-len(val)):
            val += pad_char
    return val

cont01 = st.container(height=740, border=False)
with cont01:
    radcol01, radcol02, radcol03, radcol04, radcol05 = st.columns(
        [0.15,0.15,0.4,0.05,0.15])
    with radcol01:
        select_options = ['Normal','Edit','Debug']
        if 'current_mode' not in st.session_state:
            st.session_state['current_mode'] = select_options[0]

        st.selectbox(
            'Mode',index=select_options.index(st.session_state['current_mode']),
            options=select_options,key='current_mode',on_change=on_mode_changed)

    with radcol03:
        rad01 = st.radio(
            'Presets',['Preset01','Preset02','Preset03','Preset04'], 
            key='current_preset', horizontal=True)
    with radcol05:
        st.button('Save Preset',use_container_width=True,
                  disabled=st.session_state.current_mode is not 'Edit',
                  on_click=save_preset_btn_click)

    preset_data = ds.current_data['DesktopData'][st.session_state.current_preset]
    height = 500
    if st.session_state.current_mode == 'Normal':
        ds.editing_data = copy.deepcopy(ds.current_data)
        col01, col02, col03, col04, col05 = st.columns([1,1,1,1,2])
        btn_max_length = 25
        with col01:
            with st.container(height=height, border=False):
                # st.text_area('Some01',height=10,label_visibility='hidden',)
                # st.text_area('Some02',height=10,label_visibility='hidden',)
                # st.text_area('Some03',height=10,label_visibility='hidden',)
                # st.text_area('Some04',height=10,label_visibility='hidden',)
                # st.button('000000000000000000000000000000', use_container_width=True)
                st.button(padded_text(preset_data['Button01']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button01']})
                st.button(padded_text(preset_data['Button02']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button02']})
                st.button(padded_text(preset_data['Button03']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button03']})
                st.button(padded_text(preset_data['Button04']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button04']})
                st.button(padded_text(preset_data['Button05']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button05']})
                st.button(padded_text(preset_data['Button06']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button06']})
        with col02:
            with st.container(height=height, border=False):
                st.button(padded_text(preset_data['Button07']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button07']})
                st.button(padded_text(preset_data['Button08']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button08']})
                st.button(padded_text(preset_data['Button09']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button09']})
                st.button(padded_text(preset_data['Button10']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button10']})
                st.button(padded_text(preset_data['Button11']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button11']})
                st.button(padded_text(preset_data['Button12']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button12']})
        with col03:
            with st.container(height=height, border=False):
                st.button(padded_text(preset_data['Button13']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button13']})
                st.button(padded_text(preset_data['Button14']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button14']})
                st.button(padded_text(preset_data['Button15']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button15']})
                st.button(padded_text(preset_data['Button16']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button16']})
                st.button(padded_text(preset_data['Button17']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button17']})
                st.button(padded_text(preset_data['Button18']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button18']})
        with col04:
            with st.container(height=height, border=False):
                st.button(padded_text(preset_data['Button19']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button19']})
                st.button(padded_text(preset_data['Button20']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button20']})
                st.button(padded_text(preset_data['Button21']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button21']})
                st.button(padded_text(preset_data['Button22']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button22']})
                st.button(padded_text(preset_data['Button23']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button23']})
                st.button(padded_text(preset_data['Button24']['EventName'],'_',btn_max_length), use_container_width=True, on_click=btn_on_click, kwargs={'btn_data':preset_data['Button24']})
        with col05:
            st.slider(preset_data['Slider01']['EventName'],key='slider01_val',format="%f",step=0.0001,value=0.0,min_value=preset_data['Slider01']['SliderMinValue'],max_value=preset_data['Slider01']['SliderMaxValue'], on_change=slider_on_change, kwargs={'slider_data':preset_data['Slider01'],'key_name':'slider01_val'})
            st.slider(preset_data['Slider02']['EventName'],key='slider02_val',format="%f",step=0.0001,value=0.0,min_value=preset_data['Slider02']['SliderMinValue'],max_value=preset_data['Slider02']['SliderMaxValue'], on_change=slider_on_change, kwargs={'slider_data':preset_data['Slider02'],'key_name':'slider02_val'})
            st.slider(preset_data['Slider03']['EventName'],key='slider03_val',format="%f",step=0.0001,value=0.0,min_value=preset_data['Slider03']['SliderMinValue'],max_value=preset_data['Slider03']['SliderMaxValue'], on_change=slider_on_change, kwargs={'slider_data':preset_data['Slider03'],'key_name':'slider03_val'})
            st.slider(preset_data['Slider04']['EventName'],key='slider04_val',format="%f",step=0.0001,value=0.0,min_value=preset_data['Slider04']['SliderMinValue'],max_value=preset_data['Slider04']['SliderMaxValue'], on_change=slider_on_change, kwargs={'slider_data':preset_data['Slider04'],'key_name':'slider04_val'})
    elif st.session_state.current_mode == 'Edit':

        # Load preset from editing_data.
        edit_preset_data = ds.editing_data['DesktopData'][st.session_state.current_preset]
        
        # st.write(st.session_state['debug_obj01'])
        # st.write(edit_preset_data['Button01'])

        # st.json(ds.editing_data)
        col01, col02, col03, col04 = st.columns(4)
        with col01:
            st.text_input('01',value=edit_preset_data['Button01']['EventName'], key='EditInput01', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button01','key':'EditInput01'})
            st.text_input('02',value=edit_preset_data['Button02']['EventName'], key='EditInput02', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button02','key':'EditInput02'})
            st.text_input('03',value=edit_preset_data['Button03']['EventName'], key='EditInput03', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button03','key':'EditInput03'})
            st.text_input('04',value=edit_preset_data['Button04']['EventName'], key='EditInput04', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button04','key':'EditInput04'})
            st.text_input('05',value=edit_preset_data['Button05']['EventName'], key='EditInput05', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button05','key':'EditInput05'})
            st.text_input('06',value=edit_preset_data['Button06']['EventName'], key='EditInput06', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button06','key':'EditInput06'})
            st.text_input('07',value=edit_preset_data['Button07']['EventName'], key='EditInput07', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button07','key':'EditInput07'})
            st.text_input('08',value=edit_preset_data['Button08']['EventName'], key='EditInput08', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button08','key':'EditInput08'})
        with col02:
            st.text_input('09',value=edit_preset_data['Button09']['EventName'], key='EditInput09', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button09','key':'EditInput09'})
            st.text_input('10',value=edit_preset_data['Button10']['EventName'], key='EditInput10', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button10','key':'EditInput10'})
            st.text_input('11',value=edit_preset_data['Button11']['EventName'], key='EditInput11', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button11','key':'EditInput11'})
            st.text_input('12',value=edit_preset_data['Button12']['EventName'], key='EditInput12', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button12','key':'EditInput12'})
            st.text_input('13',value=edit_preset_data['Button13']['EventName'], key='EditInput13', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button13','key':'EditInput13'})
            st.text_input('14',value=edit_preset_data['Button14']['EventName'], key='EditInput14', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button14','key':'EditInput14'})
            st.text_input('15',value=edit_preset_data['Button15']['EventName'], key='EditInput15', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button15','key':'EditInput15'})
            st.text_input('16',value=edit_preset_data['Button16']['EventName'], key='EditInput16', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button16','key':'EditInput16'})
        with col03:
            st.text_input('17',value=edit_preset_data['Button17']['EventName'], key='EditInput17', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button17','key':'EditInput17'})
            st.text_input('18',value=edit_preset_data['Button18']['EventName'], key='EditInput18', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button18','key':'EditInput18'})
            st.text_input('19',value=edit_preset_data['Button19']['EventName'], key='EditInput19', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button19','key':'EditInput19'})
            st.text_input('20',value=edit_preset_data['Button20']['EventName'], key='EditInput20', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button20','key':'EditInput20'})
            st.text_input('21',value=edit_preset_data['Button21']['EventName'], key='EditInput21', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button21','key':'EditInput21'})
            st.text_input('22',value=edit_preset_data['Button22']['EventName'], key='EditInput22', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button22','key':'EditInput22'})
            st.text_input('23',value=edit_preset_data['Button23']['EventName'], key='EditInput23', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button23','key':'EditInput23'})
            st.text_input('24',value=edit_preset_data['Button24']['EventName'], key='EditInput24', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Button24','key':'EditInput24'})
        with col04:
            st.text_input('01_1',value=edit_preset_data['Slider01']['EventName'], key='EditInput25', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Slider01','key':'EditInput25'})
            st.text_input('02_1',value=edit_preset_data['Slider02']['EventName'], key='EditInput26', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Slider02','key':'EditInput26'})
            st.text_input('03_1',value=edit_preset_data['Slider03']['EventName'], key='EditInput27', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Slider03','key':'EditInput27'})
            st.text_input('04_1',value=edit_preset_data['Slider04']['EventName'], key='EditInput28', on_change=edit_mode_text_input_changed, kwargs={'ControlName':'Slider04','key':'EditInput28'})
        # st.json(edit_preset_data)
    elif st.session_state.current_mode == 'Debug':
        st.write(ds.current_data)
st.json({
    'a':1,

})

str01 = st.text_input('Some01')
st.write(str01)
str02 = st.text_input('Some02')
st.write(str02)
