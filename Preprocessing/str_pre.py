# 해당 코드는 Jupyter lab에서 작성된 코드를 편의상 py 파일로 적어놓은 것 입니다. 

from bs4 import BeautifulSoup
import re
import konlpy
import pandas as pd
import nltk
import tensorflow as tf
import numpy as np

df = pd.read_csv("community__real.csv")

df['comments']= df['comments'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", '')

df['comments']= df['comments'].str.replace(r"헐", '')

"""
헐
ㅋ
ㅋㅋ
ㅋㅋㅋ
ㅋㅋㅋㅋ
ㅋㅋㅋㅋㅋ
ㅋㅋㅋㅋㅋㅋ
ㄹㅇ  등의 불용어 제거 
"""
