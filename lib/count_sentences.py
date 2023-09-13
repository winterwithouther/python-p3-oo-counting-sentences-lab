#!/usr/bin/env python3

class MyString:

  def __init__(self, value=""):
    self.value = value
  
  def get_value(self):
    return self._value
  
  def set_value(self, new_value):
    if (isinstance(new_value, str)):
      self._value = new_value
      return self._value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
    return "." in self.value
  
  def is_question(self):
    return "?" in self.value
  
  def is_exclamation(self):
    return "!" in self.value
  
  def count_sentences(self):
    count = 0
    valid = [".", "!", "?"]
    valueList = list(self.value)
    for i in range(0, len(valueList)):
      if valueList[i] in valid and not(valueList[i-1] in valid):
          count += 1
    return count
  
string1 = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
print(string1.count_sentences())
