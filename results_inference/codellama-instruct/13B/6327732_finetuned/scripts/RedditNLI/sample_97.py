import re

premise = "U.S. to Impose Tariffs on Another $16 Billion in Chinese Imports."
hypothesis = "U.S. to Slap Tariffs on $16 Billion of Chinese Goods on Aug. 23."

# extract the numerical entities from the premise and hypothesis
premise_amount = re.findall(r'\d+', premise)[0]
hypothesis_amount = re.findall(r'\d+', hypothesis)[0]

# check if the amount in the hypothesis contradicts the amount in the premise
if hypothesis_amount!= premise_amount:
    label = "contradiction"
else:
    label = "entailment"

print(label)
