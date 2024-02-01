import nltk
import re
from corpus_loader import word_list, name_list

def encrypt(plain, shift):
  encrypted_text = ""
  number_of_characters = 26
  # normalized_text = plain

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
  
# print(ord(" "))

def decrypt(encrypted_text, shift):
  return encrypt(encrypted_text, -shift)

def crack(encrypted_text):
  shift= 0
  word_count = 0
  cracked_text = ""
  for i in range(65):
    decrypted_subject = decrypt(encrypted_text, i)
    words = re.sub(r'[^A-Za-z]+',' ', decrypted_subject)
    shift += 1
    print(words)
    for word in words:
      if word.lower() in word_list or word in name_list:
        word_count += 1
        print(word_count)
    # if decrypted_word.lower() in word_list or decrypted_word in name_list:
    #   cracked_text += decrypted_word
    #   print(word_count)
  
    # for decrypted_word in words:

if __name__ == "__main__":
  sample = "AAAA"
  encrypt(sample, 1)