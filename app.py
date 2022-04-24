import streamlit as st
from bot import *
from bokeh.models.widgets import Button
from bokeh.models import CustomJS

# Sidebar Menu
st.sidebar.image("assets/logo.png", width=300)
st.sidebar.markdown(
    "Robert Bot is our very own implementation of a GRU Based Seq2Seq Chatbot."
)
st.sidebar.markdown("Check out the code at:")
st.sidebar.markdown(
    "[Github Repository](!https://github.com/Aakash-kaushik/robert-heroku)"
)
html_string = """
  <h2> Creators </h2>
  <p align="center">
  <ol>
  <li> Aakash Kaushik </li>
  <li> Aryan Kargwal </li>
  <li> Parikshit Kumar </li>
  <li> Aditya Choudhury </li>
  </ol>
</p>
"""
st.sidebar.markdown(html_string, unsafe_allow_html=True)

# Main Body

title = """
        <h1><a href="https://github.com/Aakash-kaushik/robert_bot">Robert Bot 🤖</a></h1>
        """

st.write("\n")
st.write("\n")

st.markdown(title, unsafe_allow_html=True)
user_input = st.text_input("Enter your Message here", "Hey")
bot_output_list = eval_input(encoder_rnn, decoder, searcher, voc, user_input)
if bot_output_list != -1:
    bot_output_str = ""
    for bot_output_word in bot_output_list:
        bot_output_str += bot_output_word
        bot_output_str += " "
    st.write("Robert: ", bot_output_str)
else:
    st.write("Robert: ", "Try something else human.🧍")

tts_button = Button(label="Speak", width=100)

tts_button.js_on_event(
    "button_click",
    CustomJS(
        code=f"""
    var u = new SpeechSynthesisUtterance();
    u.text = "{bot_output_str}";
    u.lang = 'en-US';

    speechSynthesis.speak(u);
    """
    ),
)

st.bokeh_chart(tts_button)
st.write("\n")
st.write("\n")
