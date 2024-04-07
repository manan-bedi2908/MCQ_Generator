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