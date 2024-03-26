import pandas as pd
from datetime import datetime
import re

class Preprocssing:
        def __init__(self,file):
                self.file_path = file
                
file_path = "/content/drive/MyDrive/FYP/Code Base/Q&A/DataSet_1.csv"
    
df = pd.read_csv(file_path)
df.drop(columns=df.columns[0], axis=1, inplace=True)
def stringsToList(author):
    return [s.lower().strip() for s in author.split(";")]

def dateFormatter(date):
    date_obj = datetime.strptime(date, '%d-%b-%y')
    formatted_date = date_obj.strftime('%Y-%m-%d')
    return formatted_date

def removeUnwantedCharacters(text):
  unwanted_chars = [';', ':', '!', "*", "-","_" ]
  pattern = r'\b[A-Z]+\-[0-9]+\b'
  technical_terms = re.findall(pattern, text)
  words = text.split(" ")
  new_words = []

  for word in words:
    if word in technical_terms:
      new_words.append(word)
      continue
    for c in unwanted_chars:
      word = word.replace(c, " ")
    new_words.append(word)

  formatted_text = " ".join(new_words)
  return formatted_text

def replaceAbbreviations(text):
  abbr_dict = {
      "llm" : "large language model",
      "llms" : "large language model",
      "vqa" : "visual question answering",
      "kb" : "knowledge base",
      "kbs" : "knowledge base",
      "vqas" : "visual question answering",
      "apr" : "automated program repair",
      "aprs" : "automated program repair",
      "afs" : "automated feedback system",
      "afss" : "automated feedback system",
      "ai" : "artificial intelliegence",
      "api" : "application programming interface",
      "apis" : "application programming interface"
      }

  for abbreviation, full_word in abbr_dict.items():
    pattern = r'\b' + re.escape(abbreviation) + r'\b'
    text = re.sub(pattern, full_word, text)
  return text

def cleaningText(text):
  pattern = r'\[\s*[0-9]+\s*\]'
  cleaned_text = re.sub(pattern,"",text)
  cleaned_text = cleaned_text.replace('('," ").replace(")"," ").replace(",","")
  return cleaned_text

df['Abstract'] = df['Abstract'].apply(removeUnwantedCharacters)
df['Abstract'] = df['Abstract'].str.lower()
df['Abstract'] = df['Abstract'].apply(replaceAbbreviations)
df['Abstract'] = df['Abstract'].apply(cleaningText)

# df['Pub Date'][1] = "17-Jun-23"

df['Authors'] = df['Authors'].apply(stringsToList)
df['Key Words'] = df['Key Words'].apply(stringsToList)
df['Pub Date'] = df['Pub Date'].apply(dateFormatter)