# -*- coding: utf-8 -*-
"""

OK, I knew that most female names in Latin-derived languages, as well as English and Germanic languages in general, end with -a or -e, while male names more often end with consonants. I can confirm that this also works for Slav languages, and, I believe, in Semitic ones too. I see that Pranav Jawale says it is the case in India as well. 

I wonder if the preference for the -a ending is related to the fact that this is the first phoneme a child pronounces, so using it in the mother's name makes it easier for the infant to locate / track the person that takes care of him / her?

    - Vadim Berman, CTO of LinguaSys

"""


name = input('Enter first name :')

if name[-1] in ['a','e','i']:
    print('Gender for the entered name is female')
else:
    print('Gender for the entered name is male')
    
