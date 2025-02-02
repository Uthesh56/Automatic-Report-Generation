import streamlit as Stream
import pandas as pd
import time
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def Process():
    Upload_File = Stream.file_uploader("# Upload", type=["csv", "json", "xlsx"])
    Place = Stream.empty()
    if Upload_File is not None:
        Place.text("Uploading File✅")
        time.sleep(2)
        Place.text("Uploaded Successfully✅")
        
        try:
            if Upload_File.name.endswith('.csv'):
                File = pd.read_csv(Upload_File)
            elif Upload_File.name.endswith('.json'):
                File = pd.read_json(Upload_File)
            elif Upload_File.name.endswith('.xlsx'):
                File = pd.read_excel(Upload_File)
            Data = File.dropna()
        except Exception as e:
            Stream.error(f"Error loading file: {e}")
            return None
        
        # PREPROCESS FEEDBACKS
        Lem = WordNetLemmatizer()
        Stop = set(stopwords.words('english'))

        if 'feedback' in Data.columns:
            Data['feedback'] = Data['feedback'].apply(
                lambda text: ' '.join([Lem.lemmatize(word) for word in word_tokenize(text.lower()) 
                                      if word not in Stop and word not in string.punctuation])
            )
        return Data
    return None
