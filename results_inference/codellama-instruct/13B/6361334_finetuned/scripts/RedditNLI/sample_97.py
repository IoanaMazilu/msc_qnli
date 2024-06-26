import re

premise = "U.S. to Impose Tariffs on Another $16 Billion in Chinese Imports."
hypothesis = "U.S. to Slap Tariffs on $16 Billion of Chinese Goods on Aug. 23."

# extract the numerical entities from the premise and hypothesis
premise_amount = re.findall(r'\d+', premise)[0]
hypothesis_amount = re.findall(r'\d+', hypothesis)[0]

# compare the numerical entities
if premise_amount!= hypothesis_amount:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the amount in the hypothesis does not contradict the amount in the premise, we can infer entailment
    label = "entailment"

print(label)
