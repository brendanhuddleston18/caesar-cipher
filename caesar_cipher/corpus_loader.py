import ssl
import nltk
from nltk.corpus import words, names

try:
  _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
  pass
else:
  ssl._create_default_https_context = _create_unverified_https_context

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

word_list = words.words()
name_list = names.words()