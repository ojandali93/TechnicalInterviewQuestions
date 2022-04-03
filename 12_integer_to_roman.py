# Integer to Roman Numeral

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is 
# written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Input: num = 58
# Output: "LVIII"

#------------ Pseudocode ------------------

# set the standard numerical values in an array
# set a default list that will store the roman numerals
# iterate through the the digits array.
# if the value of the numer is 0, return nothing
# check the value

#------------ Solution --------------------
class Solution:
  def intToRoman(self, num: int) -> str:
    mapping = {
      '1000': 'M',
      '900': 'CM',
      '500': 'D',
      '400': 'CD',
      '100': 'C',
      '90': 'XC',
      '50': 'L',
      '40': 'XL',
      '10': 'X',
      '9': 'IX',
      '8': 'VIII',
      '7': 'VII',
      '6': 'VI',
      '5': 'V',
      '4': 'IV',
      '3': 'III',
      '2': 'II',
      '1': 'I',
    }
    roman = ''

    for key in mapping.keys():
      value = int(key)
      if num / value > 0:
        amount = num // value
        roman += mapping[key] * amount
        num = num - amount * value
    return roman
