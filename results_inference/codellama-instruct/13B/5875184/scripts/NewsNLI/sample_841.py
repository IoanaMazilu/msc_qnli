premise_parties = 20
hypothesis_parties = 56

# the hypothesis mentions the number of parties that supported Nepal's candidacy, which is also mentioned in the premise
if hypothesis_parties > premise_parties:
    # check if the number of parties supporting Nepal's candidacy in the hypothesis is greater than the number of parties mentioned in the premise
    label = "entailment"
else:
    # if the number of parties supporting Nepal's candidacy in the hypothesis is not greater than the number of parties mentioned in the premise, we can infer neutrality
    label = "neutral"

print(label)
