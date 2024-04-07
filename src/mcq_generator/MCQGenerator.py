import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from src.mcq_generator.utils import read_file, get_table_data
from src.mcq_generator.logger import logging
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import PyPDF2

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.8)

template="""
Text: {text}
You are an expert MCQ Maker. Given the above text, it is your job to \
create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
Make sure the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
Ensure to make {number} MCQs

{response_json}
"""

quiz_generation_prompt = PromptTemplate(
    input_variables=['text', 'number', 'subject', 'tone', 'response_json'],
    template=template
)

quiz_chain = LLMChain(llm = llm,
                      prompt = quiz_generation_prompt,
                      output_key='quiz',
                      verbose = True)

