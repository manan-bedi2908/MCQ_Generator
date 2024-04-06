from setuptools import find_packages, setup

setup(
    name='MCQ Generator',
    version='0.0.1',
    author="Manan Bedi",
    author_email="mananbedi.tech@gmail.com",
    install_requires=["openai", "langchain", "langchain_community",
                      "huggingface_hub", 
                      "transformers",
                      "accelerate", "bitsandbytes", "streamlit", 
                      "python-dotenv", "PyPDF2"
                      ],
    packages=find_packages()
)