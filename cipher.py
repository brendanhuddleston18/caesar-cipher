import nltk
import re
from caesar_cipher.corpus_loader import word_list, name_list

def encrypt(plain, shift):
  encrypted_text = ""
  number_of_characters = 26

  for char in plain:
    if char.isalpha():
      if char.islower():
        base_character = "a"
      else:
        base_character = "A"
      base_code = ord(base_character)
      current_code = ord(char)
      current_position = current_code - base_code
      shifted_position = (current_position + shift) % number_of_characters
      shifted_code = base_code + shifted_position
      encrypted_text += chr(shifted_code)
    else:
      encrypted_text += char

  return encrypted_text

def decrypt(encrypted_text, shift):
  return encrypt(encrypted_text, -shift)

def crack(encrypted_text):
  shift= 0
  word_count = 0
  cracked_text = ""
  for i in range(26):
    decrypted_subject = decrypt(encrypted_text, i)
    words = re.sub(r'[^A-Za-z]+',' ', decrypted_subject).split()
    current_word_count = 0
    for word in words:
      if word.lower() in word_list or word in name_list:
       current_word_count += 1

    if current_word_count > word_count:
      word_count = current_word_count
      cracked_text = decrypted_subject

  if (word_count > len(words)) / 2:
    return cracked_text
  else:
    return ''

if __name__ == "__main__":
  sample = "AAAA"
  encrypt(sample, 1)