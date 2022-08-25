from util import *
from nltk.tokenize import PunktSentenceTokenizer
import re
delimiters = '[.?!]'

# Add your import statements here




class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		if isinstance(text, str):
			segmentedText = re.split(delimiters, text)  #Split wherever ./?/! occurs
			if '' in segmentedText:
				segmentedText.remove('')
			return segmentedText
		else:
			print("Error in argument...")
			return 0





	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		if isinstance(text, str):
			tokenizer = PunktSentenceTokenizer(text)
			segmentedText = tokenizer.tokenize(text)
			return segmentedText
		else:
			print("Error in argument...")
			return 0