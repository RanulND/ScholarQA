# get the required libraries
import pandas as pd
from datetime import datetime
import re


class Preprocessing:

  """
  this class is defined to apply basic pre-processing steps for the initial dataframe/
  """

  def __init__(self,file, abbr):

    """
        Args:
            file (str): Path to excel file containing extracted abstracts.
            abbr (str): Path to text file containing abbreviations.
        
        Output:
            dataframe with processed abstracts.
        """
       
    self.file = file
    self.abbr = abbr
    self.df = pd.read_excel(file)
    # self.df.drop(columns=self.df.columns[0], axis=1, inplace=True)
    self.df.dropna(how='any', inplace=True)

  # to get authors and keywords into a list into the
  def stringsToList(self, author):
    return [s.lower().strip() for s in author.split(";")]

  # remove unnecessary characters
  def removeUnwantedCharacters(self, text):
    unwanted_chars = [';', ':', '!', "*", "-","_" ]
    pattern = r'\b[A-Z]+\-[0-9]+\b' # defining the regular expression
    technical_terms = re.findall(pattern, text)
    words = text.split(" ")
    new_words = []
    
    # applying the match
    for word in words:
      if word in technical_terms:
        new_words.append(word)
        continue
      for c in unwanted_chars:
        word = word.replace(c, " ")
      new_words.append(word)

    formatted_text = " ".join(new_words)
    return formatted_text
  
  # create a dictionary of abbreviations
  def load_abbreviations(self):
    abbreviations = {}
    with open(self.abbr, 'r') as file:
        for line in file:
            abbreviation, full_word = line.strip().split(' - ')
            abbreviations[abbreviation] = full_word
    return abbreviations

  # replace abbreviations with thier full form
  def replace_abbreviations(self, text):
      abbreviations = self.load_abbreviations()
      for abbreviation, full_word in abbreviations.items():
          pattern = r'\b' + re.escape(abbreviation) + r'\b'
          text = re.sub(pattern, full_word, text)
      return text

  # remobe unwanted characters
  def cleaningText(self, text):
    pattern_1 = r'\[\s*[0-9]+\s*\]'
    cleaned_text = re.sub(pattern_1,"",text)
    pattern_2 = r'[\'’]s'
    cleaned_text = re.sub(pattern_2,"",cleaned_text)
    pattern_3 = r'([A-Za-z]+)\/([A-Za-z]+)'
    matches = re.findall(pattern_3, cleaned_text)
    for match in matches:
        replaced = match[0] + ' ' + match[1]
        cleaned_text = cleaned_text.replace(match[0] + '/' + match[1], replaced)
    cleaned_text = cleaned_text.replace('('," ").replace(")"," ").replace(",","")
    return cleaned_text

  # apply all the processing steps for relevant columns
  def apply_processing(self):
    self.df['Abstract'] = self.df['Abstract'].apply(self.removeUnwantedCharacters)
    self.df['Abstract'] = self.df['Abstract'].str.lower()
    self.df['Abstract'] = self.df['Abstract'].apply(self.replace_abbreviations)
    self.df['Abstract'] = self.df['Abstract'].apply(self.cleaningText)
    

    self.df['Authors'] = self.df['Authors'].apply(self.stringsToList)
    self.df['Key Words'] = self.df['Key Words'].apply(self.stringsToList)
    self.df['Pub Date'] = self.df['Pub Date'].astype(str) # convert date type to strig

    return self.df # return the df
