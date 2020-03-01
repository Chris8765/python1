#Gallows_random  - gra polega na zgadywaniu słowa, przy czym słowa zadane są już w kodzie programu,
#gracz posiada 11 prób, jeśli mu się nie uda, zostanie powieszony na szubienicy.

import random

GALLOWS = (
"""
_____
""",
"""
  |
  |
  |
  |
  |
  |
  |
__|__
""",
"""
  |
  |
  |
  |
  |
  |
  |
__|__
""",
"""
  --------
  |
  |
  |
  |
  |
  |
  |
__|__
""",
"""
  --------
  |      |
  |
  |
  |
  |
  |
  |
__|__
""",
"""
  --------
  |      |
  |      O
  |
  |
  |
  |
  |
__|__
""",
"""
  --------
  |      |
  |      O
  |      |
  |
  |
  |
  |      
__|__
""",
"""
  --------
  |      |
  |      O
  |    --+   
  |
  |
  |
  |      
__|__
""",
"""
  --------
  |      |
  |      O
  |    --+--   
  |
  |
  |
  |      
__|__
""",
"""
  --------
  |      |
  |      O
  |    --+--   
  |      |   
  |     |
  |     |
  |      
__|__   
""",
"""
  --------
  |      |
  |      O
  |    --+--   
  |      |   
  |     | | 
  |     | |
  |      
__|__   
""")

MAX_WRONG = len (GALLOWS) - 1

WORDS = ("ROWER", "BUT", "WOREK", "PIERNIK", "PYTHON", "WOREK", "DOM", "AUTO", "PLECAK", "PRACA", "CEBULA", "MARCHEWKA")

word = random.choice(WORDS)     # losowanie słowa do odgadnięcia

so_far = "-" * len(word)        # kreska zastępuje nieodgadniętą literę

wrong = 0                       # liczba nietrafionych liter

used = []                       # litery już użyte w zgadywaniu

print ("Welcome to the game \"Gallows\". Good luck!")

