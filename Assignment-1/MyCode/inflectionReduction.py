from util import *
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Add your import statements here




class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		#Fill in code here

		# stemming 
		
		# stemmer = PorterStemmer()
		# reducedText = [[ stemmer.stem(word) for word in sentence] for sentence in text]
		


		# Lemmatization 

		lemmatizer = WordNetLemmatizer()
		reducedText = [[ lemmatizer.lemmatize(word) for word in sentence] for sentence in text]
		
		return reducedText


