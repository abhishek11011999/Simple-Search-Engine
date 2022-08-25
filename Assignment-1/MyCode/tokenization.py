from util import *
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize import TreebankWordTokenizer
# Add your import statements here




class Tokenization():

	def naive(self, text):
		"""
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []
		tk = WhitespaceTokenizer()
		for sentence in text:
			token = tk.tokenize(sentence)
			tokenizedText.append(token)
		return tokenizedText



	def pennTreeBank(self, text):
		"""
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

		tokenizedText = []
		PTB_tk = TreebankWordTokenizer()
		for sentence in text:
			token = PTB_tk.tokenize(sentence)
			tokenizedText.append(token)
		return tokenizedText