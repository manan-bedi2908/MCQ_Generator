import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcq_generator.utils import read_file, get_table_data
import streamlit as st
from src.mcq_generator.MCQGenerator import generate_evaluate_chain
from src.mcq_generator.logger import logging

with open(r'C:\Users\Manan Bedi\Documents\LLM_iNeuron\MCQ_Generator\response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

st.title("MCQ Creator Application with LangChain")

with st.form("user_inputs"):
    uploaded_file = st.file_uploader("Upload a PDF or txt file")
    mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=50)
    subject = st.text_input("Enter the Subject", max_chars=20)
    tone = st.text_input("Complexity Level of Questions",
                         max_chars=20, placeholder="Simple")
    button = st.form_submit_button("Create MCQs")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Loading..."):
            try:
                text = read_file(uploaded_file)
                response=generate_evaluate_chain(
                    {
                        "text": text,
                        "number": mcq_count,
                        "subject":subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                    }
                )
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error!")
