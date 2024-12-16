#     st.session_state.counter = 0
# st.session_state.counter += 1

# for message in st.session_state.messages:
#     with st.chat_message(message['role']):
#         st.write(message['content'])

# # if prompt:=st.text_input('Something'):
# if st.button('Btn01'):
#     # with st.chat_message('user'):
#     #     # st.write(f'User typed: {prompt}')
#     #     st.markdown(prompt)
#     prompt = 'test'
#     st.session_state.counter += 1
#     # st.write(st.session_state.counter)
#     st.session_state.messages.append({'role':'user','content':prompt})

#     response = f'User said: {prompt}'

#     # with st.chat_message('ai'):
#     #     st.markdown(response)

#     st.session_state.messages.append({'role':'ai','content':response})

# st.write(st.session_state.counter)